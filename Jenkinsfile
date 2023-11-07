pipeline{
    agent any
    triggers{
        githubPush()
    }
    stages{
        stage('Checkout'){
            steps{
                Checkout scm
            }
        }
    }
}