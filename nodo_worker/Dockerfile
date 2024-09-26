FROM openjdk:11-jre-slim
RUN apt-get update && apt-get install -y wget

RUN wget https://downloads.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz && \
    tar -xzf spark-3.5.3-bin-hadoop3.tgz && \
    mv spark-3.5.3-bin-hadoop3 /opt/spark && \
    rm spark-3.5.3-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH="$PATH:$SPARK_HOME/bin"

EXPOSE 8081

CMD ["spark-class", "org.apache.spark.deploy.worker.Worker", "spark://ec2-34-239-132-172.compute-1.amazonaws.com: 7077"]