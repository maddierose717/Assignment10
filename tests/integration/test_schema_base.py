# tests/integration/test_schema_base.py

import pytest
from pydantic import ValidationError
from app.schemas.base import UserCreate


def test_user_create_valid():
    """Test UserCreate with valid data."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "SecurePass123",
    }
    user_create = UserCreate(**data)
    assert user_create.username == "johndoe"
    assert user_create.password == "SecurePass123"
    assert user_create.first_name == "John"
    assert user_create.last_name == "Doe"
    assert user_create.email == "john.doe@example.com"


def test_user_create_invalid_email():
    """Test UserCreate with invalid email."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "invalid-email",
        "username": "johndoe",
        "password": "SecurePass123",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)


def test_user_create_short_password():
    """Test UserCreate with password shorter than 6 characters."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "short",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)


def test_user_create_short_username():
    """Test UserCreate with username shorter than 3 characters."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "jd",
        "password": "SecurePass123",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)


def test_user_create_invalid_username_special_chars():
    """Test UserCreate with invalid username containing special characters."""
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "john@doe!",
        "password": "SecurePass123",
    }
    with pytest.raises(ValidationError, match="Username must be alphanumeric"):
        UserCreate(**data)


def test_user_create_missing_required_field():
    """Test UserCreate with missing required field."""
    data = {
        "first_name": "John",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "SecurePass123",
    }
    with pytest.raises(ValidationError):
        UserCreate(**data)
