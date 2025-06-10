# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fa320c7c-eca1-4dda-9fdf-9b85a2c28fe6",
# META       "default_lakehouse_name": "lh_dp_dev",
# META       "default_lakehouse_workspace_id": "f30de52c-da29-43c7-b29d-cb2bd7a178a6",
# META       "known_lakehouses": [
# META         {
# META           "id": "fa320c7c-eca1-4dda-9fdf-9b85a2c28fe6"
# META         }
# META       ]
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

wg_table_name = 'HumanResources_Department'

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

aw_raw_df = spark.read.table(wg_table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.sql("CREATE DATABASE IF NOT EXISTS silver")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

aw_raw_df.distinct().write.saveAsTable(f'silver.{wg_table_name}')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
