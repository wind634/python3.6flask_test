from flask_sqlalchemy import SQLAlchemy
# 使用pymysql 代替MySQL-Python
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()
