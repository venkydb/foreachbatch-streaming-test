from beet.cont.process_batch import * 
container = ProcessBatch()
df_stream = spark.readStream.table("samples.nyctaxi.trips")
stream = container.process_batch_func(df_stream)
