import pytest
from src.validation import validate_file


def test_valid_file(tmp_path):

    file_path = tmp_path / "sample.csv"
    file_path.write_text("id,name\n1,John")

    assert validate_file(str(file_path)) is True


def test_missing_file():

    with pytest.raises(FileNotFoundError):
        validate_file("missing.csv")


def test_empty_file(tmp_path):

    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    with pytest.raises(ValueError):
        validate_file(str(file_path))


def test_invalid_extension(tmp_path):

    file_path = tmp_path / "sample.txt"
    file_path.write_text("sample")

    with pytest.raises(ValueError):
        validate_file(str(file_path))
