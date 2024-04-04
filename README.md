# Minsk World Property

Сайт по продаже недвижимости с разделами описания ЖК, застройщика, инфраструктуры и детальным
представлением объектов недвижимости

## ENVs:
```
SITE_HOST=localhost
SECRET_KEY=my_secret_key
DEBUG=True
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
TLS_MODE=off
HTPASSWD_NODE=off
HTPASSWD=off
```

## Third party packages:
```
rest_framework
drf_spectacular
django_filters
solo
ckeditor
adminsortable2
colorful
```

### Локальный запуск проекта 
```shell
docker compose build
docker compose up
```

| Доступ  | Ссылка                        |
|---------|-------------------------------|
| Админка | http://0.0.0.0:8000/admin/    |
| Сваггер | http://0.0.0.0:8000/api/docs/ |


