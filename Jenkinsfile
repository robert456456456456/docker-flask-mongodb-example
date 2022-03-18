#!/usr/bin/env groovy
node("master"){
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