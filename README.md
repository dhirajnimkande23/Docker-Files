# Docker-Files
A collection of ready-to-run Dockerfile examples covering 8 popular technology stacks. Each folder is self-contained with application code, a well-commented Dockerfile, and a .dockerignore.
# Dockerfile Examples

A collection of ready-to-run Dockerfile examples covering 8 popular technology stacks. Each folder is self-contained with application code, a well-commented Dockerfile, and a `.dockerignore`.

---

## Repository Structure

| #   | Folder                    | Stack                                   | Port |
| --- | ------------------------- | --------------------------------------- | ---- |
| 01  | `01-python-flask-app`     | Python 3.12 + Flask 3                   | 5000 |
| 02  | `02-nodejs-express-app`   | Node.js 22 + Express 4                  | 3000 |
| 03  | `03-python-fastapi-app`   | Python 3.12 + FastAPI                   | 8000 |
| 04  | `04-go-http-server`       | Go 1.23 (multi-stage)                   | 8080 |
| 05  | `05-nginx-static-site`    | Nginx 1.27                              | 80   |
| 06  | `06-java-spring-boot-app` | Java 21 + Spring Boot 3.4 (multi-stage) | 8080 |
| 07  | `07-ruby-on-rails-app`    | Ruby 3.4 + Rails 8.0 (API)              | 3000 |
| 08  | `08-dotnet-aspnet-app`    | .NET 9 ASP.NET Core (multi-stage)       | 8080 |

---

## Prerequisites

### Install Docker

**macOS**
```bash
# Install Docker Desktop from https://docs.docker.com/desktop/install/mac-install/
# Or with Homebrew:
brew install --cask docker
```

**Ubuntu / Debian**
```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker $USER   # log out and back in to apply
```

**Amazon Linux 2 / Amazon Linux 2023**
```bash
sudo yum update -y
sudo yum install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
```

Verify installation:
```bash
docker --version
docker run hello-world
```

---

## Clone the Repository

```bash
git clone https://github.com/atulkamble/Dockerfiles.git
cd Dockerfiles
```

---

## Step-by-Step: Build & Run Each App

Each app follows the same three-command pattern:

```
cd <folder>
docker build -t <image-name> .
docker run -d -p <host-port>:<container-port> --name <container-name> <image-name>
```

---

### 01 · Python Flask

```bash
cd 01-python-flask-app

# 1. Build the image
docker build -t flask-app .

# 2. Run the container (detached, port 5000)
docker run -d -p 5000:5000 --name flask-app flask-app

# 3. Test
curl http://localhost:5000
curl http://localhost:5000/health
```

---

### 02 · Node.js Express

```bash
cd 02-nodejs-express-app

# 1. Build the image
docker build -t express-app .

# 2. Run the container (detached, port 3000)
docker run -d -p 3000:3000 --name express-app express-app

# 3. Test
curl http://localhost:3000
curl http://localhost:3000/health
```

---

### 03 · Python FastAPI

```bash
cd 03-python-fastapi-app

# 1. Build the image
docker build -t fastapi-app .

# 2. Run the container (detached, port 8000)
docker run -d -p 8000:8000 --name fastapi-app fastapi-app

# 3. Test
curl http://localhost:8000
curl http://localhost:8000/health

# Interactive API docs are also available at:
# http://localhost:8000/docs
```

---

### 04 · Go HTTP Server

```bash
cd 04-go-http-server

# 1. Build the image (multi-stage: compiles binary, then copies to Alpine)
docker build -t go-server .

# 2. Run the container (detached, port 8080)
docker run -d -p 8080:8080 --name go-server go-server

# 3. Test
curl http://localhost:8080
curl http://localhost:8080/health
```

---

### 05 · Nginx Static Site

```bash
cd 05-nginx-static-site

# 1. Build the image
docker build -t nginx-site .

# 2. Run the container (detached, port 80)
docker run -d -p 80:80 --name nginx-site nginx-site

# 3. Test
curl http://localhost
# Or open http://localhost in a browser
```

---

### 06 · Java Spring Boot

```bash
cd 06-java-spring-boot-app

# 1. Build the image (multi-stage: Maven build → JRE runtime)
#    Note: first build downloads dependencies (~1–2 min)
docker build -t spring-app .

# 2. Run the container (detached, port 8080)
docker run -d -p 8080:8080 --name spring-app spring-app

# 3. Test
curl http://localhost:8080
curl http://localhost:8080/health
```

---

### 07 · Ruby on Rails

```bash
cd 07-ruby-on-rails-app

# 1. Build the image
docker build -t rails-app .

# 2. Run the container (detached, port 3000)
docker run -d -p 3000:3000 --name rails-app rails-app

# 3. Test
curl http://localhost:3000
curl http://localhost:3000/health
```

---

### 08 · .NET ASP.NET Core

```bash
cd 08-dotnet-aspnet-app

# 1. Build the image (multi-stage: SDK build → ASP.NET runtime)
docker build -t dotnet-app .

# 2. Run the container (detached, port 8080)
docker run -d -p 8080:8080 --name dotnet-app dotnet-app

# 3. Test
curl http://localhost:8080
curl http://localhost:8080/health
```

---

## Common Docker Commands

```bash
# List running containers
docker ps

# View container logs
docker logs <container-name>

# Stop a container
docker stop <container-name>

# Remove a stopped container
docker rm <container-name>

# Remove an image
docker rmi <image-name>

# Stop and remove all containers from this project
docker stop flask-app express-app fastapi-app go-server nginx-site spring-app rails-app dotnet-app
docker rm   flask-app express-app fastapi-app go-server nginx-site spring-app rails-app dotnet-app
```

---

## Deploying on an EC2 Instance

### 1. Launch an EC2 Instance
- AMI: Amazon Linux 2023 (recommended)
- Instance type: `t3.micro` or larger
- Security Group — add inbound rules:

| Type   | Protocol | Port |
| ------ | -------- | ---- |
| SSH    | TCP      | 22   |
| HTTP   | TCP      | 80   |
| Custom | TCP      | 3000 |
| Custom | TCP      | 5000 |
| Custom | TCP      | 8000 |
| Custom | TCP      | 8080 |

### 2. Connect via SSH
```bash
chmod 400 your-key.pem
ssh -i your-key.pem ec2-user@<ec2-public-ip>
```

### 3. Install Docker and Git
```bash
sudo yum update -y
sudo yum install -y docker git
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
# Re-connect SSH for the group change to take effect
```

### 4. Clone and Run
```bash
git clone https://github.com/atulkamble/Dockerfile-Examples.git
cd Dockerfile-Examples/01-python-flask-app
docker build -t flask-app .
docker run -d -p 5000:5000 flask-app
```

Access the app at `http://<ec2-public-ip>:5000`.

---

## Best Practices Applied

- **Layer caching** — dependency files are copied and installed before application code so rebuilds reuse cached layers.
- **Multi-stage builds** — Go, Java, and .NET compile in a full SDK image; only the binary/JAR is copied to a minimal runtime image, reducing final image size significantly.
- **`.dockerignore`** — each folder excludes build artefacts, caches, and secrets from the build context.
- **`/health` endpoints** — every app exposes a health-check route compatible with container orchestrators (Kubernetes, ECS, etc.).
