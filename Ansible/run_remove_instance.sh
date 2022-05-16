#!/bin/bash

chmod 400 config/mrcSSH.pem

./unimelb-COMP90024-2022-grp-12-openrc.sh; ansible-playbook remove_instance.yaml