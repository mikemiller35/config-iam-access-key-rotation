import sys
import os
import boto3

sys.path.append(os.path.join(os.path.dirname(__file__)))
import emailhandler


def get_username(resourceId):
    """
    Take a resourceId and get friendly username, from the
        IAM user list.
    Args:
        resourceId (str): resourceId of the user

    Returns:
        UserName (str): friendly username as a string
    """
    iam = boto3.client("iam")
    response = iam.list_users()
    for x in response["Users"]:
        if x["UserId"] == resourceId:
            return x["UserName"]


def lambda_handler(event, context):
    #
    resourceId = event["detail"]["newEvaluationResult"]["evaluationResultIdentifier"][
        "evaluationResultQualifier"
    ]["resourceId"]
    complianceType = event["detail"]["newEvaluationResult"]["complianceType"]
    configMessage = event["detail"]["newEvaluationResult"]["annotation"]
    userName = get_username(resourceId)
    emailhandler.send_mesage(userName, configMessage, complianceType)
