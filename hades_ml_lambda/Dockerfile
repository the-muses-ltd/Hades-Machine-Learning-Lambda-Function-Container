# Define global args
ARG FUNCTION_DIR="/home/app/"
# Python slim-buster is a lightweight version of python, perfect for keeping down image size
ARG RUNTIME_VERSION="3.7-slim-buster"

# Stage 1 - build a copy of the base image 
FROM python:${RUNTIME_VERSION} AS python

# Stage 2 - build function and dependencies
FROM python AS build-image
# Include global args in this stage of the build
ARG FUNCTION_DIR
ARG RUNTIME_VERSION
# Create function directory
RUN mkdir -p ${FUNCTION_DIR}
# Copy handler function
COPY app/* ${FUNCTION_DIR}
# Install the function's dependencies
RUN pip install tensorflow --target ${FUNCTION_DIR}
RUN pip install keras --target ${FUNCTION_DIR}
RUN pip install numpy --target ${FUNCTION_DIR}
RUN pip install awslambdaric --target ${FUNCTION_DIR}


# Stage 3 - final runtime image
# Grab a fresh copy of the Python image
FROM python
# Include global arg in this stage of the build
ARG FUNCTION_DIR
# Set working directory to function root directory
WORKDIR ${FUNCTION_DIR}
# Copy in the built dependencies
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}
# (Optional) Add Lambda Runtime Interface Emulator and use a script in the ENTRYPOINT for simpler local runs
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie
COPY entry.sh /
RUN chmod 755 /usr/bin/aws-lambda-rie /entry.sh
ENTRYPOINT [ "/entry.sh" ]
CMD [ "app.handler" ]