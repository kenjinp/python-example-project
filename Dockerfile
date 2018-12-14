FROM python:2.7-slim
RUN pip install pipenv
ADD . /app
WORKDIR /app
RUN pipenv install --deploy --dev
ENV SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD ["python"]