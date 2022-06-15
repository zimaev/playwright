pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.23.0-focal' } }
   stages {
      stage('install') {
         steps {
            sh 'pip install playwright'
            sh 'playwright install'
         }
      stage('e2e-tests') {
         steps {
            sh 'pytest -s -v'
         }
      }
   }
}

