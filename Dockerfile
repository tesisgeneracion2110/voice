FROM ubuntu:18.04

#instalar musescore
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN yes | add-apt-repository ppa:mscore-ubuntu/mscore3-stable 
RUN apt update 
RUN apt install -y musescore3 
RUN ln -s /usr/bin/musescore3 /usr/bin/musescore

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install wget
RUN apt-get install -y cmake

#instalar python
RUN apt-get update
RUN apt install -y python3-pip
RUN pip3 install requests
RUN pip3 install music21
RUN pip3 install matplotlib
RUN pip3 install numpy
RUN pip3 install wget
RUN apt-get install -y nano
RUN apt install -y ffmpeg


RUN mkdir content

RUN cd content && git clone https://github.com/tesisgeneracion2110/voice.git
RUN cd content/voice && \
    pip3 install -r requirements.txt

#Install libespeak-NG
RUN cd /content/voice/synthesisSoftware/libespeak-NG/ && \
apt install -y make autoconf automake libtool pkg-config && \
apt install -y gcc && \
apt install -y libsonic-dev && \
apt install -y ruby-ronn && \
apt install -y ruby-kramdown && \
./autogen.sh && \
./configure --prefix=/usr && \
make

#Install espeak-ng
RUN ln -s /content/voice/synthesisSoftware/libespeak-NG/src/.libs/libespeak-ng.so /usr/lib/libespeak-ng.so && \
apt install -y libsamplerate-dev && \
apt install -y libsndfile1-dev && \
cd /content/voice/synthesisSoftware/Sinsy-NG-0.0.1 && \
mkdir -p build && \
cd build && \
cmake .. && \
make && \
ln -s /content/voice/synthesisSoftware/Sinsy-NG-0.0.1/build/libsinsy.so /lib/libsinsy.so && \
ln -s /content/voice/synthesisSoftware/libespeak-NG/src/.libs/libespeak-ng.so.1 /usr/lib/libespeak-ng.so.1 && \
cp -r /content/voice/synthesisSoftware/libespeak-NG/espeak-ng-data /usr/share/

