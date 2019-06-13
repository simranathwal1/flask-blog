from flask import Flask , render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b6ceca7dce6ddb5c912814dbeca6cf72'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

posts =[
	{
		"author":'Tugce Konuklar',
		'title': 'Blog',
		'content':'Content bla bla',
		'date_posted':'April 20,2019'
	},
	{
		"author":'Tugce Konuklar 2',
		'title': 'Blog 2',
		'content':'Content bla bla 2',
		'date_posted':'April 20,2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title='About')


@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password' :
			flash('You have been logged in !','success')
			return redirect(url_for('home'))
		else:
			flash('Please check your username and password', 'danger')
	return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
	app.run(debug=True)