# 👨‍💻 Marco Figueroa

**Full-Stack Developer | DevSecOps Engineer | Security Enthusiast**

Building robust, scalable, and secure solutions with modern technologies. Focused on making technology simple yet powerful through automation, cloud infrastructure, and best practices.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/mfigueroa23) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/marcoo.f23) [![X](https://img.shields.io/badge/X-black.svg?logo=X&logoColor=white)](https://x.com/marcoo_f23) [![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:mfigueroa@devsonic.cl)

---

## 🚀 Production Projects

### [DevSonic Ecosystem](https://devsonic.cl)
Full-stack web applications deployed on Kubernetes with modern cloud infrastructure.

| Project | Tech Stack | Status | Links |
|---------|-----------|--------|-------|
| **devsonic.cl** | React 19, Vite, TypeScript, Tailwind CSS 4 | ✅ Live | [devsonic.cl](https://devsonic.cl) |
| **api.devsonic.cl** | NestJS, Prisma, PostgreSQL 17, TypeScript | ✅ Live | [api.devsonic.cl](https://api.devsonic.cl) |
| **petsecure.devsonic.cl** | Angular 20, TypeScript, RxJS | ✅ Live | [petsecure.devsonic.cl](https://petsecure.devsonic.cl) |
| **glpi.devsonic.cl** | IT Asset Management | ✅ Live | Internal |
| **jarvis.devsonic.cl** | Custom Application | ✅ Live | Internal |

**Infrastructure:**
- Kubernetes cluster with custom resource organization (Resource Type → Project)
- Multi-namespace architecture (production, applications, databases)
- SSL/TLS with wildcard certificates
- Docker private registry integration
- Automated deployments with Ingress routing

---

## 💻 Tech Stack

### Frontend Development
![React](https://img.shields.io/badge/react_19-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) ![Angular](https://img.shields.io/badge/angular_20-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white) ![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/tailwindcss_4-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white) ![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white) ![RxJS](https://img.shields.io/badge/rxjs-%23B7178C.svg?style=for-the-badge&logo=reactivex&logoColor=white)

### Backend Development
![NestJS](https://img.shields.io/badge/nestjs-%23E0234E.svg?style=for-the-badge&logo=nestjs&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white) ![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB) ![Prisma](https://img.shields.io/badge/Prisma-3982CE?style=for-the-badge&logo=Prisma&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

### Database & ORM
![Postgres](https://img.shields.io/badge/postgres_17-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Prisma](https://img.shields.io/badge/Prisma_ORM-3982CE?style=for-the-badge&logo=Prisma&logoColor=white)

### DevOps & Infrastructure
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white)

### Cloud Platforms
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=Cloudflare&logoColor=white) ![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white) ![DigitalOcean](https://img.shields.io/badge/DigitalOcean-%230167ff.svg?style=for-the-badge&logo=digitalOcean&logoColor=white)

### Scripting & Automation
![Bash Script](https://img.shields.io/badge/bash_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

### Security & Tools
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white) ![ESLint](https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

---

## 🏗️ Infrastructure as Code

### Kubernetes Architecture
- **Custom two-tier structure**: Resource Type → Project/Environment
- **Multi-namespace design**: `devsonic-cl` (prod), `applications` (dev), `databases` (infra)
- **StatefulSets** for PostgreSQL/MySQL with persistent storage
- **Ingress controllers** with wildcard SSL/TLS certificates
- **ConfigMaps & Secrets** management with Docker registry integration

### Terraform Projects
- **AWS Infrastructure**: VPC, Subnets, EC2, Route53, Security Groups
- **Cloudflare Management**: DNS, CDN, Page Rules, SSL/TLS configuration
- **State management** with versioned backups

### Docker Orchestration
- Multi-container database stack (PostgreSQL 17, MySQL 8.0)
- Custom networks with static IP addressing
- Automated backup scripts and volume management

---

## 🔐 Security & Continuous Learning

### Cybersecurity Practice
- **HackTheBox**: CTF challenges and penetration testing labs
- **OverTheWire**: Wargames and security fundamentals
- **SecLists**: Security wordlists and payloads for authorized testing
- **Virtual Labs**: Kali Linux 2025.4 and Ubuntu Server 24.04.3 (ARM64)

### DevSecOps Approach
- SSL/TLS certificate management with automated renewal workflows
- SSH key-based authentication
- Kubernetes secrets encryption
- Security-first architecture design

---

## 📂 Key Projects & Scripts

### Automation Scripts
- **Docker Management**: Installation, container backups, orchestration
- **Web Server Automation**: Apache virtual host creation, service deployment
- **Backup Systems**: Automated backup solutions for production systems
- **System Administration**: Port extraction, network monitoring, resource management

### Learning Resources
- Comprehensive NestJS course notes with architecture patterns
- Notion Second Brain documentation and productivity systems
- Hands-on projects in React, Angular, and backend development

---

## 🎯 What I Do

- 🔨 Build **full-stack applications** with modern frameworks (React, Angular, NestJS)
- ☁️ Design and deploy **cloud infrastructure** with Kubernetes and Terraform
- 🔒 Practice **DevSecOps** principles with security-first architecture
- 📦 Automate workflows with **Docker, CI/CD, and scripting**
- 🧠 Continuously learn through **CTF challenges and hands-on projects**
- 🎵 Balance technology with creativity and music

---

## 📊 Architecture Highlights

### NestJS API Pattern (api.devsonic.cl)
```
Modular Architecture
├── Feature-based modules (users, notifications)
├── Dependency Injection for services
├── Prisma ORM for type-safe database access
├── RESTful API with Swagger documentation
└── PostgreSQL 17 with migration strategy
```

### React Frontend Pattern (devsonic.cl)
```
Modern React Stack
├── React 19 with TypeScript
├── Vite for blazing-fast builds
├── Tailwind CSS 4 for styling
├── Component-based architecture
└── Vercel deployment with analytics
```

### Kubernetes Deployment Strategy
```
Two-Tier Organization
├── Resource Type (Deployments, Services, Ingress)
│   └── Project Grouping (devsonic-cl, applications, databases)
├── Namespace isolation
├── Wildcard SSL certificates
└── Automated CI/CD integration
```

---

## 💬 Let's Connect

**Ask me about:**
- Full-stack development (React, Angular, NestJS)
- Kubernetes architecture and best practices
- Infrastructure as Code with Terraform
- DevSecOps workflows and automation
- Cybersecurity and penetration testing
- Music and creative pursuits

**Email**: [mfigueroa@devsonic.cl](mailto:mfigueroa@devsonic.cl)
**Website**: [devsonic.cl](https://devsonic.cl)

---

*Building the future, one commit at a time.*
