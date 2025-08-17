# Deployment Guide: P&C Document Digitization (Textract + SageMaker)

## 1. Prerequisites
- AWS Account with Textract, SageMaker, Lambda, and S3 access
- IAM roles with correct permissions
- GitLab repo with dev branch

## 2. Setup S3 Buckets
Create two buckets:
- `your-input-bucket` for uploading PDFs/images
- `your-output-bucket` for storing JSON outputs

## 3. Deploy CloudFormation Stack
Update `template.yaml` with:
- Bucket names
- SageMaker endpoint name
Then deploy using AWS Console or CLI.

## 4. Upload Lambda Code
Zip each Lambda function (`upload_trigger`, `textract_processor`) and upload to a deployment bucket.

## 5. Train or Deploy SageMaker Model
Use `bert_model.py` or the inference notebook to create an endpoint.
Ensure it returns the structured output expected by Textract processor.

## 6. Test End-to-End
Upload a sample PDF to the input bucket and verify output JSON in output bucket.

## 7. Monitor & Optimize
Use CloudWatch for logs and set endpoint to stop when idle (or use batch transform).
