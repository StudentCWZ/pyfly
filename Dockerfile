FROM python:3.11-slim

LABEL name="pyfly"
LABEL version="0.1.0"
LABEL description="BBS"

# System deps:
ENV TZ=Asia/Shanghai \
    TF_CPP_MIN_LOG_LEVEL=3

# Python deps:
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

# Poetry deps:
ENV POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

# Flask deps:
ENV FLASK_DEBUG=0

# Install poetry separated from system interpreter
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    python3 -m venv $POETRY_VENV && \
    $POETRY_VENV/bin/pip3 install -U pip setuptools poetry -i https://mirrors.aliyun.com/pypi/simple/

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Workspace
WORKDIR /usr/src/pyfly

# Copy poetry settings
COPY pyproject.toml poetry.lock* /usr/src/pyfly/

# Copy folder them in docker layer
COPY . /usr/src/pyfly/

# Poetry add packages
RUN poetry install --no-root && \
    poetry lock --no-update && chmod +x docker-entrypoint.sh

# Run the application:
CMD ["./docker-entrypoint.sh"]

