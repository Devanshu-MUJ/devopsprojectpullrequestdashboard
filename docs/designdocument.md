# Design Document

## System Architecture

User → Flask App → GitHub API → Response → UI Display

## Components

### 1. Frontend

* HTML/CSS interface
* Input form for username and repository
* Table to display PR data

### 2. Backend

* Flask web framework
* Handles HTTP requests and responses
* Processes API data

### 3. API Layer

* GitHub REST API
* Endpoint: /repos/{owner}/{repo}/pulls

### 4. Containerization

* Dockerfile for building image
* Docker Compose for orchestration

## Workflow

1. User enters repository details
2. Request sent to Flask backend
3. Backend calls GitHub API
4. API returns PR data
5. Data displayed on dashboard

## Data Flow

Input → API Request → JSON Response → Data Processing → HTML Rendering

## Design Considerations

* Simplicity and usability
* Scalability using Docker
* Real-time data fetching
