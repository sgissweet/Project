from Chapter import Chapter
from Report import Report #
from Comment import Comment #
from datetime import datetime, timedelta

class Book:
    def __init__(self, name, pseudonym, writer, genre, status, age_restricted, prologue):
        self.__name = name
        self.__pseudonym = pseudonym
        self.__writer = writer
        self.__genre = genre
        self.__status = status
        self.__age_restricted = age_restricted
        self.__prologue = prologue
        self.__chapter_list = []
        self.__comment_list = []
        self.__report_list = []
        self.__date_time = datetime.now()
        #*****book ควรมี pseudonym ของตัวเองเป็น str ด้วย
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name
        
    @property
    def pseudonym(self):
        return self.__pseudonym
        
    @pseudonym.setter
    def pseudonym(self, new_pseudonym):
        self.__pseudonym = new_pseudonym
        
    @property
    def writer(self):
        return self.__writer

    @property
    def genre(self):
        return self.__genre
        
    @property
    def age_restricted(self):
        return self.__age_restricted
    
    @age_restricted.setter
    def age_restricted(self,age_restricted):
        self.__age_restricted = age_restricted
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, new_status):
        self.__status = new_status
        
    @property
    def prologue(self):
        return self.__prologue
    
    @prologue.setter
    def prologue(self, new_prologue):
        self.__prologue = new_prologue
        
    @property
    def date_time(self):
        return self.__date_time
    
    #ตรงนี้แปลกๆ ไม่ควรเป็น property งี้
    @date_time.setter
    def date_time(self, now):
        self.__date_time = datetime.now()
        
    @property
    def date_time_str(self):
        return self.__date_time.strftime("%d/%m/%Y, %H:%M:%S")

    @property
    def chapter_list(self):
        return self.__chapter_list
    
    def add_chapter_list(self,chapter):
        if isinstance(chapter,Chapter):
            self.__chapter_list.append(chapter)

    @property
    def report_list(self):
        return self.__report_list

    @property
    def comment_list(self):
        return self.__comment_list
    
    @property
    def chapter_count(self):
        return len(self.__chapter_list)
    
    @genre.setter
    def genre(self,new_genre):
        self.__genre = new_genre
    
    def add_comment_list(self, comment):
        if isinstance(comment, Comment):
            self.__comment_list.append(comment)
            
    ###
    def add_report_list(self, report):
        if isinstance(report, Report):
            self.__report_list.append(report)
            
    def add_report_list(self, report):
        self.report_list.append(report)
        self.counting_date_time = datetime.now()
    

    # def counting_report_from_type(self):
    #     report_count=0
    #     for report in self.__report_list:
    #         for report_type in write_a_read.report_type_list:
    #             if report_count == 10:
    #                 break
    #             if report.report_type == report_type:
    #                 report_count+=1

    def delete_report(self, report):
        if report in self.report_list:
            self.report_list.remove(report)
    
    #check if the chapter number is repeated       
    def is_chapter_valid(self,chapter_number):
        for chapter in self.chapter_list:
            if chapter.chapter_number == chapter_number:
                return False
        return True
    
    def show_age_restricted(self):
        if self.__age_restricted:
            return "/"
        return "X"
    
    
    def show_book_info(self):
        return {"name" : self.__name,
                "pseudonym" : self.__pseudonym,
                "genre" : self.genre, ################################
                "status" : self.status,
                "prologue" : self.prologue,
                "age_retricted" : self.show_age_restricted(),
                "chapter_count" : self.chapter_count,
                "comments" : self.show_comment_list()}
        
    def show_comment_list(self):
        comment_list = []
        for comment in self.__comment_list:
            comment_list.append(comment.show_comment())
        return comment_list