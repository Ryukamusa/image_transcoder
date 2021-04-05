resource "aws_s3_bucket_notification" "s3_event_trigger" {
  bucket = "insert-data-tf"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.transcode.arn}"
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".jpg"
  }
  
  lambda_function {
    lambda_function_arn = "${aws_lambda_function.transcode.arn}"
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".png"
  }
}


resource "aws_lambda_permission" "test" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.transcode.arn
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.insert.arn
}

resource "aws_s3_bucket" "insert" {
  bucket = "insert-data-tf"
  acl    = "private"

  tags = {
    Name        = "insert-data-tf"
    Terraform   = "true"
  }
}

resource "aws_s3_bucket" "transcoded" {
  bucket = "transcoded-data-tf"
  acl    = "private"

  tags = {
    Name        = "transcoded-data-tf"
    Terraform   = "true"
  }
}