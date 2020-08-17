pipeline {
    agent any

    stages {
        stage('build api') {
            steps {
                dir('api') {
                    sh 'make build'
                }
            }
        }
        stage('test api') {
            steps {
                dir('api') {
                    sh 'make test'
                }
            }
        }
        stage('lint api') {
            steps {
                dir('api') {
                    sh 'make lint'
                }
            }
        }
        stage('build gui') {
            steps {
                dir('gui') {
                    sh 'make build'
                }
            }
        }
        stage('build package') {
            steps {
                dir('package') {
                    sh 'make build'
                }
            }
        }
        stage('test package') {
            steps {
                dir('package') {
                    sh 'make test'
                }
            }
        }
        stage('lint package') {
            steps {
                dir('package') {
                    sh 'make lint'
                }
            }
        }
        stage('verify package') {
            steps {
                sh 'make verify'
            }
        }
        stage('push api') {
            when {
                branch 'master'
            }
            steps {
                dir('api') {
                    sh 'make push'
                }
            }
        }
        stage('push gui') {
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
