import boto3
import botocore
s3_client = boto3.client('s3')
lambda_function_name = 'di_risksandbox_function_beta'
bucket_name = 'issuing-risk-pcstg-uat-tsysuatpciauthna-us-east-1'
Prefix = 'pc/uat/sandbox/1241/'
s3_client.put_bucket_notification_configuration(
    Bucket='issuing-risk-pcstg-uat-tsysuatpciauthna-us-east-1',
    NotificationConfiguration={
        'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:235744464007:function:di_risksandbox_function_beta',
                'Events': ['s3:ObjectCreated:*'],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'Prefix',
                                'Value': pc/uat/sandbox/1241/
                            }
                        ]
                    }
                }
            },
            {
                'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:235744464007:function:di_risksandbox_function_beta',
                'Events': ['s3:ObjectCreated:*'],
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {
                                'Name': 'Prefix',
                                'Value': pc/uat/sandbox/2400/
                            }
                        ]
                    }
                }
            }
        ]
    }
)
