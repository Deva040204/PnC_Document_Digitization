
# AWS Setup Checklist for P&C Document Digitization Project

## ✅ AWS Region
- Choose and configure a region (e.g., `us-east-1`, `ap-south-1`)

## 🔐 IAM Configuration
### IAM Role for Lambda
- Permissions: `textract:*`, `sagemaker:InvokeEndpoint`, `s3:*`, `sns:Subscribe`
- Trust relationship: Lambda

### IAM Role for Textract (Optional)
- Allow Textract to write to S3 and trigger SNS

### IAM User or Federated Role (for deployment)
- Access Key ID + Secret Access Key

## 🪣 Amazon S3 Buckets
| Bucket Type        | Purpose                     | Example Name             |
|--------------------|-----------------------------|--------------------------|
| Input Bucket       | Store uploaded PDFs/images  | `pnc-doc-input-bucket`   |
| Output Bucket      | Store JSON outputs          | `pnc-doc-output-bucket`  |
| Lambda Code Bucket | Store Lambda deployment zips| `pnc-lambda-code-bucket` |

## 🤖 AWS Lambda Functions
### UploadTriggerLambda
- Starts Textract job on new document upload

### TextractProcessorLambda
- Waits for Textract output, invokes SageMaker, stores JSON output

## 📄 Amazon Textract (Async)
- Requires IAM role for access
- SNS Topic ARN for completion notification
- Intermediate output stored in S3

## 📬 Amazon SNS
- Topic ARN for Textract job notification
- Must trigger TextractProcessorLambda

## 🤖 Amazon SageMaker Endpoint
- Endpoint name (e.g., `pnc-nlp-endpoint`)
- IAM role with `sagemaker:InvokeEndpoint`
- Instance type (e.g., `ml.t2.medium`)
- Model image or endpoint script

## 🛠️ CloudFormation Parameters
- `InputBucketName`
- `OutputBucketName`
- `SageMakerEndpointName`
- `NotificationTopicARN`
- `LambdaExecutionRole`

## 📈 Optional Monitoring
- CloudWatch log groups for Lambda
- AWS Cost Explorer for monitoring cost

---

## ✅ Summary Checklist

| Resource                     | Required Detail                  |
|-----------------------------|----------------------------------|
| AWS Region                  | ✅                               |
| IAM Roles (Lambda/SageMaker)| ✅                               |
| Input/Output Buckets (S3)   | ✅                               |
| SageMaker Endpoint Name     | ✅                               |
| Textract Async Setup        | ✅ SNS Topic, Lambda trigger     |
| CloudFormation Parameters   | ✅                               |
| Lambda Code Bucket (S3)     | ✅                               |
| GitLab CI/CD Token (Optional)| ✅ if using automation           |
