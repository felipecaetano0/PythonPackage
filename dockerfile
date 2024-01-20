FROM python:3.11

ADD ./dist/math-0.0.1-py3-none-any.whl ./math-0.0.1-py3-none-any.whl 

RUN pip3 install math-0.0.1-py3-none-any.whl 

CMD ["math", "8*8"]
