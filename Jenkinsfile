pipeline {
	agent any
	////agent { docker { image 'python:3.7.2' } }
	triggers{
		pollSCM('1-59 0-23 * * *')
		cron('00 1 * * *')
	}
 	stages {
 		stage("Compile") {
 			steps {
 				echo "no need to build python code"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python file_for_jenkins.py"
 			}
 		}
 	}
}
