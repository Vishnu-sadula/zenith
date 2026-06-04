# Flask + MongoDB Kubernetes Deployment

A lightweight Flask user registry application connected to a MongoDB backend database and managed via Mongo-Express.

## Getting Started

Follow these steps directly inside your terminal environment to launch the stack.

### Clone project
1. Clone the github repo
2. cd zenith

### Launch the k8s manifests
3. kubectl apply -f k8s/

... wait for 30 seconds ...

4. kubectl get pods

### To access the application

http://localhost:8000 for web app
kubectl port-forward svc/web 8000:8000 --address 0.0.0.0 &

http://localhost:8081 for mongo-express
kubectl port-forward svc/mongo-express 8081:8081 --address 0.0.0.0 &
