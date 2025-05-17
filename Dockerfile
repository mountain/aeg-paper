FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends texlive-full && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /work
COPY . /work
CMD ["./build.sh"]
