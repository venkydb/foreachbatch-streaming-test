from shared_functions import shared_foo

# Define processing function
def process_record(batch_df, batch_id):
    shared_foo()

def process_batch_func(df_stream):
  write_stream = df_stream.writeStream.foreachBatch(process_record)
  query = write_stream.trigger(once=True).start()
  query.awaitTermination()
