# Databricks notebook source
df = spark.sql("SELECT * FROM delays_table")

# COMMAND ----------

df.count()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.show()

# COMMAND ----------

display(df.select("ARR_DELAY"))

# COMMAND ----------

