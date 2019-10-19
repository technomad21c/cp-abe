properties([pipelineTriggers([githubPush()])])

node {
    stage('clone') {
        git url: "https://github.com/technomad21c/cp-abe.git", branch: "master", credentialId: '	25d12c3f-0c17-4d02-9e4a-fc41e2b9e437'

    }

    stage('run') {
        bat "./python test.py"
    }
}