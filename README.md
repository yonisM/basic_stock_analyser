# **Introduction**

How cool would it be if you received a daily email that summarises prices and volume of stocks traded for a period of time? That is exactly what I achieved in this project. By using a mix of:
+ Pythons script
+ Jupyter Notebook 
+ Windows batch file 
+ Windows Task Scheduler 


## **How does the report look like?**
This the sample daily report that is sent to me. See link below: 
http://www.ymlearn.com/official_documents/python/Projects/basic_yahoo_finance/stock_analysis.html



## **How to get this running locally**

**Step 1** - Download the data scienece toolkit from anaconda by accessing the link below
https://www.anaconda.com/products/individual#Downloads

**Step 2** - Ensure you have git installed on your computer. Either git clone or download this repository preferably in the following directory C:\Users\{{your_space}}

**Step 3** -  Run the requirement.txt using the command below. It will download all the relevant python libraries

`pip install -r requirements.txt`

**Step 4** -  Run the bat file **daily.bat**. Make relevant edit to the **sendEmail.py** file to ensure it uses your gmail app password as well as ensure the email is sent to correct recicipent. 

**Step 5**-(optional) - Set up a windows task scheduler to execute the bat file whenever you want. 






