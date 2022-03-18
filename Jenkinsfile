#!/usr/bin/env groovy
node{
    stage('Clean up Workspace')
    {
      deleteDir()
    }

    stage ('checkout'){
              checkout scm
          stage ('check'){
              sh 'pwd; ls'
        }
      }

}