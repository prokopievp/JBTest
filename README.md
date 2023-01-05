<h1>Бекенд для работы с мобильным приложением</h1><br>

<h3>Для запуска сервера вам потребуется:</h3>
<h3>1. Установить python.</h3>
<h3>2. Открыв консоль, перейти в папку JBtest, находящуюся в одной директории с файлом README.md на github.</h3>
<h3>3. Ввести в консоль pip install -r requirements.txt и дождаться установки всех пакетов.</h3>
<h3>4. В консоли перейти в папку "...JBtest/JB" и ввести "python manage.py runserver"</h3>
<h3>Сервер запущен! Перейдите на http://localhost:8000/admin для доступа к админ панели.</h3>
<br>
<h1>Примеры запросов:</h1>
<br>
<strong>GET</strong>  http://localhost:8000/posts/ - возвращает response со всеми элементами базы данных и статус кодом 200.<br><br>
<strong>POST</strong> http://localhost:8000/posts/ - добавление элемента в базу данных сервера и скачивание изображения по указанному URL на сервер, возвращает response с данными и статус код 201. <br>
Если данные проходят валидацию - возвращает response вместе с указанием некорректных данных и статус кодом 201.<br> 
Если данные не проходят валидацию - возвращает response вместе с данными и статус кодом 400. <br>
<strong>URL изображения также проверяется на существование.</strong><br><br>
DELETE http://localhost:8000/posts/ - удаление всех элементов базы данных, а также всех изображений на сервере. Возвращает response со статус кодом 204.<br>
<br><br><br>
pk - id конкретного элемента<br>
<strong>GET</strong> http://localhost:8000/posts/pk - возвращает response с отдельным элементом и статус кодом 200. <br><br>
Если элемента не существует - возвращает response со статус кодом 404.<br>
<strong>PUT</strong> http://localhost:8000/posts/pk - заменяет элемент данными из request и возвращает response с данными request и статус кодом 200.<br><br>
Если элемента не существует - возвращает response со статус кодом 404.<br>
Если данные не проходят валидацию - возвращает response с указанием некорректных данных и статус кодом 400.<br> 
<strong>URL</strong> изображения проверяется на существование.</strong> <br><br>
<strong>DELETE</strong> http://localhost:8000/posts/pk - удаляет элемент с сервера и возвращает response с статус кодом 204.<br>
Если элемента не существует - возвращает response со статус кодом 404.<br><br>
<strong>PATCH</strong> http://localhost:8000/posts/pk - изменяет данные элемента и возвращает response со статус кодом 200.<br>
Если данные не проходят валидацию возвращает response с указанием на некорректные данные и статус кодом 400.
Если элемента не существует - возвращает response со статус кодом 404.<br><br><br>

pk - id элемента<br>
<strong>GET</strong> http://localhost:8000/posts/pk/image - возвращает response с изображением.<br>
Если элемента не существует - возвращает response со статус кодом 404.<br>
Если изображения не существует на сервере, а элемент есть - возвращает response со статус кодом 404.<br><br><br>

<strong>GET</strong> http://localhost:8000/posts/updated - возвращает response со всеми элементами базы данных, отсортированных по дате создания, и статус кодом 200.<br><br>
<strong>GET</strong> http://localhost:8000/posts/created - возвращает response со всеми элементами базы данных, отсортированных по дате последнего обновление, и статус кодом 200.<br><br>