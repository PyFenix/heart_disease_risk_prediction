import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_container_deploy_app.cdk_container_deploy_app.ecr_repository_stack import CdkContainerDeployAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_container_deploy_app/cdk_container_deploy_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkContainerDeployAppStack(app, "cdk-container-deploy-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
