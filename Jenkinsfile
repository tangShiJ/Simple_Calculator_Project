pipeline {
  agent any
  stages {
    stage('Build and Test (Docker)') {
      agent {
        docker {
          image 'python:3.11-slim'
          args '-v $WORKSPACE:/workspace'
        }
      }
      steps {
        dir('/workspace') {
          sh 'python -m pip install --upgrade pip'
          sh 'python -m pip install -r requirements.txt || true'
          sh 'python -m pip install -e .'
          sh 'pytest -q --junitxml=results.xml'
          // archive JUnit report
          junit 'results.xml'
        }
      }
    }
  }
}

