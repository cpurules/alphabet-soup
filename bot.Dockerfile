FROM python:3
COPY wait-for-it.sh /
WORKDIR /code
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt ; rm requirements.txt
COPY ./alphabet-soup .
ENTRYPOINT ["/wait-for-it.sh", "alphabet-soup-db:8529", "--", "python", "-u", "alphabet_soup.py"]
