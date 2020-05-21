from app import manager
from main import *

if __name__ == "__main__":
    manager.run()
    #py manage.py db init -- это в консоле дял того чтобы создалась папка миграции и версии, чтобы сохранить БД пока не испротили ее
    #py manage.py db migrate -- создат файл миграции апргрейт и даунгрейд
    #py manage.py db upgrade 