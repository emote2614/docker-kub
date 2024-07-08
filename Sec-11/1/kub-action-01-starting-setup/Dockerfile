FROM node:14

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 8080

CMD [ "node", "app.js" ]


# minikube start --driver=docker

# minikube dashboard

# kubectl create deployment first-app --image=emote2614/first-app

# kubectl get deployments

# kubectl expose deployment first-app --type=LoadBalancer --port=8080

# kubectl get services

# minikube service first-app

# kubectl scale deployment/first-app --replicas 3

# ---------------------------------------------------------------

# kubectl set image deployment/first-app first-app=emote2614/first-app:v2

# kubectl rollout history deployment/first-app (--revision N)

# kubectl rollout undo deployment/first-app (--to-revision N)