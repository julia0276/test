import urllib
import json
import os
from flask import Flask
from flask import request
from flask import.make_response

#Flask app shoul start in global layout
app=Flask(__name__)

@app.route('/webhook', method=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req,indent=4))
    res=makeWebhookResult(req)
    res=json.dumps(res,indent=4)
    print(res)
    r=make_response(res)
    r.headers['Content-Type']='application/json'
    return r

def makeWebhookResult(req) :
    if req.get("result").get("action")!= "ineterest":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    name = parameters.get("bank-name")
    bank = {'Federal Bank':'6.7%', 'Andhra Bank':'6.85%', 'Bandhan Bank':'7.15%'}
    speech = "The interest rate of" + name + " is " + str(bank[name])
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source" : "BankInterestRates"
    }

if __name__ == '__main__'
    port = int(os.getenv('PORT', 80))
    print("Starting app on port %d" % (port))
    app.run(debug=True, port=port, host='0.0.0.0')