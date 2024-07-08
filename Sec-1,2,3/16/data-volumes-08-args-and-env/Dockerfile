 FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ARG DEFAULT_PORT=80

ENV PORT $DEFAULT_PORT

EXPOSE $PORT

# VOLUME [ "/app/node_modules" ]

CMD [ "npm", "start" ]

# 이미지 빌드할때 인자값 포함해서 빌드
# docker build -t 16_image:dev --no-cache --build-arg DEFAULT_PORT=8000 .   


