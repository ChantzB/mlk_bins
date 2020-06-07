from tkinter import *
from record import Record
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

def main_screen():
    global screen
    screen = Tk()
    screen.geometry('500x450')
    Label(text="").pack(side=LEFT)
    Label(text="Welcome to your personal records database", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', pady='5px', relief='ridge').pack()
    Label(text="").pack()   
    submit_button = Button(text='Add a Record', activebackground='grey', height='8', width='50', pady='2px', relief='groove', command = submit_screen).pack()
    Label(text="").pack()
    search_button = Button(text='Search Records', activebackground='grey', height='8', width='50', relief='groove', command = search_screen).pack()
    screen.mainloop()

def submit_record():
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

def submit_screen():
    global submit
    submit = Toplevel(screen)
    submit.title('Records Log')
    submit.geometry('500x450')

    title_get = StringVar()
    artist_get = StringVar()
    year_get = StringVar()
    rec_company_get = StringVar()
    producer_get = StringVar()

    Label(submit, text="Store you records", width='400', height='3', bg='dark olive green', font=('Courier', 12), fg='white', pady='5px', relief='ridge').pack()
    Label(submit, text='').pack()

    Label(submit, text='Title:').pack()
    title_entry = Entry(submit, textvariable = title_get)
    title_entry.pack()
    Label(submit, text='').pack()

    Label(submit, text='Artist:').pack()
    artist_entry = Entry(submit, textvariable = artist_get)
    artist_entry.pack()
    Label(submit, text='').pack() 
    
    Label(submit, text='Year:').pack()
    year_entry = Entry(submit, textvariable = year_get)
    year_entry.pack()
    Label(submit, text='').pack() 
    
    Label(submit, text='Record Company').pack()
    rec_company_entry = Entry(submit, textvariable = rec_company_get)
    rec_company_entry.pack()
    Label(submit, text='').pack() 

    Label(submit, text='Producer(s)').pack()
    producer_entry = Entry(submit, textvariable = producer_get)
    producer_entry.pack()
    Label(submit, text='').pack()           
    Button(submit, text='Submit', height='1', width='5', command = submit_record).pack()

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
    Button(search, text='search', height='1', width='5', command = queryset).pack()

    Label(search, text='Search by artist').pack()
    search_entry = Entry(search, textvariable = artist_search).pack()
    Button(search, text='search', height='1', width='5').pack()

def queryset():
    query_search = Toplevel(screen)
    query_search.title('Search Records')
    query_search.geometry('500x450')
    #display records
    session = Session()

    title = title_search.get()

    queryset = session.query(Record).all()
    
    if title != '':
        queryset = session.query(Record).filter_by(title = title)

    for record in queryset:
        Label(query_search, text=record.artist).pack()
    session.close()


if __name__ == "__main__":
    main_screen()