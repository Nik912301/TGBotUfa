install:
    pip install poetry && \
    poetry install

start:
    poetry run python TgBotProject/main.py