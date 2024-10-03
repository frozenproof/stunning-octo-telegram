# 1. Install Nexus Repository on Windows
- First of all, download Nexus Repository OSS.
- Unpack and go to bin folder
- Powershell to run
```
nexus.exe /run
```
- Nexus should now be running on http://localhost:8081.
## Access Nexus:

Open a browser and go to http://localhost:8081.
Log in with the default credentials (username: admin, password: located in nexus-data/admin.password).
## Make a new password admin
```
rVkTVJ5U2RdhJgu
```
# Step 2: Create a Docker Repository
## Navigate to Repositories:
Click here btw
![alt text](image.png)
In the Nexus UI, go to the "Repositories" menu.
## Create a New Docker Repository:
- Click "Create repository" and choose docker (hosted) from the list.
- Name it 
  ```
  cattus-nexus
  ```
- Select your desired port or leave the default, and configure other settings like the Blob store.
- I chose 8082 on http
# Step 3: Enable the Docker V2 API.
## 3.1 Set Up Docker to Use Nexus
Edit Docker Daemon Settings:
To use Nexus as a Docker registry, especially if you're not using HTTPS, you need to configure Docker to allow insecure registries.
On Windows, edit the Docker daemon settings:
Go to Docker Desktop settings.
Click on Docker Engine.
## 3.2 Add your Nexus repository IP/hostname under "insecure-registries" like so:

```
{
  "insecure-registries": ["<your-nexus-ip>:<port>"]
}
```
In my case, use

```
hostname
``` 

to get the proper ip address
```
{
  "insecure-registries": ["DESKTOP-0OFL577:8082"]
}
```
Save the settings and restart Docker Desktop.
# Step 4: Push Docker Images to Nexus
## Tag the Image:

In your Command Prompt or PowerShell, tag your Docker image:
```
docker tag <your-image>:<tag> <your-nexus-ip>:<port>/docker-hosted/<your-image>:<tag>
```
In my case
```
docker tag truclinhgm/cattus-nginx:deploy-ready DESKTOP-0OFL577:8082/cattus-nexus/cattus-nginx:deploy-ready
```
Since my image is
```
docker pull truclinhgm/cattus-nginx:deploy-ready
```
## Login to Nexus via Docker:

- Run the Docker login command:
```
docker login <your-nexus-ip>:<port>
```
In my case
```
docker login DESKTOP-0OFL577:8082
```

# Step 5: Push the Image:

Push the tagged image to Nexus:
```
docker push <your-nexus-ip>:<port>/docker-hosted/<your-image>:<tag>
```
In my case
```
docker push DESKTOP-0OFL577:8082/cattus-nexus/cattus-nginx:deploy-ready
```
# Step 6: Pull Docker Images from Nexus
Log in (if required):
```
docker login <your-nexus-ip>:<port>
```

```
docker login DESKTOP-0OFL577:8082
```
Pull the Image:

```
docker pull <your-nexus-ip>:<port>/docker-hosted/<your-image>:<tag>
```
```
docker pull DESKTOP-0OFL577:8082/cattus-nexus/cattus-nginx:deploy-ready
```
# Optional: Using HTTPS
If you want to secure your Nexus Docker registry with HTTPS:

You’ll need to configure Nexus to use SSL or set up a reverse proxy with Nginx or Apache on Windows.
By following these steps, you'll be able to push and pull Docker images from your Nexus Repository on Windows. Let me know if you run into any issues!