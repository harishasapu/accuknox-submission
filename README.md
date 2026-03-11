# Wisecow Deployment – GitOps Approach 🚀

This repository demonstrates the **GitOps deployment of the Wisecow application** on Kubernetes using **ArgoCD**, **Traefik**, **Cert-Manager**, and **GitHub Actions CI/CD**.  

All deployments are fully **declarative**, with automatic synchronization between your Git repository and Kubernetes cluster.  

---

## 🌐 Live Application

Access the deployed application securely via HTTPS:  
[https://harishwisecow.duckdns.org](https://harishwisecow.duckdns.org) ✅  

---

## 🏗️ Architecture
```
GitHub → Actions → Docker Hub → ArgoCD → Kubernetes
   ↓         ↓         ↓          ↓         ↓
 Code    Build/Push  Registry  GitOps   Deploy
 ```



- **GitOps Principle:** The Kubernetes cluster state always matches the Git repository.  
- **CI/CD Flow:**  
  - GitHub Actions builds and pushes Docker images on code changes  
  - ArgoCD monitors the GitOps repo and deploys changes automatically  

---

## ✅ Tasks Completed

### 1. Dockerization
- Created Dockerfile for Wisecow  
- Installed packages: `fortune`, `cowsay`, `netcat-openbsd`  

### 2. Kubernetes Deployment
- **Deployment:** 2 replicas  
- **Service:** ClusterIP  
- **Ingress:** TLS-enabled for secure HTTPS at [harishwisecow.duckdns.org](https://harishwisecow.duckdns.org)  
  
![argocd-ui](/assets/argocd-UI-wisecow.png)

### 3. TLS Implementation
- Installed **cert-manager** for automatic certificate provisioning  
- Created **ClusterIssuer** with Let's Encrypt ACME provider  
- Annotated Ingress with `cert-manager.io/cluster-issuer` for auto TLS  
- Domain points to Traefik LoadBalancer  

> Result: Secure HTTPS access at [https://harishwisecow.duckdns.org](https://harishwisecow.duckdns.org)  

![Wisecow HTTPS](/assets/tls-and-output-ingress.png)

### 4. CI/CD Pipeline
**CI (GitHub Actions)**  
- Trigger: Push/PR to `main` (excluding GitOps manifests)  
- Build: Docker image tagged with commit SHA  
- Push: To Docker Hub

![CI](/assets/CI.png)  

### 5. CD (ArgoCD)
- ArgoCD Image Updater monitors GitOps repo  
- Automatically syncs manifests to the cluster  
- Ensures declarative GitOps workflow is always maintained  

---

## ⚡ Deployment Steps

### Prerequisites

```bash
# Install Traefik via Helm
helm repo add traefik https://traefik.github.io/charts
helm repo update
helm install traefik traefik/traefik --namespace traefik --create-namespace

# Install Cert-Manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml
```

## 🔍 Verification

✅ Application accessible via HTTPS at harishwisecow.duckdns.org

✅ TLS certificate auto-provisioned

✅ CI pipeline triggers on code changes

✅ ArgoCD automatically deploys updates

✅ GitOps workflow ensures cluster state matches Git