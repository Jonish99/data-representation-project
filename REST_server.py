#Risk Register REST Server
#Author Jon Ishaque GMIT Data Representation

from flask import Flask,url_for,request,redirect,abort,jsonify,render_template
from RisksDAO import RisksDAO

app = Flask(__name__, 
        static_url_path='',
        static_folder='staticpages')

@app.route('/' )#index function
def index():
    #url_for('static', filename='index.html')
    return app.send_static_file('index.html')  #(Pieters and Kumar, 2021)

   # return ("balls") 
    #     url_for('index')
    #redirect(url_for('index'))
    #return "Hello World"
    #curl http://127.0.0.1:5000
#all risks   
@app.route('/risks' )
def getAll():
    #see all the risks
    return jsonify(RisksDAO.getAllRisks())
    #curl http://127.0.0.1:5000/risks

#find risk by id
@app.route('/risks/<int:id>' ) #
def findById(id):
   #foundRisks = list(filter(lambda t: t["id"]== id, risks))
    #print (foundRisks)
    #if len(foundRisks) == 0:
    #    return jsonify({}), 204    
    return jsonify(RisksDAO.findByRiskID(id))
#curl http://127.0.0.1:5000/risks/72

#Create risk
@app.route('/risks',methods=['POST'])
def createRisk():
    #print(request.json["rid"])
    if not request.json:
        abort(400)
    risk= {"rid": request.json["rid"], # need a function to do this.
        "Risk_Description": request.json["Risk_Description"],
        "RiskLevel": request.json["RiskLevel"],
        "Owner": request.json["Owner"],
        "Review_Frequency": request.json["Review_Frequency"],
        "RiskArea": request.json["RiskArea"],
        "Man_Ctrs": request.json["Man_Ctrs"],
        "Impact": request.json["Impact"],
        "Likelihood": request.json["Likelihood"],
        "Category": request.json["Category"]
        }
    
    #return jsonify(risk)
    #risks.append(risk)
    #nextid +=1
    return jsonify(RisksDAO.createRisk(risk))
    #curl -X "POST" http://127.0.0.1:5000/risks
    #curl -X "POST" -H "content-type:application/json" -d "{\"rid\":\"C1\",\"Risk_Description\":\"Risk+risingfromthediscontinuationoftheeuro50000fundingfromDESforGDPRandPensionsprojects\",\"RiskLevel\":\"3\",\"RiskArea\":\"Schools\",\"Man_Ctrs\":\"stuff\",\"Review_Frequency\":\"Annually\",\"Category\":\"3\",\"Impact\":\"3\",\"Likelihood\":\"3\",\"Owner\": \"DFET,DOSD\"}" http://127.0.0.1:5000/risks

#update risk
@app.route('/risks/<int:id>',methods=['PUT'])
def updateRisk(id):
    foundRisk = RisksDAO.findByRiskID(id)
    print (foundRisk)
    if foundRisk == {}:
        return jsonify({}), 404    
    
    currentRisks = RisksDAO.findByRiskID(id)#returns a list of dictionary, even though only one risk is founrd
    currentRisk = currentRisks[0]
    
    if "Risk_Description" in request.json:
        currentRisk['Risk_Description'] =request.json["Risk_Description"]
    currentRisk['RiskLevel']="9" #function required
    if "Owner" in request.json:
        currentRisk['Owner'] = request.json["Owner"] 
    if "Last_Review" in request.json:
        currentRisk['Last_Review'] =""# request.json["Last_Review"] 

    currentRisk['Next_Review'] = ""#function reuried""
    if "Review_Frequency" in request.json:
        currentRisk['Review_Frequency']= request.json["Review_Frequency"] 
    if "RiskArea" in request.json:
        currentRisk['RiskArea'] =request.json["RiskArea"] 
    if "Man_Ctrs" in request.json:
        currentRisk['Man_Ctrs'] =request.json["Man_Ctrs"] 
    if "Impact" in request.json:
        currentRisk['Impact'] =request.json["Impact"] 
    if "Likelihood" in request.json:
        currentRisk['Likelihood'] = request.json["Likelihood"] 





    return  jsonify(RisksDAO.UpdateRisk(currentRisk))
    #curl -X PUT http://127.0.0.1:5000/risks/2
    #curl -X "PUT" -H "content-type:application/json" -d "{\"Risk_Description\":\"NEW DESCRIPTION\",\"risklevel\":\"3\",\"Last_Review\":\"28-02-2020\",\"RiskArea\":\"Schools\",\"Review_Frequency\":\"Annually\",\"Owner\": \"DFET,DOSD\"}" http://127.0.0.1:5000/risks/2
#delete risk
@app.route('/risks/<int:id>',methods=['DELETE'])
def deleteRisk(id):
    RisksDAO.DeleteRisk(id)
    return jsonify({"done":True})
    #curl -X DELETE http://127.0.0.1:5000/risks/

if __name__ == '__main__':
    #print("In if")
       app.run(debug=True)

#