from pathlib import Path

from data_cleaning import clean_data
from mongodb_connection import (
    connect_database,
    insert_data
)
from logger import logger


# ---------------------------------------
# Project directories
# ---------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"


# Create output directory if required
OUTPUT_DIR.mkdir(exist_ok=True)


def generate_output_filename(file_name):
    """
    Convert source CSV filename into
    a cleaned output filename.
    """

    output_name = (
        file_name
        .lower()
        .replace(".csv", "")
        .replace("$", "")
        .replace(" ", "_")
        .replace("-", "_")
    )

    return f"{output_name}_cleaned.csv"


def generate_collection_name(file_name):
    """
    Convert source filename into a
    MongoDB collection name.
    """

    collection_name = (
        file_name
        .lower()
        .replace(".csv", "")
        .replace("$", "")
        .replace(" ", "_")
        .replace("-", "_")
    )

    return collection_name


def main():

    logger.info("=" * 60)
    logger.info("ETL PIPELINE STARTED")

    # ---------------------------------------
    # Check input directory
    # ---------------------------------------

    if not DATA_DIR.exists():

        logger.error(
            "Data directory does not exist"
        )

        return

    # ---------------------------------------
    # Find CSV files
    # ---------------------------------------

    csv_files = sorted(
        DATA_DIR.glob("*.csv")
    )

    if not csv_files:

        logger.warning(
            "No CSV files found in data directory"
        )

        return

    logger.info(
        f"Found {len(csv_files)} CSV file(s)"
    )

    # ---------------------------------------
    # Connect MongoDB
    # ---------------------------------------

    client = None

    try:

        client, database = connect_database()

        # ---------------------------------------
        # Process each CSV
        # ---------------------------------------

        total_records = 0

        for csv_file in csv_files:

            logger.info(
                f"Processing file: {csv_file.name}"
            )

            try:

                # Data cleaning and validation
                cleaned_df = clean_data(csv_file)

                # ---------------------------------------
                # Generate output CSV
                # ---------------------------------------

                output_file_name = (
                    generate_output_filename(
                        csv_file.name
                    )
                )

                output_file = (
                    OUTPUT_DIR / output_file_name
                )

                cleaned_df.to_csv(
                    output_file,
                    index=False,
                    encoding="utf-8"
                )

                logger.info(
                    f"Output file generated: "
                    f"{output_file.name}"
                )

                # ---------------------------------------
                # MongoDB collection
                # ---------------------------------------

                collection_name = (
                    generate_collection_name(
                        csv_file.name
                    )
                )

                # ---------------------------------------
                # Insert into MongoDB
                # ---------------------------------------

                inserted_count = insert_data(
                    database,
                    collection_name,
                    cleaned_df
                )

                total_records += inserted_count

                # ---------------------------------------
                # Final file status
                # ---------------------------------------

                if output_file.exists():

                    logger.info(
                        f"Output verification successful: "
                        f"{output_file.name}"
                    )

                logger.info(
                    f"Successfully completed: "
                    f"{csv_file.name}"
                )

            except Exception as error:

                logger.exception(
                    f"Processing failed for "
                    f"{csv_file.name}: {error}"
                )

                # Continue with next CSV file
                continue

        logger.info(
            f"Total records synchronized: "
            f"{total_records}"
        )

        logger.info(
            "ETL PIPELINE COMPLETED"
        )

    except Exception as error:

        logger.exception(
            f"Pipeline execution failed: {error}"
        )

    finally:

        if client:

            client.close()

            logger.info(
                "MongoDB connection closed"
            )

        logger.info("=" * 60)


if __name__ == "__main__":
    main()