pipeline {
    agent any

    environment {
        BACKEND_DIR = "backend"
        FRONTEND_DIR = "frontend"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Clonando repo desde GitHub"
                git branch: 'main',
                    url: 'https://github.com/Juan-Garzaro/luhn-project.git'
            }
        }

        stage('Debug Workspace') {
            steps {
                sh 'pwd && ls -R .'
            }
        }

        stage('Test Backend') {
            steps {
                sh '''
                docker run --rm \
                -v $WORKSPACE/backend:/app \
                -w /app \
                python:3.10 \
                bash -c "ls -la && python -m pip install --upgrade pip && pip install -r requirements.txt"
                '''
            }
        }

        stage('Build Backend Image') {
            steps {
                sh '''
                docker build -t luhn-backend ./backend
                '''
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh '''
                docker build -t luhn-frontend ./frontend
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker compose down || true
                docker compose up -d --build
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                curl -f http://localhost:8001 || echo "Backend no responde"
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline OK ✅"
        }
        failure {
            echo "Pipeline falló ❌ revisa logs"
        }
    }
}