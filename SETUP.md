
# Development Environment 

There are a few different ways to set up your environment:

1. Using Docker Compose via command line
2. Running Rails directly via command line

Notes if using Docker (option 1): 

- You will need to have Docker already installed on your local machine. If you don't already have it installed, please use option 2 - it isn't necessary to learn a new tool (although it's very handy) for this exercise.

### Using Docker Compose via command line

To run the main application container (`app`) in the background use:

    docker-compose up -d 

Then, to start a bash session inside the running app container run:

    docker-compose exec app /bin/bash

Here you should have access to `python`, `pip`, and `pipenv`.

You can start multiple session inside the container using the same `docker-compose exec` command in multiple terminals. This may make it easier to run the Flask.

### Running Flask directly via command line

Ensure you have Python 3.9 installed. (Other versions may work, however this has only been tested on 3.9.4) and [pipenv](https://pipenv.pypa.io/en/latest/install/).

## Finishing Up

#### Flask 

Initialize a virtual Python 3 environment via `pipenv`:

    pipenv --three

Then run `bootstrap.sh`:

    ./bootstrap.sh

You should now be able to access the Flask app at `http://localhost:5000/`.

## Notes 

- This is meant to (hopefully) keep the amount of set up and configuration needed to start on the assignment to a minimum. Feel free to add any python packages, npm packages or other tools that will be helpful!
- We are always improving our projects, so please share any feedback or suggestions on your experience.
