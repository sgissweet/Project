#Reader.py
from datetime import datetime, date, timedelta
import Book
import Chapter
import Coin
import ChapterTransaction
import CoinTransaction

class Reader:
    def __init__(self, username, password, birth_date):
        self.__username = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = Coin.GoldenCoin(0)
        self.__silver_coin_list = []
        self.__book_shelf_list = []
        self.__recent_read_chapter_list = []
        self.__chapter_transaction_list = []
        self.__coin_transaction_list = []
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @username.setter
    def password(self,password):
        self.__password = password

    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def golden_coin(self):
        return self.__golden_coin
    def add_golden_coin(self, amount):
        self.golden_coin.balance += amount
    def deduct_golden_coin(self, amount):
        self.__golden_coin.balance -= amount
    
    def get_silver_coin_list(self):
        return self.__silver_coin_list
    def add_silver_coin(self, amount):
        self.__silver_coin_list.append(Coin.SilverCoin(amount))
    def delete_exp_silver_coin(self):
        for silver_coin in self.__silver_coin_list:
            if silver_coin.exp_date_time - datetime.today():
                self.__silver_coin_list.remove(silver_coin)
    def deduct_silver_coin(self, amount):
        self.delete_exp_silver_coin()
        for silver_coin in self.__silver_coin_list:
            if amount > silver_coin.balance :
                self.__silver_coin_list.remove(silver_coin)
                amount -= silver_coin.balance
            elif amount < silver_coin.balance :
                silver_coin.balance -= amount
                break
            else :
                self.__silver_coin_list.remove(silver_coin)
                break
    
    def show_coin_list(self):
        my_coin_list = []
        silver_coin_balance = 0
        for silver_coin in self.__silver_coin_list:
            silver_coin_balance += silver_coin.balance
            
        my_coin_list.append(self.__golden_coin.balance)
        my_coin_list.append(silver_coin_balance)
        
        return my_coin_list
            
    def show_coin_transaction(self):
        show_list = []
        for coin_transaction in self.__coin_transaction_list:
            payment_type = coin_transaction.payment.name
            golden_amount = coin_transaction.golden_amount
            silver_amount = coin_transaction.silver_amount
            price = coin_transaction.price
            date_time = coin_transaction.date_time
            show_list.append(f"{payment_type} +{golden_amount}_golden_coin +{silver_amount}_silver_coin -{price} baht at {date_time}")
        return show_list
    
    def get_book_shelf_list(self):
        return self.__book_shelf_list
    def add_book_shelf_list(self, book):
        if isinstance(book,Book.Book):
            self.__book_shelf_list.append(book)

    def get_recent_read_chapter_list(self):
        return self.__recent_read_chapter_list
    def add_recent_read_chapter_list(self, chapter):
        if isinstance(chapter,Chapter.Chapter):
            self.__recent_read_chapter_list.append(chapter)

    def get_chapter_transaction_list(self):
        return self.__chapter_transaction_list
    def add_chapter_transaction_list(self, chapter_transaction):
        if isinstance(chapter_transaction, ChapterTransaction):
            self.__chapter_transaction_list.append(chapter_transaction)
    
    def get_coin_transaction_list(self):
        return self.__coin_transaction_list
    def add_coin_transaction_list(self, coin_transaction):
        if isinstance(coin_transaction, CoinTransaction.CoinTransaction):
            self.__coin_transaction_list.append(coin_transaction)

class Writer(Reader):
    money_balance = 0
    def __init__(self, username, password, birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_book_list = []
    
    @property
    def writing_book_list(self):
        return self.__writing_book_list
    def add_writing_book_list(self, book):
        if isinstance(book, Book.Book):
            self.__writing_book_list.append(book)