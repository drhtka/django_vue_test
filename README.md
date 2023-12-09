# django_vue_test

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

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
