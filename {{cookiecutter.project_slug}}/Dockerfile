FROM python:3.6
ENV TZ UTC
ADD ./requirements.txt /opt/code/requirements.txt
WORKDIR /opt/code
RUN mkdir -p /opt/logs && \
   mkdir -p /opt/media && \
  apt-get update && apt-get install --no-install-recommends -y \
  gcc \
  build-essential &&\
  pip install --no-cache-dir -r requirements.txt && \
  apt-get purge -y \
  gcc \
  build-essential && \
  apt-get clean autoclean && \
  apt-get autoremove -y && \
  rm -rf /var/lib/{apt,dpkg,cache,log}/
EXPOSE 8080
ENV FLASK_APP {{ cookiecutter.package_name }}/wsgi.py
ENV FLASK_CONFIG Dev
ENV FLASK_DEBUG 1
ADD . /opt/code/
RUN python /opt/code/setup.py develop
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
