FROM node:19

WORKDIR /home/app/react

COPY src/package.json entrypoint.sh /

RUN yarn

RUN chmod +x /entrypoint.sh
