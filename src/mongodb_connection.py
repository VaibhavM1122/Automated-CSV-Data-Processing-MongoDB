import os

from dotenv import load_dotenv
from pymongo import MongoClient
from logger import logger


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")


def connect_database():

    try:
        client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000
        )

        # Test MongoDB connection
        client.admin.command("ping")

        logger.info("MongoDB connection successful")

        database = client[DATABASE_NAME]

        return client, database

    except Exception as error:

        logger.error(
            f"MongoDB connection failed: {error}"
        )

        raise


def insert_data(database, collection_name, dataframe):

    try:

        collection = database[collection_name]

        records = dataframe.to_dict(
            orient="records"
        )

        if not records:
            logger.warning(
                f"No records found for {collection_name}"
            )
            return 0

        # Insert records into MongoDB
        result = collection.insert_many(
            records
        )

        count = len(result.inserted_ids)

        logger.info(
            f"{count} record(s) inserted into "
            f"MongoDB collection '{collection_name}'"
        )

        return count

    except Exception as error:

        logger.error(
            f"MongoDB insert failed for "
            f"'{collection_name}': {error}"
        )

        raise