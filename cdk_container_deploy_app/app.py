#!/usr/bin/env python3
from aws_cdk import Stack, App, CfnOutput
from constructs import Construct
from cdk_container_deploy_app.ecr_repository_stack import EcrRepositoryStack
from cdk_container_deploy_app.ec2_instance_stack import Ec2InstanceStack

app = App()

root_stack = Stack(app, "RootStack")

# Instantiate ECR stack
ecr_stack = EcrRepositoryStack(root_stack, "EcrStack")

# Get the image uri to pass it to the ec2 instance
image_uri = ecr_stack.docker_image_asset.image_uri

# Instantiate EC2 stack
ec2_stack = Ec2InstanceStack(root_stack, "Ec2Stack", image_uri=image_uri)

# MainStack(app, stack_id)

app.synth()

CfnOutput(
    root_stack,
    "InstancePublicIP",
    value=ec2_stack.ec2_instance.instance_public_ip,
    description="Public IP address of the EC2 instance",
)
