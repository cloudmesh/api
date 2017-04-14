import click

from cloudmesh.cli.boot.commands import boot

import logging
logger = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def main(ctx, debug):
    """Some description"""
    logging.basicConfig(level=logging.INFO)


main.add_command(boot)



if __name__ == '__main__':
    main()
