from Book import Book
from Chapter import Chapter
from Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from Promotion import BookPromotion, CoinPromotion
from Reader import Reader, Writer
from Controller import Controller
from CoinTransaction import CoinTransaction
from ChapterTransaction import ChapterTransaction

from datetime import datetime, date, timedelta
from typing import Optional, Annotated
from fastapi import FastAPI, Query, HTTPException
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

shin_chan_prologue = "Shin Chan is a 50-year-old boy"

book1 = Book("Shin_chan", "Mola", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_list(book1)

book2 = Book("Shinosuke", "Mola", Mo, ["kids", "comedy","crime"], "publishing", 7, shin_chan_prologue)
Mo.add_writing_list(book2)

book1.add_chapter_list(Chapter("Shin_chan", "1", "first_ch", "this is the first chapter of shincha", 184))

# book_name, chapter_number, chapter_name, context, cost
Chapter1_1 = Chapter("Shin_chan", 1, "Last of us", "jhahahahhahah", 5)

book_sale = BookPromotion("01/01/2021", 50, [])
write_a_read.add_promotion(book_sale)

promotion_12_12 = CoinPromotion("01/01/2021", 40, "December")
promotion_11_11 = CoinPromotion("01/01/2021", 20, "November")
write_a_read.add_promotion(promotion_12_12)
write_a_read.add_promotion(promotion_11_11)


now = datetime.now()
# write_a_read.buy_coin("Pinttttt", (TrueMoneyWallet("0123456789")), "December", 5000)
# print(write_a_read.buy_coin("Pinttttt", (OnlineBanking("0123456789")), "November", 100))


Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", now))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("9876543210"), 500, "+500", "+50", now))

Mo.add_chapter_transaction_list(ChapterTransaction(Chapter1_1, 5))
#=====================================================================================================

app = FastAPI()

# if __name__ == "__main__":
#      uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")

#============================================tangmo

from fastapi.middleware.cors import CORSMiddleware
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

#=============================================api
@app.get("/get_coin_transaction", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    user = write_a_read.get_user_by_username(username)
    return {"Coin_Transaction" : user.show_coin_transaction()}

@app.get("/get_my_coin", tags=['My Coin'])
def get_my_coin(username:str):
    user = write_a_read.get_user_by_username(username)
    return {"Golden_Coin_balance" : user.golden_coin.balance, "Silver Coin balance" : user.show_silver_coin_list()}

class dto_buy_coin(BaseModel):
    username : str
    golden_coin_amount : int
    payment_method : str 
    payment_info : str
    code: Optional[str] = None
    
@app.post("/buy_coin", tags=['Buy Coin'])
def buy_coin(dto : dto_buy_coin):
    payment = write_a_read.create_payment_method(dto.payment_method, dto.payment_info)
    write_a_read.buy_coin(dto.username, payment, dto.code, dto.golden_coin_amount)  
    return "Purchase successful, THANK YOU"

@app.get("/show_chapter_transaction", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
     user = write_a_read.get_user_by_username(username)
     if write_a_read.if_user_not_found(user): return user
     return {"Chapter_Transaction" : user.show_chapter_transaction()}
 
class dto_create_book(BaseModel):
     name:str
     pseudonym:str
     writer_name:str
     genre: str
     prologue: str
     age_restricted: bool
     status: str 

# ยังแตกอยุ่
# เพิ่มเก็บชื่อusernameของไร้เต้อ
@app.post("/book", tags=['Book'])
def CreateBook(dto : dto_create_book):
     return write_a_read.create_book(dto.name, dto.pseudonym, dto.writer_name, dto.genre, dto.status, dto.age_restricted, dto.prologue)

class dto_create_chapter(BaseModel):
     book_name:str
     chapter_number:int
     name:str
     context: str
     cost : int
     
@app.post("/chapter", tags=['Chapter'])
def CreateChapter(dto : dto_create_chapter):
     return write_a_read.create_chapter(dto.book_name, dto.chapter_number, dto.name, dto.context, dto.cost)
 
class dto_edit_book(BaseModel):
     old_name : str = None
     new_name : str = None
     new_genre: str = None
     prologue: str = None
     age_restricted: bool = None
     status: str = None
     
@app.put("/edit_book", tags=['Book'])
def EditBookInfo(dto : dto_edit_book):
     book =  write_a_read.edit_book_info(dto.old_name,dto.new_name,dto.new_genre,dto.status,dto.age_restricted,dto.prologue)
     if isinstance(book,Book):
          return book
     else:
          return {"error": "Book not found"}
     
class dto_edit_chapter(BaseModel):
     chapter_id : str = None
     name : str = None
     context : str = None
     cost : int = None
     
@app.put("/edit_chapter", tags=['Chapter'])
def EditChapterInfo(dto : dto_edit_chapter):
     chapter =  write_a_read.edit_chapter_info(dto.chapter_id, dto.name, dto.context, dto.cost)
     if isinstance(chapter,Chapter):
          return chapter
     else:
          return {"error": "Book not found"}