
import boto3
import json

def lambda_handler(event, context):
    textract = boto3.client('textract')
    job_id = json.loads(event['Records'][0]['Sns']['Message'])['JobId']
    
    result = textract.get_document_text_detection(JobId=job_id)
    full_text = '\n'.join([b['Text'] for b in result['Blocks'] if b['BlockType'] == 'LINE'])

    # Call SageMaker endpoint
    sagemaker = boto3.client('sagemaker-runtime')
    endpoint_name = 'YOUR_ENDPOINT_NAME'
    response = sagemaker.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/plain',
        Body=full_text
    )

    output = response['Body'].read().decode()
    s3 = boto3.client('s3')
    s3.put_object(
        Bucket='your-output-bucket',
        Key=f'extracted/{job_id}.json',
        Body=output
    )
