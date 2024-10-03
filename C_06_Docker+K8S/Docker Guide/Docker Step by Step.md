# Docker from scratch
## Step 1: Get a jar
Pretty obvious but you need an actual image first. In this guide we use a **helloworld.jar file as complete software** ready for image build. More compilcated services would requires more jars or different files types to deploy depends on the services.

This also go the same for **a parent image**, the actual image that would run the software, in this case, the actual JRE itself.
## Step 2: Get MobaXterm Portable
It's already included in this folder.

## Step 3: Install docker. 
Recommended to use a strong vm to run the docker since it consumes a lot of resources.

### Update your package index
sudo apt-get update

### Install necessary packages
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

### Add the Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

### Add the Docker APT repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

### Update your package index again
sudo apt-get update

### Install Docker
sudo apt-get install -y docker-ce

## Step 3: Make a Dockerfile
### What is a Dockerfile? 
A Dockerfile is a file that configure the actual docker process for a specific image

### Example Dockerfile for **helloworld.jar**

#### Use an official OpenJDK runtime as a parent image/ Warning: OpenJDK is deprecated
#### Switching to eclipse-temurin
FROM eclipse-temurin:21

#### Set the working directory
WORKDIR /app

#### Copy the JAR file into the container
COPY helloworld.jar app.jar
COPY visitorpattern.jar app2.jar

#### Command to run the JAR file
ENTRYPOINT ["java", "-jar", "app2.jar"]

## Step 4: Telling the docker to build
```
sudo docker build -t hello-world-app .
```
- sudo run the program with root privilege.
- docker is the app.
- build is the command.
- -t is an option, after it is the chosen image name.
- hello-world-app is the image name.
- . mean the docker will bundle everything inside this folder into a single image, this allow everything to depends on each other properly.
## Step 5: Verify the docker image
If it is safe to run, we can verify it with a command
```
sudo docker images
```
**images** option tell the docker to list every single image on the system.

## Step 6: Run the actual image itself
Seriously, why else would the image be born?
```
sudo docker run --name hello-world-container hello-world-app
```
- **run** create and start a new container from a specified image
- **--name** option choose the container name
- **hello-world-container** is the chosen container name
- **hello-world-app** is the image name that we chose from previous step
## Step 7: Check the docker output
```
sudo docker logs hello-world-container
```
- **logs** option specify the output the container generated
- **hello-world-container** is the container name we chose from previous step
## Step 8: Stop and remove the container, image

- Stop the container first
```
sudo docker stop hello-world-container
```
- Remove the container after stopping it
```
sudo docker rm hello-world-container
```
- Remove the image name after stopping it
```
sudo docker rmi hello-world-app
```
- Remove the image after stopping it
```
sudo docker image remove <image-id>
```
# Step 9: Cleanup and Pruning
If you want to free up space, you can remove unused images and containers using:

# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove all unused data (containers, networks, images, and optionally volumes)
docker system prune

# See all containers: docker ps -a 
# Start an container: docker start -ai <container_id_or_name>
Or just 
```
docker start <container_id_or_name>
```
The -ai flags will attach the standard input and output, allowing interaction with the container directly.
# Access an container: 

You can access the container using the docker exec command. Here’s how:
```
docker exec -it <container_id_or_name> /bin/bash
```
Replace <container_id_or_name> with the actual ID or name of your container.
- The -it flags allow you to run the command in an interactive terminal.
/bin/bash opens a Bash shell. 
- If your container doesn’t have Bash, you can use /bin/sh instead.

# Don't ever make a dockerfile without an entrypoint or cmd, or it will shut itself down.