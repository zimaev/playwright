pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'sudo pip install -r requirements.txt'
            sh 'pytest -s -v'
         }
      }
   }
}

