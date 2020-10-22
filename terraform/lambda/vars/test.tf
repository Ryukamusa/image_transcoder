aws_region="eu-central-1"
transcode_sizes="1024,2048"
timeout=40
lambda_memory=1024
iam_policy_arn=["arn:aws:iam::aws:policy/AmazonS3FullAccess","arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"]
runtime_env="python3.8"
lambda_handler="lambda-transcode.lambda_handler"