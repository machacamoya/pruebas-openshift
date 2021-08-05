Repositorio para pruebas openshift

- docker search imagen
- docker pull imagen
- docker run imagen -d
- docker images
- docker ps
- docker ps -a
- docker stop contenedor
- docker rm contenedor
- docker rmi imagen


https://two-oes.medium.com/working-with-nfs-as-a-storageclass-in-openshift-4-44367576771c

- oc create namespace openshift-nfs-storage
- oc label namespace openshift-nfs-storage "openshift.io/cluster-monitoring=true"
- oc project openshift-nfs-storage
- oc create -f deploy/rbac.yaml
- oc adm policy add-scc-to-user hostmount-anyuid system:serviceaccount:$NAMESPACE:nfs-client-provisioner
- oc create -f deploy/class.yaml 
- oc create -f deploy/deployment.yaml
- oc get pods -n openshift-nfs-storage



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

