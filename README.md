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

This should output current status of the project:

```sh
% make coverage
cd /Users/ccabrera/programacion/github/serverless_shortener/src;\
	python -m pytest ../tests --cov /Users/ccabrera/programacion/github/serverless_shortener/src --cov-report=term-missing ../tests
================================== test session starts ==================================
platform darwin -- Python 2.7.13, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /Users/ccabrera/programacion/github/serverless_shortener, inifile:
plugins: cov-2.4.0
collected 9 items

../tests/test__app.py ..
../tests/test__regexs.py ..
../tests/test_database.py .....

---------- coverage: platform darwin, python 2.7.13-final-0 ----------
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
app.py                      29     12    59%   41-45, 55-58, 64-67
chalicelib/__init__.py       0      0   100%
chalicelib/database.py      45      1    98%   62
chalicelib/regexs.py         2      0   100%
------------------------------------------------------
TOTAL                       76     13    83%


=============================== 9 passed in 1.78 seconds ================================
[:~/programacion … serverless_shortener] [27] master(+178/-99)* ±
```

### Running

To run you can execute simply execute `make run`:

```sh
$ make run
chalice --project-dir /Users/ccabrera/programacion/github/serverless_shortener/src local
Serving on localhost:8000
```

This starts a local simulation of the server, you can now use curl to test it:
```sh
curl -s localhost:8000| jq .
{
  "endpoints": [
    {
      "url": "POST /short",
      "description": "Receives url as DATA:\n        {\"long_url\": \"http://google.com\"}\n       returns shorten url:\n        {\"short_url\": \"gy\"}\n    "
    },
    {
      "url": "GET /short",
      "description": "Receives url as URL param <Q>:\n        service.com?q=http://google.com\n    "
    },
    {
      "url": "GET /{short_url}",
      "description": "Re-direct to the original url."
    },
    {
      "url": "GET /",
      "description": "Describes available endpoints"
    }
  ],
  "service": "serverless url shortener"
}
```

The root endpoint does instrospection and describes the service. If you dont
have 'jq' installed you may want to use your browser.

### Deploying

Additionally, all you need to deploy is to run:
```sh
$ make deploy
chalice --project-dir /Users/ccabrera/programacion/github/serverless_shortener/src deploy --profile tudev --no-autogen-policy --stage dev
Initial creation of lambda function.
Creating role
The following execution policy will be used:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*",
      "Effect": "Allow"
    },
    {
      "Action": [
        "dynamodb:*"
      ],
      "Resource": [
        "arn:aws:dynamodb:*:*:table/dev-urls"
      ],
      "Effect": "Allow"
    }
  ]
}
Would you like to continue?  [Y/n]: y
Creating deployment package.
Initiating first time deployment...
Deploying to: dev
https://pp7yyf75sb.execute-api.eu-west-1.amazonaws.com/dev/
```

You can specify **AWS_PROFILE** as a enviroment variable or as a Make flag.
To delete an existing stack you can run:

```sh
$ make delete
chalice --project-dir /Users/ccabrera/programacion/github/serverless_shortener/src delete --profile tudev --stage dev
Deleting rest API eaqpv7zc11
Deleting lambda function shortener-dev
Delete the role shortener-dev? [y/N]: y
Deleting role name shortener-dev
```

This will delete all but the DynamoDB table.

There is a live instance running on https://pp7yyf75sb.execute-api.eu-west-1.amazonaws.com/dev/
- To register a new url you can run: https://pp7yyf75sb.execute-api.eu-west-1.amazonaws.com/dev/short?q=http://Engrish.com
- To use a shortened url you can go to: https://pp7yyf75sb.execute-api.eu-west-1.amazonaws.com/dev/n1

### Deploying to production

Well, if everything went well on 'dev' (the default stage) you can now
deploy to production.

For this you can pass the 'STAGE' flag to 'make'. The Enviroment variables and other per/stage configuration can be defined [here][config].

[app]: https://github.com/pointtonull/serverless_shortener/blob/master/src/app.py#L17
[Urls]: https://github.com/pointtonull/serverless_shortener/blob/master/src/chalicelib/database.py#L38
[getuid]: https://github.com/pointtonull/serverless_shortener/blob/master/src/chalicelib/database.py#L96
[req1]: https://github.com/pointtonull/serverless_shortener/blob/master/requirements.txt
[req2]: https://github.com/pointtonull/serverless_shortener/blob/master/src/requirements.txt
[config]: https://github.com/pointtonull/serverless_shortener/blob/master/src/.chalice/config.json

<!-- vim: set sw=4 et ts=4 :-->