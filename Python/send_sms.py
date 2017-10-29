from flask import Flask, request, session
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime, timedelta

import re

SECRET_KEY = 'a secret key'
app = Flask(__name__)
app.config.from_object(__name__)

account_sid = "AC07e0d1e1abc8f066bf7bc4b993cde73c"
auth_token  = "37aa55f8cbae672f3e10e1d080321830"

client = Client(account_sid, auth_token)

"""message = client.messages.create(
    to="+16175155778", 
    from_="+16175051429",
    body="Hello from the script!")"""

#https://4d620adc.ngrok.io 
@app.route("/", methods=['GET', 'POST'])
def hello_user():
    """Respond and greet the caller by name."""

    

    counter = session.get('counter', 0)

    counter += 1

    session['counter'] = counter
    #session['counter'] = 0
    
    expires=datetime.utcnow() + timedelta(minutes=1)

    print(counter)


    callers = {
        "+14158675309": "Curious George",
        "+14158675310": "Boots",
        "+14158675311": "Virgil",
        "+16176948759": "Gene",
        "+16175155778": "Pablo",
    }
    
    from_number = request.values.get('From', None)
    msg_body = request.values.get('Body', None)

    message2 = callers[from_number] if from_number in callers else "User"

    #flag = True
    respo = MessagingResponse()
    if(counter==1 and (from_number in callers)):
        respo.message("Welcome back {}! How far are you running today?".format(message2))
        return str(respo)
    elif(counter==1 and (from_number not in callers)):
        respo.message("Welcome to FullCircle! Please send us your name")
        return str(respo)
    elif(counter==2 and (from_number not in callers)):
        # save from_number,msg_body to database
        respo.message("Thanks, you have been successfully registered!")
        session['counter'] = 0
        return str(respo)
    
    arr = []
    unit = ""
    distance = 0.0
    #Error handling, checking if the user inputs "miles" etc
    #while flag:    
    if "miles" in str(msg_body):
        unit = "mi"
        arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(msg_body))
    elif "mi" in str(msg_body):
        unit = "mi"
        arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(msg_body))  
    elif "km" in str(msg_body):
        unit = "km"
        arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(msg_body))  
    elif "kilometers" in str(msg_body):
        unit = "km"
        arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(msg_body))  
    else:
        respo.message("I didn't catch that, please enter how far you want to run in km/mi.")
        return str(respo)


    if(unit=="km" and len(arr) != 0):
        #arr[0] is in km
        distance = float(arr[0])
    elif(unit=="mi" and len(arr) != 0):
        #convert arr[0]
        distance = float(arr[0])*1.60934
        unit="km"
    else:
        respo.message("I didn't catch that, please enter how far you want to run in km/mi.")
        return str(respo)
    
    distance = round(distance,1)

    #respo.message("You want to run {} {}".format(distance, unit))
    respo.message("Generating a route for you!")
    session['counter'] = 0
    return str(respo)

    '''
    message = callers[from_number] if from_number in callers else "Monkey"

    resp = MessagingResponse()
    resp.message("{}, thanks for the message!".format(message))

    return str(resp)
    '''

if __name__ == "__main__":
    app.run(debug=True)
