FROM python:3.7-alpine

WORKDIR /home/ubuntu/COMP90024/BackEnd
ENV FLASK_APP=BackEnd.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers


# Install dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]