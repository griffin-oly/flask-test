node {
    def app
    container_nm = "pipeline-test2"  // mybe move this to an env Var later

    stage('Clone repo'){
        checkout scm
    }
    stage('Build Image'){
        app = docker.build("ggriffin924/flask-test")
    }
    stage('Push Image to dockerhub'){
        docker.withRegistry('https://registry-1.docker.io/v2/', 'pipeline-docker-hub') {
             app.push("${container_nm}-${env.BUILD_NUMBER}")
             app.push("latest")
        }
    }
    stage('Deploy Docker image'){
        // docker run -d --name pipeline-test2 -p 5000:5000 ggriffin924/flask-test:<label>
            def mytag = "ggriffin924/flask-test:pipeline2-${env.BUILD_NUMBER}"
            echo "My current build image: ${mytag}"
            try {
                sh  "docker stop ${container_nm}"
                sh  "docker rm ${container_nm}"
            } catch (all) {
                // do cleanup
                echo "Docker ${container_nm} not found"
                // throw new Exception("Stop docker container failed")
            }
            sh "docker run -d --name ${container_nm} -p 5000:5000 ${mytag}"           
    }
}