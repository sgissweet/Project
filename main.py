from Book import Book
from Chapter import Chapter
from Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from Promotion import BookPromotion, CoinPromotion
from Reader import Reader, Writer
from Controller import Controller

from datetime import datetime, date, timedelta
from typing import Optional, Annotated
from fastapi import FastAPI, Query
import uvicorn

WriteARead = Controller()

#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
pintt = Reader("Pinttttt", "sawasdee", "01/01/2005")
Controller.add_writer(Mo)
Controller.add_reader(pintt)
Controller.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
Controller.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):
Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
Mo.add_writing_book_list(Book1)
Mo.add_writing_book_list(Book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = BookPromotion("01/01/2021", 50, [])
Controller.add_promotion(book_sale)

promotion_12_12 = CoinPromotion("01/01/2021", 40, "December")
promotion_11_11 = CoinPromotion("01/01/2021", 20, "November")
Controller.add_promotion(promotion_12_12)
Controller.add_promotion(promotion_11_11)


# now = datetime.now()
# Controller.buy_coin("Pinttttt", (TrueMoneyWallet("0123456789")), "December", 5000)
# Controller.buy_coin("Pinttttt", (OnlineBanking("0123456789")), "November", 100)

#=====================================================================================================

app = FastAPI()

@app.get("/signup", tags=['Sign up'])
def SignUp(username:str, password:str, birth_date: str):
    new_reader = Reader(username,password,birth_date)
    if isinstance(new_reader, Reader)==True:
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

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = Controller.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

@app.get("/get_my_coin", tags=['My Coin'])
def get_my_coin(username:str):
    user = Controller.get_user_by_username(username)
    return {"Golden Coin balance" : user.golden_coin.balance, "Silver Coin balance" : user.show_silver_coin_list()}

@app.post("/post_payment_method", tags=['Buy Coin'])
def buy_coin(username:str, golden_coin_amount:int, payment_info: Annotated[str | None, Query(max_length = 10)], payment_method:str = Query("Payment Method", enum = Controller.payment_list, description ='Choose your payment method'), code: Optional[str] = None):
    payment = Controller.create_payment_method(payment_method, payment_info)
    Controller.buy_coin(username, payment, code, golden_coin_amount)  
    return "Purchase successful, THANK YOU"

@app.post("/Buy Chapter", tags=['chapter'])
def BuyChapter(username:str, chapter_id:str):
     return {"Buy Chapter" : WriteARead.buy_chapter(username, chapter_id)}
#uvicorn main:app --reload

