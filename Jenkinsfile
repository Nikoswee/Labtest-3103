pipeline {
	agent any
	stages {
		stage('Checkout SCM') {
			steps {
				git 'C:/Users/nikos/Desktop/Labtest 3103'
			}
		}

		stage('OWASP DependencyCheck') {
			steps {
				dependencyCheck additionalArguments: '--format HTML --format XML', odcInstallation: 'Default'
			}
		}
	}	
	post {
		success {
			dependencyCheckPublisher pattern: 'dependency-check-report.xml'
		}
	}
}