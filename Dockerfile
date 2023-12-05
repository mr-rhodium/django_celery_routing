FROM python:3.11 AS builder
RUN pip install --upgrade pip setuptools wheel

# PDM
RUN pip install pdm

# pdm copy file  
WORKDIR /app
COPY pyproject.toml pdm.lock  /app/
RUN mkdir __pypackages__ && pdm sync --prod --no-editable

# run stage

FROM python:3.11 

ENV PYTHONPATH=/app/pkgs
COPY --from=builder /app/__pypackages__/3.11/lib /app/pkgs
COPY --from=builder /app/__pypackages__/3.11/bin/* /bin/
WORKDIR /app
COPY . /app/

EXPOSE 5000

CMD [ "python", "manage.py", "runserver" ]
