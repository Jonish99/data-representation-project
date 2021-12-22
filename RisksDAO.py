#Risks Data Access Object
#Author Jon Ishaque GMIT Data Representation
#Provide access for REST server to MYSQL database
#copy curl command from comments in functions to assist debug.


#import connector library to enable server to connect to database

import mysql.connector
import dbconfig as cfg
from dateutil.relativedelta import relativedelta
from datetime import datetime
from flask import jsonify
from dateutil import parser
#################################################


##############################################
class RisksDAO:
    db=''
    def __init__(self):
        self.db =  mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database'],
        )   
      

 ##############################################   
    def id_to_prefix(self,argument):
        #function to get 'rid' prefix from dictionary
        #(Switch Case in Python (Replacement) - GeeksforGeeks, 2021)
        switcher = {           
        1: 'BC/',
        2: 'C/',
        3: 'F/',
        4: 'L/',
        5: 'L/R/',
        6: 'PHSW/',
        7: 'P/',
        8: 'S/',
        9:'S/T/A'
        }
        return switcher.get(int(argument), '??')
  ##############################################
    def createRid(self,Category_id):
        #function to create a the rid from risk category_id        
        cursor = self.db.cursor()        
        sql = 'SELECT max(rid) FROM risks WHERE Category_id = (%s)'
        values=(Category_id,)
        try:
            cursor.execute(sql,values)
        except Exception as e:
            print(e)
        maxID = cursor.fetchone()
        maxID1 = maxID[0]
        #check for rid values!
        if maxID1:          
            #get number from maxid
            MaxNum=int(''.join(filter(str.isdigit, maxID1)))
        else:
            MaxNum = 0

        NewNum = MaxNum+1
        NewNum1 = str(NewNum)
        print(NewNum1)
        #ensure numeric value string is always same length for max db sort above
        while len(str(NewNum1)) <3: 
            print(len(NewNum1))
            NewNum1 = '0'+ str(NewNum1)

        #get category prefix
        pfx = str(self.id_to_prefix(Category_id))
        rid= pfx + NewNum1
        print(rid)
        return rid
 ##############################################
    #calculate level serverside
    def getRiskLevelID(self,impact,likelihood):
        #print(impact)
        rlid = int(impact)*int(likelihood)
        return rlid
 ##############################################
    #calculate level serverside
    def getRevFreq(self,impact,likelihood):
        #print(impact)
        rlid = int(impact)*int(likelihood)
        if rlid < 6:
            freq = 'Annually'
        elif rlid < 9:
            freq = 'Bi-annually'
        else:
            freq = 'Quarterly'
        return freq
 ##############################################
    #def getLastReview(self,LastReview): #(How to Format Dates in Python, 2021)
    #    dt = parser.parse(LastReview)
    #    return dt
  ##############################################           
    def getNextReview(self,LastReview,impact,likelihood) :
        lastreview = dt = parser.parse(LastReview)
        print('In last review' + str(lastreview))
        #method for adding months to dates > (python?, Stocks and Ragazzi, 2021)
        three_mon_rel = relativedelta(months=3)
        rlid = int(impact)*int(likelihood)
        print('rlid:'+str(rlid))
        if rlid >  8:
            nextreview = lastreview + three_mon_rel
        elif (rlid > 5 and rlid < 9):
            nextreview = lastreview + relativedelta(months=6)
        else: #less than 12
            nextreview = lastreview + relativedelta(months=12)
        print("In get Next review: " + str(nextreview))
        return nextreview
 ##############################################
    def createRisk(self,risk):
        
        #also create new risk from previousids.
        cursor = self.db.cursor()
        #last review not needed on creation
        #create sql string, parameterise values to avoid sql injection
        #print(risk)
        rid = self.createRid(risk['Category_id'])
        sql='INSERT INTO risks (rid,Risk_Description,Category_id,RiskLevel_id,Owner,\
            Review_Frequency,RiskArea,Man_Ctrs,Impact,Likelihood,Last_Review,Next_Review) VALUES (%s,%s,%s,%s\
            ,%s,%s,%s,%s,%s,%s,%s,%s);'
        values = [
            self.createRid(risk['Category_id']),
            risk['Risk_Description'],
            risk['Category_id'],
            self.getRiskLevelID(risk['Impact'],risk['Likelihood']),
            risk['Owner'],
            self.getRevFreq(risk['Impact'],risk['Likelihood']),
            risk['RiskArea'],
            risk['Man_Ctrs'],
            risk['Impact'],
            risk['Likelihood'],
            risk['Last_Review'],
            self.getNextReview(risk['Last_Review'],risk['Impact'],risk['Likelihood'])
            ]
               #print(sql)
        #print(values)
        #return risk['Risk_Description']
        cursor.execute(sql,values)
        #commit triggers the work on database
        self.db.commit#
        return cursor.lastrowid
##############################################
    
    def UpdateRisk(self,risk): #update the risk values which are allowed to be updated.
        #print('In DAO')
        #print(risk)
        cursor = self.db.cursor()
        sql='UPDATE risks SET Risk_Description = %s,Category_id = %s,RiskLevel_id = %s,\
            Owner = %s, Next_Review = %s, Last_Review=%s,\
            Review_Frequency = %s, RiskArea = %s,Man_Ctrs = %s,\
            Impact = %s,Likelihood = %s, Archive = %s WHERE id=%s;'
          #(MySQL, 2021)
        values = [            
            risk['Risk_Description'],
            risk['Category_id'],
            self.getRiskLevelID(risk['Impact'],risk['Likelihood']),
            risk['Owner'],                     
            self.getNextReview(risk['Last_Review'],risk['Impact'],risk['Likelihood']),
            risk['Last_Review'],
            risk['Review_Frequency'],
            risk['RiskArea'],
            risk['Man_Ctrs'],
            risk['Impact'],
            risk['Likelihood'],  
            risk['Archive'],
            risk['id']
            ]
 
        cursor.execute(sql,values)
        #print(sql)
        self.db.commit()
        return('risk updated')
############################################## 
    #function to get all risks due in the next 30 days
    def getAllCategories(self):
        
        cursor=''
        cursor = self.db.cursor()#get cursor
        sql='SELECT * FROM Category' 
        try:
            cursor.execute(sql)#pass sql to cursor
        except Exception as e:
            print('Error1:')
            print(e)
        
        try:
            results= cursor.fetchall()#return contents of cursor
        except Exception as e:
            print('Error2:')
            print(e)   
        returnArray=[]#create array to contain returnedrisks
        
        for result in results:
            resultAsDict= self.ConvertCatToDict(result)#call convert dict to make risk a categories.                  
            returnArray.append(resultAsDict)#build dictionary of categories
        #print (results)
        return returnArray
############################################## 
    #function to get all risks due in the next 30 days
    def getAllRisks(self):
        cursor = self.db.cursor()#get cursor
        sql='SELECT * FROM risks \
            LEFT OUTER JOIN Category on \
            Category_id = cid \
            LEFT OUTER JOIN risklevel on \
            rlid=RiskLevel_id \
            WHERE Archive = 0 ORDER BY Next_Review asc;'
        
        cursor.execute(sql)#pass sql to cursor
        results= cursor.fetchall()#return conents of cursor
        returnArray=[]#create array to contain returnedbooks
        for result in results:
            resultAsDict= self.ConvertToRiskDict(result)#call convert dict to make risk a dictionary.
           
            returnArray.append(resultAsDict)#build dictionary of risks
        #print (results)
        return returnArray
 ##############################################  
    def getArchiveRisks(self):
        cursor = self.db.cursor()#get cursor
        sql='SELECT * FROM risks \
            LEFT OUTER JOIN Category on \
            Category_id = cid \
            LEFT OUTER JOIN risklevel on \
            rlid=RiskLevel_id \
            WHERE Archive = 1 ORDER BY Next_Review asc;' 
        cursor.execute(sql)#pass sql to cursor
        results= cursor.fetchall()#return conents of cursor
        returnArray=[]#create array to contain returnedbooks
        for result in results:
            resultAsDict= self.ConvertToRiskDict(result)#call convert dict to make risk a dictionary.
           
            returnArray.append(resultAsDict)#build dictionary of risks
        #print (results)
        return returnArray
 ############################################## 
    #function to get risk by id, to show in html for editing
    def findByRiskID(self,id):
        #print('in find risk')
        cursor=''
        cursor = self.db.cursor()
        sql='SELECT * FROM risks \
            LEFT OUTER JOIN Category ON \
            Category_id = cid \
            LEFT OUTER JOIN risklevel ON \
            rlid=RiskLevel_id \
            WHERE id=(%s) ;'
        values=(id,) #validation check here
        #print(id)
        #print('in find risk2')
        try:
            cursor.execute(sql,values)
        except Exception as e:
            print(e)
        risk = cursor.fetchone()
        #print(risk)
        returnRisk=[]#return empty if not found and deal with empty array.
        returnRisk.append(self.ConvertToRiskDict(risk))#covernt to dictionary
        #print (returnRisk)
        return returnRisk
    
##############################################

    def DeleteRisk(self,id):
        values=(id,) 
        cursor = self.db.cursor()
        sql = 'DELETE FROM risks WHERE id=(%s)'
        cursor.execute(sql,values)        
        cnt = cursor.rowcount ##Nothing is returned why??????????????
        self.db.commit()
        return(cnt)
##############################################    
    def ConvertToRiskDict(self,result):

        colnames=['id','rid','Risk_Description','RiskLevel_id',\
            'Owner','Next_Review','Last_Review',\
            'Review_Frequency','RiskArea','Man_Ctrs',\
            'Impact', 'Likelihood','Archive','cid','Category_id','category','rlid','risklevel',]
        #create dict
        risk={}
        
        if result:
            #find colnames in result, value = next value
            for i, colname in enumerate(colnames):
                value = result[i]
                risk[colname]=value
            #print(risk)
            return risk
        else:
            print('error:convert to dict')
  ############################################## 
    def ConvertCatToDict(self,result):
        colnames=['cid','Category']
        cat={}
        if result:
            #find colnames in result, value = next value
            for i, colname in enumerate(colnames):
                value = result[i]
                cat[colname]=value
        return cat
##############################################

#create instance of risksDAO
RisksDAO = RisksDAO()
