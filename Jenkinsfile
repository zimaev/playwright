pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:focal' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pytest -s -v'
         }
      }
   }
}

