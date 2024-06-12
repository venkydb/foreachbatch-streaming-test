from pyspark.sql import SparkSession
def get_spark():
    spark = SparkSession.builder.getOrCreate()
    return spark
