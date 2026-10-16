# Exercise 2: Minikube, Kubectl and Flask

## Objective
Deploy a Python Flask application on Kubernetes using Minikube.

## Technologies
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Files
- `app.py` - Flask web application.
- `Dockerfile` - Builds the application image.
- `deployment.yaml` - Defines the Kubernetes Deployment.
- `service.yaml` - Exposes the application through a NodePort Service.

## Implementation
1. Built the image using `minikube image build -t flask-app:latest .`.
2. Deployed the application using `kubectl apply -f deployment.yaml`.
3. Exposed it using `kubectl apply -f service.yaml`.
4. Verified the pod and service using kubectl.
5. Accessed the application using `kubectl port-forward service/flask-app-service 15000:15000`.

## Result
Successfully deployed the Flask application on Kubernetes.

Output: `Hello from Flask on Kubernetes!`
