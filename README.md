# Problem Statement 1: Wisecow Application Deployment

## Overview
Containerized and deployed the Wisecow application on Kubernetes with secure TLS communication, automated CI/CD pipeline using GitHub Actions and Argo CD, and HTTPS access via NGINX Ingress.

## Prerequisites
- AWS CLI configured with appropriate permissions
- kubectl installed
- eksctl installed
- Docker installed
- A registered domain name
- Domain DNS managed by Route53 (recommended)

## Step 1: Create EKS Cluster
```bash
# Create EKS cluster
eksctl create cluster \
  --name wisecow \
  --region ap-south-1 \
  --nodegroup-name wisecow-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --node-volume-size 20 \
  --managed

# Associate IAM OIDC Provider
eksctl utils associate-iam-oidc-provider \
  --region ap-south-1 \
  --cluster wisecow\
  --approve
```

## Step 2: Install NGINX Ingress Controller 
```bash
#To install the NGINX Ingress Controller on your Kubernetes cluster, run:
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml

#Get the LoadBalancer endpoint
kubectl get svc -n ingress-nginx
```
## Copy the EXTERNAL-IP (the URL or hostname)
```bash
# Paste it into your wisecow-ingress.yaml in the hosts section
tls:
  - hosts:
      - a872dbe38ea2049fb8fa988074e52ceb-1726839868.ap-south-1.elb.amazonaws.com  # Paste your NGINX Ingress Controller LoadBalancer endpoint here
    secretName: wisecow-tls
rules:
  - host: a872dbe38ea2049fb8fa988074e52ceb-1726839868.ap-south-1.elb.amazonaws.com  # Paste your NGINX Ingress Controller LoadBalancer endpoint here
```

## Step 3: Install cert-manager
```bash
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml

# Wait for cert-manager to be ready
kubectl wait --namespace cert-manager --for=condition=ready pod --selector=app=cert-manager --timeout=90s
```


