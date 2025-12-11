"""
Unit tests for the application.
"""

import pytest

from app.main import app, calculate_factorial, calculate_sum


class TestCalculations:
    """Test calculation functions."""

    def test_calculate_sum_positive(self):
        """Test sum of positive numbers."""
        assert calculate_sum(2, 3) == 5

    def test_calculate_sum_negative(self):
        """Test sum with negative numbers."""
        assert calculate_sum(-2, 3) == 1

    def test_calculate_sum_zeros(self):
        """Test sum of zeros."""
        assert calculate_sum(0, 0) == 0

    def test_factorial_zero(self):
        """Test factorial of zero."""
        assert calculate_factorial(0) == 1

    def test_factorial_one(self):
        """Test factorial of one."""
        assert calculate_factorial(1) == 1

    def test_factorial_five(self):
        """Test factorial of five."""
        assert calculate_factorial(5) == 120

    def test_factorial_negative_raises(self):
        """Test factorial of negative number raises error."""
        with pytest.raises(ValueError):
            calculate_factorial(-1)


class TestAPI:
    """Test API endpoints."""

    @pytest.fixture
    def client(self):
        """Create test client."""
        app.config["TESTING"] = True
        with app.test_client() as client:
            yield client

    def test_home_endpoint(self, client):
        """Test home endpoint returns correct response."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.get_json()
        assert "message" in data
        assert data["version"] == "1.0.0"

    def test_health_endpoint(self, client):
        """Test health endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"

    def test_sum_endpoint(self, client):
        """Test sum endpoint."""
        response = client.get("/api/sum/5/3")
        assert response.status_code == 200
        data = response.get_json()
        assert data["sum"] == 8

    def test_factorial_endpoint(self, client):
        """Test factorial endpoint."""
        response = client.get("/api/factorial/5")
        assert response.status_code == 200
        data = response.get_json()
        assert data["factorial"] == 120

    def test_factorial_large_number(self, client):
        """Test factorial endpoint with larger number."""
        response = client.get("/api/factorial/10")
        assert response.status_code == 200
        data = response.get_json()
        assert data["factorial"] == 3628800
