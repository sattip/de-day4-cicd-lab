"""Citizen data cleanup pipeline — Day 4 Lab demo."""
from pyspark.sql.functions import col


def clean_citizen_data(df):
    """Deduplicate and filter citizen records.

    Keeps records with a non-null id and a valid email (contains @).
    """
    return (
        df.dropDuplicates()
        .filter(col("id").isNotNull())
        .filter(col("email").rlike("@"))
    )
