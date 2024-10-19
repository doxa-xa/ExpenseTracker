from flask import Flask, render_template, request,redirect, url_for, session, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask_bcrypt import Bcrypt
from models import db, User, Expenses
from utils import categories
import numpy as np
import matplotlib.pyplot as plt
import uuid, io, datetime

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\ctodo\\Documents\\upwork\\tracker\\tracker.db'
bcrypt = Bcrypt(app)
db.init_app(app)

plt.rcParams['figure.figsize'] = [7.50,3.50]
plt.rcParams['figure.autolayout'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form:
            user_name = request.form.get('username')
            password = request.form.get('passwd')
            user = User.query.filter_by(name=user_name).first()
            is_valid = bcrypt.check_password_hash(user.passwd_hash,password)
            if is_valid:
                session['user_id'] = user.id
                return redirect(url_for('category'))
            else:
                return 'Wrong password <a href="/login">Try Again</a>'

    else:
        return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        if request.form:
            name = request.form.get('username')
            passwd = request.form.get('passwd')
            confpasswd = request.form.get('confpasswd')
            email = request.form.get('email')
            if passwd == confpasswd:
                user = User(name = name,
                            passwd_hash = bcrypt.generate_password_hash(passwd).decode('utf-8'),
                            email = email)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('category'))
            else:
                return 'Passwords do not match <a href="/register">Try Again</a>'
        else:
            return "500 - Something went wrong"
    else:
        return render_template('register.html')

@app.route('/category', methods=['GET','POST'])
def category():
    e_cat = categories.keys()
    if request.method == 'POST':
        if request.form:
            return redirect(url_for('expense',data = request.form.get('category')))
    else:
        return render_template('category.html',data = e_cat)
    
@app.route('/expense',methods=['GET','POST'])
def expense():
    if request.method == 'POST':
        if request.form:
            ex_type = request.form.get('etype')
            amount = request.form.get('amount')
            name = request.form.get('name')
            cat = request.form.get('cat')
            date = request.form.get('date')
            day_of_week = request.form.get('dayofweek')
            new_expense = Expenses(
                category = cat,
                expense_type = ex_type,
                amount = amount,
                expense_name = name,
                date = date,
                day_of_week = day_of_week,
                user_id = session['user_id']
            )
            db.session.add(new_expense)
            db.session.commit()
            return redirect(url_for('status'))
    else:
        return render_template('expense.html', data = categories[request.args['data']],cat = request.args['data'])
    
@app.route('/status')
def status():
    user_expenses = Expenses.query.filter_by(user_id = session['user_id']).all()
    ttl_amount = sum([item.amount for item in user_expenses])
    return render_template('status.html',exp = user_expenses, ttl = ttl_amount)

@app.route('/expensetypes')
def expense_types():
    exp_types = categories.keys()
    return render_template('expensetype.html',pics=exp_types)

import period_routes


@app.route('/printplot')
def print_plot():
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    expenses = Expenses.query.filter_by(user_id = session['user_id']).all()
    xs = [item.date for item in expenses]
    ys = [item.amount for item in expenses]
    axis.plot(xs,ys)
    axis.set_title('Expense amount per day')
    axis.set_xlabel('Date')
    axis.set_ylabel('Amount')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/printpie')
def print_pie():
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    user_expenses = Expenses.query.filter_by(user_id = session['user_id']).all()
    week = {'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}
    for item in user_expenses:
        week[item.day_of_week] += item.amount
    ys = [week[item] for item in week.keys() if week[item] !=0]
    xs = [item for item in week.keys() if week[item] !=0]
    axis.pie(ys,labels=xs)
    axis.set_title('Expenses share per day of the week')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/printbar')
def print_bar():
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    user_expenses = Expenses.query.filter_by(user_id = session['user_id']).all()
    cat = categories.keys()
    result = {}
    for item in cat:
        result[item] = 0
    for item in user_expenses:
        result[item.category] += item.amount
    ys = [result[item] for item in result.keys() if result[item] !=0]
    xs = [item for item in result.keys() if result[item] !=0]
    axis.bar(x=xs,height=ys)
    axis.set_title('Expenses share per category')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
