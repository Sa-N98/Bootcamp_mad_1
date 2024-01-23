from flask import Flask , render_template , request ,redirect, url_for
from flask_restful import Api
from model import *
from api import *
import os

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + \
    os.path.join(current_dir, "bootcampDB.sqlite3")

api = Api(app) 
api.add_resource(databaseAPI, '/api/Bootcamp/','/api/Bootcamp/<num1>/<num2>',)



















db.init_app(app)
app.app_context().push()



@app.route("/", methods=['POST','GET'])
def index():
    if request.method=='POST':
        valueEmail = request.form['email']
        valurPassword = request.form['password']
        if users.query.filter(users.Email== valueEmail and  users.Password == valurPassword ).first():
            return redirect(url_for('home'))
        return redirect(url_for('signup'))
    return render_template('login.html')


@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method=='POST':
        valueUsename = request.form['username']
        valueEmail = request.form['email']
        valurPassword = request.form['password']

        if not users.query.filter(users.Email== valueEmail ).all():
                newUser = users(Username=valueUsename,Email=valueEmail, Password=valurPassword)
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('index'))
        return render_template('signup.html', error='This User Already Exists')



    return render_template('signup.html')


@app.route("/home")  # / = http://192.168.160.141:5000
def home():
    listOfMovies= movies.query.all()
    first3Movie = movies.query.limit(3).all()
    print(first3Movie)
    choice = movies.query.filter(movies.title == "Thor").first()

    return render_template("page.html" , shows= first3Movie  ) # var = listOfMovies

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bookings", methods=['POST', 'GET'])
def bookings():
    if request.method == 'POST':
        value = request.form['searchKey']
        print(value)
    return render_template("bookings.html")

@app.route("/add")
def add():
    newMovie=movies(rating = 7,title="Don_2", poster ="RandomLink" )
    db.session.add(newMovie)
    db.session.commit()
    return "data was added"

@app.route("/filter", methods=['POST'])
def filter():
    value = request.form['searchKey']
    searchType = request.form['filterOptions']

    if  searchType == "title":
        result = movies.query.filter(movies.title.like('%'+value+'%') ).all()
    elif searchType == "rating":
        result = movies.query.filter(movies.rating.like(value+'%') ).all()
    elif searchType == "genre":
        value = value.title()
        result = movies.query.filter(movies.genre.any(type=value)).all()
    return render_template("filter.html", data=result)

@app.route("/admin", methods=['POST','GET'])
def admin():
    if request.method == "POST":
        if request.form['formType'] == 'add':
            valueTitle = request.form['title']
            valueRating = request.form['rating']
            valurPoster = request.form['poster']

            if not movies.query.filter(movies.title== valueTitle ).all():
                newData = movies(title=valueTitle,rating=valueRating, poster=valurPoster)
                db.session.add(newData)
                db.session.commit()
                return "new movie added"
            return "Movie exists try adding a different movie"
        
        elif request.form['formType'] == 'delete':
            valueTitle = request.form['title']
            toBeDeleted=movies.query.filter(movies.title == valueTitle ).first()
            if toBeDeleted:
                db.session.delete(toBeDeleted)
                db.session.commit()
                return "movie deleted"
            return "This movie does not exists"
            
    return render_template('admin.html') 

@app.route("/api")
def Demoapi():
    return render_template("api.html")


if __name__ == '__main__':
    db.create_all()
    app.debug= True
    app.run(host='0.0.0.0')

