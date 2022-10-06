pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.22.0-focal' } }
   stages {
      stage('install') {
         steps {
            sh 'pip3 install playwright'
            sh 'playwright install'
         }
      }
   }
}

