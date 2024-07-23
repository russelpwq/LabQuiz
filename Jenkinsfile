pipeline {
    agent any

    environment {
        // Define environment variables
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
                // Run tests with pytest
                script {
                    sh 'venv/bin/pytest --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                // Archive test results
                junit 'test-results/results.xml'
            }
        }
        stage('OWASP Dependency-Check Vulnerabilities') {
            steps {
                withCredentials([string(credentialsId: 'nvd-api-key', variable: 'NVD_API_KEY')]) {
                    dependencyCheck additionalArguments: '''
                        -o './'
                        -s './'
                        -f 'ALL'
                        --prettyPrint
                        --nvdApiKey '${NVD_API_KEY}'
                    ''', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
                    
                    dependencyCheckPublisher pattern: 'dependency-check-report.xml'
                }
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
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
