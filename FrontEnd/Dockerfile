FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /home/ubuntu/COMP90024/FrontEnd

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# install project dependencies
RUN yarn install

# build app for production with minification
RUN yarn build



EXPOSE 4000
CMD [ "http-server", "-p 4000", "dist" ]