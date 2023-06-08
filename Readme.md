Steps To Run Server:
1. cd Flask
2. pip install flask flask_sqlalchemy flask_migrate
3. flask --app=index.py db init
4. flask --app=index.py db migrate -m "Initial migration"
5. flask --app=index.py db upgrade
6. python index.py
7. cd ../backend
8. npm install
9. nodemon index.js
10. hit url: http://localhost:3000
11. To verfiy: hit url: http://localhost:5000/listEventToDb. You will see saved Data.