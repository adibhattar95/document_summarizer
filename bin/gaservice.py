import flask
from flask import request, Flask
import json
from summarizer import FindSummary

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def checkApiStatus():
    return "Boom!! Api is working"


@app.route('/get_summary', methods = ['POST']) 
def summarise():
    article = json.loads(request.data.decode())['article']
    summaryObj = FindSummary('../config/config2.yaml')
    summaryText = summaryObj.summarize(article)
    return summaryText

@app.route('/about_us', methods = ['POST'])
def dummyRequest():
    jsonStr = request.data.decode()
    dataDict = json.loads(jsonStr)
    article = dataDict['article']
    print('printing data: \n', article)
    return "Ok, request works"
    
if __name__ == "__main__":
    app.run(host = 'localhost', port = 8080)