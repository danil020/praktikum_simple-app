
pipeline {
    agent any

    environment {
        IMAGE_NAME = 'nielldd/simple-app'
        REGISTRY = 'https://index.docker.io/v1/'
        REGISTRY_CREDENTIALS = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Mengambil kode dari GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Memeriksa Docker dan Docker Compose...'
                bat 'docker --version'
                bat 'where docker-compose'
                bat 'docker-compose version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Membangun Docker image...'
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Deploy App + Database') {
            steps {
                echo 'Menjalankan aplikasi dan database...'
                bat 'docker compose up -d --build'
                bat 'ping -n 21 127.0.0.1 > nul'
            }
        }

        stage('Verify') {
            steps {
                echo 'Memeriksa aplikasi Flask...'
                bat 'curl --fail --silent --show-error http://localhost:5000/'
                bat 'curl --fail --silent --show-error http://localhost:5000/db'
            }
        }

        stage('Push Docker Image') {
            steps {
                echo 'Mengirim image ke Docker Hub...'
                script {
                    docker.withRegistry(REGISTRY, REGISTRY_CREDENTIALS) {
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push('latest')
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline selesai.'
        }
    }
}
