#Reader.py
from Chapter import Chapter
from Book import Book
from Coin import GoldenCoin, SilverCoin
from ChapterTransaction import ChapterTransaction
from CoinTransaction import CoinTransaction
from Payment import OnlineBanking, DebitCard, TrueMoneyWallet

from datetime import datetime, date, timedelta
from dateutil import relativedelta

class Reader:
    def __init__(self,username,password,birth_date):
        self.__username = username
        self.__display_name = username
        self.__password = password
        self.__birth_date = birth_date #check age_restricted
        self.__golden_coin = GoldenCoin(0)
        self.__silver_coin_list = []
        self.__book_shelf_list = []
        self.__recent_read_chapter_list = []
        self.__chapter_transaction_list = []
        self.__coin_transaction_list = []
        self.__follower_list = []
        self.__introduction = ''
    
    #=============================================property
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,username):
        self.__username = username

    @property
    def display_name(self):
        return self.__display_name
    @display_name.setter
    def display_name(self, display_name):
        self.__display_name = display_name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password = password

    @property
    def birth_date(self):
        return self.__birth_date
    
    @property
    def follower_list(self):
        return self.__follower_list
    
    @property
    def golden_coin(self):
        return self.__golden_coin
    def add_golden_coin(self,amount):
        self.golden_coin.balance += amount
    def deduct_golden_coin(self,amount):
        self.golden_coin.balance -= amount
        
    @property
    def silver_coin_list(self):
        return self.__silver_coin_list
    def add_silver_coin(self, amount):
        self.__silver_coin_list.append(SilverCoin(amount))
    
    @property
    def introduction(self):
        return self.__introduction
    @introduction.setter
    def introduction(self, text):
        self.__introduction = text
        
    @property
    def book_shelf_list(self):
        return self.__book_shelf_list
    def add_book_shelf_list(self, book):
        if isinstance(book, Book):
            self.__book_shelf_list.append(book)
        
    @property
    def recent_read_chapter_list(self):
        return self.__recent_read_chapter_list
    def add_recent_read_chapter_list(self, chapter):
        if isinstance(chapter,Chapter):
            self.__recent_read_chapter_list.append(chapter)

    @property
    def chapter_transaction_list(self):
        return self.__chapter_transaction_list
    def add_chapter_transaction_list(self,chapter_transaction):
        if isinstance(chapter_transaction, ChapterTransaction):
            self.__chapter_transaction_list.append(chapter_transaction)
    
    @property
    def coin_transaction_list(self):
        return self.__coin_transaction_list
    def add_coin_transaction_list(self,coin_transaction):
        if isinstance(coin_transaction,CoinTransaction):
            self.__coin_transaction_list.append(coin_transaction)   
       
    #=========================================================method 
    
    #jueen
    def get_user_coin_balance(self):
      return self.__golden_coin.balance + self.get_silver_coin_balance()
    
    def get_silver_coin_balance(self):
      silver_coin_balance = 0
      for silver_coin in self.__silver_coin_list:
        silver_coin_balance += silver_coin.balance
      return silver_coin_balance
    
    def show_silver_coin_list(self):
        silver_coin_balance = 0
        for silver_coin in self.__silver_coin_list:
            silver_coin_balance += silver_coin.balance
        return silver_coin_balance

    def delete_exp_silver_coin(self):
        for silver_coin in self.__silver_coin_list:
            if silver_coin.exp_date_time - datetime.today():
                self.__silver_coin_list.remove(silver_coin)

    def deduct_silver_coin(self,amount):
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

    def check_age_restricted(self):
        day, month, year = map(int, self.__birth_date.split('/'))
        birth = datetime(year, month, day)
        date_diff = relativedelta.relativedelta(datetime.now(),birth)
        if date_diff.years>=18 :
            return "over 18"
        else: 
            return "under 18"
        
    def show_coin_transaction(self):
        show_list = []
        for coin_transaction in self.__coin_transaction_list:
            payment_type = coin_transaction.payment
            golden_amount = coin_transaction.golden_amount
            silver_amount = coin_transaction.silver_amount
            price = coin_transaction.price
            date_time = coin_transaction.date_time
            
            if(isinstance(payment_type, str)):
                if(silver_amount == '0'):
                    show_list.append(f"{payment_type} {golden_amount}_golden_coin at {date_time}")
                elif(golden_amount == '0'):
                    show_list.append(f"{payment_type} {silver_amount}_silver_coin at {date_time}")
                else:
                    show_list.append(f"{payment_type} {golden_amount}_golden_coin {silver_amount}_silver_coin at {date_time}")
            else:    
                payment_type = coin_transaction.payment.name
                show_list.append(f"{payment_type} -{price}baht {golden_amount}_golden_coin {silver_amount}_silver_coin at {date_time}")
            
        return show_list
    
    def show_chapter_transaction(self):
        show_list = []
        for chapter_transaction in self.__chapter_transaction_list:
            show_list.append(chapter_transaction.chapter_transaction())
        return show_list
    
    def edit_introduction(self, text):
        if len(text) > 50:
            return "Introduction cannot be longer than 50 letters"
        else:
            self.__introduction = text
            return "Introduction updated"
    
    def check_repeated_purchase(self, chapter):
        for transaction in self.__chapter_transaction_list:
            if chapter == transaction.chapter:
                return True
        return False
    
    def check_age_restricted(self):
        day, month, year = map(int, self.__birth_date.split('/'))
        birth = datetime(year, month, day)
        date_diff = relativedelta.relativedelta(datetime.now(),birth)
        if date_diff.years>=18 :
            return "over 18"
        else: 
            return "under 18"


class Writer(Reader):
    money_balance = 0
    def __init__(self,username,password,birth_date):
        super().__init__(username,password,birth_date)
        self.__writing_list = []
        self.__pseudonym_list = []
    
    @property
    def writing_list(self):
        return self.__writing_list
    
    def add_writing_list(self,book):
        if isinstance(book,Book):
            self.__writing_list.append(book)
    
    @property
    def pseudonym_list(self):
        return self.__pseudonym_list
    
    def add_pseudonym(self, pseudonym):
        self.__pseudonym_list.append(pseudonym)
    
    @property
    def viewer_count(self):
        count = 0
        for book in self.__writing_list:
            for chapter in book.chapter_list:
                count += chapter.viewer_count
        return count
    
    @property
    def comment_list(self):
        comment_list = []
        for book in self.__writing_list:
            comment_list.append(book.comment_list())
        return comment_list
    
    def show_comment_list(self):
        comment_list = []
        for book in self.__writing_list:
            for comment in book.comment_list:
                comment_list.append(comment.show_comment())
        return comment_list
    
    def show_writing_name_list(self):
        writing_name_list = []
        for book in self.__writing_list:
            book_dict = {"book_name" : book.name,
                                "pseudonym": book.pseudonym,
                                "genre" : book.genre}
            writing_name_list.append(book_dict)
        return writing_name_list
    
    def check_repeated_pseudonym(self, new_pseudonym):
        for pseudonym in self.__pseudonym_list:
            if pseudonym.lower() == new_pseudonym.lower():
                return True
        return False