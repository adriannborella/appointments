# Config Proyect

## Starting

go to devops folder

```
cd devops
```

Execute docker-compose up

```
docker-compose up
```

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

