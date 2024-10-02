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

# For Python
```
docker pull python
```
## Dockerfile
```
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
```