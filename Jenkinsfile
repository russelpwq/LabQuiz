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
        stage('Code Quality Check via SonarQube') {
            steps {
                script {
                    def scannerHome = tool 'SonarQube';
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=OWASP -Dsonar.sources=."
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                // Navigate to the folder containing tests and run pytest
                dir('labproject/myapp') { 
                    script {
                        sh 'pytest'
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up actions
            script {
                sh 'rm -rf venv'
            }
        }
        success {
            dependencyCheckPublisher pattern: 'dependency-check-report.xml'
        }
    }
}
