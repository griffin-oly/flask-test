node {
    def app

    stage('Clone repo'){
        checkout scm
    }
    stage('Build Image'){
        app = docker.build("ggriffin924/flask-test")
    }
    stage('Push Image to dockerhub'){
        docker.withRegistry('https://registry-1.docker.io/v2/', 'pipeline-docker-hub') {
             app.push("pipeline2-${env.BUILD_NUMBER}")
             app.push("latest")
        }
    }
    stage('Deploy Docker image'){
        // docker run -d --name pipeline-test2 -p 5000:5000 ggriffin924/flask-test:<label>
            echo "${env.BUILD_NUMBER}"
            try {
                sh  docker stop pipeline-test2
                sh  docker rm pipeline-test2
            } catch (all) {
                // do cleanup
                echo "Docker container not found"
                // throw new Exception("Stop docker container failed")
            }
            // sh docker run -d --name pipeline-test2 -p 5000:5000 ggriffin924/flask-test:pipeline2-${env.BUILD_NUMBER}           
    }
}