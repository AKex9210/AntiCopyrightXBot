FROM debian:latest 
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
RUN chmod +x start.sh
CMD ["bash", "start.sh"]
