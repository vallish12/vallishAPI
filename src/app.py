
import json
import logging






def lambda_handler(event, context, users_db=None):
    # Ensure users_db is initialized as an empty dictionary if it's None
    if users_db is None:
        users_db = {}

    endpoint = event['path']
    method = event['httpMethod']

    # Check if 'body' is present in the event and parse it if exists
    if 'body' in event and event['body']:
        body = json.loads(event['body'])
    else:
        body = {}

    if endpoint == '/get-all-users' and method == 'GET':
        # Return all users in users_db
        return {
            "statusCode": 200,
            "body": json.dumps(users_db)
        }
    elif endpoint == '/get-user-details' and method == 'GET':
        user_id = None
        if "queryStringParameters" in event and "user_id" in event["queryStringParameters"]:
            user_id = event["queryStringParameters"]["user_id"]
        if user_id and user_id in users_db:
            return {"statusCode": 200, "body": json.dumps(users_db[user_id])}
        return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}
    elif endpoint == '/create-user' and method == 'POST':
        user_id = body.get("user_id")
        if user_id in users_db:
            return {"statusCode": 400, "body": json.dumps({"message": "User already exists"})}
        users_db[user_id] = body
        return {"statusCode": 201, "body": json.dumps({"message": "User created"})}
    elif endpoint == '/update-user' and method == 'PUT':
        user_id = body.get("user_id")
        if user_id not in users_db:
            return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}
        users_db[user_id].update(body)
        return {"statusCode": 200, "body": json.dumps({"message": "User updated"})}

    elif endpoint == '/delete-user' and method == 'DELETE':
        user_id = body.get("user_id")
        if user_id not in users_db:
            return {"statusCode": 404, "body": json.dumps({"message": "User not found"})}
        del users_db[user_id]
        return {"statusCode": 200, "body": json.dumps({"message": "User deleted"})}

    return {"statusCode": 404, "body": json.dumps({"message": "Endpoint not found"})}


