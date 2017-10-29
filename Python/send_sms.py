from Python import data_access
from flask import Flask, request, session
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import decimal
from datetime import datetime, timedelta

import re

SECRET_KEY = 'a secret key'  # change this to something appropriate
app = Flask(__name__)
app.config.from_object(__name__)

# Configure Twilio account with public key

account_sid = "AC07e0d1e1abc8f066bf7bc4b993cde73c"
auth_token = "37aa55f8cbae672f3e10e1d080321830"

client = Client(account_sid, auth_token)

"""message = client.messages.create(
    to="+16175155778", 
    from_="+16175051429",
    body="Hello from the script!")"""

# https://4d620adc.ngrok.io is the url currently hosting the script
@app.route("/", methods=['GET', 'POST'])
def hello_user():
	counter = session.get('counter', 0)  # Get counter value, otherwise initialize to 0

	counter += 1  # Increment counter
	session['counter'] = counter  # Set counter to incremented value

	# For hard resetting
	# session['counter'] = 0

	# For debug
	# print(counter)

	sender_num = request.values.get('From', None)  # number text recieved from
	sender_msg = request.values.get('Body', None)  # message body of text
	user = data_access.retreive_user(sender_num)  # name lookup in database

	# Second url for the web app to get the phone number in order to know which user the web service needs to speak to.
	url2 = "http://www.example.com/index.php?id=%s" % str(sender_num)



	respo = MessagingResponse()
	if counter == 1 and user is not None:  # Returning user first text
		respo.message("Welcome back {}! How far are you running today?".format(user['Name']))
		return str(respo)
	elif counter == 1 and user is None:  # New user first text
		respo.message("Welcome to FullCircle! Please send us your name")
		return str(respo)
	elif counter == 2 and user is None:  # New user registration (2nd text)
		# save from_number,msg_body to database
		respo.message("Thanks, you have been successfully registered! How far are you going to run today?")
		data_access.create_user(sender_num, sender_msg)
		session['counter'] = 1
		return str(respo)
	elif counter == 3:  # Back from route
		respo.message("Welcome back! Did you enjoy your route?")
		return str(respo)
	elif counter == 4:  # Feedback from route
		# import tone analyzer
		# number = toneAnalyze(msg_body)
		# if number > value, happy response
		# else sorry
		respo.message("Thanks for the feedback!")
		session['counter'] = 0
		return str(respo)

	arr = []
	unit = ""
	distance = 0.0

	# Error handling, checking if the user inputs "miles, kilometers" etc
	if "miles" in str(sender_msg):
		unit = "mi"
		arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(sender_msg))
	elif "mi" in str(sender_msg):
		unit = "mi"
		arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(sender_msg))
	elif "km" in str(sender_msg):
		unit = "km"
		arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(sender_msg))
	elif "kilometers" in str(sender_msg):
		unit = "km"
		arr = re.findall(r"[-+]?\d*\.\d+|\d+", str(sender_msg))
	else:
		respo.message("I didn't catch that, please enter how far you want to run in km/mi.")
		counter -= 1  # Decrement counter to prompt again
		session['counter'] = counter
		return str(respo)

	# Check if user entered a number in miles or kilometers
	if (unit == "km" and len(arr) != 0):
		# arr[0] is in km
		distance = float(arr[0])
	elif (unit == "mi" and len(arr) != 0):
		# convert arr[0]
		distance = float(arr[0]) * 1.60934
		unit = "km"
	else:
		respo.message("I didn't catch that, please enter how far you want to run in km/mi.")
		counter -= 1  # Decrement counter to prompt again
		session['counter'] = counter
		return str(respo)

	distance = round(distance, 1)  # 1 decimal place

	data_access.update_dist(sender_num, str(distance))

	# After user entered running details generate route with variable 'distance'
	respo.message("Generating a route for you! %s" % url2)
	return str(respo)


# Run app in debug
if __name__ == "__main__":
	app.run(debug=True)