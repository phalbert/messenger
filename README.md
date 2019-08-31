# Messenger

A serverless message sender service for sending smses and emails

## Built with AWS Chalice

Chalice, a Python Serverless Microframework developed by AWS, enables you to quickly spin up and deploy a working serverless app that scales up and down on its own as required using AWS Lambda.

## Build and Run Locally

Install requirements:

```bash
(env)$ pip install -r requirements.txt
```

You can simulate the app by running it locally using the local utility of Chalice:

```bash
(env)$ chalice local
Serving on 127.0.0.1:8000
```

By default, Chalice runs on port 8000. We can now check the index route by making a curl request to http://localhost:8000/:

```bash
$ curl -X GET http://localhost:8000/
{"hello": "world"}
```

## Deploy on AWS Lambda

Before we begin deployment, we need to make sure we have our AWS credentials in place,usually located at ~/.aws/config. The contents of the file look as follows:

```shell
[default]
aws_access_key_id=<your-access-key-id>
aws_secret_access_key=<your-secret-access-key>
region=<your-region>
```

With AWS credentials in place, let’s begin our deployment process with just a single command:

```bash
(env)$ chalice deploy
Creating deployment package.
Updating policy for IAM role: hello-world-dev
Creating lambda function: hello-world-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:ap-south-1:679337104153:function:hello-world-dev
  - Rest API URL: https://fqcdyzvytc.execute-api.ap-south-1.amazonaws.com/api/
```

> Note: The generated ARN and API URL in the above snippet will vary from user to user.
