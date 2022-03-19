#!/usr/bin/env groovy
node{
    stage('Clean up Workspace')
    {
      deleteDir()
    }
    stage ('checkout'){
           checkout scm
      }
    stage ('Update K8S'){
              sh 'kubectl apply -f ./kubernetes'
      }
    stage ('Check K8S'){
          sh'kubectl get services;kubectl get pods'
        }
    stage('Open Ports For Services'){
            sh 'kubectl port-forward --address 0.0.0.0 services/random-demo-service 2101:2101 &> /dev/null &'
            sh 'kubectl port-forward --address 0.0.0.0 services/fulltext-search-service 2102:2102 &> /dev/null &'
        }
}