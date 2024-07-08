# FROM node

# WORKDIR /app

# COPY . /app

# RUN npm install

# EXPOSE 80

# CMD ["node", "server.js"]

# -------------최적화------------------
#  package.json 파일이 변경되지 않는 한 'npm install' 명령어가 재실행되지 않음
# -------------------------------------
FROM node

WORKDIR /app

COPY package.json /app

RUN npm install

COPY . /app

EXPOSE 80

CMD ["node", "server.js"]