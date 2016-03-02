import sys
import signal
import logging
import threading

from nanoservice import config


def ping():
    return 'pong'


def stop(dummy_signum=None, dummy_frame=None):
    """ Stop script """
    logging.info('Exiting ...')
    sys.exit(0)


def prepare(configpath):
    """ Read json configuration and respond to CTR-C """

    # Respond to CTRL-C
    if threading.current_thread().name == 'MainThread':
        signal.signal(signal.SIGINT, stop)

    # Load configuration file
    conf_data = config.load(configpath)

    # Set logging level
    logging.basicConfig(
        format=conf_data['logging.format'],
        level=getattr(logging, conf_data.get('logging', 'info').upper()))

    return conf_data


def enhance(service):
    """ enhance a service by registering additional methods """
    service.register('ping', ping)
    service.register('stop', stop)
