FROM python:3

ENV USER mpitest
ENV HOME /home/$USER
ENV MPI_DIR=/opt/ompi
ENV PATH="$MPI_DIR/bin:$HOME/.local/bin:$PATH"
ENV LD_LIBRARY_PATH="$MPI_DIR/lib:$LD_LIBRARY_PATH"
WORKDIR /home/ubuntu/COMP90024/Harvester/tweepySearchCovid

# copy local repo to docker
COPY . .

# Install dependencies
RUN pip3 install -r requirements.txt

ADD https://download.open-mpi.org/release/open-mpi/v3.1/openmpi-3.1.4.tar.bz2 .
RUN tar xf openmpi-3.1.4.tar.bz2 \
    && cd openmpi-3.1.4 \
    && ./configure --prefix=$MPI_DIR \
    && make -j4 all \
    && make install \
    && cd .. && rm -rf \
    openmpi-3.1.4 openmpi-3.1.4.tar.bz2 /tmp/*

RUN groupadd -r mpitest \
    && useradd -r -g mpitest $USER \
    && chown -R mpitest:mpitest $HOME

USER $USER
RUN pip3 install --user -U setuptools \
    && pip3 install --user mpi4py

# crawl tweet ID from github
CMD ["mkdir covidTweetID"]
CMD ["crawlTweetID.py"]
# filter twitter if it from australia
CMD ["mpiexec -np 4 python crawlTweetMultiProcess.py"]

ENTRYPOINT ["python3"]