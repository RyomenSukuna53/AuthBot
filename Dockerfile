FROM python:3.10

WORKDIR /root/AuthBot

COPY . .

RUN pip3 install -U -r requirements.txt

CMD ["python", "-m", "bot.py"]
