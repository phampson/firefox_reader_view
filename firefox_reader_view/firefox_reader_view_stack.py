from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)


class FirefoxReaderViewStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the lambda function in this stack
        my_lambda = _lambda.Function(
            self, 'HelloHandler',
            runtime=_lambda.Runtime.NODEJS_14_X,
            code=_lambda.Code.from_asset('lambda'),
            handler='hello.handler',
        )

        # Adding in a gateway to route the lambda
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=my_lambda,
        )

        # I don't think I need this so let's find out lol
        # queue = sqs.Queue(
        #     self, "FirefoxReaderViewQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        #
        # topic = sns.Topic(
        #     self, "FirefoxReaderViewTopic"
        # )
        #
        # topic.add_subscription(subs.SqsSubscription(queue))
