FROM python:3

WORKDIR /home/ubuntu/COMP90024/CouchDB

COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt

CMD ["dataUpload.py"]

ENTRYPOINT ["python3"]