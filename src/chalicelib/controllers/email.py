import json
import boto3
from chalicelib.controllers import BaseController

class EmailController(BaseController):

    def __init__(self, *kwargs):
        super(EmailController, self).__init__(*kwargs)

    def send_email_sns(self):
        # This function receives JSON input: 
        # The message is then sent to the SNS topic.

        try:
            sns = boto3.client('sns')
            result = sns.publish(
                TopicArn=self.config.get('SNS_TOPIC'),
                Subject=self.json_params['subject'],
                Message=json.dumps(self.json_params)
            )
            self.logger.info(result)
            self.logger.info(self.json_params)
            return {
                'status': 200,
                'msg': 'Message queued'
            }
        except KeyError as error:
            return {
                'status': 500,
                'msg': 'missing key in request: {0}'.format(str(error))
            }