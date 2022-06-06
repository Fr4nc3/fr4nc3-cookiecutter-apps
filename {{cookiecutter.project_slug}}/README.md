# {{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}

## TODO after cloning this

```bash

# Initialize the virtual environment
$ pipenv --python {{ cookiecutter.python_version }}

# Import the requirements
$ pipenv install -r requirements.txt


# Make sure the repository stays that nice
$ pre-commit install

```

## Installation

```bash
$ pipenv install .
```

## Run Local

```bash
$ pipenv shell

# run python local
# TODO
```

## DEPLOY AWS SERVERLESS

- use the azuredevops [Azure DevOps](pipeline/azure_pipeline.yml)
