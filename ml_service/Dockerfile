
FROM python:3.10-slim
WORKDIR /app
COPY ml_log_analyzer.py .
RUN pip install pandas scikit-learn
EXPOSE 5050
CMD ["python", "ml_log_analyzer.py"]
