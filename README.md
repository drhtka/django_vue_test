# django_vue_test

## Customize configuration

## Project Setup

```sh
docker-compose up --build -d
```

### Create settings your IP http://...:8000

```sh
settings.py
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://...:8000',
    'http://...:8080',
]
```

### Create settings your IP http://...:8000

```sh
        return {
            baseUrl: "http://...:8000",
            posts: [],
        };
```
