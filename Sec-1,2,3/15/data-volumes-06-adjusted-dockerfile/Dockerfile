FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ENV PORT 80

EXPOSE ${PORT}

# VOLUME [ "/app/node_modules" ]

CMD [ "npm", "start" ]

# docker run -d --rm -p 3000:8000 --env PORT=8000 --name 15_run -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/15/data-volumes-06-adjusted-dockerfile:/app:ro" -v /app/node_modules -v /app/temp 15_image

# or

# docker run -d --rm -p 3000:8000 -e PORT=8000 --name 15_run -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/15/data-volumes-06-adjusted-dockerfile:/app:ro" -v /app/node_modules -v /app/temp 15_image

# or (.env)

# docker run -d --rm -p 3000:8000 --env-file ./.env --name 15_run -v feedback:/app/feedback -v "/Users/cbs/Downloads/docker/15/data-volumes-06-adjusted-dockerfile:/app:ro" -v /app/node_modules -v /app/temp 15_image