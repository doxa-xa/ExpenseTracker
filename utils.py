categories = {
    'utility':['electricity','internet & tv','phone','water','heating','cleaning','rent/mortgage'],
    'transportation':['tickets','fuel','vehicle maintenance','vehicle taxes'],
    'nourishment':['meat','fish','dairy','fruits & vegetables','sweets & junk food','soft drinks','alcohol','tobacco'],
    'entertainment':['concerts','movies & teathre','sports events','gambling','video games'],
    'education':['courses','materials','tuition fees'],
    'health':['treatment','dental','drugs'],
    'hobbies':['materials','instruments'],
    'appearance':['clothes','shoes','grooming','cosmetics'],
    'taxes':['home','vehicle','personal']
}

week = {'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0,'Sunday':0}

import datetime, io
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def expense_period(user_expenses,period):
    current_date = datetime.date.today()
    if period == 'daily':
        daily_expenses = []
        for item in user_expenses:
            date = datetime.datetime.strptime(item.date,"%Y-%m-%d")
            if current_date.year == date.year and current_date.month == date.month and current_date.day == date.day:
                daily_expenses.append(item)
        ttl_amount = sum([item.amount for item in daily_expenses])
        return (daily_expenses,ttl_amount)
    elif period == 'weekly':
        weekly_expenses = []
        for item in user_expenses:
            date = datetime.datetime.strptime(item.date,"%Y-%m-%d")
            if current_date.isocalendar()[1] == date.isocalendar()[1]:
                weekly_expenses.append(item)
        ttl_amount = sum([item.amount for item in weekly_expenses])
        return(weekly_expenses,ttl_amount)
    elif period == 'monthly':
        monthly_expenses = []
        for item in user_expenses:
            date = datetime.datetime.strptime(item.date,"%Y-%m-%d")
            if current_date.year == date.year and current_date.month == date.month:
                monthly_expenses.append(item)
        ttl_amount = sum([item.amount for item in monthly_expenses])
        return (monthly_expenses,ttl_amount)
    elif period == 'yearly':
        yearly_expenses = []
        for item in user_expenses:
            date = datetime.datetime.strptime(item.date,"%Y-%m-%d")
            if current_date.year == date.year:
                yearly_expenses.append(item)
        ttl_amount = sum([item.amount for item in yearly_expenses])
        return (yearly_expenses,ttl_amount)

def extract_expense_types(expenses,exp_type):
    result = {item:0 for item in categories[exp_type]}
    for item in expenses:
        if item.expense_type in categories[exp_type]:
            result[item.expense_type] += item.amount
    return (result.keys(),result.values()) 

def print_exp_type_bar(expenses,exp_type):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    xs,ys = extract_expense_types(expenses, exp_type)
    axis.bar(x=xs,height=ys)
    axis.set_title(f'Expenses share per {exp_type}')
    axis.tick_params(axis='x',labelrotation=45)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output

def print_plot(expenses):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    xs = [item.date for item in expenses]
    ys = [item.amount for item in expenses]
    axis.plot(xs,ys)
    axis.set_title('Expense amount per day')
    axis.set_xlabel('Date')
    axis.set_ylabel('Amount')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output

def print_pie(expenses):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    for item in expenses:
        week[item.day_of_week] += item.amount
    ys = [week[item] for item in week.keys() if week[item] !=0]
    xs = [item for item in week.keys() if week[item] !=0]
    axis.pie(ys,labels=xs)
    axis.set_title('Expenses share per day of the week')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output

def print_bar(expenses):
    fig = Figure()
    axis = fig.add_subplot(1,1,1)
    cat = categories.keys()
    result = {}
    for item in cat:
        result[item] = 0
    for item in expenses:
        result[item.category] += item.amount
    ys = [result[item] for item in result.keys() if result[item] !=0]
    xs = [item for item in result.keys() if result[item] !=0]
    axis.bar(x=xs,height=ys)
    axis.set_title('Expenses share per category')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output