FROM python:3

WORKDIR /home/ubuntu/COMP90024/Harvester/tweepySearchCovid

COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt

CMD ["tweepySearchCovid.py"]

ENTRYPOINT ["python3"]