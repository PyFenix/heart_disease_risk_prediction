#!/bin/bash

echo "*************************"
echo "Setting up the AWS account"
echo "*************************"

# Load environment variables from the .env file
if [ -f .env ]; then
  echo "Loading environment variables from .env file..."
  set -o allexport
  source .env
  set +o allexport
else
  echo ".env file not found!"
  exit 1
fi

# Configure AWS CLI using environment variables
echo "Configuring AWS CLI using environment variables..."
aws configure set aws_access_key_id "$AWS_ACCESS_KEY_ID"
aws configure set aws_secret_access_key "$AWS_SECRET_ACCESS_KEY"
aws configure set default.region "$AWS_DEFAULT_REGION"
aws configure set default.output "$AWS_OUTPUT_FORMAT"

# Get the AWS Account ID
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
if [ $? -ne 0 ]; then
  echo "Failed to retrieve AWS account ID"
  exit 1
fi

echo "Account Id: $ACCOUNT_ID"
echo "AWS CLI configured!"
echo "*************************"

# Generate a Key Pair for SSH Access
echo "*************************"
echo "Generating a Key Pair for SSH Access"

KEY_PAIR_NAME="ec2-key-pair"
KEY_PAIR_FILE="$KEY_PAIR_NAME.pem"

# Check if the local key pair file already exists
if [ -f "$KEY_PAIR_FILE" ]; then
  echo "A local key pair file '$KEY_PAIR_FILE' already exists."
  read -p "Do you want to delete it and create a new one? (Y/N): " user_input
  if [[ "$user_input" =~ ^[Yy]$ ]]; then
    rm -f "$KEY_PAIR_FILE"
    echo "Deleted local key pair file '$KEY_PAIR_FILE'."
  else
    echo "Key pair generation aborted by user."
    exit 0
  fi
fi

# Attempt to create the key pair
echo "Creating the key pair on AWS..."
KEY_MATERIAL=$(aws ec2 create-key-pair --key-name "$KEY_PAIR_NAME" --query 'KeyMaterial' --output text)
if [ $? -ne 0 ]; then
  echo "Failed to create key pair on AWS."
  exit 1
fi

# Save the private key to a file
echo "$KEY_MATERIAL" > "$KEY_PAIR_FILE"

# Verify that the key file was created
if [ -f "$KEY_PAIR_FILE" ]; then
  echo "Key pair generated and saved to: $KEY_PAIR_FILE"
else
  echo "Failed to save key file."
  exit 1
fi

# Set appropriate permissions on the private key file
chmod 400 "$KEY_PAIR_FILE"
echo "Permissions set on the private key file."

echo "Key Pair generated!"
echo "*************************"

# Bootstrap CDK
echo "Bootstrapping CDK..."
npx cdk bootstrap "$ACCOUNT_ID/$AWS_DEFAULT_REGION"
if [ $? -ne 0 ]; then
  echo "CDK bootstrap failed."
  exit 1
fi

echo "CDK bootstrap complete!"
