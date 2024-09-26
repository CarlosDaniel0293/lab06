from pyspark.sql import SparkSession
# Inicializa la sesión de Spark
spark = SparkSession.builder \
    .appName("MovieLens Analysis") \
    .master("spark://ec2-34-239-132-172.compute-1.amazonaws.com: 7077") \
    .getOrCreate()
# Ruta al archivo CSV de MovieLens
data_file = "ml-100k/u.data"
 
try:
# Lee el archivo CSV
    movies_df = spark.read.csv(data_file, sep='\t', header=False, inferSchema=True)
# Muestra el esquema del DataFrame movies_df.printSchema()
    movies_df.printSchema()
# Muestra las primeras filas del DataFrame movies_df.show()
    movies_df.show()

except Exception as e:
    print("Error during processing: {e}")
# Detén la sesión de Spark
spark.stop()