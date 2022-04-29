# Group 12



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
