cd C:\Users\yonis\python_projects\Yahoo_Finance_Historical_Data
setx PATH "%path;C:\Users\yonis\anaconda3;C:\Users\yonis\anaconda3\Scripts"
call "C:\Users\yonis\anaconda3\Scripts\activate.bat"
jupyter nbconvert --to html --execute stock_analysis.ipynb --no-input
python sendEmail.py 
