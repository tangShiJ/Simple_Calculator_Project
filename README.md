# Simple_Calculator_Project

A minimal calculator package used to demonstrate pytest-driven tests and a simple CI flow.

## Install for development (editable)

Create and activate a virtual environment, then install the project in editable mode so tests can import `simple_calculator`:

```powershell
cd /d D:\python3\Simple_Calculator_Project
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Run tests

Run pytest from the project root (this will discover tests under `tests/`):

```powershell
python -m pytest -q
```

For CI (Jenkins) inside Docker, ensure the agent image includes Python and pip, install dependencies and the package before running pytest. You can either:

- mount the repo into the container and run the same editable install commands inside the container; or
- build a Docker image that copies the repo and installs it during image build.

Example Dockerfile snippet:

```dockerfile
FROM mcr.microsoft.com/windows/servercore:latest
# or a linux python base image if your agents are linux-based
WORKDIR /workspace
COPY . /workspace
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m pip install -e .
CMD ["python", "-m", "pytest", "-q"]
```

Notes
- The project is installed in editable mode for local development so tests can import the package without modifying `sys.path`.
- The tests include some skipped/xfail examples for demonstration; adjust as needed for a strict green CI.
