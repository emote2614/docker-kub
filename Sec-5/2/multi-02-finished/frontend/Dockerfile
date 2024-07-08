FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]

# docker run 
#     -v /Users/emote2614/Downloads/docker/Sec-5/2/multi-02-finished/frontend/src 
#     --name goals-frontend 
#     --rm 
#     -p 3000:3000 
#     -it 
#     goals-react;  
