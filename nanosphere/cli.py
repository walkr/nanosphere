import click
from nanosphere import service


# ################ SMS SERVICE #################################


@click.group()
def sms():
    """ sms service """
    pass


@sms.command('start', short_help='start sms service')
@click.option('--config', required=True, help='json configuration filepath')
def sms_start(config):
    """ Start service with configuration file """
    service.sms.start(config)


# ################ PUSH SERVICE #################################


@click.group()
def push():
    """ push notifications service """
    pass


@push.command('start', short_help='start push service')
@click.option('--config', required=True, help='json configuration filepath')
def push_start(config):
    """ Start service with configuration file """
    service.push.start(config)


# ################ AUTH SERVICE #################################


@click.group()
def auth():
    """ auth notifications service """
    pass


@auth.command('start', short_help='start auth service')
@click.option('--config', required=True, help='json configuration filepath')
def auth_start(config):
    """ Start service with configuration file """
    service.push.start(config)
