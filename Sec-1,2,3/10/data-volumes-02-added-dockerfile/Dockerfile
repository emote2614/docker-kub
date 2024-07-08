FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

CMD [ "node", "server.js" ]

# 실행 방법
# docker run -d --rm --name 10_run -p 3000:80 -v feedback:/app/feedback 10_image