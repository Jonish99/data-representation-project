#REST applicaiton for risk register
#Author Jon Ishaque GMIT Data Representation
#Provide access for http queries
#use commented curl commands to assist debuggin.

#call libraries
from flask import Flask,url_for,request,redirect,abort,jsonify,render_template
#import RiskDAO class from RisksDAO
from RisksDAO import RisksDAO
##############################################
#initiate flask server
app = Flask(__name__, 
        static_url_path='',
        static_folder='staticpages')

##############################################
#set base path for application
@app.route('/' )#index function
def index():
    #url_for('static', filename='index.html')
    return app.send_static_file('index.html')  #(Pieters and Kumar, 2021)

##############################################
#set path for get all risks function 
@app.route('/risks' )
def getAll():
    #Call getall the risks
    return jsonify(RisksDAO.getAllRisks())
    #curl http://127.0.0.1:5000/risks

##############################################
#set path to get archived risks function veRisks
@app.route('/risks/a' )
def getArchive():
    #call get the archived risks
    return jsonify(RisksDAO.getArchiveRisks())
    #curl http://127.0.0.1:5000/risks
##############################################
#set the path to get categories function 
@app.route('/risks/c' )
def getCats():
    #Get the risk categories 
    return jsonify(RisksDAO.getAllCategories())
    #curl http://127.0.0.1:5000/risks/c

##############################################
#set the path to the find risk by id function  
@app.route('/risks/<int:id>',methods=['GET']) #
def findById(id):
    #find risk by id
    return jsonify(RisksDAO.findByRiskID(id))
#curl http://127.0.0.1:5000/risks/72
##############################################
#set the path to the create risk function 

@app.route('/risks',methods=['POST'])
#Create risk
def createRisk():
    if not request.json:
        abort(400)
    #add risk to dict
    risk= {
        "Risk_Description": request.json["Risk_Description"],
        "Category_id": request.json["Category_id"],
        "Owner": request.json["Owner"],
        "Review_Frequency": request.json["Review_Frequency"],
        "RiskArea": request.json["RiskArea"],
        "Man_Ctrs": request.json["Man_Ctrs"],
        "Impact": request.json["Impact"],
        "Last_Review": request.json["Last_Review"],
        "Likelihood": request.json["Likelihood"],
        
        }    
    #pass risk dict to DAO
    return jsonify(RisksDAO.createRisk(risk))
    #curl -X "POST" http://127.0.0.1:5000/risks
    #curl -X "POST" -H "content-type:application/json" -d "{\"rid\":\"C1\",\"Risk_Description\":\"Risk+risingfromthediscontinuationoftheeuro50000fundingfromDESforGDPRandPensionsprojects\",\"RiskLevel\":\"3\",\"RiskArea\":\"Schools\",\"Man_Ctrs\":\"stuff\",\"Review_Frequency\":\"Annually\",\"Category\":\"3\",\"Impact\":\"3\",\"Likelihood\":\"3\",\"Owner\": \"DFET,DOSD\"}" http://127.0.0.1:5000/risks
##############################################

#set the path to the update risk function
@app.route('/risks/<int:id>',methods=['PUT'])
def updateRisk(id):
    #find the risk to be updated
    foundRisk = RisksDAO.findByRiskID(id)
    
    if foundRisk == {}:
        return jsonify({}), 404    
    #returns a list of dictionaries, even though only one risk is founrd
    currentRisks = RisksDAO.findByRiskID(id)
    currentRisk = currentRisks[0]
        
    currentRisk['Risk_Description'] =request.json["Risk_Description"]
    currentRisk['RiskLevel_id']=int((request.json["Impact"]) * int(request.json["Likelihood"])) , 
    currentRisk['Owner'] = request.json["Owner"] 
    currentRisk['Last_Review'] = request.json["Last_Review"] 
    currentRisk['Next_Review'] = request.json["Next_Review"] 
    currentRisk['Category_id']= request.json["Category_id"] 
    currentRisk['Review_Frequency']= request.json["Review_Frequency"] 
    currentRisk['RiskArea'] =request.json["RiskArea"] 
    currentRisk['Man_Ctrs'] =request.json["Man_Ctrs"] 
    currentRisk['Impact'] =request.json["Impact"] 
    currentRisk['Likelihood'] = request.json["Likelihood"] 
    currentRisk['Archive'] = request.json["Archive"] 

    return  jsonify(RisksDAO.UpdateRisk(currentRisk))
    #curl -X PUT http://127.0.0.1:5000/risks/2
    #curl -X "PUT" -H "content-type:application/json" -d "{\"Risk_Description\":\"NEW DESCRIPTION\",\"risklevel\":\"3\",\"Last_Review\":\"28-02-2020\",\"RiskArea\":\"Schools\",\"Review_Frequency\":\"Annually\",\"Owner\": \"DFET,DOSD\"}" http://127.0.0.1:5000/risks/2

##############################################

#se the path to the Delete risk function
@app.route('/risks/<int:id>',methods=['DELETE'])
def deleteRisk(id):
    #c
    RisksDAO.DeleteRisk(id)
    return jsonify({"done":True})
    #curl -X DELETE http://127.0.0.1:5000/risks/

##############################################
if __name__ == '__main__':
    #print("In if")
       app.run(debug=True)

