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
from pydantic import BaseModel

WriteARead = Controller()

#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
pintt = Reader("Pinttttt", "sawasdee", "01/01/2005")
WriteARead.add_writer(Mo)
WriteARead.add_reader(pintt)
WriteARead.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
WriteARead.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):
Book1 = Book("Shin_chan", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
Mo.add_writing_book_list(Book1)
Mo.add_writing_book_list(Book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = BookPromotion("01/01/2021", 50, [])
WriteARead.add_promotion(book_sale)

promotion_12_12 = CoinPromotion("01/01/2021", 40, "December")
promotion_11_11 = CoinPromotion("01/01/2021", 20, "November")
WriteARead.add_promotion(promotion_12_12)
WriteARead.add_promotion(promotion_11_11)


# now = datetime.now()
# WriteARead.buy_coin("Pinttttt", (TrueMoneyWallet("0123456789")), "December", 5000)
# WriteARead.buy_coin("Pinttttt", (OnlineBanking("0123456789")), "November", 100)

#=====================================================================================================

app = FastAPI()

@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Coin Transaction" : user.show_coin_transaction()}

@app.get("/get_my_coin", tags=['My Coin'])
def get_my_coin(username:str):
    user = WriteARead.get_user_by_username(username)
    return {"Golden Coin balance" : user.golden_coin.balance, "Silver Coin balance" : user.show_silver_coin_list()}

class dto_buy_coin(BaseModel):
    username : str
    golden_coin_amount : int
    payment_info : str
    payment_method : str 
    code: Optional[str] = None

@app.post("/buy_coin", tags=['Buy Coin'])
def buy_coin(dto : dto_buy_coin):
    payment = WriteARead.create_payment_method(dto.payment_method, dto.payment_info)
    WriteARead.buy_coin(dto.username, payment, dto.code, dto.golden_coin_amount)  
    return "Purchase successful, THANK YOU"

# class dto_buy_chapter(BaseModel):
#     username :str
#     chapter_id : str
    
# @app.post("/buy_chapter", tags=['chapter'])
# def BuyChapter(dto : dto_buy_chapter):
#      return {"Buy Chapter" : WriteARead.buy_chapter(dto.username,dto.chapter_id)}
#uvicorn main:app --reload

