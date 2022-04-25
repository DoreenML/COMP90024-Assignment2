#!/bin/bash

./unimelb-COMP90024-2022-grp-12-openrc.sh; ansible-playbook --key-file ./config/mrcSSH.pem create_instance.yaml