from flask import Flask
from twilio.rest import Client
from flask import request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

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
    # Try adding your own number to this list!
    callers = {
        "+14158675309": "Curious George",
        "+14158675310": "Boots",
        "+14158675311": "Virgil",
        "+16176948759": "Gene",
        "+16175155778": "Pablo",
    }
    
    from_number = request.values.get('From', None)
    msg_body = request.values.get('Body', None)
    print(from_number)
    print(msg_body)

    message2 = callers[from_number] if from_number in callers else "Monkey"

    #flag = True
    respo = MessagingResponse()
    #respo.message("{}, thanks for the message!".format(message2))

    #Error handling, checking if the user inputs "miles" etc
    #while flag:    
    if "miles" in msg_body:
        respo.message("{}, thanks for the correct inputs!".format(message2))
            
    elif "mi" in msg_body:
        respo.message("{}, thanks for the correct inputs!".format(message2))
            
    elif "km" in msg_body:
        respo.message("{}, thanks for the correct inputs!".format(message2))
            
    elif "kilometers" in msg_body:
        respo.message("{}, thanks for the correct inputs!".format(message2))
            
    else:
        respo.message("{}, wrong inputs!".format(message2))

    return str(respo)

    '''
    message = callers[from_number] if from_number in callers else "Monkey"

    resp = MessagingResponse()
    resp.message("{}, thanks for the message!".format(message))

    return str(resp)
    '''

if __name__ == "__main__":
    app.run(debug=True)





