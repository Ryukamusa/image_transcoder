terraform {
  required_providers {
    aws = "~> 2.60"
  }
}
provider "aws" {
  region = var.aws_region
}
