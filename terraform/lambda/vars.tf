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
