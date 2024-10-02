# Kubernetes
Basically a software that is used to manage other containers.

# Why not Docker?
Docker itself is **not** an image but rather a tool to manage the container. Originally, containers are mostly complete softwares without a need for extra management.

# How does Kurbenetes help
As the time go by, eventually we have so many containers since it's easier to deploy an item which you control the dependency, this also means we have an extended need to manage more containers without wasting too much resources. Each container has for itself an operating system and all of it's infrastructure, which could be shared among many containers.

Thus, kurbenetes take over the role of being a host, and become multi-hosts per cluster.