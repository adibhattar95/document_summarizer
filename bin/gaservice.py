import flask
from flask import request, Flask
import json
from summarizer import FindSummary

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def checkApiStatus():
    return "Boom!! Api is working"


@app.route('/get_summary', methods = ['GET']) 
def summarise():
    summaryObj = FindSummary('../config/config2.yaml')
    summaryText = summaryObj.summarize()
    return summaryText
    
if __name__ == "__main__":
    app.run(host = 'localhost', port = 8080)