#!/usr/bin/python3
"""generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """tgz archive"""
    local("mkdir -p versions")
    created = datetime.now()
    formated = created.strftime("%Y%m%d%H%M%S")
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(formated))

    return "versions/web_static_{}".format(formated)
