FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

# VOLUME [ "/app/node_modules" ]

CMD [ "npm", "start" ]

#  docker run -d --rm -p 3000:80 --name 13_run -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/13/data-volumes-05-temporary-anonymous-volume:/app:ro" -v /app/node_modules -v /app/temp 13_image
