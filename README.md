# 🚀 Pull Request Dashboard (DevOps Project)

## 📌 Introduction

The Pull Request Dashboard is a DevOps-based web application that allows users to monitor and analyze pull requests from any public GitHub repository. It provides real-time insights into repository activity, helping developers and teams track contributions efficiently.

---

## 🎯 Objectives

* To build a web-based dashboard for monitoring GitHub pull requests
* To integrate GitHub REST API for real-time data fetching
* To implement containerization using Docker
* To demonstrate DevOps concepts such as automation and portability

---

## 🛠️ Technologies Used

* **Python (Flask)** – Backend web framework
* **HTML/CSS** – Frontend user interface
* **Docker & Docker Compose** – Containerization
* **Git & GitHub** – Version control
* **GitHub API** – Data source for pull requests

---

## ⚙️ Features

* 🔍 Enter any GitHub username and repository name
* 📊 Display list of pull requests with:

  * PR Number
  * Title
  * Author
  * Status
* 📈 Show total number of pull requests
* 🌐 Works for any public GitHub repository
* 🐳 Fully containerized using Docker for easy deployment

---

## 📂 Project Structure

```
devopsprojectpullrequestdashboard/
│
├── src/
│   └── main/
│       ├── app.py
│       └── templates/
│           └── index.html
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run the Project

### 🔹 Prerequisites

* Docker installed on your system
* Git installed

### 🔹 Steps

1. Clone the repository:

```
git clone https://github.com/Devanshu-MUJ/devopsprojectpullrequestdashboard.git
cd devopsprojectpullrequestdashboard
```

2. Run the application:

```
docker-compose up --build
```

3. Open in browser:

```
http://localhost:8080
```

---

## 📸 Usage

1. Enter GitHub username
2. Enter repository name
3. Click **Fetch PRs**
4. View pull request details instantly

---

## 💡 Advantages

* Eliminates manual tracking of pull requests
* Provides quick insights into repository activity
* Works across different environments using Docker
* Simple and user-friendly interface

---

## ⚠️ Limitations

* Works only with public repositories
* Limited to API response (default pagination)
* No authentication for private repositories

---

## 🚀 Future Enhancements

* Add GitHub authentication for private repositories
* Display closed and merged pull requests
* Add charts and visual analytics
* Implement CI/CD pipeline using GitHub Actions

---

## 📚 Conclusion

This project demonstrates the practical implementation of DevOps concepts such as API integration, containerization, and automation. The Pull Request Dashboard simplifies monitoring of repository activity and can be extended into a more advanced DevOps tool.

---

## 👨‍💻 Author

Developed by: **Devanshu Sharma**

---

## 🔗 Repository Link

(https://github.com/Devanshu-MUJ/devopsprojectpullrequestdashboard)
