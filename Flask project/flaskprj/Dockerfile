FROM python
RUN groupadd -r groupflask && useradd -r -g groupflask userflask

RUN pip install --upgrade pip
RUN pip install flask psycopg2-binary
WORKDIR /app
COPY . .
EXPOSE 5000
USER userflask
VOLUME /app
ENTRYPOINT [ "python", "site.py" ]