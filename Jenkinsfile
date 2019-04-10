node {
    checkout scm
    docker.withRegistry('https://registry-1.docker.io/v2/', '${credentialsId}'{
        def customImage = docker.build("my-image:${env.BUILD_ID}")
        customImage.push('mytest')
    })
}