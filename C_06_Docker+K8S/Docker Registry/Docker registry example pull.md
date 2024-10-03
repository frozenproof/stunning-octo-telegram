Using our already pushed image that we pulled
```
docker run -d \
  --name cattus_nginx_container \
  -p 8080:80 \
  -v /home/images/data:/data \
  -v /home/images/nginx/html:/usr/share/nginx/html \
  -v /home/images/nginx/conf/nginx.conf:/etc/nginx/nginx.conf \
  truclinhgm/cattus-nginx:deploy-ready
```