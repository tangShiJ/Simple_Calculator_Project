# Dockerfile for running tests in a CI container (Python 3.11)
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /workspace

# Copy only metadata first to leverage layer caching
COPY pyproject.toml README.md requirements.txt /workspace/
COPY simple_calculator /workspace/simple_calculator
COPY tests /workspace/tests

# Install build tools (required if any dependency needs compilation)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Ensure pip is up-to-date and install dependencies and the package
RUN python -m pip install --upgrade pip
RUN if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi
RUN python -m pip install -e .

# Default command runs tests and writes JUnit XML
CMD ["pytest", "-q", "--junitxml=results.xml"]

