node {
    checkout scm
    docker.withRegistry([ credentialsId:'docker-hub', url:'https://registry-1.docker.io/v2/' ]) {
        def customImage = docker.build("my-image:${env.BUILD_ID}")
        customImage.push('mytest')
    })
}