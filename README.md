# Doc Search Service

Сервис для поиска документов по тексту.

Данные хранятся в PostgreSQL, поисковый индекс — в Elasticsearch.  
Сервис умеет:

- загружать документы из CSV;
- искать документы по тексту;
- возвращать первые 20 результатов;
- удалять документ из PostgreSQL и Elasticsearch по `id`.

## Стек

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Elasticsearch
- Docker

## Запуск

### 1. Установить зависимости

```bash
pip install -r requirements.txt
```

### 2. Создать `.env`

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/doc_search_service
```

### 3. Запустить Elasticsearch

```bash
docker compose up -d
```

### 4. Применить миграции

```bash
alembic upgrade head
```

### 5. Загрузить данные из CSV

```bash
python -m app.loader
```

### 6. Запуск через Docker

```bash
docker compose up -d postgres elasticsearch backend
docker compose exec backend alembic upgrade head
docker compose run --rm loader
```

Swagger будет доступен по адресу:

```text
http://127.0.0.1:8000/docs
```

## API

### Поиск документов

```http
GET /search?query=текст
```

Возвращает до 20 документов, найденных по тексту.

### Удаление документа

```http
DELETE /documents/{document_id}
```

Удаляет документ из PostgreSQL и Elasticsearch.

## OpenAPI

OpenAPI-документация доступна по адресу:

```text
http://127.0.0.1:8000/openapi.json
```