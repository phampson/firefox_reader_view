#!/usr/bin/env python3

import aws_cdk as cdk

from firefox_reader_view.firefox_reader_view_stack import FirefoxReaderViewStack
from pipeline.pipeline_stack import PipelineStack

app = cdk.App()

# FirefoxReaderViewStack(app, "firefox-reader-view")
PipelineStack(
    app,
    "PipelineStack",
    env=cdk.Environment(account="653592191043", region="us-west-1")
)

app.synth()
