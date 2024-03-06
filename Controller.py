import CoinTransaction
from Book import Book
from Chapter import Chapter
from Comment import Comment
from ChapterTransaction import ChapterTransaction
from Reader import Reader, Writer
from Payment import OnlineBanking, TrueMoneyWallet, DebitCard

from dateutil import relativedelta
from datetime import datetime, date, timedelta


class Controller:
    def __init__(self):
        self.__reader_list = []
        self.__writer_list = []
        self.__payment_list = ["OnlineBanking", "Debit Card", "TrueMoney Wallet"]
        self.__promotion_list = []
        self.__report_type_list = ["violence","harrasment"]
    #=
    # =============================================property
    
    @property
    def report_type_list(self):
        return self.__report_type_list
    @property
    def reader_list(self):
        return self.__reader_list
    @property
    def writer_list(self):
        return self.__writer_list
    
    def add_reader(self, reader):
        self.__reader_list.append(reader)
    def add_writer(self, writer):
        self.__writer_list.append(writer)
    def add_payment(self, payment):
        self.__payment_list.append(payment)
    def add_promotion(self, promotion):
        self.__promotion_list.append(promotion)
        
    #==================================================method
    
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
    
    def get_book_by_name(self, book_name):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                if book.name == book_name:
                    return book
    
    def search_coin_promotion(self, code):
        pass
    
    def search_user_list_by_name(self, username):
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
          
    def get_user_by_username(self, username):
        for reader in self.__reader_list:
            if reader.username == username:
                return reader
        
        for writer in self.__writer_list:
            if writer.username == username:
                return writer
            
        return "User Not Found"
    
    def search_chapter_by_chapter_id(self,chapter_id):
        for writer in self.__writer_list:
            for book in writer.writing_list:
                for chapter in book.chapter_list:
                    if chapter.chapter_id == chapter_id:
                        return chapter
        return "Not found"
                    
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
    
    def buy_chapter(self, chapter_id, book_name, username):
        book = self.get_book_by_name(book_name)
        chapter_list = book.get_chapter_list()

        for chapter in chapter_list:
            if chapter.chapter_id == chapter_id:
                cost = chapter.cost

        user = self.get_user_by_username(username)
        coin_balance = user.get_user_coin_balance()

        if coin_balance >= cost:
            user.deduct_coin(cost)
            user.add_chapter_transaction()
        else:
            return "Not enough coin"

    def show_my_page(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "introduction" : user.introduction,
                "writing_count" : writing_count,
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
    
    def show_my_profile(self, username):
        writing_count = 0
        reads = 0
        writing_list = None
        pseudonym_list = None
        comments = None
        user = self.get_user_by_username(username)
        if isinstance(user, Writer):
            writing_count = len(user.get_writing_list())
            reads = user.get_viewer_count()
            writing_list = user.get_writing_name_list()
            pseudonym_list = user.get_pseudonym_list()
            comment_list = user.get_json_comment_list()
        else:
            return "User Not Found"
        return {"display_name" : user.display_name,
                "username" : user.username,
                "password" : "*" * len(user.password),
                "book_on_shelf_count" : len(user.get_book_shelf_list()),
                "followers" : len(user.get_follower_list()),
                "read_count" : len(user.get_recent_read_chapter_list()),
                "viewer_count" : reads,
                "writings" : writing_list,
                "pseudonyms" : pseudonym_list,
                "comments" : comment_list}
        
    def show_coin(self, username):
        user = self.get_user_by_username(username)
        # print(user)
        if user:
            return f"Golden Coin : {user.golden_coin.balance} | Silver Coin : {user.silver_coin_balance}"
        return "User Not Found"
    
    def sign_in(self,username, password):
        user = self.get_user_by_username(username)
        print(user.username, user.password, user.birth_date)
        if (isinstance(user,Reader) or isinstance(user,Writer)):
            if user.password == password:
                return "log in successfully"
            else: 
                return "wrong password"
        else:
            return "can not find username/password"
    
    def sign_up(self,username:str, password:str, birth_date: str):
        user = self.get_user_by_username(username)
        if isinstance(user,Reader) == False or isinstance(user,Writer) == False:
            new_reader = Reader(username,password,birth_date)
            self.add_reader(new_reader)
            return {"User": "sign up successfully"}
        else : 
            return {"User": "invalid username"}
        
    def create_book(self, name:str, writer_name:str, tag_list: str, status: str, age_restricted: bool, prologue: str):
        writer = self.get_user_by_username(writer_name)
        book = self.get_book_by_name(name)
        if isinstance(writer,Writer) and isinstance(book,Book) == False:
            new_book = Book(name,writer,tag_list,status,age_restricted,prologue)
            writer.add_writing_book_list(new_book)
            return {"Book": "create book successfully"}
        else : 
            return {"Book": "please try again"}
    
    def create_chapter(self,book_name,chapter_number, name, context, cost):
        book = self.get_book_by_name(book_name)
        if isinstance(book,Book) and book.is_chapter_valid(chapter_number):
            chapter = Chapter(book_name,chapter_number, name, context, cost)
            book.add_chapter_list(chapter)
            return {"Chapter": "create Chapter successfully"}
        else : 
            return {"Chapter": "please try again"}   
        
    def create_comment(self, chapter_id, username, context):
        chapter = self.search_chapter_by_chapter_id(chapter_id)
        user = self.get_user_by_username(username)
        # print(chapter)
        if isinstance(chapter,Chapter):
            new_comment = Comment(chapter,user,context)
            #find book and append in book 
            chapter.add_comment(new_comment)
            return {"Comment": "create comment success"}
        else : 
            return {"Comment": "please try again"}
    # รับ username มาด้วยดีมั้ย แล้วเพิ่มpaymentmethodไว้ในuserแต่ละคน  
    def create_payment_method(self, payment_method_name, payment_info):
        if payment_method_name == OnlineBanking.name:
            return OnlineBanking(payment_info)
        elif payment_method_name == TrueMoneyWallet.name:
            return TrueMoneyWallet(payment_info)
        elif payment_method_name == DebitCard.name:
            return DebitCard(payment_info)
            
    def edit_book_info(self, name, add_tag_list, delete_tag_list, status, age_restricted, prologue):
        book = self.get_book_by_name(name)
        if name:
            book.name=name
        if add_tag_list:
            book.add_tag(add_tag_list)
        if delete_tag_list:
            book.delete_tag(delete_tag_list)
        if status:
            book.status = status
        if age_restricted:
            book.age_restricted = age_restricted
        if prologue:
            book.prologue = prologue
        # book.date_time(0)
        return book
            
    def edit_chapter_info(self,chapter_id, name, context, cost):
        chapter = self.search_chapter_by_chapter_id(chapter_id)
        if name:
            chapter.name=name
        if context:
            chapter.context(context)
        if cost:
            chapter.cost(cost)
        # chapter.publish_date_time(0)
        return chapter
    

