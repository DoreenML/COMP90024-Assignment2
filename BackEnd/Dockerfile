FROM python:3

WORKDIR /home/ubuntu/COMP90024/BackEnd

COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["BackEnd.py"]

ENTRYPOINT ["python3"]