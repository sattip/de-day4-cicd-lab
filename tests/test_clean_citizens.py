"""Unit tests for clean_citizen_data."""
import pytest
from pyspark.sql import SparkSession
from notebooks.clean_citizens import clean_citizen_data


@pytest.fixture(scope="module")
def spark():
    return (
        SparkSession.builder
        .master("local[1]")
        .appName("clean-citizens-test")
        .getOrCreate()
    )


def test_dedupe_and_filter(spark):
    data = [
        (1, "a@x.gr"),
        (1, "a@x.gr"),  # duplicate
        (2, None),       # null email
        (3, "no-at"),    # invalid email
        (4, "ok@y.gr"),  # valid
    ]
    df = spark.createDataFrame(data, ["id", "email"])
    out = clean_citizen_data(df).collect()
    ids = sorted(r["id"] for r in out)
    assert ids == [1, 4]
