FROM python:2.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE lqconfig.settings_staging
ENV PIP_DOWNLOAD_CACHE /src/.pip_download_cache

RUN groupadd -r web && useradd -r -g web web

RUN mkdir /src && chown web:web /src

WORKDIR /src

VOLUME /src

COPY settings_staging.py /
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
