import boto3

def create_user(phonenumber,name,coords=None):
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
