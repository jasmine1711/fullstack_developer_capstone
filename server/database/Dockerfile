# Use Node base image
FROM node:18.12.1-bullseye-slim

# Set working directory in the container
WORKDIR /usr/src/app

# Optional: install a specific version of npm
RUN npm install -g npm@9.1.3

# Copy only package.json first to leverage Docker caching
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy entire project (including app.js, models, data, etc.)
COPY . .

# Expose the backend port
EXPOSE 3030

# Start the app
CMD ["node", "app.js"]
