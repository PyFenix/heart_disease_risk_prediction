#!/bin/bash
# Install updates and Docker
yum update -y
amazon-linux-extras install docker -y
service docker start
usermod -a -G docker ec2-user

# Enable Docker to start on boot
chkconfig docker on

# Install AWS CLI (already installed on Amazon Linux 2, but include for completeness)
# yum install -y aws-cli

# Log in to ECR
$(aws ecr get-login --no-include-email --region ${AWS::Region})

# Pull the Docker image from ECR
docker pull ${AWS::IMAGE_URI}

# Run the Docker container
docker run -d -p 80:8000 ${AWS::IMAGE_URI}
