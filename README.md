[![Maintainability](https://api.codeclimate.com/v1/badges/b682d0ce3040893c6d81/maintainability)](https://codeclimate.com/github/phalbert/messenger/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b682d0ce3040893c6d81/test_coverage)](https://codeclimate.com/github/phalbert/messenger/test_coverage)

# Messenger

A serverless message sender service for sending smses and emails

## Built with AWS Chalice

Chalice, a Python Serverless Microframework developed by AWS, enables you to quickly spin up and deploy a working serverless app that scales up and down on its own as required using AWS Lambda.

## How to run/deploy

### Credentials

Before you can run/deploy the application, be sure you have credentials
configured.  If you have previously configured your machine to run boto3 (the
AWS SDK for Python) or the AWS CLI then you can skip this section.

If this is your first time configuring credentials for AWS you can follow these
steps to quickly get started:

```sh
$ mkdir ~/.aws
$ cat >> ~/.aws/config
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=YOUR_REGION (such as us-west-2, us-west-1, etc)
Assuming you have your '~/.aws/config' file defined.
```

### Building

To clone a local of the project:

```sh
git clone git@github.com:phalbert/messenger.git
cd messenger
```

To install dependences:

```sh
make deps
```

### Testing

To run tests and coverage you can use the respective targets:

```sh
make test
make coverage
```

### Running

To run you can execute simply execute `make run`:

```sh
$ make run
Serving on localhost:8000
```

### Deploying

Additionally, all you need to deploy is to run:

```sh
$ make deploy
Initial creation of lambda function.
Creating role
Initiating first time deployment...
Deploying to: dev
```

You can specify **AWS_PROFILE** as a enviroment variable or as a Make flag.
To delete an existing stack you can run:

```sh
$ make delete
```
