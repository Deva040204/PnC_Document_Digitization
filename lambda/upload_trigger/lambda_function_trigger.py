
import boto3

def lambda_handler(event, context):
    textract = boto3.client('textract')
    s3_info = event['Records'][0]['s3']
    bucket = s3_info['bucket']['name']
    document = s3_info['object']['key']

    response = textract.start_document_text_detection(
        DocumentLocation={'S3Object': {'Bucket': bucket, 'Name': document}},
        NotificationChannel={
            'RoleArn': 'arn:aws:iam::<account-id>:role/TextractServiceRole',
            'SNSTopicArn': 'arn:aws:sns:<region>:<account-id>:TextractTopic'
        }
    )

    return {"JobId": response['JobId']}
