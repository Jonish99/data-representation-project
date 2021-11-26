#Risk Register Database Access object
#Author Jon Ishaque GMIT Data Representation


#import connector library to enable server to connect to database
import mysql.connector
 
class RisksDAO:
    rkdb=""
    def __init__(self):
        self.rkdb =  mysql.connector.connect(
        host="localhost",user="root",
        password="",
        database="risk_register"
        )
        print("Connection mode")

    def createRisk(self,risk):
        print (risk)
        #also create new risk from previousids.
        cursor = self.rkdb.cursor()#think about where to calculate risklevel CS/SS
        #last review not needed on creation
        #create sql string, parameterise values to avoid sql injection
        sql="INSERT INTO risks (rid,Risk_Description,RiskLevel,Owner,\
            Review_Frequency,RiskArea,Man_Ctrs,Impact,Likelihood,Category) VALUES (%s,%s,%s,%s\
            ,%s,%s,%s,%s,%s,%s);"
        values = [
            risk['rid'],
            risk['Risk_Description'],
            risk['RiskLevel'],
            risk['Owner'],
            risk['Review_Frequency'],
            risk['RiskArea'],
            risk['Man_Ctrs'],
            risk['Impact'],
            risk['Likelihood'],
            risk['Category']
            ]
        #print(values)
        cursor.execute(sql,values)
        #commit triggers the work on database
        self.rkdb.commit#
        return cursor.lastrowid
    
    def UpdateRisk(self,risk): #update the risk values which are allowed to be updated.
        cursor = self.rkdb.cursor()
        sql="UPDATE risks SET Risk_Description = %s ,RiskLevel = %s,\
            Owner = %s, Next_Review = %s, Last_Review=%s,\
            Review_Frequency = %s, RiskArea = %s,Man_Ctrs = %s,\
            Impact = %s,Likelihood = %s WHERE id=%s;"
          #https://stackoverflow.com/questions/1136437/inserting-a-python-datetime-datetime-object-into-mysql#
        values = [
            
            risk['Risk_Description'],
            risk['RiskLevel'],
            risk['Owner'],
            risk['Next_Review'],
            risk['Last_Review'],
            risk['Review_Frequency'],
            risk['RiskArea'],
            risk['Man_Ctrs'],
            risk['Impact'],
            risk['Likelihood'],
            risk['id']
            ]
        print(sql)
        print(values)
        cursor.execute(sql,values)
        rkdb.commit()

   
    #function to get all risks due in the next 30 days
    def getAllRisks(self):
        cursor = self.rkdb.cursor()#get cursor
        sql="SELECT * FROM risks" 
        cursor.execute(sql)#pass sql to cursor
        results= cursor.fetchall()#return conents of cursor
        returnArray=[]#create array to contain returnedbooks
        for result in results:
            resultAsDict= self.CovertToDict(result)#call convert dict to make risk a dictionary.
            returnArray.append(resultAsDict)#build dictionary of risks
        #print (returnArray)
        return returnArray
    
    #function to get risk by id, to show in html for editing
    def findByRiskID(self,risk):
        cursor = self.rkdb.cursor()
        sql="SELECT * FROM risks WHERE id=%s"
        values=[risk['id']]
        cursor.execute(sql,values)
        risk = cursor.fetchone()

        returnRisk=[]#return empty if not found and deal with empty array.
        returnRisk.append(self.CovertToDict(risk))#covernt to dictionary
        print (returnRisk)
        return returnRisk
    


    def DeleteRisk(self,risk):
        values=[risk['id']] #ge risk id out of dict
        cursor = self.rkdb.cursor()
        sql = "DELETE FROM risks WHERE id=(%s)"
      
        cursor.execute(sql,values)
        
        cnt = cursor.rowcount ##Nothing is returned why??????????????
        self.rkdb.commit()
        print(cnt)
        


    def CovertToDict(self,result):
        colnames=['id','rid','Risk_Description','RiskLevel',\
            'Owner','Next_Review','Last_Review',\
            'Review_Frequency','RiskArea','Man_Ctrs',\
            'Impact', 'Likelihood','Archive','Category']
        risk={}
        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                risk[colname]=value
        return risk






#create instance of risksDAO
RisksDAO = RisksDAO()
