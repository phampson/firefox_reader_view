#!/usr/bin/env python3

import aws_cdk as cdk

from firefox_reader_view.firefox_reader_view_stack import FirefoxReaderViewStack


app = cdk.App()
FirefoxReaderViewStack(app, "firefox-reader-view")

app.synth()
