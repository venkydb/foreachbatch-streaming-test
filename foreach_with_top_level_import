from process_batch import process_batch_func
df_stream = spark.readStream.table("samples.nyctaxi.trips")
process_batch(df_stream)
