# COMP90024-Assignment2

## YouTube Link

YouTube link:
Analysis and Front-end UI(deployed version):
https://youtu.be/OdsyBCp4U
Analysis and Front-end UI(Research Presentation):
https://youtu.be/e1Pj3rdj_RY
https://youtu.be/7wF-oYmbCgY

Cloud Architectures:
https://youtu.be/mPg9JhnOxoM
https://youtu.be/Pm2XoCHdvBI
https://youtu.be/8UTsqlMSsBc
https://youtu.be/V6z1-JnERq0
https://youtu.be/0UyxxL10_Hc
https://youtu.be/5nE3SPhfMw0
https://youtu.be/Bp0L0TUcmes
https://youtu.be/Pr9nvtQPv5k
https://youtu.be/DEOb56aRha0
https://youtu.be/nNglE2Xeuf0
https://youtu.be/8bJXW_fajg4



## Team Member

| Name           | UID     | Email                             |
| -------------- | ------- | --------------------------------- |
| Qi Li          | 1138875 | lql4@student.unimelb.edu.au       |
| Yuheng Guo     | 1113036 | yuhengg1@student.unimelb.edu.au   |
| Zhaoyang Zhang | 1240942 | zhaoyangz1@student.unimelb.edu.au |
| Zhaoyu Wei     | 1258372 | zhangyuw@student.unimelb.edu.au   |
| Xiaohan Ma     | 1145763 | mxm3@student.unimelb.edu.a        |



## File Structure

-- Ansible

​	--- config

​	---host_vars

​	---inventory

​	---roles

--Backend

​	---BackEnd.py

​	---requirements

​	---util.py

--CouchDB

​	---dataUpload.py

​	---dataUpload.zip

--Frontend 

​	---node_modules

​	---public

​	---src

​		----api

​		----assets

​		----components

​		----router

​		----store

​		----views

--Harvester

​		----tagTweet

​		----tweepySearch30

​		----tweepySearchCovid

​		----tweepySearchFull

​		----tweepySearchRecent

​		----tweepySearchStreaming

​		----tweepyUserTimeline

​		----tweetFilter

​		----couchdbURL

--Report

--snapshot





## Ansible

It build a blueprint of automation tasks for instance deployment on MRC server, which assign following config:
### install instance
The following configure will be done after install
name: '{{ item.name }}'
image: '{{ instance_image }}'
key_name: '{{ instance_key_name }}'
flavor: '{{ instance_flavor }}'
availability_zone: '{{ availability_zone }}'
security_groups: '{{ sg_names }}'
volumes: '{{ item.volumes }}'

That define the system which port available, and which system image it used.

### install dependencies
Install docker pip and python on instance, prepare for the app running in the docker container

### deploy app
All running app, including harvester, CouchDB, backend and frontend will be deployed in docker container. And Those part will be discussed in following part.



## CouchDB deploy

There are three instances will be used for CouchDB, instance1 play a role of master node, and instance2 and 3 play role of slave node. They consist of the couch
Cluster. After deployment, they share the volumn and will be extended if new slave node join.



## Twitter Harvester

-- auth method: using user access token and access secret
-- implement tweepy api: search_30, search_full_archieve, streaming

All data crawled will be automatically store in the dataset, we build dataset base on our requirement:

- tweet_doc_stream_stable_mark5- Live data for several major cities in Australia

- tweet_doc_melbourne_coordinator_mark7 - tweets collected for each sub-region in Melbourne
- tweet_covid_australia_mark6 - tweets on covid topics across Australia
- tweet_doc_melbourne_coordinator_30_mark8- 30 days of tweets for all Melbourne sub-regions
- tweet_users_time_line_mark9- A timeline of tweets from mark1-mark8 users, spanning a wide range of time periods

The test dataset from mark1 to mark4 will not displayed in our dataset. We mainly interested in the COVID relevant twitter content.



## Front-End Running

### how to run the code

First use command prompt to go to the front-end directory, then run the following code

```
npm run serve
```



## Project setup

```
yarn install
```

### Compiles and hot-reloads for development

```
yarn serve
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).



### VUE3 Download

Tutorial: https://www.youtube.com/watch?v=GArgxNOYF_o

1. Install Node and NPM
2. Install Vue Cli 
3. Create applications
4. Run Application
5. Checkout put



**Node version checking** 

```
node -v
```

**NPM version checking**

```
npm -v
```

**Cli installing**

```
npm install -g @vue/cli
```

**Cli version checking**

```
vue -V
```

**Missing node_modules**

```
npm init
```



## Error and solutions

**node.js error and could not start the local server**  (solve by @Kenwei @ Songlin)

The VUE3 always shows the local server could not be started

The problem is on the node_module file missing

Delete the node_module file and npm -install 



**Could not start the VUE3 in docker**  (supported by @ Mendes @Kenwei)

Docker shows a timeout error when starting

docker compose up --build solve part of the problem

Still need to find out why might be because of the VPN



**RUN yarn install**

<img src="C:\Users\Yuheng Guo\AppData\Roaming\Typora\typora-user-images\image-20220407020540988.png" alt="image-20220407020540988" style="zoom: 25%;" />

Resource from: https://stackoverflow.com/questions/54254121/error-an-unexpected-error-occurred-https-registry-yarnpkg-com-react-getaddr

This error happened when trying to run 

```
docker compose up --build
```

The solution is:

1. Delete package-lock.json

2. Disable VPN to solve time out issue

3. Run again

   ```
   docker compose up --build
   ```



**Missing cli dependency**

First, delete node_module file, then run 

```
npm i
```

```
npm run serve
```



**Vue errors summary**

| Vue Error                                       | Solution                                                   | Example       |
| ----------------------------------------------- | ---------------------------------------------------------- | ------------- |
| Missing space before value for key 'components' | A space needed to be kept in between components and braces | components: { |
| Missing space before value for key 'name'       | There need to be a space before assigning names            | name: 'Home'  |
| Newline required at end of file not found       | we need to switch lines after the <style>                  | </style>      |
| Unexpected tab character                        | tab spaces are not allowed, replace with spaces instead    | <div>         |



**Debugging services**

*Markup Validation Service*: https://validator.w3.org/

This website could validate a markup file by uploading an HTML file or it could validate by using a URL

CSS Validation Service: https://jigsaw.w3.org/css-validator/

This website could validate a CSS file by uploading or by separating CSS code from HTML



**Fitting two charts into one VUE page**

We could put two charts into one webpage by setting two separate containers using different division classes. 

What we need to change from the original graph is to define two container classes and one separate in the 

template. Then define our spacer using CSS by setting the height. We could separate those two charts vertically.



**Color scheme**

A convenient website for tracing the color code can be found on http://www.flatuicolorpicker.com/blue-rgba-color-model/



**The initial design for Motion Assessment Imaging**

- The initial design is used as a separate header for different organs like 
- Motion Assessment Imaging/ Thorax
- Motion Assessment Imaging/ Liver
- Motion Assessment Imaging/ Lung
- Motion Assessment Imaging/ Kidney
- Motion Assessment Imaging/ Others



**IGRT Imaging modalities** 

The X-axis, for now, has the following categories but is subject to change 

depending on the client's requirement:

      'kV planar',
      'kV CBCT-3D',
      'kV CBCT-4D',
      'kV CBCT-gated(FB)',
      'kV CBCT-gated(BH)',
      'kV-MV pair',
      'Surface Imaging-Optical',



**Vue chart requiring toggle boxes for switch**

- Motion Assessment Imaging
- Motion Limitation
- Dose calculation dataset
- Reasons for Implementing
- Barriers to Implementing



**Home webpage jumping pages**

**Survey Info**: when user lick on this page,  it would jump to the survey info page

**Citation Info**: when user lick on the picture, it will be prompted to another citation webpage

**How to use page**: A picture with how  to use the webpage will be shown, then after the click it would jump to another website with instructions for the website.



**Scheme for the jumping boxes and multiple choices**

Now for the Reasons for implementing chart a jumping boxes and a multiple choice dropdown list are 

candidates for the switch. 



**Map polygon samples for Germany and Australia**

The main resources are from the https://www.highcharts.com/demo/maps/geojson and it's still a high chart written in jQuery, but it was transferred into a pure Vue script for convenience. Right now it only has a   simple polygon, but later on the related color will be added into the map. 
