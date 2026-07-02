# Databricks notebook source
import pandas as pd

# COMMAND ----------

files = [
    {"file":"map_cancellation_reasons"},
    {"file":"map_cities"},
    {"file":"map_payment_methods"},
    {"file":"map_ride_statuses"},
    {"file":"map_vehicle_makes"},
    {"file":"map_vehicle_types"}
]

sas_token = "sp=r&st=2026-06-28T13:58:28Z&se=2026-07-30T22:13:28Z&spr=https&sv=2026-02-06&sr=c&sig=bpCLF%2BMRLpeCeb%2FxhErhw8UslZoSOm0vQg6ORR6iXfo%3D"

for file in files:
    url = f"https://storageprojectuberdev.blob.core.windows.net/raw/ingestion/{file['file']}.json?{sas_token}"
    df = pd.read_json(url)
    df_spark = spark.createDataFrame(df)

    df_spark.write.format("delta")\
        .mode("overwrite")\
        .option("overwriteSchema", "true")\
        .saveAsTable(f"uber.bronze.{file['file']}")

# COMMAND ----------

url = f"https://storageprojectuberdev.blob.core.windows.net/raw/ingestion/bulk_rides.json?{sas_token}"
df = pd.read_json(url)
df_spark = spark.createDataFrame(df)

if not spark.catalog.tableExists("uber.bronze.bulk_rides"):
    df_spark.write.format("delta")\
        .mode("overwrite")\
        .saveAsTable("uber.bronze.bulk_rides")
    print("Not run more than 1 time")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uber.bronze.map_cities

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from uber.bronze.rides_raw

# COMMAND ----------

