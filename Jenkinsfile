
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
                echo 'Memeriksa aplikasi...'
                bat 'python --version'
                bat 'docker --version'
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
