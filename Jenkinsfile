pipeline {
    agent any

    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }

    stages {
        stage('Clone') {
            steps {
                echo "Cloning repository..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Creating virtual environment and installing from requirements.txt..."
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running pytest..."
                sh '''
                source venv/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                echo "Running Flask app..."
                sh '''
                source venv/bin/activate
                nohup flask run --host=0.0.0.0 --port=5000 &
                sleep 5
                curl http://localhost:5000
                '''
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh 'pkill -f "flask run" || true'
        }
    }
}
