#!/bin/bash

chmod 400 config/mrcSSH.pem

ansible-playbook --private-key=/home/ubuntu/.ssh/id_rsa deploy_instance.yaml -i inventory/hosts.ini