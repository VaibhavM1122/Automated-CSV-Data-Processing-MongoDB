import pandas as pd
from logger import logger


def clean_data(file_path):

    logger.info(f"Reading file: {file_path.name}")

    try:
        df = pd.read_csv(file_path)
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="ISO-8859-1")

    logger.info(
        f"{file_path.name}: {len(df)} rows, "
        f"{len(df.columns)} columns loaded"
    )

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("$", "", regex=False)
    )

    logger.info(
        f"{file_path.name}: column names standardized"
    )

    # Remove completely empty rows
    df.dropna(how="all", inplace=True)

    # Remove duplicate records
    duplicates = df.duplicated().sum()

    if duplicates > 0:
        df.drop_duplicates(inplace=True)

        logger.info(
            f"{file_path.name}: removed "
            f"{duplicates} duplicate record(s)"
        )

    # Check missing values
    missing = df.isnull().sum()

    for column, count in missing.items():

        if count > 0:
            logger.warning(
                f"{file_path.name}: {count} missing "
                f"value(s) in '{column}'"
            )

    # Dataset-specific validation
    if "contractvalue" in df.columns:

        df["contractvalue"] = pd.to_numeric(
            df["contractvalue"],
            errors="coerce"
        )

        invalid = (
            df["contractvalue"].isna().sum()
        )

        if invalid > 0:
            logger.warning(
                f"{file_path.name}: {invalid} "
                f"invalid contract value(s)"
            )

    if "employee_count" in df.columns:

        df["employee_count"] = pd.to_numeric(
            df["employee_count"],
            errors="coerce"
        )

    if "num_of_users" in df.columns:

        df["num_of_users"] = pd.to_numeric(
            df["num_of_users"],
            errors="coerce"
        )

    logger.info(
        f"{file_path.name}: data validation completed"
    )

    return df