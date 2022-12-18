FROM node:16-alpine3.15
LABEL MAINTAINER="STK, Stanley Sakai <stanley@stanographer.com>"
RUN mkdir -p /home/frontend && chown -R node:node /home/frontend
WORKDIR /home/frontend
COPY --chown=node:node . .
USER node
RUN npm i
EXPOSE 3000
CMD ["npm", "run", "dev"]

# FROM node:16-alpine3.15
# RUN mkdir -p /app
# WORKDIR /app
# COPY package*.json /app
# RUN npm i
# COPY . /app
# EXPOSE 3000
# CMD ["npm", "run", "dev"]

# FROM node:16-alpine3.15
# RUN mkdir -p /app && chown -R node:node /app
# WORKDIR /app
# COPY --chown=node:node package*.json /app
# USER node
# RUN npm i
# COPY . /app
# EXPOSE 3000
# CMD ["npm", "run", "dev"]


# FROM node:lts-alpine as build

# RUN mkdir /app

# WORKDIR /app

# COPY package.json .
# COPY next.config.js .
# COPY api-server.js .
# COPY .env.local .

# RUN npm install
# RUN npm run build

# COPY .next ./.next
# COPY public ./.public
# COPY . .

# # ---------------

# FROM node:lts-alpine

# ENV NODE_ENV production
# ENV API_PORT 3001

# WORKDIR /app

# COPY --from=build /app/package.json .
# COPY --from=build /app/next.config.js .
# COPY --from=build /app/api-server.js .
# COPY --from=build /app/.env.local .
# COPY --from=build /app/.next ./.next
# COPY --from=build /app/public ./public

# RUN npm install

# EXPOSE 3000
# EXPOSE 3001

# CMD npm start
