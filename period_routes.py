from main import app, session, Expenses, render_template, Response
import datetime, io
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from utils import categories, expense_period, week, print_bar, print_pie, print_plot, print_exp_type_bar

plt.rcParams['figure.figsize'] = [7.50,3.50]
plt.rcParams['figure.autolayout'] = True

    
@app.route('/daily')
def dayly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    daily_expenses, ttl_amount = expense_period(user_expenses,'daily')
    return render_template('daily.html',exp=daily_expenses,ttl=ttl_amount)

@app.route('/monthly')
def monthly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    monthly_expenses, ttl_amount = expense_period(user_expenses,'monthly')
    return render_template('monthly.html',exp=monthly_expenses,ttl=ttl_amount)

@app.route('/weekly')
def weekly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    weekly_expenses,ttl_amount = expense_period(user_expenses,'weekly')
    return render_template('weekly.html',exp=weekly_expenses,ttl=ttl_amount)

@app.route('/yearly')
def yearly():
    current_date = datetime.date.today()
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    yearly_expenses, ttl_amount = expense_period(user_expenses,'yearly')
    return render_template('yearly.html',exp=yearly_expenses,ttl=ttl_amount)



@app.route('/daily/printplot')
def print_plot_daily():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    daily_expenses,_ = expense_period(user_expenses,'daily')
    output = print_plot(daily_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/daily/printbar')
def print_bar_daily():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    daily_expenses, _ = expense_period(user_expenses,'daily')
    output = print_bar(daily_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/weekly/printplot')
def print_plot_weekly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    weekly_expenses, _ = expense_period(user_expenses, 'weekly')
    output = print_plot(weekly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/weekly/printpie')
def print_pie_weekly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    weekly_expenses, _ = expense_period(user_expenses, 'weekly')
    output = print_pie(weekly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/weekly/printbar')
def print_bar_weekly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    weekly_expenses, _ = expense_period(user_expenses,'weekly')
    output = print_bar(weekly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/montly/printplot')
def print_plot_monthly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    monthly_expenses, _ = expense_period(user_expenses, 'monthly')
    output = print_plot(monthly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/monthly/printbar')
def print_bar_monthly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    monthly_expenses, _ = expense_period(user_expenses, 'monthly')
    output = print_bar(monthly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/monthly/printpie')
def print_pie_monthly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    monthly_expenses, _ = expense_period(user_expenses,'monthly')
    output = print_pie(monthly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/yearly/printplot')
def print_plot_yearly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    yearly_expenses, _ = expense_period(user_expenses, 'yearly')
    output = print_plot(yearly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/yearly/printbar')
def print_bar_yearly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    yearly_expenses, _ = expense_period(user_expenses, 'yearly')
    output = print_bar(yearly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/yearly/printpie')
def print_pie_yearly():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    yearly_expenses, _ = expense_period(user_expenses,'yearly')
    output = print_pie(yearly_expenses)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/utility')
def utility():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    utility_bar = print_exp_type_bar(user_expenses,'utility')
    return Response(utility_bar.getvalue(),mimetype='image/png')

@app.route('/nourishment')
def nourishment():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    nourishment_bar = print_exp_type_bar(user_expenses,'nourishment')
    return Response(nourishment_bar.getvalue(),mimetype='image/png')

@app.route('/transportation')
def transportation():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    transportation_bar = print_exp_type_bar(user_expenses,'transportation')
    return Response(transportation_bar.getvalue(),mimetype='image/png')

@app.route('/entertainment')
def entertainment():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    entertainment_bar = print_exp_type_bar(user_expenses,'entertainment')
    return Response(entertainment_bar.getvalue(),mimetype='image/png')

@app.route('/education')
def education():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    education_bar = print_exp_type_bar(user_expenses,'education')
    return Response(education_bar.getvalue(),mimetype='image/png')

@app.route('/health')
def health():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    health_bar = print_exp_type_bar(user_expenses,'health')
    return Response(health_bar.getvalue(),mimetype='image/png')

@app.route('/appearance')
def appearance():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    appearance_bar = print_exp_type_bar(user_expenses,'appearance')
    return Response(appearance_bar.getvalue(),mimetype='image/png')

@app.route('/hobbies')
def hobbies():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    hobbies_bar = print_exp_type_bar(user_expenses,'hobbies')
    return Response(hobbies_bar.getvalue(),mimetype='image/png')

@app.route('/taxes')
def taxes():
    user_expenses = Expenses.query.filter_by(user_id=session['user_id']).all()
    taxes_bar = print_exp_type_bar(user_expenses,'taxes')
    return Response(taxes_bar.getvalue(),mimetype='image/png')
