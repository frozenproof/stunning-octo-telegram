We are going to use nginx as a server for the deployment image, since most images are going to be used as services.

# Step 1: Create a nginx image
## 1. A configuration file in conf/nginx.conf
I won't write it here since it's best not to duplicate the documents.
## 2. A html directory so that nginx can load file
Just follow the example
## 3. A dockerfile so that Docker can build it
It's in the folder
### Explanation:
- FROM nginx:latest: Use the latest official Nginx image as the base.
- COPY ./conf/nginx.conf /etc/nginx/nginx.conf: Copy the custom Nginx configuration to the container.
- COPY ./html /usr/share/nginx/html: Copy the local html folder with static files to Nginx's default directory for serving content.
- EXPOSE 80: Expose port 80 for HTTP traffic.
- CMD ["nginx", "-g", "daemon off;"]: Ensure Nginx runs in the foreground (required in Docker containers).
# Step 2: Build the nginx image
Use the following command
```
docker build -t cattus-nginx .
```

# Step 3: Run the image in a container
```
docker run -d \
  --name cattus_nginx_container \
  -p 8080:80 \
  -v /home/images/data:/data \  # Replace with your absolute path
  -v /home/images/nginx/html:/usr/share/nginx/html \
  -v /home/images/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
  cattus-nginx
```
## Explanation:
-d: Runs the container in detached mode (background).

--name cattus_nginx_container: Names the container.

-p 8080:80: **Maps the container's port 80 to port 8080 on host** (accessible via http://localhost:8080).

-v /home/images/nginx/html:/etc/nginx/nginx.html: This mounts your local Nginx configuration file to the container, allowing you to modify it on your host without rebuilding the image.
# Step 4: Make sure the containers are running
```
docker ps -a
```

If something is wrong, it has to be the conf file that is usually wrong.

# Step 5: Check the actual website that got deployed

Say Cheese

![alt text](image.png)

