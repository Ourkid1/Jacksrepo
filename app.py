from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

#SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#    username="bannisterj",
#    password="",
#    hostname="bannisterj.mysql.pythonanywhere-services.com",
#    databasename="bannisterj$comments",
#)
#app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
#app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
#db = SQLAlchemy(app)

#class Comment(db.Model):

#    __tablename__ = "comments"

#    id = db.Column(db.Integer, primary_key=True)
#    content = db.Column(db.String(4096))

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html')
 #       return render_template("contact.html", comments=Comment.query.all())

 #   comment = Comment(content=request.form["contents"])
 #   db.session.add(comment)
 #   db.session.commit()
 #   return redirect(url_for('contact'))


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')  #  '/about'
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

