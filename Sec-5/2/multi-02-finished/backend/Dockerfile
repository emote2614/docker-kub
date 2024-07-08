FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

ENV MONGODB_USERNAME=root
ENV MONGODB_PASSWORD=secret

CMD ["npm", "start"]

# docker run 
#     --name goals-backend 
#     -v /Users/emote2614/Downloads/docker/Sec-5/2/multi-02-finished/backend:/app 
#     -v logs:/app/logs 
#     -v /app/node_modules 
#     -e MONGODB_USERNAME=max 
#     -d 
#     --rm 
#     -p 80:80 
#     --network goals-net 
#     goals-node