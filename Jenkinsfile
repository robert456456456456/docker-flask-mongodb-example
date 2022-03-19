#!/usr/bin/env groovy
node{
    stage('Clean up Workspace')
    {
      deleteDir()
    }
    stage ('checkout'){
              checkout scm
          stage ('check'){
              sh 'kubectl apply -f ./kubernetes;kubectl get services;kubectl get pods;kubectl port-forward --address 0.0.0.0 services/random-demo-service 2001:2101&'
        }
      }
}