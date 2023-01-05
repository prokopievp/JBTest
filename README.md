<h1>Бекенд для работы с мобильным приложением</h1><br>

<h2><strong>Для запуска сервера вам потребуется:</strong></h2>
<h3>1. Установить python.</h3>
<h3>2. Открыв консоль, перейти в папку JBtest, находящуюся в одной директории с файлом README.md на github.</h3>
<h3>3. Ввести в консоль pip install -r requirements.txt и дождаться установки всех пакетов.</h3>
<h3>4. В консоли перейти в папку "...JBtest/JB" и ввести "python manage.py runserver"</h3>
<h3>5. <strong>Готово.</strong>
<h3>5. Ссылка на админ панель: http://localhost:8000/admin.</h3>
<br>
<h2><strong>Примеры запросов:</strong></h2>
GET http://localhost:8000/posts/
POST http://localhost:8000/posts/
DELETE http://localhost:8000/posts/

GET http://localhost:8000/posts/pk
PUT http://localhost:8000/posts/pk
DELETE http://localhost:8000/posts/pk
PATCH http://localhost:8000/posts/pk

GET http://localhost:8000/posts/96/image
GET http://localhost:8000/posts/created
GET http://localhost:8000/posts/created


картинки ![Описание](ссылка)           <img src="путь к файлу" alt="альтернативный текст">
