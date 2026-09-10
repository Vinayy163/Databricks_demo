from pyspark.sql import DataFrame


def remove_duplicates(df: DataFrame) -> DataFrame:
    return df.dropDuplicates(["id"])


def add_bonus(df: DataFrame) -> DataFrame:
    return df.withColumn("bonus", df.salary * 0.10)