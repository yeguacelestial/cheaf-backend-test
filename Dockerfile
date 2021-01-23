# Configure and activate conda environment
FROM continuumio/miniconda3

# Create and set working directory
RUN mkdir /app
WORKDIR /app

# Add current directory code to working directory
ADD . /app/

# Create and init conda environment
ADD environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
ENV PATH /opt/conda/envs/cheaf-backend-test/bin:$PATH

# Set project env variables
ENV PORT=8888

EXPOSE 8888
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT