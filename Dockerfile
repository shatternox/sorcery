FROM python
RUN apt-get update -y && apt-get install tesseract-ocr -y
COPY ./webnya/requirements.txt /requirements.txt
RUN pip install -r requirements.txt
CMD python /sorcery/app.py


