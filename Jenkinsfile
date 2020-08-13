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
        stage('Build module') {
            steps {
                dir('module') {
                    sh 'make build'
                }
            }
        }
        stage('Test module') {
            steps {
                dir('module') {
                    sh 'make test'
                }
            }
        }
        stage('Setup module') {
            steps {
                sh 'make setup'
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
