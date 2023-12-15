FROM node:16-alpine3.15
RUN mkdir -p /home/frontend && chown -R node:node /home/frontend
WORKDIR /home/frontend
COPY --chown=node:node . .
USER node
RUN npm i
# RUN sudo npm install --location=global --unsafe-perm=true --allow-root
EXPOSE 3000
CMD ["npm", "run", "dev"]
