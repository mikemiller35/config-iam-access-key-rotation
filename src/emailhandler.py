import os
import boto3
from botocore.exceptions import ClientError


def send_mesage(username, configmsg, compliance):
    """
    Send an email

    Args:
        username (str): username
        configmsg (str): The annotation from Config
        compliance (str): compliance status
    """
    SENDER = os.getenv("SENDER_EMAIL")
    RECIPIENT = os.getenv("RECIPIENT_EMAIL")
    AWS_REGION = os.getenv("AWS_REGION")
    SUBJECT = "[AWS] IAM Access Key Notification - {}".format(username)
    BODY_HTML = """
    <html>
    <head></head>
    <body>
      <h3>Please see access key information below</h3>
        <p>{user} is {compliance}.</p>
        <p>{configmsg}</p>
        <p>Please change access keys, and maybe your password too!</p>
        <p>If the account is COMPLIANT, nothing to see here!</p>
    </body>
    </html>
                """.format(
        user=username, compliance=compliance, configmsg=configmsg
    )
    CHARSET = "UTF-8"
    client = boto3.client("ses", region_name=AWS_REGION)

    # Try to send the email
    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [
                    RECIPIENT,
                ],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": CHARSET,
                        "Data": BODY_HTML,
                    },
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": SUBJECT,
                },
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        print(response["MessageId"])
