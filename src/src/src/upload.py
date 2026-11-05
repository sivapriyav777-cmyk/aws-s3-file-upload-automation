import boto3
import time

from botocore.exceptions import ClientError, BotoCoreError
from src.validation import validate_file
from src.logging_config import setup_logging

logger = setup_logging()


def upload_file(file_path, bucket, object_name):

    try:
        validate_file(file_path)

        s3 = boto3.client("s3")

        try:
            s3.head_object(
                Bucket=bucket,
                Key=object_name
            )

            logger.warning("File already exists")
            return False

        except ClientError as error:

            code = error.response.get(
                "Error", {}
            ).get("Code")

            if code not in ["404", "NoSuchKey", "NotFound"]:
                raise

        for attempt in range(1, 4):

            try:
                logger.info(f"Upload attempt: {attempt}")

                s3.upload_file(
                    file_path,
                    bucket,
                    object_name
                )

                logger.info("Upload successful")
                return True

            except (ClientError, BotoCoreError):

                logger.exception("Upload failed")

                if attempt == 3:
                    raise

                time.sleep(2 ** (attempt - 1))

    except Exception:
        logger.exception("File processing failed")
        return False


if __name__ == "__main__":

    upload_file(
        "sample_data/sample.csv",
        "your-s3-bucket-name",
        "sample.csv"
    )
