# ContentsService

[![.github/workflows/pipeline.yml](https://github.com/CyberpunkTeam/ContentsService/actions/workflows/pipeline.yml/badge.svg?branch=master)](https://github.com/CyberpunkTeam/ContentsService/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/CyberpunkTeam/ContentsService/branch/main/graph/badge.svg?token=HbfzsPmeCj)](https://codecov.io/gh/CyberpunkTeam/ContentsService)


## Setup

1. ```Install python ^3.9```
2. ```Install peotry => pip install poetry```
3.  ```poetry install``` (if you use pycharm, skip this step)
4. Complete env vars in makefile or set in local env(if not use docker):
- ```DATABASE_NAME```
- ```DATABASE_USER```
- ```DATABASE_PASSWORD```

### Pycharm:
1. Add poetry plugin
2. Add interpreter using poetry plugin


## Run API

### Using docker

1. ```make build```
2. ```make start```

### Using local host
1. ```uvicorn app.main:app```

## Run test

### Using docker

1. ```make test```

### Using local host
2. ```python3 -m pytest ./tests &&  python3 -m behave```
