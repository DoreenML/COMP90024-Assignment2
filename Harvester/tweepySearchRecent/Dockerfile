FROM python:3

WORKDIR /home/ubuntu/COMP90024/Harvester/tweepySearchRecent

COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt

CMD ["tweepySearchRecent.py"]

ENTRYPOINT ["python3"]