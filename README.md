# How to connect to MongoDB using Spark over SSL
This repo documents how to use access MongoDB from Apache Spark using the MongoDB connector and also how to connect to a MongoDB over SSL.

The `mongo_spark.py` file has a very simple example on how to connect to a MongoDB instance and collection and read its data. You basically need to create a a new spark session and provide the mongo URL along with the required parameters like user, password and others.<BR><BR>
Then just use the spark context to read the data into a Spark dataframe.
>The `ssl=true` flag can be omitted if no SSL is being used. If you're not using SSL, this code is all that's needed to read data from a MongoDB.
  
To submit this spark job without using SSL simply run the following command:
```
spark-submit --master local[2] --packages org.mongodb.spark:mongo-spark-connector_2.11:2.2.0 mongo_spark.py
```
For the examples, I'm using a local master but you can run in any Spark cluster you may be working on.

####Connecting to MongoDB over SSL

Before submitting a Spark job connecting to a MongoDB using SSL, first you need to get your database certificate (usually a file called something.cert) and save to the machine where you are running the Spark job (the Spark driver) then generate a truststore file using the MongoDB certificate as follows:
```
keytool -import -file <the mongo certificate file> -alias <any alias> -keystore <the truststore file name>
```
>To use the keytool utility you must have java installed. You probably do since you are running spark ;-)

With the generated file run the following spark-submit command:
```
spark-submit --master local[2] --packages org.mongodb.spark:mongo-spark-connector_2.11:2.2.0 --driver-java-options -Djavax.net.ssl.trustStore=<truststore file name> --conf spark.executor.extraJavaOptions=--Djavax.net.ssl.trustStore=<trsutstore file name> mongo_spark.py
```


