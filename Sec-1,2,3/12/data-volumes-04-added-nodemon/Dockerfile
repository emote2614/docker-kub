FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

# VOLUME [ "/app/node_modules" ]

CMD [ "npm", "start" ]

# docker run -d --name 12_run -p 3000:80 -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/12/data-volumes-04-added-nodemon:/app" -v /app/node_modules 12_image

# -v /app/data                  => Anonymous Volume
# -v data:/app/data             => Named Volume
# -v /path/to/code:/app/code    => Bind Mount