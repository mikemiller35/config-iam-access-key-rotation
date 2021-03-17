# config-iam-access-key-rotation

We want to ensure people's access keys are within a certain age.

## Requirements

* Configure AWS Config to record `AWS::IAM::User`
* Have aws cli setup on your local machine (Or wherever you're reading this)
* serverless framework installed
* Follow steps below

## Lambda Deploy

With a CloudWatch event trigger

```bash
sls deploy --sendto "null@null.com" --sendfrom "null@null.com"
```

That's it, simple right?

## Custom Config Rule

### Pre-Flight

Run the following on your local machine. More info [here](https://github.com/awslabs/aws-config-rdk).

```bash
pip install rdk
rdk init
git clone https://github.com/awslabs/aws-config-rules
cd aws-config-rules/python/
```

### Deploy

For this we're going to use a community custom Config rule.  [Here's](https://github.com/awslabs/aws-config-rules/tree/master/python/IAM_ACCESS_KEY_ROTATED) the one we're using.  It has a optional parameter of `WhitelistedUserList`, very helpful.

Make whatever changes to `parameters.json` you'd like.

```bash
vim IAM_ACCESS_KEY_ROTATED/parameters.json
```

Then we deploy it

```bash
rdk deploy IAM_ACCESS_KEY_ROTATED
```

And evaluate the rule

```bash
aws configservice start-config-rules-evaluation --config-rule-names IAM_ACCESS_KEY_ROTATED
```

Check CloudWatch to make sure it's working!
