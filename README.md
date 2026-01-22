# 📚 Dockerized Book Manager

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A lightweight, **containerized** Book Management System built with **Flask** and **Docker**.
This project demonstrates how to package an application to run consistently on any machine, solving the *"It works on my machine"* problem.

---

## 🚀 Quick Start

You only need **Docker** installed. No Python setup required!

```bash
# 1. Clone the repo
git clone [https://github.com/palak878/book.git](https://github.com/palak878/book.git)
cd book

# 2. Build the Docker Image
docker build -t book-manager .

# 3. Run the Container
docker run -p 5000:5000 book-manager
