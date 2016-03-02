# Push notifications

import sys

from nanoservice import Service
from nanoservice.encoder import JSONEncoder

from twilio.rest import TwilioRestClient
from nanosphere import util

CONF = None


# *****************************************************
# UTILITIES
# *****************************************************

def _make_client(configuration):
    account_sid = configuration['twilio']['account_sid']
    auth_token = configuration['twilio']['auth_token']
    number = configuration['twilio']['number']
    client = TwilioRestClient(account_sid, auth_token)
    client.from_ = number
    return client


# *****************************************************
# SERVICE METHODS
# *****************************************************

def send(phone, message, options=None):
    """ Send a notification
    Options: `url`,`app_key`, `app_id`, `production` """

    options = options or {}
    sms_client = options.get('sms_client', _make_client(CONF))

    result = sms_client.messages.create(
        to=phone, from_=sms_client.from_, body=message)
    return result.status == 'queued' and result.error_code is None


# *****************************************************
# MAIN
# *****************************************************

def start(configpath):
    """ Read config file and start service """
    global CONF
    CONF = util.prepare(configpath)

    service = Service(CONF.address, encoder=JSONEncoder())
    service.register('send', send)
    util.enhance(service)
    service.start()


def main():
    configpath = sys.argv[1]
    start(configpath)


if __name__ == '__main__':
    main()
