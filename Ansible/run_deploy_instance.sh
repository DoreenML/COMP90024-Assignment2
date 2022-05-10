./unimelb-COMP90024-2022-grp-12-openrc.sh

chmod 400 config/mrcSSH.pem

./unimelb-COMP90024-2022-grp-12-openrc.sh; ansible-playbook --private-key=/home/ubuntu/.ssh/id_rsa deploy_instance.yaml -i inventory/hosts.ini