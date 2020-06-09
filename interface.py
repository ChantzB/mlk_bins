from tkinter import *
from record import Record
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

base = declarative_base()
engine = create_engine('sqlite:///records.db', echo=True)
base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

submit = None
screen = None
title_get = ''
artist_get = ''
year_get = ''
rec_company_get = ''
producer_get = ''
title_entry = ''
artist_entry = ''
year_entry = ''
rec_company_entry =''
producer_entry = ''
title_search = ''
artist_search = ''

class Main_Screen(object):
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry('500x450')
        self.space = Label(text="").pack()
        self.title = Label(text="Welcome to your personal records database", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', relief='ridge').pack()
        
        self.add = Button(text='Add a Record', activebackground='grey', height='8', width='50', relief='groove', command = Submit_Screen).pack()
        self.search = Button(text='Search Records', activebackground='grey', height='8', width='50', relief='groove', command = search_screen).pack()
        self.screen.mainloop()

class Submit_Screen(object):
    def __init__(self):
        self.screen = Toplevel(screen)
        self.screen.geometry('500x450')
        self.space = Label(text="").pack()
        self.title = Label(self.screen, text="Store your records", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', pady='5px', relief='ridge').pack()

        self.title_var = StringVar()
        self.title = Label(self.screen, text='Title:').pack()
        self.title_entry = Entry(self.screen, textvariable = self.title_var)
        self.title_entry.pack()

        self.artist_var = StringVar()
        self.artist = Label(self.screen, text='Artist:').pack()
        self.artist_entry = Entry(self.screen, textvariable = self.artist_var)
        self.artist_entry.pack()

        self.year_var = StringVar()
        self.year = Label(self.screen, text='Year:').pack()
        self.year_entry = Entry(self.screen, textvariable = self.year_var)
        self.year_entry.pack()

        self.rec_company_var = StringVar()
        self.rec_company = Label(self.screen, text='Record Company:').pack()
        self.rec_company_entry = Entry(self.screen, textvariable = self.rec_company_var)
        self.rec_company_entry.pack()

        self.producer_var = StringVar()
        self.producer = Label(self.screen, text='Producer(s):').pack()
        self.producer_entry = Entry(self.screen, textvariable = self.producer_var)
        self.producer_entry.pack()

        def submit_record(self):
            title = title_get.get()
            artist = artist_get.get()
            year = year_get.get()
            rec_company = rec_company_get.get()
            producer = producer_get.get()
                
            session = Session()
            queryset = session.query(Record).all()
            record = Record(title, artist, year, rec_company, producer, None)
            session.add(record)
            session.commit()
            session.close()

            title_entry.delete(0, END)
            artist_entry.delete(0, END)
            year_entry.delete(0, END)
            rec_company_entry.delete(0, END)
            producer_entry.delete(0,END)

            Label(submit, text='Record Added', fg='red').pack()
        self.submit = Button(self.screen, text='Submit', height='1', width='5', command = submit_record).pack()
# def submit_screen():
#     global submit
#     submit = Toplevel(screen)
#     submit.title('Records Log')
#     submit.geometry('500x450')

#     title_get = StringVar()
#     artist_get = StringVar()
#     year_get = StringVar()
#     rec_company_get = StringVar()
#     producer_get = StringVar()

#     Label(submit, text="Store you records", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', pady='5px', relief='ridge').pack()
#     Label(submit, text='').pack()

#     Label(submit, text='Title:').pack()
#     title_entry = Entry(submit, textvariable = title_get)
#     title_entry.pack()
#     Label(submit, text='').pack()

#     Label(submit, text='Artist:').pack()
#     artist_entry = Entry(submit, textvariable = artist_get)
#     artist_entry.pack()
#     Label(submit, text='').pack() 
    
#     Label(submit, text='Year:').pack()
#     year_entry = Entry(submit, textvariable = year_get)
#     year_entry.pack()
#     Label(submit, text='').pack() 
    
#     Label(submit, text='Record Company').pack()
#     rec_company_entry = Entry(submit, textvariable = rec_company_get)
#     rec_company_entry.pack()
#     Label(submit, text='').pack() 

#     Label(submit, text='Producer(s)').pack()
#     producer_entry = Entry(submit, textvariable = producer_get)
#     producer_entry.pack()
#     Label(submit, text='').pack()           
#     Button(submit, text='Submit', height='1', width='5', command = submit_record).pack()

def search_screen():
    search = Toplevel(screen)
    search.title('Search Records')
    search.geometry('500x450')

    global title_search
    title_search = StringVar()
    artist_search = StringVar()

    Label(search, text="Search your records", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', pady='5px', relief='ridge').pack()
    Label(search, text='').pack()

    Label(search, text='Search by title').pack()
    search_entry = Entry(search, textvariable = title_search).pack()
    Button(search, text='search', height='1', width='5', command = Table).pack()

    Label(search, text='Search by artist').pack()
    search_entry = Entry(search, textvariable = artist_search).pack()
    Button(search, text='search', height='1', width='5').pack()

class Table(object):
    def __init__(self):
        self.table = Toplevel(screen)
        self.table.title('Search Records')
        self.table.geometry('1500x450')
        session = Session()
        queryset = session.query(Record).all()

        for i in range(len(queryset)):
            df = pd.Series(vars(queryset[i])).to_frame()
            df.columns = ['value']
            value_list = df['value'].tolist()[1:]
            total_rows = len(value_list)

            for j in range(len(value_list)): 
                self.e = Entry(self.table, width=20, fg='blue', 
                               font=('Arial',16,'bold')) 
                  
                self.e.grid(row=i, column=j)
                try:
                    self.e.insert(END, value_list[j])
                except:
                    self.e.insert(END, "NONE")

if __name__ == "__main__":
    Main_Screen()