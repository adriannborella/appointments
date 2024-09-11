
ARG APP_IMAGE_FROM

FROM $APP_IMAGE_FROM

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/appointments \
    && mkdir /opt/appointments/web \
    && mkdir /opt/appointments/static \
    && mkdir /opt/appointments/media \
    && mkdir /opt/appointments/import_files \
    && mkdir /opt/appointments/logs \
    && mkdir /cache

WORKDIR /opt/appointments/web

ARG APP_REQUIREMENT_FILE

COPY requirements/base.txt requirements/$APP_REQUIREMENT_FILE entrypoint.sh /cache/

RUN pip install -U pip \
    && pip install -r /cache/$APP_REQUIREMENT_FILE

ADD appointments /opt/appointments/web

RUN chmod +x /cache/entrypoint.sh