# Stage 1: Build the Next.js app
FROM node:16-alpine AS builder

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the Next.js app source code
COPY . .

# Build the Next.js app
RUN npm run build

# Stage 2: Run the Next.js app
FROM node:16-alpine

WORKDIR /app

# Copy the built app from the builder stage
COPY --from=builder /app ./

# Expose the port Next.js listens on
EXPOSE 3000

# Run Next.js
CMD ["npm", "run", "start"]
