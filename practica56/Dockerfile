FROM websphere-liberty:kernel-java11-openj9
USER root 
RUN apt-get update && apt-get install -y curl
EXPOSE 9080 9443
ENV GID="28000" UID="28000" WLP_HOME="/opt/ibm"

RUN groupadd -g $GID wlp && useradd -rm -d /home/wlp -s /bin/bash -g wlp -u $UID wlp 
RUN chown -R wlp:wlp $WLP_HOME /logs

USER wlp
ADD --chown=wlp:wlp crud-jsp.ear /config/dropins/crud-jsp.ear
ADD --chown=wlp:wlp server.xml /config/
RUN installUtility install --acceptLicense defaultServer
ENTRYPOINT ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]
