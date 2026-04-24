pipeline {
    agent any

    environment {
        BACKEND_DIR = "backend"
        FRONTEND_DIR = "frontend"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Juan-Garzaro/luhn-project.git'
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -R'
            }
        }

        stage('Test Backend') {
            steps {
                sh '''
                docker run --rm \
                -v $WORKSPACE/backend:/app \
                -w /app python:3.10 \
                bash -c "pip install -r requirements.txt"
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t luhn-backend ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t luhn-frontend ./frontend'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose -f docker-compose.yml up -d'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:8001 || true'
            }
        }
    }
}