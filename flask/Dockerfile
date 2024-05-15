FROM python:slim

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y make
RUN apt install -y libsm6 libxext6
RUN apt-get -y install tesseract-ocr && apt-get -y install tesseract-ocr-fra
RUN apt-get install -y libpq-dev build-essential
RUN apt-get install -y libgl1-mesa-glx



COPY . /flask
COPY tessdata/ /usr/share/tesseract-ocr/5/tessdata
WORKDIR /flask

RUN mkdir /uploads

RUN pip install -r requirements.txt
CMD ["python", "app.py"]