## JBTest Backend для работы с мобильным приложением

Проект написан на python 3.8.7.
Используются Django и PostgreSQL.

### Инструкция к запуску:

#### Необходимо иметь установленными:

- **python** версии 3.хх
- установщик пакетов **pip** *(при установке python версии 3.4 и выше устанавливается автоматически)*
- **PostgreSQL**
  *(при установке postgres нужно оставить данные настройки дефолтными, в качестве пароля - 33113311).*

  ![](https://postgrespro.ru/media/2021/10/05/windows_setup2.png.502x390.jpg)
- Так как в дальнейшей инструкции будет использоваться GUI для PostgreSQL **pgAdmin4**, рекомендуется его установить(
  если я правильно помню, он устанавливается вместе с PostgreSQL).
  *Но в дальнейшем потребуется создать лишь создать базу данных, что можно сделать и через psql shell.*

### Подготовка и запуск сервера

- Для начала необходимо создать базу данных под названием JBdb.
  В pgAdmin это можно сделать таким образом:

![create-database.png](https://b.radikal.host/2023/01/06/create-database.png)
![create-JBdb.png](https://b.radikal.host/2023/01/06/create-JBdb.png)

- *Далее*, нужно перейти в командной строке в основную директорию проекта и запустить установку необходимых пакетов
  через pip:

```sh
pip install -r requirements.txt
```

- *Затем* нужно выполнить следующие команды(обязательно после создания БД):

```sh 
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
#создание логин/пароля для входа в админ панел

python manage.py runserver
 ```

- Сервер запущен. Теперь можно открыть https://localhost:8000/admin для входа в админ панель.

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