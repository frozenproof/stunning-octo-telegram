# For java
```
docker pull eclipse-temurin
```
## Dockerfile
```
FROM eclipse-temurin:21
RUN mkdir /opt/app
COPY japp.jar /opt/app
CMD ["java", "-jar", "/opt/app/japp.jar"]
```