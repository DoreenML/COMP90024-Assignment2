# COMP90024-Assignment2

## Ansible
It build a blueprint of automation tasks for instace deployment on mrc server, which assign following config:
### install instance
The following configure will be done anfter install
name: '{{ item.name }}'
image: '{{ instance_image }}'
key_name: '{{ instance_key_name }}'
flavor: '{{ instance_flavor }}'
availability_zone: '{{ availability_zone }}'
security_groups: '{{ sg_names }}'
volumes: '{{ item.volumes }}'

That define the system which port avaialbe, and which system image it used.

### install dependiencies
Install docker pip and python on instance, prepare for the app running in the docker container

### deploy app
All running app, including harvester, couchdb, backend and frontend will be deployed in docker container. And Those part will be discussed in following part.

## Couchdb deploy
There are three instances will be used for couchdb, instance1 play a role of master node, and instance2 and 3 play role of slave node. They consist of the couch
Cluster. After deployment, they share the volumn and will be extended if new slave node join.

## Twitter Harvester
-- auth method: using user access token and access secret
-- implement tweepy api: search_30, search_full_archieve, streaming

All data crawled will be automatically store in the dataset, we build dataset base on our requirement:

### tweet_doc_stream_stable_mark5- Live data for several major cities in Australia
### tweet_doc_melbourne_coordinator_mark7 - tweets collected for each sub-region in Melbourne
### tweet_covid_australia_mark6 - tweets on covid topics across Australia
### tweet_doc_melbourne_coordinator_30_mark8- 30 days of tweets for all Melbourne sub-regions
### tweet_users_time_line_mark9- A timeline of tweets from mark1-mark8 users, spanning a wide range of time periods

The test dataset from mark1 to mark4 will not displayed in our dataset. We mainly intrested in the covid relevant twitter content.
