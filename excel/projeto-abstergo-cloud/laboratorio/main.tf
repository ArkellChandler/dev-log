# Configuração Terraform para Abstergo Cloud - Laboratório de Custos

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# 1. Bucket S3 com Intelligent-Tiering para Dados Genômicos
resource "aws_s3_bucket" "abstergo_genomics_data" {
  bucket = "abstergo-genomics-data-2026-unique" # Nome único global

  tags = {
    Name        = "Abstergo Genomics"
    Dept        = "Laboratorio"
    CostCenter  = "Research-01"
  }
}

# Configuração de Intelligent-Tiering (Otimização Automática de Armazenamento)
resource "aws_s3_bucket_intelligent_tiering_configuration" "tiering_config" {
  bucket = aws_s3_bucket.abstergo_genomics_data.id
  name   = "EntireBucketIntelligentTiering"

  tiering {
    access_tier = "ARCHIVE_ACCESS"
    days        = 90
  }

  tiering {
    access_tier = "DEEP_ARCHIVE_ACCESS"
    days        = 180
  }
}

# 2. Busca da AMI mais recente do Amazon Linux 2
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# 3. Solicitação de Instância EC2 Spot (Economia de até 90%)
resource "aws_spot_instance_request" "abstergo_spot_worker" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t3.micro" # Instância de baixo custo para laboratório
  
  # O preço spot é definido pelo mercado; se o preço subir acima deste valor, a instância é terminada
  spot_price    = "0.01" 
  wait_for_fulfillment = true
  spot_type     = "one-time"

  tags = {
    Name = "Abstergo Spot Worker"
    Project = "Genomics-Processing"
  }
}
