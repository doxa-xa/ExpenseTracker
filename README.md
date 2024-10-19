# **Expense Tracker**

## **Introduction**
An exprense tracker web applicaton. This app enables you to keep track of your finances by logging your expenses and providing analysis on: **daily, weekly, monthly and yearly** basis. With **8 main categories** and with over **30 subcategories**, you will be identify any excessive spending and plan your finances better.
**The app uses sqlite3 as a database. You can modify it to work with your preffered DB.**

## **Installation**

1. Install Python *version 3.12*
2. Install git
2. Setup git,Python and pip in environmental variables
3. Clone the repository: *`git clone https://github.com/doxa-xa/ExpenseTracker.git`*
4. Install packeges requirements with pip: *`pip install -r requirements.txt`*
5. Run the application: *`flask --app main run`*
6. Open a browser the applicaton is at: *localhost:5000*


## **How to use**

- Create an account by clicking the *register* link ![register link](/static/register_link.jpg)
- Add an expense by selecting an expense category ![add expense](/static/add_expense.jpg)
- Fill out the expense form and add the expense ![add expense following](/static/add_expense2.jpg)
- It will redirect you to the status screen to check the expense you've added
- Use the *add another* button to add the expenses you like. 
- From the *status* screen you can access various reports and visualization to help you determine your spending: ![status menu](/static/status_menu.jpg)

## **To do and to fix**

### **Known issues**

1. After registrtion dosen't create a `session` with the *user ID* - You need to logout and login in order to create it.
2. It throws: **Status 500 internal server error** when the email is already in use - Need to handle that.


## **Contribution**
*Feel free to additional information in order to imporve the project. I will appreciate any suggestion on improvement. Please message me if you identify additional issues. The product is free to use, improve and change as you deem fit.*


**Author:** Stoyan Todorov