import boto3
import decimal

def create_user(phonenumber,name,coords=None, dist=None):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('UserData')
	table.put_item(
		Item={
			'Phonenumber': phonenumber,
			'Distance': dist,
			'Name': name,
		}
	)

def update_dist(phonenumber, distance):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('UserData')
	table.update_item(
		Key={
			'Phonenumber': phonenumber
		},
		UpdateExpression='SET Distance = :Distance',
		ExpressionAttributeValues={
			':Distance': distance
		}
	)

def retreive_user(phonenumber):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('UserData')
	try:
		response = table.get_item(
			Key={
				'Phonenumber': phonenumber
			}
		)
		item = response['Item']
		return item
	except KeyError as e:
		return None