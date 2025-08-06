## Данное приложение выполнено в рамках тестового задания.

Для запуска приложения необходимо собрать и запустить Docker образ.
```shell
docker build -t automiq . 
docker run -p 8000:8000 automiq
```

Собранный docker-контейнер будет доступен по адресу http://127.0.0.1:8000/api/ или http://localhost:8000/api/

Так же в репозитории реализованы Actions, на linter и test

## Для запуска без использования Docker необходимо выполнить следующие команды:

1. Клонируем репозиторий:

```shell
git clone https://github.com/DenisSedovEd/automiq_tt.git 
```

2. Переходим в папку репозитория и устанавливаем окружение проекта:

```shell
cd automiq_tt
uv sync
```

3. Далее активируем окружение и запускаем проект на сервере uvicorn:

```shell
.venv\Scripts\activate
uvicorn main:app --port 8080
```

Приложение будет доступно по адресу http://127.0.0.1:8080/api/ или http://localhost:8080/api/
