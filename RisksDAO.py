#Risks Data Access Object
#Author Jon Ishaque GMIT Data Representation
#Provide access for REST server to MYSQL database
#copy curl command from comments in functions to assist debug.


#import connector library to enable server to connect to database
import mysql.connector
import dbconfig as cfg
from flask import jsonify

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
        #function to get rid prefix from dictionary
        
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
        sql = 'SELECT count(*) FROM risks WHERE Category_id = (%s)'
        values=(Category_id,)
        try:
            cursor.execute(sql,values)
        except Exception as e:
            print(e)
        count = cursor.fetchone()
        count1 = count[0]
        print(count1)
        pfx = str(self.id_to_prefix(Category_id))
        rid= pfx + str(count1+1)
        return rid
 ##############################################
    #calculate level serverside
    def createRiskLevelID(self,impact,likelihood):
        #print(impact)
        rlid = int(impact)*int(likelihood)
        return rlid
 ##############################################
    def createRisk(self,risk):
        #print('In DAO')
        #print (jsonify(risk))
        #also create new risk from previousids.
        cursor = self.db.cursor()#think about where to calculate risklevel CS/SS
        #last review not needed on creation
        #create sql string, parameterise values to avoid sql injection
        #print(risk)
        rid = self.createRid(risk['Category_id'])
        sql='INSERT INTO risks (rid,Risk_Description,Category_id,RiskLevel_id,Owner,\
            Review_Frequency,RiskArea,Man_Ctrs,Impact,Likelihood) VALUES (%s,%s,%s,%s\
            ,%s,%s,%s,%s,%s,%s);'
        values = [
            self.createRid(risk['Category_id']),
            risk['Risk_Description'],
            risk['Category_id'],
            self.createRiskLevelID(risk['Impact'],risk['Likelihood']),
            risk['Owner'],
            risk['Review_Frequency'],
            risk['RiskArea'],
            risk['Man_Ctrs'],
            risk['Impact'],
            risk['Likelihood'],
            
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
            self.createRiskLevelID(risk['Impact'],risk['Likelihood']),
            risk['Owner'],
            risk['Next_Review'],
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
            ORDER BY Next_Review asc;'
        
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
        sql='SELECT * FROM risks  LEFT OUTER JOIN Category on Category_id = cid where Archive =1;' 
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
        risk={}
        #print('in dict')
        if result:
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
            for i, colname in enumerate(colnames):
                value = result[i]
                cat[colname]=value
        return cat
##############################################

#create instance of risksDAO
RisksDAO = RisksDAO()
