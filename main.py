from Book import Book
from Chapter import Chapter
from Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from Promotion import BookPromotion, CoinPromotion
from Reader import Reader, Writer
from Controller import Controller
from CoinTransaction import CoinTransaction

from datetime import datetime, date, timedelta
from typing import Optional, Annotated
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles


#=============================================================================create instance
write_a_read = Controller()

#create temporary instance
Mo = Writer("Mozaza", "namchakeawpun", "12/05/2000")
pintt = Reader("Pinttttt", "sawasdee", "01/01/2005")
write_a_read.add_writer(Mo)
write_a_read.add_reader(pintt)
write_a_read.add_reader(Reader("Pangrum", "ehehe", "02/01/2005"))
write_a_read.add_reader(Reader("Jueeen", "whippedcream", "12/11/2004"))

# Book (self,name,writer,tag_list,status,age_restricted,prologue,date_time):
# Book1 = Book("Shin_chan","eiei", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
# Book2 = Book("Shinosuke", Mo, ["kids", "comedy","crime"], "publishing", 7, "shin_chan_prologue")
book1 = Book("Shin_chan", "Mola", Mo, ["kids", "comedy","crime"], "publishing", 7, "Shin Chan is a 50-year-old boy")
# Mo.add_writing_list(book1)
# Mo.add_writing_book_list(book1)
Mo.add_writing_list(book1)
# print(book1.pseudonym)
# Mo.add_writing_book_list(book2)

#chapter_number, name, context, date_time, cost):
Chapter1_1 = Chapter("1", "first chapter of shinchan", "this is the first chapter of shinchan", "01/01/2020", 5)

book_sale = BookPromotion("01/01/2021", 50, [])
write_a_read.add_promotion(book_sale)

promotion_12_12 = CoinPromotion("01/01/2021", 40, "December")
promotion_11_11 = CoinPromotion("01/01/2021", 20, "November")
write_a_read.add_promotion(promotion_12_12)
write_a_read.add_promotion(promotion_11_11)


now = datetime.now()
# write_a_read.buy_coin("Pinttttt", (TrueMoneyWallet("0123456789")), "December", 5000)
# write_a_read.buy_coin("Pinttttt", (OnlineBanking("0123456789")), "November", 100)

Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", now))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("9876543210"), 500, "+500", "+50", now))
#=====================================================================================================

app = FastAPI()

#============================================tangmo
origins = [
    "http://localhost:5500",
    "localhost:5500",
    "http://127.0.0.1:5500",
    "127.0.0.1:5500/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#=============================================dto
class dto_buy_coin(BaseModel):
    username : str
    golden_coin_amount : int
    payment_method : str 
    payment_info : str
    code: Optional[str] = None

#=============================================api
@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = write_a_read.get_user_by_username(username)
    return {"Coin_Transaction" : user.show_coin_transaction()}

@app.get("/get_my_coin", tags=['My Coin'])
def get_my_coin(username:str):
    user = write_a_read.get_user_by_username(username)
    return {"Golden_Coin_balance" : user.golden_coin.balance, "Silver Coin balance" : user.show_silver_coin_list()}

@app.post("/buy_coin", tags=['Buy Coin'])
def buy_coin(dto : dto_buy_coin):
    payment = write_a_read.create_payment_method(dto.payment_method, dto.payment_info)
    write_a_read.buy_coin(dto.username, payment, dto.code, dto.golden_coin_amount)  
    return "Purchase successful, THANK YOU"

