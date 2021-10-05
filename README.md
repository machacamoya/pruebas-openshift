Repositorio para pruebas openshift

------------------------------------------------------------------------------------------------
https://two-oes.medium.com/working-with-nfs-as-a-storageclass-in-openshift-4-44367576771c

- oc login -u kubeadmin -p XXXXXXXX https://api.crc.testing:6443
oc create namespace openshift-nfs-storage
oc project openshift-nfs-storage
 
cd kubernetes-incubator/nfs-client/
NAMESPACE=`oc project -q`
oc create -f deploy/rbac.yaml
oc adm policy add-scc-to-user hostmount-anyuid system:serviceaccount:$NAMESPACE:nfs-client-provisioner
oc create -f deploy/class.yaml 
oc create -f deploy/deployment.yaml
oc get pods -n openshift-nfs-storage

------------------------------------------------------------------------------------------------
################## DOCKER ######################
- docker search imagen
- docker pull imagen
- docker run imagen -d
- docker images
- docker ps
- docker ps -a
- docker stop contenedor
- docker rm contenedor
- docker rmi imagen
- docker system prune -a
- docker container prune
- docker build -f Dockerfile.slave -t slave-ansiable .
- docker build -f Dockerfile.jenkins -t jenkins-ansiable .
- docker run --name jenkins_ansible -p 8080:8080 -p 50000:50000 --env JAVA_OPTS="-Djava.util.logging.config.file=/PATH_TO_DIR/log.properties" -v /PATH_TO_DIR/data:/var/jenkins_home --env JAVA_OPTS=-Dhudson.footerURL=http://XXXX.org jenkins_ansible
- docker run --name server1 -h server1 -d slave
- docker inspect server1 | grep IPAddress
------------------------------------------------------------------------------------------------
################## CRC ########################
- crc start
- crc start --log-level debug
- crc status
- crc status --log-level debug
- crc console --credentials

############ REINSTALAR ######################
- crc delete -f
- crc cleanup
- Enable Docker
- Restart laptop
- rm -fr ~/.crc
- crc setup
- crc start -p pull-secret.txt --log-level debug
------------------------------------------------------------------------------------------------
################## OC ########################
- oc create namespace openshift-nfs-storage
- oc label namespace openshift-nfs-storage "openshift.io/cluster-monitoring=true"
- oc project openshift-nfs-storage
- oc create -f deploy/rbac.yaml
- oc adm policy add-scc-to-user hostmount-anyuid system:serviceaccount:$NAMESPACE:nfs-client-provisioner
- oc create -f deploy/class.yaml 
- oc create -f deploy/deployment.yaml
- oc get pods -n openshift-nfs-storage

------------------------------------------------------------------------------------------------
################## JENKINS ########################

docker run --name jenkins -p 8080:8080 -p 50000:50000 --env JAVA_OPTS="-Djava.util.logging.config.file=./log.properties" -v ./data:/var/jenkins_home jenkins

-------------------------------------------------------------------------------------------------

- DNSMASQ

/etc/NetworkManager/conf.d/crc-nm-dnsmasq.conf

[main]

#dns=dnsmasq


O

/etc/NetworkManager/NetworkManager.conf # deshabilitar dnsmasq en NetworkManager

[main]

dns=none




/etc/dnsmasq.d/crc.conf 

server=/crc.testing/XXX.XXX.XXX.XXX

address=/apps-crc.testing/XXX.XXX.XXX.XXX

local=/nfs-server/


/etc/hosts

XXX.XXX.XXX.XXX nfs-server

