FROM python:3.11

WORKDIR /usr/src/app

COPY . . 
RUN pip install -q -U google-generativeai

# Run the script
ENTRYPOINT ["python3", "GeminiApi.py"]
