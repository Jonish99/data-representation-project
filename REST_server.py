#REST applicaiton for risk register
#Author Jon Ishaque GMIT Data Representation
#Provide access for http queries


#call libraries
from flask import Flask,url_for,request,redirect,abort,jsonify,render_template
#import RiskDAO class from RisksDAO
from RisksDAO import RisksDAO
##############################################
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
#all risks   
@app.route('/risks' )
def getAll():
    #see all the risks
    return jsonify(RisksDAO.getAllRisks())
    #curl http://127.0.0.1:5000/risks

##############################################
#all risks   
@app.route('/risks/a' )
def getArchive():
    #see all the risks
    #print("in archive/server")
    return jsonify(RisksDAO.getArchiveRisks())
    #curl http://127.0.0.1:5000/risks

##############################################
#all risks   
@app.route('/risks/c' )
def getCats():
    #see all the risks
    return jsonify(RisksDAO.getAllCategories())
    #curl http://127.0.0.1:5000/risks/c

##############################################
#find risk by id
@app.route('/risks/<int:id>',methods=['GET']) #
def findById(id):
    #debug
    #foundRisks = list(filter(lambda t: t["id"]== id, risks))
    #print (id)
    #if len(foundRisks) == 0:
    #    return jsonify({}), 204    
    return jsonify(RisksDAO.findByRiskID(id))
#curl http://127.0.0.1:5000/risks/72
##############################################

#Create risk
@app.route('/risks',methods=['POST'])
def createRisk():
    #print(request.json["rid"])
    if not request.json:
        abort(400)
    #impact = int(request.json["Impact"]) 
    
    risk= {
        "Risk_Description": request.json["Risk_Description"],
        #"RiskLevel_id": int((request.json["Impact"]) * int(request.json["Likelihood"])) ,
        "Category_id": request.json["Category_id"],
        "Owner": request.json["Owner"],
        "Review_Frequency": request.json["Review_Frequency"],
        "RiskArea": request.json["RiskArea"],
        "Man_Ctrs": request.json["Man_Ctrs"],
        "Impact": request.json["Impact"],
        "Last_Review": request.json["Last_Review"],
        "Likelihood": request.json["Likelihood"],
        
        }
    #print(risk)
    #return jsonify(risk)
    #risks.append(risk)
    #nextid +=1
    
    return jsonify(RisksDAO.createRisk(risk))
    #curl -X "POST" http://127.0.0.1:5000/risks
    #curl -X "POST" -H "content-type:application/json" -d "{\"rid\":\"C1\",\"Risk_Description\":\"Risk+risingfromthediscontinuationoftheeuro50000fundingfromDESforGDPRandPensionsprojects\",\"RiskLevel\":\"3\",\"RiskArea\":\"Schools\",\"Man_Ctrs\":\"stuff\",\"Review_Frequency\":\"Annually\",\"Category\":\"3\",\"Impact\":\"3\",\"Likelihood\":\"3\",\"Owner\": \"DFET,DOSD\"}" http://127.0.0.1:5000/risks
##############################################

#update risk
@app.route('/risks/<int:id>',methods=['PUT'])
def updateRisk(id):
    foundRisk = RisksDAO.findByRiskID(id)
    #print (foundRisk)
    if foundRisk == {}:
        return jsonify({}), 404    
    
    currentRisks = RisksDAO.findByRiskID(id)#returns a list of dictionary, even though only one risk is founrd
    currentRisk = currentRisks[0]
    #print("in server:")
    print(currentRisk)
    
    currentRisk['Risk_Description'] =request.json["Risk_Description"]
    currentRisk['RiskLevel_id']=int((request.json["Impact"]) * int(request.json["Likelihood"])) , #function required
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

#delete risk
@app.route('/risks/<int:id>',methods=['DELETE'])
def deleteRisk(id):
    RisksDAO.DeleteRisk(id)
    return jsonify({"done":True})
    #curl -X DELETE http://127.0.0.1:5000/risks/

##############################################
if __name__ == '__main__':
    #print("In if")
       app.run(debug=True)

#