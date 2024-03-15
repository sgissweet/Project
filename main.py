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


import database
from database import write_a_read
#=====================================================================================================

app = FastAPI()

if __name__ == "__main__":
     uvicorn.run("main:app", host="127.0.0.1", port=5500, log_level="info")

app.mount("/page", StaticFiles(directory="page"), name="page")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")
#============================================tangmo

from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:5500",
    "localhost:5500",
    "http://127.0.0.1:5500",
    "127.0.0.1:5500/"
    "http://localhost:8000",
    "localhost:8000",
    "http://127.0.0.1:8000",
    "127.0.0.1:8000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#=============================================api
@app.get("/get_coin_transaction/{username}", tags=['Coin Transaction'])
def get_coin_transaction(username:str):
    return write_a_read.get_coin_transation(username)

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
    return write_a_read.buy_coin(dto.username, dto.payment_method, dto.payment_info, dto.code, dto.golden_coin_amount)

@app.get("/show_chapter_transaction/{username}", tags=['Chapter Transaction'])
def ShowChapterTransaction(username:str):
     user = write_a_read.get_user_by_username(username)
     if write_a_read.if_user_not_found(user): return user
     return user.show_chapter_transaction()
 
class dto_create_book(BaseModel):
     name:str
     pseudonym:str
     writer_name:str
     genre: str
     prologue: str
     age_restricted: bool
     status: str 

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
     return chapter

@app.get("/chapter/info/{chapter_id}")
async def get_chapter_info(chapter_id: str):
     chapter =write_a_read.get_chapter_by_chapter_id(chapter_id)
     print("chapterrrrrrrrrrrrrrrrrrrrr_id", chapter_id)
     if isinstance(chapter, Chapter):
          return chapter.show_chapter_info()
     else:
          raise HTTPException(status_code=404, detail="Chapter not found")
     
     
@app.get("/sign_in", tags=['sign up/sign in'])
def SignIN(username:str, password:str):
     return write_a_read.sign_in(username, password)

class dto_sign_up(BaseModel):
     username:str
     password:str
     birth_date: str
     role: str

@app.post("/sign_up", tags=['sign up/sign in'])
def SignUp(dto : dto_sign_up):
     return write_a_read.sign_up(dto.username, dto.password, dto.birth_date, dto.role)

# print(write_a_read.create_chapter("Shin_chan", 2, "chap2", "eewewewe", 0))
# print(write_a_read.edit_chapter_info("Shin_chan/2", "chap2 edit", "content edit", 10))
