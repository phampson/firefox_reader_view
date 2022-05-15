import aws_cdk as cdk

from firefox_reader_view.firefox_reader_view_stack import FirefoxReaderViewStack


class PipelineStage(cdk.Stage):
    def __init__(self, scope, stage_name, **kwargs) -> None:
        super().__init__(scope, stage_name, **kwargs)

        lambda_stack = FirefoxReaderViewStack(self, "FirefoxReaderViewStack", stage_name)
