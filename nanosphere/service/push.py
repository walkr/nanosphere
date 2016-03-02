# Push notifications

import sys
from apns import APNs, Frame, Payload

from nanoservice import Service
from nanoservice.encoder import JSONEncoder
from nanosphere import util

CONF = None


def initialize(configuration):
    configuration.apns = APNs(**configuration.ios)
    configuration.android = None
    return configuration


def send_android():
    pass


def send_ios(config, device_token, payload):
    return CONF.apns.gateway_server.send_notification(
        device_token, Payload(**payload))


# *****************************************************
# SERVICE METHODS
# *****************************************************


def send(platform, device_tokens, payload, options=None):
    """ Send a notification
    Options: `url`,`app_key`, `app_id`, `production` """

    options = options or {}
    result = False

    if platform == 'ios':
        for token in device_tokens:
            send_ios(CONF.ios, token, payload)
        result = True

    if platform == 'android':
        for token in device_tokens:
            send_android(CONF.android, token, payload)
        result = True

    return result


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
