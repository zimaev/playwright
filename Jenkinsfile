pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pytest -s -v'
         }
      }
   }
}

