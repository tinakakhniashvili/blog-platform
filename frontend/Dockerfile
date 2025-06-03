FROM node:14
WORKDIR /app
COPY index.html .
RUN npm install -g serve
CMD ["serve", "-s", ".", "-l", "5000"]

