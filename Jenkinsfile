pipeline {
    agent { label 'Recursive'}
    stages{
        stage('Create Images') {
            steps {
                sh 'python3 Dockerdeploy.py'
                sh 'pip install docker'
                archiveArtifacts artifacts: 'images.list', fingerprint: true
            }
        }
        stage('Update on dockerHUB') {
            steps {
                sh 'ls'
            }
        }
    }
}