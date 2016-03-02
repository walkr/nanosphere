# Authentication service

import sys
import time
import uuid
import random
import logging
import jwt

from nanoservice import Service
from nanoservice.encoder import JSONEncoder

from nanosphere import util

CONF = None


# *****************************************************
# UTILITIES
# *****************************************************

def _gen_random_code(low=1001, high=9999):
    """ Generate a random integer code between `low` and `high` """
    return random.randint(low, high)


def _gen_random_token():
    """ Generate a random uuid4 token """
    return uuid.uuid4().hex


# *****************************************************
# SERVICE METHODS
# *****************************************************

def decode_jwt(token, options=None):
    """ Authenticate via JSON Web Token

    Options: `secret`, `algorithms` """

    options = options or {}
    secret = options.get('secret', CONF and CONF.secret)
    algorithms = options.get('algorithms', CONF and CONF.algorithms)

    try:
        data = jwt.decode(token, secret, algorithms)
    except jwt.DecodeError:
        raise Exception('Cannot decode token')
    else:
        logging.debug('* Decoded data = {}'.format(data))
        return data


def generate_jwt(data, options=None):
    """ Generate a new JSON Web Token from data

    Options: `secret`, `algorithm` """

    options = options or {}
    secret = options.get('secret', CONF and CONF.secret)
    algorithm = options.get('algorithm', CONF and CONF.algorithms[0])
    return jwt.encode(data, secret, algorithm=algorithm).decode('utf-8')


def generate_sms(phone):
    """ Generate sms data with random code and secret fields """

    return {
        'phone': phone,
        'code': _gen_random_code(),
        'secret': _gen_random_token(),
        'timestamp': int(time.time()),
    }


def validate_sms(sms, options=None):
    """ Validate if an sms is valid
    Options: `code_is_old_after` """

    options = options or {}
    sms_code_lifetime = options.get(
        'sms_code_lifetime', CONF and CONF['sms_code_lifetime']
    )

    now = time.time()
    if sms['timestamp'] + sms_code_lifetime < now:
        raise Exception('Code expired')

    return True


# *****************************************************
# MAIN
# *****************************************************


def start(configpath):
    """ Read config file and start service """

    global CONF
    CONF = util.prepare(configpath)

    service = Service(CONF.address, encoder=JSONEncoder())
    util.enhance(service)

    service.register('decode_jwt', decode_jwt)
    service.register('generate_jwt', generate_jwt)
    service.register('generate_sms', generate_sms)
    service.register('validate_sms', validate_sms)
    service.start()


def main():
    configpath = sys.argv[1]
    start(configpath)


if __name__ == '__main__':
    main()
