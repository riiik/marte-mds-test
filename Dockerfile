# syntax=docker/dockerfile:1
FROM avstephen/marte2-demos-sigtools-centos7:v1.0.4
RUN yum -y install xterm
RUN yum -y install sudo
# added to allow MDSplus TDI to use python functions:
RUN yum -y install python-devel
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN pip install numpy==1.16

RUN useradd -ms /bin/bash xtermuser
RUN echo 'Docker!' | passwd --stdin root
RUN echo 'Docker!' | passwd --stdin xtermuser
RUN usermod -aG wheel xtermuser
USER xtermuser
WORKDIR /home/xtermuser

RUN mkdir projects

CMD /bin/bash


## invocation (where the last 'docker' is the name of the directory containing the Dockerfile):

# docker build -t x1 docker
# docker run --rm -it -e DISPLAY=${DISPLAY} -v /tmp/.X11-unix:/tmp/.X11-unix -v ~/.ssh:/home/xtermuser/.ssh/:ro -v ~/.ssh:/root/.ssh/:ro --network host --name x1.1 x1
# docker exec -it -user root x1 bash

