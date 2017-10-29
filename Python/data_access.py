import boto3

def create_user(phonenumber,name,coords):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('UserData')
	table.put_item(
		Item={
			'Phonenumber':phonenumber,
			'Name':name,
			'Coordinates':coords
		}
	)


def retreive_user(phonenumber):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('UserData')
	try:
		response = table.get_item(
			Key={
				'Phonenumber' : phonenumber,
			}
		)
		item = response['Item']
		return item
	except KeyError as e:
		return None


#create_user('+16508633802','Nick',{'42.351083','-71.110179'})
pablo = '+16175155778'
nick = '+16508633802'
pabloDB = retreive_user(pablo)
nickDB = retreive_user(nick)


if(pabloDB is not None):
	coords = list(pabloDB['Coordinates'])
	lat = coords[0]
	long = coords[1]
	print('Pablo is at '+str(lat)+", "+str(long))
else:
	print('Couldnt find that bitch..... will add')
