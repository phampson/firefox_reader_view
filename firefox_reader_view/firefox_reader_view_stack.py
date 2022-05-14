from aws_cdk.aws_apigateway import StageOptions
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class FirefoxReaderViewStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, stage_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the lambda function in this stack
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.NODEJS_14_X,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
            memory_size=4096,
            timeout=Duration.seconds(60),
            environment={"stage_name": stage_name}
        )

        deployment_options = StageOptions(stage_name=stage_name)

        # Adding in a gateway to route the lambda
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
            deploy_options=deployment_options
        )
