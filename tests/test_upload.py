from unittest.mock import patch
from botocore.exceptions import ClientError

from src.upload import upload_file


@patch("src.upload.boto3.client")
def test_successful_upload(mock_boto, tmp_path):

    file_path = tmp_path / "sample.csv"
    file_path.write_text("id,name\n1,John")

    mock_s3 = mock_boto.return_value

    mock_s3.head_object.side_effect = ClientError(
        {"Error": {"Code": "404"}},
        "HeadObject"
    )

    result = upload_file(
        str(file_path),
        "test-bucket",
        "sample.csv"
    )

    assert result is True

    mock_s3.upload_file.assert_called_once()
