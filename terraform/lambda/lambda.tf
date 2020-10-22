resource "aws_lambda_function" "transcode" {
  filename      = "resources/lambda.zip"
  function_name = "s3-transcode"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda-transcode.lambda_handler"

  source_code_hash = filebase64sha256("resources/lambda.zip")

  runtime = "python3.8"
  layers = [aws_lambda_layer_version.pil_layer.arn]
  timeout = var.timeout
  memory_size = var.lambda_memory
  tags = {
    Name = "s3-transcode"
    Terraform = "true"
  }

  depends_on = [aws_s3_bucket.transcoded]
  environment {
    variables = {
      TRANSCODE_SIZES = var.transcode_sizes
      S3_DESTINATION_BUCKET = aws_s3_bucket.transcoded.id
    }
  }
}

resource "aws_lambda_layer_version" "pil_layer" {
  filename   = "resources/pil.zip"
  layer_name = "pil-package"

  compatible_runtimes = ["python3.8"]
}


resource "aws_iam_role" "lambda_exec_role" {
  name        = "lambda-s3-access"
  path        = "/"
  description = "Allows Lambda Function to call AWS services on your behalf."

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "role_policy_attachment" {
  role       = aws_iam_role.lambda_exec_role.name
  count      = "${length(var.iam_policy_arn)}"
  policy_arn = "${var.iam_policy_arn[count.index]}"
}
