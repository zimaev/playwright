#!groovy

pipeline {

    agent {
        docker { image 'mcr.microsoft.com/playwright/python:v1.26.0-focal' }
    }

    parameters {
        choice(
            name:'measured_environment',
            choices: ['test', 'prod', 'dev'],
            description: 'среда')
    }

    environment {
        mail_to='123456789@qq.com'
    }

    options {
        buildDiscarder(
            logRotator(daysToKeepStr: '7', numToKeepStr: '10', artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10'))
    }

    triggers {
		cron('H 2 * * 1-5')
    }

    stages {
        stage('Prepare'){
            steps {
                script{
                    echo "Среда：${params.measured_environment}"
                }
            }
        }
        stage('Test') {
            steps {
                script{
		    sh "pip install --user -r requirements.txt"
                    sh "pytest --alluredir allure-results --env ${measured_environment}"
                    sh "allure generate allure-results --clean -o allure-report"
                    }
                }
            }
        }

    post {
        always {
            allure([
                disabled: false,
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-report/']]
                ])
            step([
                $class: 'Mailer',
                recipients: "${mail_to}",
                notifyEveryUnstableBuild: true,
                sendToIndividuals: true
                ])
            deleteDir()
        }
    }

}
