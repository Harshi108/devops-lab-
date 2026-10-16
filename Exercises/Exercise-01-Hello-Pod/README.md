\# Exercise 1: Hello Pod



\## Objective

Deploy an Nginx application inside Kubernetes and access it using a NodePort Service.



\## Tools

\- Docker Desktop

\- Minikube

\- kubectl

\- Kubernetes

\- Nginx



\## Steps Performed



1\. Started the Kubernetes cluster using `minikube start --driver=docker`.

2\. Verified the node using `kubectl get nodes`.

3\. Created the Pod using `kubectl run hello-k8s --image=nginx --port=80`.

4\. Verified the Pod using `kubectl get pods`.

5\. Exposed the Pod using `kubectl expose pod hello-k8s --type=NodePort --port=80`.

6\. Checked the Service using `kubectl get services`.

7\. Verified the endpoint using `kubectl get endpoints hello-k8s`.

8\. Opened the application using `minikube service hello-k8s`.



\## Result

The Nginx Pod reached the Running state, the Service was connected to the Pod, and the Nginx welcome page was displayed successfully in the browser.



\## Conclusion

Successfully deployed and accessed an Nginx application on a local Kubernetes cluster using Minikube.

