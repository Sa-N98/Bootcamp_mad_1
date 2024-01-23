from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class movies(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Integer)
    poster = db.Column(db.String, nullable=False)
    genre = db.relationship("genre", secondary="movie_g")
    

class venue(db.Model):
    __tablename__ = "venues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,unique=True)
    location = db.Column(db.String, unique= True)

class genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, autoincrement=True,
                   primary_key=True, unique=True)
    type = db.Column(db.String, unique=True, nullable=False)

class movie_g(db.Model):
    __tablename__ = 'movie_g'
    m_id = db.Column(db.Integer, db.ForeignKey("movies.id"),
                     primary_key=True, nullable=False)
    g_id = db.Column(db.Integer, db.ForeignKey("genre.id"),
                     primary_key=True, nullable=False)

class users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True,primary_key=True, unique=True)
    Username = db.Column(db.String, unique=True, nullable=False)
    Email = db.Column(db.String, unique=True, nullable=False)
    Password = db.Column(db.String, unique=True, nullable=False)