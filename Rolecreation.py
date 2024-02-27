import boto3

# Specify the IAM role name
role_name = 'S3CrossRegionReplicationRole'

# Define the trust policy document
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

# Define the IAM role permissions policy
permissions_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetReplicationConfiguration",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        }
    ]
}

# Create an IAM client
iam_client = boto3.client('iam')

# Create the IAM role
try:
    create_role_response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=str(trust_policy)
    )
    
    # Attach permissions policy to the role
    attach_policy_response = iam_client.put_role_policy(
        RoleName=role_name,
        PolicyName='S3CrossRegionReplicationPolicy',
        PolicyDocument=str(permissions_policy)
    )
    
    print("IAM role for S3 cross-region replication created successfully!")
    
except Exception as e:
    print("Error creating IAM role:", e)
