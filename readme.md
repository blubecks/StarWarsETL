# Browse StarWars API

Just a simple use case of an ETL in python using StarWarsAPI

## Table of Contents

- [Installation and Usage](#installation)
- [Tests](#tests)


## Installation and Usage


1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/project-name.git
2. Build the docker image:
   ```bash
   docker build -t my-python-app .  
3. Run it!!:
   ```bash
   docker run  my-python-app  

## Tests
1. Build the docker image:
   ```bash
   docker build -t my-python-app .  
2. Run it!!:
   ```bash
   docker run -v $(pwd):/app my-python-app python -m pytest
  
