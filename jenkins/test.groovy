properties([pipelineTriggers([githubPush()])])

node {
    stage('clone') {
        git url: "https://github.com/technomad21c/cp-abe.git", branch: "master", credentialId: '6ba8dfad-86b4-43be-b926-04762eb1bdba'

    }

    stage('run') {
        bat "./python test.py"
    }
}