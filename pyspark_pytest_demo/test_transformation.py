from transformations import remove_duplicates, add_bonus


def test_remove_duplicates(spark):
    data = [
        (1, "Vinay", 50000),
        (1, "Vinay", 50000),
        (2, "Rahul", 40000),
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "salary"]
    )

    result = remove_duplicates(df)

    assert result.count() == 2


def test_add_bonus(spark):
    data = [
        (1, "Vinay", 50000),
        (2, "Rahul", 40000),
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "salary"]
    )

    result = add_bonus(df)

    vinay_bonus = (
        result
        .filter(result.id == 1)
        .select("bonus")
        .collect()[0][0]
    )

    assert vinay_bonus == 5000