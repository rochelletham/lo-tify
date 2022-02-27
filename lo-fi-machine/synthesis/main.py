import json
import boto3

def main(event, context):
    s3 = boto3.client('s3')
    
    # Output the bucket names
    print("This is from the synthesis directory AGAIN AGAIN AGAIN.")
    response = s3.get_object(
        Bucket="lo-tify",
        Key='text.txt',
    )
    
    body = response['Body'].read()
    print(body)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }