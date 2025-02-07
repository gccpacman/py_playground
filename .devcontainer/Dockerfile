FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Install dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        libxml2-dev \
        libxmlsec1-dev \
        libffi-dev \
        liblzma-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pyenv and poetry
USER vscode
ENV PYENV_ROOT="/home/vscode/.pyenv"
ENV PATH="${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:/home/vscode/.local/bin:$PATH"

RUN curl https://pyenv.run | bash \
    && pyenv install 3.11.11 \
    && pyenv global 3.11.11 \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

# Set the working directory
WORKDIR /workspace

# Install project dependencies
COPY pyproject.toml poetry.lock ./
RUN poetry install

# Copy the rest of the application code
COPY . .

# Set the entry point
CMD ["poetry", "run", "python", "helloworld.py"]