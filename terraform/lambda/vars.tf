variable "transcode_sizes" {
    description = "The sizes to transcode to"
}

variable "iam_policy_arn" {
    description = "Policy ARN to attach to lambda role"
}

variable "timeout" {
    description = "Lambda timeout"
}

variable "lambda_memory" {
    description = "Lambda RAM memory"
}

variable "aws_region" {
    description = "The aws region"
}

variable "runtime_env" {
    description = "Lambda runtime"
}

variable "lambda_handler" {
    description = "The lambda function handler"
}