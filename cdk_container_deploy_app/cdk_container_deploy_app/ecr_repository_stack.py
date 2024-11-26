from aws_cdk import (
    NestedStack,
    aws_ecr as ecr,
    aws_ecr_assets as ecr_assets,
)
from constructs import Construct

class EcrRepositoryStack(NestedStack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create an ECR repository
        self.repository = ecr.Repository(
            self,
            "EcrRepository",
            repository_name="heart-risk-predict-app",
        )

        # Build and push Docker image to ECR
        self.docker_image_asset = ecr_assets.DockerImageAsset(
            self,
            "DockerImageAsset",
            directory="../",  # Replace with your app directory
            # repository_name=self.repository.repository_name,
        )
