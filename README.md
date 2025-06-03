# Blog Platform - Microservices Project

## Overview

This project is a simple blog platform composed of three microservices and a frontend:

- User Service (Node.js + MongoDB)
- Post Service (Flask + PostgreSQL)
- Comment Service (Spring Boot + MySQL)
- Frontend (HTML + React + Axios)

All services are containerized using Docker and run via Docker Compose and Minikube. Optional deployment is available on GCP using GKE.

## How to Run Locally (Docker Compose)

```bash
docker-compose up --build


