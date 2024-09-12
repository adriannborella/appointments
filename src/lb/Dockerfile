# Use the official Nginx image
FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf

# Copy the Nginx configuration file to the container
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 to the outside world
EXPOSE 80

# Start Nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]