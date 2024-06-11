# Databricks notebook source
from shared_functions import shared_foo

# Define processing function
def process_record(record):
    shared_foo()

df_stream = spark.readStream.table("samples.nyctaxi.trips")
write_stream = df_stream.writeStream.foreachBatch(process_record)
query = write_stream.trigger(once=True).start()
query.awaitTermination()

# COMMAND ----------


