FROM open-liberty:full
EXPOSE 9080
EXPOSE 9443
ENV HTTP_ENDPOINT true
COPY --chown=1001:0 PCMEAR.ear /config/dropins/PCMEAR.ear
COPY --chown=1001:0 server.xml /config/
RUN configure.sh
RUN installUtility install --acceptLicense defaultServer
CMD ["/opt/ol/wlp/bin/server", "run", "defaultServer"]
