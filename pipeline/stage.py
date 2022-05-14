from aws_cdk import Stage

from firefox_reader_view.firefox_reader_view_stack import FirefoxReaderViewStack


class PipelineStage(Stage):
    def __init__(self, scope, stage_name, **kwargs) -> None:
        super().__init__(scope, stage_name, **kwargs)

        lambda_stack = FirefoxReaderViewStack(scope, "FirefoxReaderViewStack", stage_name)
