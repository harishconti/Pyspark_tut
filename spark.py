from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("app").getOrCreate()


df = spark.read.csv("data/train.csv", header=True)