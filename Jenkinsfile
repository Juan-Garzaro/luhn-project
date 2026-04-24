pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Juan-Garzaro/luhn-project.git'
            }
        }

        stage('CI Backend') {
            steps {
                sh """
                docker run --rm \
                -v $WORKSPACE/backend:/app \
                -w /app python:3.10 \
                bash -c "pip install -r requirements.txt && python -m unittest discover"
                """
            }
        }

        stage('CI Frontend') {
            steps {
                sh """
                echo "Validando frontend..."
                ls frontend
                docker build -t luhn-frontend ./frontend
                """
            }
        }

        stage('Build Backend Image') {
            steps {
                sh "docker build -t luhn-backend ./backend"
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh "docker build -t luhn-frontend ./frontend"
            }
        }

        stage('Deploy') {
            steps {
                sh "docker compose up -d"
            }
        }

        stage('Health Check') {
            steps {
                sh "curl http://localhost:8001 || true"
            }
        }
    }
}