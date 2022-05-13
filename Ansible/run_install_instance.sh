chmod 400 config/mrcSSH.pem

./unimelb-COMP90024-2022-grp-12-openrc.sh; ansible-playbook install_instance.yaml -i inventory/hosts.ini