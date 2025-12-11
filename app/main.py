"""
Simple REST API application for CI/CD demonstration.
"""

from flask import Flask, jsonify

app = Flask(__name__)


def calculate_sum(a: int, b: int) -> int:
    """Calculate sum of two numbers."""
    return a + b


def calculate_factorial(n: int) -> int:
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@app.route("/")
def home():
    """Home endpoint."""
    return jsonify(
        {
            "message": "Welcome to CI/CD Demo API",
            "version": "1.0.0",
            "endpoints": ["/", "/health", "/api/sum", "/api/factorial"],
        }
    )


@app.route("/health")
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


@app.route("/api/sum/<int:a>/<int:b>")
def sum_numbers(a: int, b: int):
    """Sum two numbers."""
    result = calculate_sum(a, b)
    return jsonify({"a": a, "b": b, "sum": result})


@app.route("/api/factorial/<int:n>")
def factorial(n: int):
    """Calculate factorial."""
    try:
        result = calculate_factorial(n)
        return jsonify({"n": n, "factorial": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
