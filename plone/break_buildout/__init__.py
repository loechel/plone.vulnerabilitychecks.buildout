# -*- coding: utf-8 -*-

import logging
import os

from zc.buildout import UserError

disclaimer = \
"""If you have a good reason to bypass this restriction,
remove the plone.break_buildout extension from your buildout."""


def check_vulnerability(buildout, logger):
    """ Refuse to run if a unsecure Plone setup is tried to be installed """

    if os.geteuid() == 0:
        effective_user = buildout['buildout'].get('buildout-user', 'buildout_user')
        logger.error("""
***********************************************************
Buildout should not be run while superuser. Doing so allows
untrusted code to be run as root.
Instead, you probably wish to do something like:
sudo -u %s bin/buildout

%s
***********************************************************
""" % (effective_user, disclaimer))
        raise UserError('User attempt to give system ownership to Internet')


def main(buildout):
    logger = logging.getLogger("plone.break_buildout")
    check_vulnerability(buildout, logger)