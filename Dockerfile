FROM debian:latest

# Update and install required packages
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg python3 python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Check Python and pip installation
RUN python3 --version
RUN pip3 --version

# Set the working directory
WORKDIR /app/

# Copy the contents of the current directory into the container
COPY . /app/

# Upgrade pip and install the required Python packages
RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

# Make the start.sh script executable
RUN chmod +x start.sh

# Run start.sh when the container launches
CMD ["bash", "start.sh"]
