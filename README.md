## JBTest Backend для работы с мобильным приложением

Проект написан на python 3.8.7.
Используются Django, PostgreSQL, docker/docker-compose.

### Инструкция к запуску:
В файле .env.dev, лежащем в корне проекта, необходимо в переменную DJANGO_ALLOWED_HOSTS вписать **ip**-адрес вашей виртуальной машины.
#### Затем необходимо в корневой директории проекта выполнить следующие команды:

```sh 
#Создание контейнеров на виртуальной машине:
docker-compose up -d —build

#Миграция моделей в базу данных:
docker-compose exec web python ./JBtest/manage.py migrate

#Создание логин/пароля для входа в админ панель:
docker-compose exec web python ./JBtest/manage.py createsuperuser

#Включение контейнеров и запуск сервера
docker-compose up
 ```

- Сервер запущен. Теперь можно открыть https://*:8000/admin, где * - ip-адрес виртуальной машины, для входа в админ панель.

## Примеры запросов к серверу:

**GET**  http://localhost:8000/api/posts/ - возвращает response со всеми элементами базы данных и статус кодом 200.

**POST** http://localhost:8000/api/posts/ - добавление элемента в базу данных сервера и скачивание изображения по
указанному URL на сервер, возвращает response с данными и статус код 201.

- Если данные проходят валидацию - возвращает response вместе с указанием некорректных данных и статус кодом **201** .
- Если данные не проходят валидацию - возвращает response вместе с данными и статус кодом  **400**.
  <strong>URL изображения проверяется на существование.</strong><br>

**DELETE** http://localhost:8000/api/posts/ - удаление всех элементов базы данных, а также всех изображений на сервере.
Возвращает response со статус кодом 204.<br><br>

<l>**GET**</l> http://localhost:8000/api/posts/id - возвращает response с отдельным элементом и статус кодом 200.

- Если элемента не существует - возвращает response со статус кодом 404.<br>

<l>**PUT**</l> http://localhost:8000/api/posts/id - заменяет элемент данными из request и возвращает response с данными
request и статус кодом 200.<br>

- Если элемента не существует - возвращает response со статус кодом 401.
- Если данные не проходят валидацию - возвращает response с указанием некорректных данных и статус кодом 400.
  <strong>URL изображения проверяется на существование.</strong> <br>

<l>**DELETE**</l> http://localhost:8000/api/posts/id - удаляет элемент с сервера и возвращает response с статус кодом
204.

- Если элемента не существует - возвращает response со статус кодом 404.

<l>**PATCH**</l> http://localhost:8000/api/posts/id - изменяет данные элемента и возвращает response со статус кодом
200.

- Если данные не проходят валидацию возвращает response с указанием на некорректные данные и статус кодом 400.
- Если элемента не существует - возвращает response со статус кодом 404.<br><br>

<l>**GET**</l> http://localhost:8000/api/posts/id/image - возвращает response с изображением.<br>

- Если элемента не существует - возвращает response со статус кодом 404.<br>
- Если изображения не существует на сервере, а элемент есть - возвращает response со статус кодом 404.

<l>**GET**</l> http://localhost:8000/api/posts/updated - возвращает response со всеми элементами базы данных,
отсортированных по дате создания, и статус кодом 200.<br>
<l>**GET**</l> http://localhost:8000/api/posts/created - возвращает response со всеми элементами базы данных,
отсортированных по дате последнего обновление, и статус кодом 200.<br><br>