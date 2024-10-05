```
docker build -t cattus-shield-app .
```

```
docker run --name cattus-shield \
-v /home/images/data:/data \
cattus-shield-app
```

```
docker stop cattus-shield
docker rm cattus-shield

docker run --name cattus-shield \
-v /home/images/data:/data \
cattus-shield-app

```