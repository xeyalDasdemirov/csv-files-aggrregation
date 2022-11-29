import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == "__main__":

    print(len(sys.argv))
    if (len(sys.argv) != 3):
        print("Usage: spark-etl [input-folder] [output-folder]")
        sys.exit(0)

spark = SparkSession.builder.master("local").appName("PL analyses")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()

PL = spark.read.format("csv")\
    .option("header", "true")\
    .option("mode", "FAILFAST")\
    .option("inferSchema", "true")\
    .load(sys.argv[1])

Res_PL = PL.groupBy("FTR").count()

Res_PL.repartition(1)\
    .write.format("csv")\
    .option("header", "true")\
    .mode("overwrite")\
    .save(sys.argv[2])