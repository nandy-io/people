pipeline {
    agent any

    stages {
        stage('Build api') {
            steps {
                dir('api') {
                    sh 'make build'
                }
            }
        }
        stage('Test api') {
            steps {
                dir('api') {
                    sh 'make test'
                }
            }
        }
        stage('Build gui') {
            steps {
                dir('gui') {
                    sh 'make build'
                }
            }
        }
        stage('Build package') {
            steps {
                dir('package') {
                    sh 'make build'
                }
            }
        }
        stage('Test package') {
            steps {
                dir('package') {
                    sh 'make test'
                }
            }
        }
        stage('Verify package') {
            steps {
                sh 'make verify'
            }
        }
        stage('Push api') {
            when {
                branch 'master'
            }
            steps {
                dir('api') {
                    sh 'make push'
                }
            }
        }
        stage('Push gui') {
            when {
                branch 'master'
            }
            steps {
                dir('gui') {
                    sh 'make push'
                }
            }
        }
    }
}
