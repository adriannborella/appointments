# Config Proyect

## Starting

### deploy.sh
This script set some enviroment variables and execute the docker compose command to deploy the project

It has 2 parameters
* e = The enviroment name. Posible options [local - production - qa - ci]
* c = command which is going to be executed


## Config Debug

Configuration
```
"configurations": [
        {
            "name": "Python: Remote Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 10002
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/src/web/src",
                    "remoteRoot": "."
                }
            ],
            "justMyCode": true
        }
    ]
```

## How to deploy

