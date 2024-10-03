# Installing the actual tool
Based on the vm details(included in vminfo file in the outermost fodler), we must install everything from scratch, which allows the best of customization for the installs.

## Step 1: Add the actual repo for kube tool itself

Run the following command if running on Red Hat based linux
```
# This overwrites any existing configuration in /etc/yum.repos.d/kubernetes.repo
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://pkgs.k8s.io/core:/stable:/v1.31/rpm/
enabled=1
gpgcheck=1
gpgkey=https://pkgs.k8s.io/core:/stable:/v1.31/rpm/repodata/repomd.xml.key
EOF
```

Run this for other linux
```
sudo vi /etc/yum.repos.d/kubernetes.repo
```
Paste the following in for normal linux
```
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
```
## Step 2: Installing tool at once
Clean everything at once
```
sudo dnf clean all
```
Install the tool for Red Hat
```
sudo yum install -y kubectl
```

## Step 3: Install kurbenetes cluster
Get and install the cluster
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

# Initiate the cluster
## Step 4: Start the cluster
If your image is already pushed to an online registry
```
minikube start
```
Use this for local image, which start minikube with the actual local Docker driver
```
minikube start --driver=docker
```
## Step 5: Make a docker account
Kurbenetes pull images from a registry, thats why we need to push it online. Or don't.

## Step 6: Changing the local variable of docker env to use the docker cli inside minikube
```
eval $(minikube docker-env)
```

# Create a deployment
## Step 7: Build the image like you normally do with a docker

## Step 8: Create a deployment.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deploy
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cattus
  template:
    metadata:
      labels:
        app: cattus
    spec:
      containers:
      - name: cattus
        image: bb  # Use your local Docker image name here, i use bb because :3
        ports:
        - containerPort: 80
```
## Step 9: Apply the said deployment configuration and deploy it
```
kubectl apply -f deployment.yaml
```

# Run and access deployment
## Step 10: See all the deployments
```
kubectl get deployments
```
## Step 11: Check all pods status
```
kubectl get pods
```
## Step 12: Apply the service configuration if needed to access
Use a service.yaml file to access said deployment
```
apiVersion: v1
kind: Service
metadata:
  name: cattus-nginx-service
spec:
  type: NodePort  # You can also use LoadBalancer if preferred
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: cattus
```
Run the command to configure the service
```
kubectl apply -f service.yaml
```
## Step 13: Access said service
```
minikube service cattus-nginx-service
```

# Useful commands to manage the minikube

## Minikube
### Managing the minikube
Use this to see all existing cluster of minikube
```
minikube profile list
```

### Stopping the minikube
```
minikube stop
```

### Delete Specific Profiles
```
minikube delete -p profile-name
```

### Delete Default Profile:
```
minikube delete -p minikube
```
### Delete All Kubernetes Resources 
```
kubectl delete all --all
```

## Pod
### List all pods:

```
kubectl get pods
```
Delete a specific pod:

```
kubectl delete pod <pod-name>
```
Force delete a pod (if necessary):
```
kubectl delete pod <pod-name> --grace-period=0 --force
```
Delete multiple pods by name:
```
kubectl delete pod pod1 pod2 pod3
```
Delete all pods with a specific label:
```
kubectl delete pods -l key=value
```

```
Cái crashloopbackoff báo khi pod dừng chạy nhưng vì cái helloworld chỉ chạy xong dừng luôn nên nó báo lỗi đúng không ạ?
```