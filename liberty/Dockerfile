--------------------------------- websphere-open-liberty --------------------------

FROM open-liberty:full
EXPOSE 9080
EXPOSE 9443
ENV HTTP_ENDPOINT true
COPY --chown=1001:0 PCMEAR.ear /config/dropins/PCMEAR.ear
RUN configure.sh
ENTRYPOINT ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]

docker build -t owlppcm1 .
docker run -d -p 9080:9080 -p 9443:9443 --name owlppcm1 owlppcm1


--------------------------------- websphere-liberty --------------------------
FROM websphere-liberty:kernel
USER root 
RUN apt-get update && apt-get install -y curl
EXPOSE 9080 9443
ENV GID="28000" UID="28000" WLP_HOME="/opt/ibm"
ENV HTTP_ENDPOINT true

RUN groupadd -g $GID wlp && useradd -rm -d /home/wlp -s /bin/bash -g wlp -u $UID wlp 
RUN chown -R wlp:wlp $WLP_HOME

USER wlp
ADD --chown=wlp:wlp PCMEAR.ear /config/dropins/PCMEAR.ear
ADD --chown=wlp:wlp server.xml /config/
RUN installUtility install --acceptLicense defaultServer
ENTRYPOINT ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]

docker build -t wlppcm1 .
docker run -d -p 9080:9080 -p 9443:9443 --name wlppcm1 wlppcm1

