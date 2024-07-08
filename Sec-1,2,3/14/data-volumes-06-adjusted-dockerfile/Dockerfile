FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

# VOLUME [ "/app/node_modules" ]

CMD [ "npm", "start" ]

# docker run -d --rm -p 3000:80 --name 14_run -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/14/data-volumes-06-adjusted-dockerfile:/app:ro" -v /app/node_modules -v /app/temp 14_image