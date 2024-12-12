# Use the official R base image
FROM r-base:latest

# Install required system libraries
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# Install necessary R packages
RUN R -e "install.packages(c('genetics', 'LDheatmap', 'BiocManager'), repos='https://cloud.r-project.org/')"
RUN R -e "BiocManager::install('SNPRelate')"

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy your R script into the container
COPY ./script.R .

# Command to run your script
CMD ["Rscript", "script.R"]
