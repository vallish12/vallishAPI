
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)



print('hi vallish')
def lambda_handler(event, context):
    endpoint = event['path']
    print('Hello world!')
    logger.info(f"Received request for endpoint: {endpoint}")
    if endpoint == '/get-all-users':
        #implement your logic
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "processing get-all-users",
                # "location": ip.text.replace("\n", "")
            }),
        }
    elif endpoint == "/get-user-details":
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "processing get-user-details",
                # "location": ip.text.replace("\n", "")
            }),
        }

    return {
        "statusCode": 404,
        "body": json.dumps({
            "message": "error",
            # "location": ip.text.replace("\n", "")
        }),
    }
