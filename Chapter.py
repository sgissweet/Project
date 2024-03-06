from datetime import datetime

class Chapter:
    __chapter_id = 1

    def __init__(self, book_name, chapter_number, name, context, cost):
        self.__chapter_id = str(book_name) + "/" + str(chapter_number)
        self.__chapter_number = chapter_number
        self.__name = name
        self.__context = context
        self.__publish_date_time = datetime.now()
        self.__viewer_count = 0
        self.__comment_list = []
        self.__cost = cost
    #==========================================property
    
    @property
    def chapter_id(self):
        return self.__chapter_id
    
    @property
    def name(self):
        return self.__name
    def update_name(self, new_name):
        self.__name = new_name
    
    @property
    def chapter_number(self):
        return self.__chapter_number
    
    @property
    def context(self):
        return self.__context
    @context.setter
    def context(self,new_context):
        self.__context = new_context
    #
    def update_context(self, context):
        self.__context = context
        
    @property
    def publish_date_time(self):
        return self.__publish_date_time
    @publish_date_time.setter
    def publish_date_time(self,now):
        self.__publish_date_time = datetime.now()
        
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self,cost):
        self.__cost = cost
    #
    def update_cost(self, new_cost):
        self.__cost = new_cost
        
    @property
    def viewer_count(self):
        return self.__viewer_count
    def add_viewer_count(self):
        self.__viewer_count += 1
    
    def add_comment(self, comment):
        self.__comment_list.append(comment)
        
        
    
        
    
        
    