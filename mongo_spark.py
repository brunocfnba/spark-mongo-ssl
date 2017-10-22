from pyspark.sql import SparkSession

my_spark = SparkSession \
    .builder \
    .appName("mySparkMongoJob") \
    .config("spark.mongodb.input.uri", "mongodb://<user>:<pwd>@<hostname>:<port>/<database name>.<collection name>?ssl=true") \
    .getOrCreate()

df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()

df.show()
