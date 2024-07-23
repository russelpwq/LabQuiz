pipeline {
    agent any

    environment {
        // Define environment variables if needed
        DJANGO_SETTINGS_MODULE = 'labproject.settings'
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git url: 'https://github.com/russelpwq/LabQuiz.git', branch: 'main'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                // Set up Python environment
                script {
                    // Create and activate virtual environment
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install project dependencies
                script {
                    sh 'venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run integration tests
                script {
                    sh 'venv/bin/python manage.py test'
                }
            }
        }

        stage('Post-Test Actions') {
            steps {
                // Archive test results, generate reports, etc.
                junit '**/tests.xml'
            }
        }
    }

    post {
        always {
            // Clean up actions, such as removing the virtual environment
            script {
                sh 'rm -rf venv'
            }
        }
    }
}
