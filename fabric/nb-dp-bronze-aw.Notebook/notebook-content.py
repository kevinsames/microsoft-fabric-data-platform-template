# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "33b0d599-61cf-4deb-9f6b-631f736c202d",
# META       "default_lakehouse_name": "lh_dp",
# META       "default_lakehouse_workspace_id": "f30de52c-da29-43c7-b29d-cb2bd7a178a6",
# META       "known_lakehouses": [
# META         {
# META           "id": "33b0d599-61cf-4deb-9f6b-631f736c202d"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from typing import Union, List

# Get or create SparkSession
spark = SparkSession.builder.getOrCreate()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

def read_trip_data(spark: SparkSession, years: Union[int, List[int]] = [2017,2018,2019,2020,2021,2022]) -> DataFrame:
    """
    Reads trip data for one or more years from a Microsoft Fabric Lakehouse table.

    Parameters:
    - spark: The active SparkSession.
    - years: An int or list of ints representing years (e.g., 2017 or [2017, 2018]).

    Returns:
    - A Spark DataFrame containing the union of trip data for the given year(s).
    """
    if isinstance(years, int):
        years = [years]

    valid_years = set(range(2017, 2023))
    for year in years:
        if year not in valid_years:
            raise ValueError(f"Year {year} is out of supported range: {sorted(valid_years)}")

    dfs = []
    for year in years:
        table_name = f"lh_dp.year_{year}.green_tripdata_{year}"
        df = spark.read.table(table_name)
        dfs.append(df)

    # Union all DataFrames
    result_df = dfs[0]
    for df in dfs[1:]:
        result_df = result_df.unionByName(df)

    return result_df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_df = read_trip_data(spark=spark)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

raw_df.distinct().write.mode('overwrite').saveAsTable(f'dbo.green_tripdata')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
