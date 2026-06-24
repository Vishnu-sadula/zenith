# Enterprise-Grade Flask & MongoDB Kubernetes Cluster

A highly available, production-ready microservices architecture showcasing advanced DevOps engineering. This repository deploys a Python Flask web application tightly coupled with a MongoDB backend and Mongo-Express administrative dashboard, orchestrated entirely within Kubernetes.

## Project Highlights
**Automated Kubernetes Orchestration:** Production-grade Deployment and Service manifests utilizing precise readiness/liveness probes for self-healing infrastructure.
**Secure State & Configuration Management:** Zero-cleartext secrets utilizing Kubernetes Secret objects and injected environmental contexts.
**Persistent Storage Lifecycles:** Zero-data-loss database layer via PersistentVolumeClaim (PVC) bindings ensuring storage state survives pod lifecycles.
**Optimized Containerization:** Multi-stage Dockerfile configurations designed to minimize attack surfaces and image footprints.

## Quick Start & Deployment Blueprint

### 1. Provision Persistent Storage Layer
```bash
kubectl apply -f k8s/mongo-pvc.yaml
```
### 2. Deploy Applications & Database Workloads
```bash
kubectl apply -f k8s/
```
