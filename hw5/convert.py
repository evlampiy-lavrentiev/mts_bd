from pyspark.sql import SparkSesstion
from onetl.connection import SparkHDFS
from onetl.file import FileDFReader
from onetl.file.format import CSV
from onetl.file.format import ORC
from onetl.file import FileDFWriter

spark = SparkSession.builder.master("local").appName("spark").gerOrCreate()

hdfs = SparkHDFS(host="",ipc_port=8080,cluster="test",spark=spark)
hdfs.check()

csv = CSV(delimiter=",")
reader = FileDFReader(connection=hdfs, format=csv, source_path="")

df = reader.run(["charts.csv", "Netflix TV Shows and Movies.csv"])

df.write.orc("my_file.orc")

df = spark.read.orc("my_file.orc")

orc = ORC()

writer = FileDFWriter(connection=hdfs, target_path="/home/hadoop/my_file.orc", format=orc)

writer.run(df.coalesce(1))
