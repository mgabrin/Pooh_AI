FROM ubuntu:16.10

# Installs
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y python3-pip && \
  apt-get install -y libssl-dev && \
  apt-get install -y libffi-dev && \
  apt-get install -y python3-dev python3.6-dev && \
  apt-get install -y libasound-dev portaudio19-dev && \
  apt-get install -y libportaudio2 libportaudiocpp0 && \
  apt-get install -y ffmpeg libav-tools unixodbc-dev python3.6 && \
  apt-get install -y mpg321 pulseaudio

# Importing the project
WORKDIR /app
ADD . /app

# Installing project requirements
RUN python3.6 -m pip install --upgrade pip setuptools wheel
RUN python3.6 -m pip install -r requirements.txt

# Exposing port 3000 so that I can communicate
EXPOSE 3000

# Running the project
CMD ["python3.6", "pooh_main.py"]

