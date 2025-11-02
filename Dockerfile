#                                  Build Stage                                #

FROM cgr.dev/chainguard/python:latest-dev AS build

USER root

ENV VENV_PATH=/opt/pysetup/.venv \
    PYSETUP_PATH=/opt/pysetup

RUN apk add --no-cache --virtual .build-deps \
        glibc-dev \
        gcc \
    libffi-dev \
    && python -m venv "${VENV_PATH}" \
    && "${VENV_PATH}/bin/pip" install uv

WORKDIR "${PYSETUP_PATH}"

COPY pyproject.toml ./
RUN "${VENV_PATH}/bin/uv" sync --no-cache --no-dev \
    && apk del .build-deps

#                                 Runtime Stage                               #

FROM cgr.dev/chainguard/python:latest AS runtime

COPY --from=build \
     /opt/pysetup/.venv/lib/python3.13/site-packages/ \
     /usr/lib/python3.13/site-packages/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER nonroot
WORKDIR /app

COPY --chown=nonroot:nonroot ./src /app

EXPOSE 8000

#                               Production Stage                              #

FROM runtime AS prod

ENTRYPOINT ["python", "-m", "granian"]
CMD ["--interface", "wsgi", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--backpressure", "4", "--workers-lifetime", "3600", "sgi.wsgi:application"]

