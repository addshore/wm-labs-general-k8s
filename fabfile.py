from fabric.api import *  # noqa

env.use_ssh_config = True
env.sudo_user = 'root'
env.roledefs = {
    'host': [
        'k8s-master-01.general-k8s.eqiad.wmflabs',
        'k8s-node-01.general-k8s.eqiad.wmflabs',
        'k8s-node-02.general-k8s.eqiad.wmflabs',
        'k8s-node-03.general-k8s.eqiad.wmflabs',
        'k8s-node-04.general-k8s.eqiad.wmflabs',
        'k8s-node-05.general-k8s.eqiad.wmflabs',
        'k8s-node-06.general-k8s.eqiad.wmflabs',
    ],
    'master': ['k8s-master-01.general-k8s.eqiad.wmflabs'],
    'node': [
        'k8s-node-01.general-k8s.eqiad.wmflabs',
        'k8s-node-02.general-k8s.eqiad.wmflabs',
        'k8s-node-03.general-k8s.eqiad.wmflabs',
        'k8s-node-04.general-k8s.eqiad.wmflabs',
        'k8s-node-05.general-k8s.eqiad.wmflabs',
        'k8s-node-06.general-k8s.eqiad.wmflabs',
    ]
}

@task
def printHostnames(role_from_arg='host'):
    execute(printHostname, role=role_from_arg)

@parallel
def printHostname(**kwargs):
    run('hostname')
