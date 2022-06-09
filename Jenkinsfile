pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:focal' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pip install pytest'
            sh 'pytest -s -v'
         }
      }
   }
}

