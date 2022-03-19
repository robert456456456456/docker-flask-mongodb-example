#!/usr/bin/env groovy
node{
    def _port_random_demo="2101"
    def _port_fulltext_search="2102"
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
            sh 'pkill -f "port-forward"'
            sh 'JENKINS_NODE_COOKIE=dontKillMe nohup kubectl port-forward --address 0.0.0.0 services/random-demo-service '+_port_random_demo+':'_port_random_demo+' &> /dev/null &'
            sh 'JENKINS_NODE_COOKIE=dontKillMe nohup kubectl port-forward --address 0.0.0.0 services/fulltext-search-service '+_port_fulltext_search+':'_port_fulltext_search+' &> /dev/null &'
        }
}