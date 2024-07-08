FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

# VOLUME [ "app/node_modules" ]

CMD [ "node", "server.js" ]

# 실행 방법
# docker run -d --name 11_run -p 3000:80 -v feedback:/app/feedback 
# -v "/Users/cbs/Downloads/docker/11/data-volumes-02-added-dockerfile:/app" 
# -v /app/node_modules 11_image

# docker run -d --name 11_run -p 3000:80 -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/11/data-volumes-02-added-dockerfile:/app" -v /app/node_modules 11_image
