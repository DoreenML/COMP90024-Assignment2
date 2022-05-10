FROM python:3

WORKDIR /home/ubuntu/COMP90024/Harvester/tweepySearchStreaming

COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt

CMD ["tweepyStreamingTest.py"]

ENTRYPOINT ["python3"]