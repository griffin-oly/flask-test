node {
    checkout scm
    docker.withRegistry('https://registry-1.docker.io/v2/', 'pipeline-docker-hub') {
        def customImage = docker.build("ggriffin924/flask-test:${env.BUILD_ID}")
        customImage.push('mytest')
    }
}