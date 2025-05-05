from flask import Flask
from .models import db  # ← استدعاء قاعدة البيانات
from .models import Task  # ← مهم جدًا تستورد الموديل

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@db/testdb'  # ← عدل حسب حالتك
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()  # ← دي أهم سطر، بيعمل إنشاء تلقائي للجداول

    return app
