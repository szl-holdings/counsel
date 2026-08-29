# Ayllu Counsel — Hugging Face Space. Stdlib HTTP. No Gradio.
# Explicit COPY: the org deployer forbids bare COPY .
FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PORT=7860
COPY allodial.py ./allodial.py
COPY app.py ./app.py
COPY index.html ./index.html
EXPOSE 7860
CMD ["python", "-u", "app.py"]
