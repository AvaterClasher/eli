import pytest

from eli.exceptions.auth import CredentialsError


def test_credentials_error():
    with pytest.raises(CredentialsError):
        raise CredentialsError("Invalid credentials.")
