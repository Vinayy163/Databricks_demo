import pytest
from pyspark.sql import SparkSession
import os
import sys


@pytest.fixture(scope="session")
def spark():
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("PySparkTests")
        .getOrCreate()
    )

    yield spark

    spark.stop()