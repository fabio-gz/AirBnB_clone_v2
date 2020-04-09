#!/usr/bin/python3
"""Deploy archive"""
from fabric.api import put, run, env
from datetime import datetime
from os import path

env.hosts = ['35.231.230.134', '54.167.66.124']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/holberton'


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not path.exists(archive_path):
        return False

    file_name = archive_path.split('/')
    name = file_name[1].rstrip('.tgz')
    route = "/data/web_static/releases/{}/".format(name)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(route))
        run("tar -xzf /tmp/{} -C {}".format(file_name[1], route))
        run("rm /tmp/{}".format(file_name[1]))
        run("mv {}web_static/* {}".format(route, route))
        run("rm -rf {}web_static".format(route))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(route))
        return True
    except:
        return False
