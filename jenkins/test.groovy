properties([pipelineTriggers([githubPush()])])

node {
    stage('clone') {
        git url: "https://github.com/technomad21c/cp-abe.git", branch: "master"
    }

    stage('run') {
        bat "./python test.py"
    }
}