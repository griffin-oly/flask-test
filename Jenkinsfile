node {
    checkout scm
    docker.withRegistry('https://registry-1.docker.io/v2/', 'credentials-id'{
        def customImage = docker.build("my-image:${env.BUILD_ID}")
        customImage.push('mytest')
    })
}