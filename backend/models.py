   from flask_sqlalchemy import SQLAlchemy

   db = SQLAlchemy()

   class User(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       username = db.Column(db.String(80), unique=True, nullable=False)
       password = db.Column(db.String(120), nullable=False)

   class Declaration(db.Model):
       id = db.Column(db.Integer, primary_key=True)
       cargo_type = db.Column(db.String(50), nullable=False)
       value = db.Column(db.Float, nullable=False)
       user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   
