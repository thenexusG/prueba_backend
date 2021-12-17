FROM alphine:3.15.0

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
    