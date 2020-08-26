# **Introduction**

How cool would it be if you received a daily email that summarises prices and volume of stocks traded for a period of time? That is exactly what I achieved in this project. By using a mix of:
+ Pythons script
+ Jupyter Notebook 
+ Windows batch file 
+ Windows Task Scheduler 


## **How does the report look like?**
This the sample daily report that is sent to me. See link below: 
http://www.ymlearn.com/official_documents/python/Projects/basic_yahoo_finance/stock_analysis.html


## **The requirement**

If you hit the URL below, you will get CSV file containing the share price of Apple between the dates of 22/08/2019 and 22/08/2020. For this project, I want a daily email report which tells me:

+ Volume of stocks traded in the last 30 days - Show bar chart
+ Graph out the highest price and lowest stock price in the last 30 days - Show in line chart
+ For context, show the Highest and lowest price
+ Was divided paid out this month? How much?
+ The report should do this for any company or index of my choosing
+ The report should be sent to me only on workdays at midnight.
+ A quick description of each index, company, or commodity
The URL is the following format https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=1566432000&period2=1598054400&interval=1d&events=history where:

AAPL = Apple stock
+ period1 = Is the starting day. The timestamp is in unix format. see for unix timestamp converter. Ensure it set to minus 30 days
+ period2 is the end day. Ensure yesterdays is selected
+ For now, follow APPL (Apple), FDM.L (FDM), IAG.L, ^GSPC (S&P 500), GC=F (Gold), CL=F (Crude Oil)


## **How to get this running locally**

**Step 1** - Download the data scienece toolkit from anaconda by accessing the link below
https://www.anaconda.com/products/individual#Downloads

**Step 2** - Ensure you have git installed on your computer. Either git clone or download this repository preferably in the following directory C:\Users\{{your_space}}

**Step 3** -  Run the requirement.txt using the command below. It will download all the relevant python libraries

`pip install -r requirements.txt`

**Step 4** -  Run the bat file **daily.bat**. Make relevant edit to the **sendEmail.py** file to ensure it uses your gmail app password as well as ensure the email is sent to correct recicipent. 

**Step 5**-(optional) - Set up a windows task scheduler to execute the bat file whenever you want. 






