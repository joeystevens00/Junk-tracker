FROM python:3.9.4

RUN mkdir /workspace

COPY ./Pipfile ./Pipfile.lock /workspace

RUN pip install pipenv && \
    cd /workspace/ && \
    pipenv install --system --deploy