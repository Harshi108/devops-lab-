pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Exercise 6: Quick-Commerce Monitoring'
                checkout scm
            }
        }

        stage('Validate Project Files') {
            steps {
                echo 'Checking Exercise 6 project files'
                bat 'dir Exercises\Exercise-06-Grafana-Monitoring'
                bat 'python --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t quick-commerce-monitor Exercises\Exercise-06-Grafana-Monitoring'
            }
        }
    }

    post {
        success {
            echo 'Quick-commerce monitoring image built successfully.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
