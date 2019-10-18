node {
    stage('clone') {
        git 'https://github.com/technomad21c/cp-abe.git'
    }

    stage('run') {
        bat './python test.py'
    }
}