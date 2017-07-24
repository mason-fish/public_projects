# Fabric configuration file for THE_TANK integration and deployment
from fabric.api import *
from fabric.operations import *

env.use_ssh_config = True
env.hosts = ['41_web_02']

def deploy():
    local('tar -X exclude.txt -czf the_tank.tar.gz .')
    put('./the_tank.tar.gz', '/tmp/')
    sudo('tar -xzf /tmp/the_tank.tar.gz -C /var/www/', shell=False)
    run('rm -f /tmp/the_tank.tar.gz')
    local('rm -f ./the_tank.tar.gz')
