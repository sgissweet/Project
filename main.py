from Book import Book
from Chapter import Chapter
from Payment import Payment
from Promotion import Promotion
from Reader import Reader
from Reader import Writer
from Controller import Controller

from datetime import datetime, date, timedelta

Controller = Controller.Controller()

#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
Controller.add_writer_to_list(Mo)
pintt=Reader("Pinttttt", "sawasdee", "01/01/2005")
Controller.add_reader_to_list(pintt)
Controller.add_reader_to_list(Reader("Pangrum", "ehehe", "02/01/2005"))
Controller.add_reader_to_list(Reader("Jueeen", "whippedcream", "12/11/2004"))

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):
Book1 = Book.Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue", "01/01/2020")
Book2 = Book.Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue", "01/01/2020")
Mo.add_writing_book_list(Book1)
Mo.add_writing_book_list(Book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter.Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = Promotion.BookPromotion("01/01/2021",50, [])
Controller.add_promotion(book_sale)

free_coin = Promotion.CoinPromotion("01/01/2021",40, "chakeawaroi")

# print(WriteARead.search_book_by_name("Shin_chan"))
#=====================================================================================================
now = datetime.now()


Controller.buy_coin("Pinttttt", (Payment.TrueMoneyWallet("0123456789")), None, 5000)
Controller.buy_coin("Pinttttt", (Payment.OnlineBanking("0123456789")), None, 100)

from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/signup", tags=['Sign up'])
def SignUp(username:str, password:str, birth_date: str):
    new_reader = Reader.Reader(username,password,birth_date)
    if isinstance(new_reader,Reader.Reader)==True:
        Controller.add_reader(new_reader)
        return {"User": "sign up success"}
    else : 
        return {"User": "please try again"}

@app.get("/bookname", tags=['Search'])
def searchBook(book_name:str):
    return {"Book": Controller.search_book_by_name(book_name)}

@app.get("/username", tags=['Search'])
def SearchUser(username:str):
     return {"username": Controller.search_user(username)}

@app.get("/get_coin_transacttion", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = Controller.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

# @app.get("/get_my_coin", tags=['My Coin'])
# def get_my_coin(username:str):
#     user = Controller.get_user_by_username(username)
#     return {"Golden Coin balance" : user.show_my_coin_list[0], "Silver Coin balance" : user.show_my_coin_list[1]}

# Mo.show_coin_list()
print(pintt.get_silver_coin_balance())
# for silver_coin in Mo.get_silver_coin_list():
#     print(silver_coin)
#     print(silver_coin.balance)


# print(Mo.show_coin_transaction())

