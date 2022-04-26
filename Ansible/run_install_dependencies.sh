#!/bin/bash

chmod 400 config/gitSSH.pem
chmod 400 config/mrcSSH.pem
./unimelb-COMP90024-2022-grp-12-openrc.sh; ansible-playbook run_install_dependencies.yaml -i inventory/hosts.ini