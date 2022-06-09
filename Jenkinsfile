pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright/python' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'pip install pytest'
            sh 'pytest -s -v'
         }
      }
   }
}

