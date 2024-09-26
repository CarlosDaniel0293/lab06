
# Dockerfile para el nodo maestro
FROM openjdk: 11-jre-slim
# Instalar wget
RUN apt-get update && apt-get install -y wget
# Descargar e instalar Apache Spark
RUN wget https://downloads.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.3-bin-hadoop3.tgz && \
    mv spark-3.5.3-bin-hadoop3 /opt/spark && \
    rm spark-3.5.3-bin-hadoop3.tgz
# Configurar variables de entorno
ENV SPARK_HOME=/opt/spark
ENV PATH="$PATH: $SPARK_HOME/bin"
# Exponer puertos necesarios EXPOSE 8080 7077
EXPOSE 8080 7077
# Comando por defecto
CMD ["spark-class", "org.apache.spark.deploy.master.Master"]