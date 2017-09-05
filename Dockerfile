FROM ubuntu:16.04

# Installs
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y python3-pip && \
  apt-get install -y libssl-dev && \
  apt-get install -y libffi-dev && \
  apt-get install -y python3-dev && \
  apt-get install -y libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg libav-tools unixodbc-dev

# Importing the project
WORKDIR /app
ADD . /app

# Installing project requirements
RUN pip3 install -r requirements.txt

# Exposing port 3000 so that I can communicate
EXPOSE 3000

# Running the project
CMD ["python3", "pooh_main.py"]

