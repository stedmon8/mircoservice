FROM node:8

WORKDIR /app
ENV PATH="./node_modules/.bin:$PATH"

COPY /frontend/ .
RUN CI=true 
RUN npm install react-scripts 


# add app
#COPY . /app

CMD ["npm", "start"]