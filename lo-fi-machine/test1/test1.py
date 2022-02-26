import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Output the bucket names
    print("THIS IS EVEN MORE NEW!")
    print('Existing object:')
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

# aws lambda update-function-code --function-name hello-world --zip-file fileb://test-1.zip