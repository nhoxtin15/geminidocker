FROM python:3.11

WORKDIR /usr/src/app

COPY . . 
RUN pip install -q -U google-generativeai

CMD ["AIzaSyAUYOLZuRdh_yYvNzBq0Q0BLsC8Ba9J_sE"]
# Run the script
ENTRYPOINT ["python3", "GeminiApi.py"]
