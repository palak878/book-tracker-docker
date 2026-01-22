# 📚 Dockerized Book Manager

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **"Build Once, Run Anywhere."**
> A lightweight, containerized CRUD application designed to demonstrate modern **DevOps** workflows and **Microservices** architecture.

---

## 📖 About The Project

This project is a **Book Management System** that solves the classic *"It works on my machine"* problem. By containerizing the application with Docker, it ensures that the entire environment (OS, dependencies, and code) is packaged together, allowing it to run consistently on any platform—from a local laptop to a cloud server.

### 🌟 Key Features
* **🐳 Fully Containerized:** Zero-configuration setup using Docker.
* **🎨 Modern UI:** Server-side rendered interface with a **Dark Mode Glassmorphism** design.
* **⚡ Lightweight:** Built on the `python:slim` base image for fast deployment (~2 seconds startup).
* **🔄 REST API:** Stateless backend handling `GET` and `POST` requests.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Containerization** | [Docker](https://www.docker.com/) | Creates the isolated environment. |
| **Backend** | [Python Flask](https://flask.palletsprojects.com/) | REST API and Routing logic. |
| **Frontend** | HTML5 / CSS3 | Jinja2 Templates with responsive design. |
| **Version Control** | Git | Source code management. |

---

## 🚀 How to Run (The Magic of Docker)

You do **not** need Python installed on your machine. You only need Docker.

### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/palak878/book.git](https://github.com/palak878/book.git)
cd book
