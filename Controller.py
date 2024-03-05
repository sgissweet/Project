import CoinTransaction

from dateutil import relativedelta
from datetime import datetime, date, timedelta


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = ["OnlineBanking", "Debit Card", "TrueMoney Wallet"]
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]

    def add_reader_to_list(self, reader):
        self.__reader_list.append(reader)
    
    def add_writer_to_list(self, writer):
        self.__writer_list.append(writer)

    def search_book_list_by_name(self, book_name):
        search_list=[]
        for writer in self.__writer_list:
            for book in writer.writing_book_list:
                if book_name.lower() in book.name.lower():
                    search_list.append(book.name)
                    
        if search_list==[]:
            return "Not found"
        else:
            return search_list
          
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"
                    
    # def check_report_count(self, book, webmaster):
    # if len(book.get_report_list()) > 10:
    #     if webmaster.check_book_edits(book):
    #         book.hide_book()
    #         webmaster.notify_book_hidden(book)
    #         writer = book.writer
    #         writer.notify_book_hidden(book)
    #         return True
    #     else:
    #         book.delete_report_list()
    # return False              
    
    def check_age_restricted(self):
        day, month, year = map(int, self.__birth_date.split('/'))
        birth = datetime(year, month, day)
        date_diff = relativedelta.relativedelta(datetime.now(),birth)
        if date_diff.years>=18 :
            return "over 18"
        else: 
            return "under 18"
    
    def search_user_list(self, username):
        search_list = []
        for reader in self.__reader_list:
            if username.lower() in reader.username.lower():
                search_list.append(reader.username)
        
        for writer in self.__writer_list:
            if username.lower() in writer.username.lower() and writer.username not in search_list:
                search_list.append(writer.username)

        if search_list == []:
            return "user not found"
        else:
            return search_list
    
    def add_coin_to_user(self, user, payment, golden_amount, silver_amount, price):
        payment.buy_coin(price)
        date_time = datetime.now()
        user.add_golden_coin(golden_amount)
        user.add_silver_coin(silver_amount)
        user.add_coin_transaction_list(CoinTransaction.CoinTransaction(payment, price, [golden_amount, silver_amount], date_time.strftime("%d/%m/%Y, %H:%M:%S")))
        
    def buy_coin(self, username, payment, code, golden_amount):
        price = golden_amount
        silver_amount = int(golden_amount * 10 / 100)
        user = self.get_user_by_username(username)
        if(code != None):
            coin_promotion = self.search_coin_promotion(code)
            if coin_promotion in payment.__coin_promotion:
                print("Applying code")
                price = (100 - coin_promotion.discount) / 100 * price #ลดราคา 
            else:
                return "Your code is expired or not exist"
        else:
            print("Not applying any code")
            
        self.add_coin_to_user(user, payment, golden_amount, silver_amount, price)
            
    @property
    def report_type_list(self):
        return self.__report_type_list
    @property
    def reader_list(self):
        return self.__reader_list
    @property
    def writer_list(self):
        return self.__writer_list

    def search_coin_promotion(self, code):
        pass

    def add_writer(self, writer):
        self.__writer_list.append(writer)

    def add_payment(self, payment):
        self.__payment_list.append(payment)

    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)

    def buy_chapter(self, chapter_id, book_id, user_id):
        pass


