from aws_cdk import NestedStack, aws_ec2 as ec2, CfnOutput, aws_iam as iam
from constructs import Construct

import requests


class Ec2InstanceStack(NestedStack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        image_uri: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieve the account ID
        account_id = self.account
        region = self.region
        key_pair_name = "ec2-key-pair"


        self.my_ip = requests.get("http://whatismyip.akamai.com/").text.strip()

        # Read the user data script
        with open("user_data/ec2_user_data.sh", "r") as f:
            user_data_script = f.read()

        # Replace placeholders
        user_data_script = user_data_script.replace("${AWS::IMAGE_URI}", image_uri)
        user_data_script = user_data_script.replace("${AWS::AccountId}", account_id)
        user_data_script = user_data_script.replace("${AWS::Region}", region)

        vpc = ec2.Vpc(
            self,
            "MyVpc",
            max_azs=2,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public-subnet-1",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                )
            ],
        )

        # Create a security group
        security_group = ec2.SecurityGroup(
            self,
            "EC2SecurityGroup",
            vpc=vpc,
            description="Allow SSH and HTTP access",
            allow_all_outbound=True,
        )

        # Allow SSH access from your IP
        my_ip_ec2 = ec2.Peer.ipv4(f"{self.my_ip}/32")
        security_group.add_ingress_rule(
            peer=my_ip_ec2,
            connection=ec2.Port.tcp(22),
            description="Allow SSH access from my IP",
        )
                # Allow HTTP access from anywhere
        security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP access from anywhere",
        )

        # Allow SSH access from EC2 Instance Connect IP addresses
        ec2_instance_connect_ips = [
            "18.206.107.24/29",
        ]
        for cidr in ec2_instance_connect_ips:
            security_group.add_ingress_rule(
                peer=ec2.Peer.ipv4(cidr),
                connection=ec2.Port.tcp(22),
                description="Allow SSH access from EC2 Instance Connect",
            )

        # IAM role for EC2 instance
        ec2_role = iam.Role(
            self,
            "EC2InstanceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )

        # Attach policies to the role
        ec2_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2ContainerRegistryReadOnly")
        )
        ec2_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSSMManagedInstanceCore")
        )

        # Create the EC2 instance
        self.ec2_instance = ec2.Instance(
            self,
            "EC2Instance",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2(),
            vpc=vpc,
            # key_name=key_pair_name,
            key_pair=ec2.KeyPair.from_key_pair_name(self, "KeyPair", key_pair_name),
            role=ec2_role,
            security_group=security_group,
            associate_public_ip_address=True,
            user_data=ec2.UserData.custom(user_data_script),
        )

        # # Output Instance ID
        # CfnOutput(self, "InstanceId", value=self.ec2_instance.instance_id)

        # Output the public DNS of the EC2 instance
        CfnOutput(
            self,
            "EC2PublicDNS",
            value=self.ec2_instance.instance_public_dns_name,
            description="Public DNS of the EC2 instance",
        )
