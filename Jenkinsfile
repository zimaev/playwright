pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python:v1.22.0-focal' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pip install playwright'
            sh 'playwright install --with-deps'
            sh 'pytest -s -v'
         }
      }
   }
}

