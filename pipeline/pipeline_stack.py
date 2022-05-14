import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, ManualApprovalStep
from constructs import Construct

from pipeline.stage import PipelineStage


class PipelineStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline = CodePipeline(
            self,
            "Pipeline",
            pipeline_name="MyPipeline",
            synth=ShellStep(
                "Synth",
                input=CodePipelineSource.git_hub("phampson/firefox_reader_view", "main"),
                commands=[
                    "npm install -g aws-cdk",
                    "python -m pip install -r requirements.txt",
                    "cdk synth"
                ]
            )
        )

        test_stage = pipeline.add_stage(PipelineStage(self, "test", env=cdk.Environment(account="653592191043", region="us-west-1")))
        test_stage.add_post(ManualApprovalStep("Approval"))

        prod_stage = pipeline.add_stage(PipelineStage(self, "prod", env=cdk.Environment(account="653592191043", region="us-west-1")))

