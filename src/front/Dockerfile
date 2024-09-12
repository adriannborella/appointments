# Stage 1: Build the Next.js app
FROM node:19-alpine AS builder

WORKDIR /app

# Install dependencies
COPY next/package.json ./
RUN yarn

# Copy the Next.js app source code
COPY ./next .

# Build the Next.js app
RUN yarn build

# Stage 2: Run the Next.js app
FROM node:19-alpine

WORKDIR /home/app/next

# Copy the built app from the builder stage
COPY --from=builder ./ /home/app/next

# Expose the port Next.js listens on
EXPOSE 3000

# Run Next.js
CMD ["yarn", "start"]
