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
    stage ('Creat Deploy'){
     try{sh 'pkill -f "port-forward"'}catch (Exception e) {sh 'echo port not forward '}
        sh'python3 replace_string.py '
    }
    stage ('Update K8S'){
              sh 'kubectl apply -f ./kubernetes'
      }
    stage ('Check K8S'){
          sh 'kubectl get services -A;kubectl get pods -A'
        }

    stage('Post Deploy Test'){
      sh 'wget http://ec2-52-54-170-77.compute-1.amazonaws.com:'+_port_random_demo+'/apidocs/ && echo "WE GOT IT";exit 0 || echo "Failure";exit 1'
      sh 'wget http://ec2-52-54-170-77.compute-1.amazonaws.com:'+_port_fulltext_search+'/apidocs/ && echo "WE GOT IT";exit 0 || echo "Failure";exit 1'
    }
}