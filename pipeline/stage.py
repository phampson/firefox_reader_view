from aws_cdk import Stage

from firefox_reader_view.firefox_reader_view_stack import FirefoxReaderViewStack


class PipelineStage(Stage):
    def __init__(self, scope, stage_name, props) -> None:
        super().__init__(scope, stage_name)

        lambda_stack = FirefoxReaderViewStack(self, "FirefoxReaderViewStack", stage_name)
