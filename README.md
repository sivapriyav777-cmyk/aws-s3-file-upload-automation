# AWS S3 File Upload Automation

## Project Overview

This project automates CSV file uploads to Amazon S3 using Python and Boto3.

The application validates files before uploading and includes duplicate detection, retry handling, exception handling and logging.

## Technologies Used

- Python
- AWS S3
- Boto3
- Pytest
- GitHub

## Key Features

- Automated CSV file uploads
- File existence validation
- Empty file validation
- File extension validation
- Duplicate object detection
- Retry mechanism
- Exception handling
- Application logging
- Unit testing

## Project Structure

```text
aws-s3-file-upload-automation/
├── src/
│   ├── __init__.py
│   ├── upload.py
│   ├── validation.py
│   └── logging_config.py
├── tests/
│   ├── test_upload.py
│   └── test_validation.py
├── sample_data/
│   └── sample.csv
├── config/
│   └── config.example.json
├── requirements.txt
└── README.md
```

## AWS Configuration

Configure AWS credentials securely using an AWS CLI profile or IAM role.

Create an S3 bucket and update the bucket name in the application.

## How to Run

Install the dependencies:

`pip install -r requirements.txt`

Run the application:

`python -m src.upload`

Run the tests:

`python -m pytest -v`

## Expected Outcome

A reusable Python automation solution that validates CSV files and uploads them to Amazon S3 while handling common errors.

## Future Enhancements

- CloudWatch monitoring
- AWS Lambda integration
- GitHub Actions CI/CD
- File checksum validation
- Improved retry and recovery mechanisms
