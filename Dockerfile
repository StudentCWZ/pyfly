FROM python:3.8.15-slim

LABEL name="elasticsearch_log_parse"
LABEL version="1.3.1.beta"
LABEL description="Elasticsearch Log Parse"

# System deps:
ENV TZ=Asia/Shanghai \
    PIPURL="https://pypi.tuna.tsinghua.edu.cn/simple" \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TF_CPP_MIN_LOG_LEVEL=3 \
    FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_ENV=production \
    FLASK_DEBUG=false \
    FLASK_RUN_PORT=5500 \
    CONSUL_HOST=172.28.5.39 \
    CONSUL_PORT=8500 \
    CONSUL_TOKEN="092288b5-824f-854c-39aa-a958afd9a633" \
    CONSUL_DC=dc1 \
    CONSUL_KEY=elasticsearch-log-parse/conf \
    CONSUL_REGISTER_HOST=172.28.12.88 \
    CONSUL_REGISTER_PORT=5500 \
    SERVICE=elasticsearch-log-parse \
    PGSQL_TABLENAME=elasticsearch_parse_log

# Install poetry separated from system interpreter
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && \
    python3 -m venv $POETRY_VENV && \
    $POETRY_VENV/bin/pip3 install -U pip setuptools && \
    $POETRY_VENV/bin/pip3 install poetry

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Workspace
WORKDIR /usr/src/pyfly

# Copy poetry settings
COPY pyproject.toml poetry.lock* /usr/src/pyfly/

# Poetry add packages
RUN poetry install --no-root
RUN poetry lock --no-update

# Copy folder them in docker layer
COPY . /usr/src/pyfly/

# Project initialization:
RUN chmod +x docker-entrypoint.sh

# Run the application:
CMD ["./docker-entrypoint.sh"]
