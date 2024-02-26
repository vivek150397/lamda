import boto3

s3_client = boto3.client('s3')

bucket_name = 'issuing-risk-pcstg-uat-tsysuatpciauthna-us-east-1'
lambda_function_name = 'di_risksandbox_function_beta'

prefixes = ['pc/uat/sandbox/1241/', 'pc/uat/sandbox/2400/']

lambda_arn = f'arn:aws:lambda:us-east-1:235744464007:function:{lambda_function_name}'

lambda_configurations = []

for prefix in prefixes:
    lambda_configurations.append({
        'LambdaFunctionArn': lambda_arn,
        'Events': ['s3:ObjectCreated:*'],
        'Filter': {
            'Key': {
                'FilterRules': [
                    {
                        'Name': 'Prefix',
                        'Value': prefix
                    }
                ]
            }
        }
    })

s3_client.put_bucket_notification_configuration(
    Bucket=bucket_name,
    NotificationConfiguration={
        'LambdaFunctionConfigurations': lambda_configurations
    }
)
