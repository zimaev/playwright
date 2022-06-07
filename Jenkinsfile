pipeline {
   agent { docker { image 'mcr.microsoft.com/playwright:v1.22.0-focal' } }
   stages {
      stage('e2e-tests') {
         steps {
            sh 'python -m pip install --upgrade pip'
            sh 'pip install playwright'
         }
      }
   }
}

