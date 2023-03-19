FROM node:18-slim

ENV TZ Asia/Tokyo

WORKDIR /app

RUN apt-get update \
    && apt-get install -y \
    git \
    vim  

RUN npm install -g npm 

RUN npm install --save axios vue-axios

RUN yarn add @nuxtjs/axios
    # yarn global add @vue/cli @vue/cli-init