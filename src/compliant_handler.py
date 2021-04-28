import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__)))
from helpers import get_username, send_mesage


def lambda_handler(event, context):
    print(event)
    resourceId = event["detail"]["newEvaluationResult"]["evaluationResultIdentifier"][
        "evaluationResultQualifier"
    ]["resourceId"]
    complianceType = event["detail"]["newEvaluationResult"]["complianceType"]
    try:
        configMessage = event["detail"]["newEvaluationResult"]["annotation"]
    except KeyError:
        configMessage = "No message."
    userName = get_username(resourceId)
    send_mesage(userName, configMessage, complianceType)
