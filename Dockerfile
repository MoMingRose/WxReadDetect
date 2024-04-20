FROM miigotu/python3.10-slim
LABEL authors="MoMingLog"

COPY . /root/WxReadDetect

WORKDIR /root/WxReadDetect

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]