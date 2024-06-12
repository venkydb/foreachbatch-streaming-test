import sys,os
from beetles.container.spark import *
from beetles.container.shared_functions import *
#spark = get_spark()

class ProcessBatch:
    def __init__(self):
        # Initialize any necessary attributes here
        self.zone_name = " "
        self._reset_zone_name()

    def _reset_zone_name(self):
        self.zone_name = "venky"

    def __foreach_batch(self, batch_df, batch_id):
        # Call shared_foo or any other necessary processing
        shared_foo()

    def process_batch_func(self, df_stream):
        write_stream = df_stream.writeStream.foreachBatch(lambda batch_df,epoch_id: self.__foreach_batch(batch_df, epoch_id)).trigger(once=True).queryName(self.zone_name + '_write_stream_data_working_path').start()
        write_stream.awaitTermination()


