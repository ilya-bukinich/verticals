## Pеализация:
Задачи в точности выполнить задание не преследовал, делаю, чтобы разобраться как это всё работает

Технологии: Python3, Django, DRF, SQLite/PostgreSQL. Сделан простой фронтенд на Bootsrap

## Создать JSON API для сайта объявлений
Необходимо создать сервис для хранения и подачи объявлений. Объявления должны храниться в базе данных. Сервис должен предоставлять API, работающее поверх HTTP в формате JSON.

### Требования
- язык, технологии: Go/Python/PHP/Java/JavaScript, PostgreSQL/MySQL, любой фреймворк (или без него)
- код должен быть выложен на github
- 3 метода: получение списка объявлений, получение одного объявления, создание объявления
- валидация полей (~~не больше 3 ссылок на фото~~ **+загрузка фото**, описание не больше 1000 символов, название не больше 200 символов)

### Метод получения списка объявлений
- нужна пагинация, на одной странице должно присутствовать 10 объявлений ✔
- нужна возможность сортировки: по цене (возрастание/убывание) и по дате создания (возрастание/убывание)✔
- поля в ответе: **+id**, название объявления, ссылка на главное фото (первое в списке), цена✔

### Метод получения конкретного объявления
- обязательные поля в ответе: **+все**, т.к. все формы сделаны на дженериках ~~название объявления, цена, ссылка на главное фото~~✔
- ~~опциональные поля (можно запросить, передав параметр fields): описание, ссылки на все фото~~

### Метод создания объявления:
- принимает все поля: **+фото** ~~название, описание, несколько ссылок на фотографии (сами фото загружать никуда не требуется)~~✔
- возвращает ID созданного объявления и код результата (ошибка или успех)✔

### Усложнения
Не обязательно, но задание может быть выполнено с любым числом усложнений:
- написаны юнит тесты 🚧
- контейнеризация – возможность поднять проект с помощью `docker-compose up` 🚧
- кеширование – для увеличения скорости ответа от сервера, может быть добавлено кеширование (Redis/Memcached) 🚧

## Документация по API

### API Root
`curl -i -X GET 'http://127.0.0.1:8000/api/?format=json'`

### Получить список объявлений
`curl -i -X GET 'http://127.0.0.1:8000/api/adverts/?format=json'`

**Фильтры:**
- `?ordering=price` - по возрастанию цены
- `?ordering=-price` - по убывынию цены
- `?ordering=create_datetime` - по дате от новых к старым
- `?ordering=-create_datetime` - по дате от старых к новым

**Пагинация:**
- 2-я страница `?limit=10&offset=10`
- 3-я страница `?limit=10&offset=20`
- 4-я страница `?limit=10&offset=30`

**Пример запроса:**
`curl -i -X GET 'http://127.0.0.1:8000/api/adverts/?offset=20&ordering=price?format=json'` - 3-я страница, сортировка по возрастанию цены

### Получить объявление
**Пример запроса:**

`curl -i -X GET 'http://127.0.0.1:8000/api/advert/1/?format=json'`

### Создать объявление

Требуется Basic авторизация

**Пример запроса:**

```
curl -i -X POST \
 -H 'Accept: application/json' \
 -H 'Content-Type: multipart/form-data' \
 -F "title=Продам гараж" \
 -F "price=1000" \
 -F "author=Василий" \
 -F "summary=Продам гараж. Хорошая транспортная доступность. Гараж сухой и светлый." \
 -F "image=@/path/to/your_photo.jpg;type=image/jpg" \
 -F "category=1" \
'http://test:QqnSnm9h6CxPSAP@127.0.0.1:8000/api/advert/create/?format=json'
```

**Пример ответа:**
```
HTTP/1.1 201 Created
Date: Sun, 22 Mar 2020 11:07:35 GMT
Content-Type: application/json
Vary: Accept
Allow: POST, OPTIONS
```

```
{
  "id": 84,
  "title": "Продам гараж",
  "create_datetime": "2020-03-22T14:07:35.921405",
  "price": "1000.00",
  "author": "Василий",
  "summary": "Продам гараж. Хорошая транспортная доступность. Гараж сухой и светлый.",
  "image": "http://127.0.0.1:8000/media/442d4ea1-cf00-40e8-ac6b-711d09567e8b.jpg",
  "category": 1
}
```
