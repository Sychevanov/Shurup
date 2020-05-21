from app import app # импорт апп из апп
from app import db # базы данных из апп

import view #ипорт вью
from posts.blueprint import posts # блуприанта (отлельная программка)
app.register_blueprint(posts, url_prefix='/blog') # регистрация блупринта

if __name__ == "__main__":
    app.run()