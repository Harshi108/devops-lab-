# Exercise 10: Minikube Multi-Node Multi-App Deployment

## Objective
Deploy two Flask applications on a multi-node Kubernetes cluster using Minikube.

## Applications
- Product Catalog: Displays available products.
- Shopping Cart: Allows users to view and add cart items.

## Technologies
- Python and Flask
- Docker
- Kubernetes
- Minikube

## Project Files
- product_catalog.py
- shopping_cart.py
- Dockerfile.product
- Dockerfile.shopping
- product_catalog_deployment.yaml
- shopping_cart_deployment.yaml
- product_catalog_service.yaml
- shopping_cart_service.yaml

## Deployment Design
- Minikube profile: devops-multinode
- Cluster nodes: 3
- Product Catalog replicas: 2
- Shopping Cart replicas: 3
- Services: NodePort

Pod anti-affinity is configured to distribute replicas across nodes.

## Setup and Deployment

Start the multi-node cluster:

    minikube start --nodes 3 -p devops-multinode

Enable the registry add-on:

    minikube -p devops-multinode addons enable registry

Build the images:

    docker build -t product-catalog:latest -f Dockerfile.product .
    docker build -t shopping-cart:latest -f Dockerfile.shopping .

Load images into Minikube:

    minikube -p devops-multinode image load product-catalog:latest
    minikube -p devops-multinode image load shopping-cart:latest

Deploy the applications and services:

    kubectl apply -f product_catalog_deployment.yaml
    kubectl apply -f shopping_cart_deployment.yaml
    kubectl apply -f product_catalog_service.yaml
    kubectl apply -f shopping_cart_service.yaml

Inspect pod placement:

    kubectl get pods -o wide

Access the services:

    minikube -p devops-multinode service product-catalog-service
    minikube -p devops-multinode service shopping-cart-service

## API Endpoints
- Product Catalog: GET /products
- Shopping Cart: GET /cart
- Shopping Cart: POST /cart

## Note
The deployment instructions are documented here. The cluster has not
been created and the applications have not been executed as part of
preparing these files.