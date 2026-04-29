# 🌐 Multi-Cloud Application (AWS ↔ Azure)

A real-world multi-cloud project demonstrating containerization, deployment, and cross-cloud communication.

---

## ☁️ Architecture
![Architecture](screenshots/multi-cloud-architecture.png)

- AWS ECS (Fargate) hosts nginx container  

![Architecture](screenshots/multi-cloud-architecture.png)

---

- Amazon ECR stores Docker image  

![ECR](screenshots/Amazon%20ECR%20stores%20Docker%20image.png)

---

- Azure App Service hosts Flask API  

![Azure App Service](screenshots/awsCluster&AzureAppService.png)

---

- AWS communicates with Azure via HTTPS  

![Result](screenshots/Result.png)

---

## 🔗 Flow

User → AWS ECS → Azure API → Response → User

---

## 🛠️ Tech Stack

- Docker  
- nginx  
- Python Flask  
- AWS ECS (Fargate)  
- Amazon ECR  
- Azure App Service  

---

## 🚀 Author

Khalid Korena
