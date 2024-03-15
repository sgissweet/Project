from Book import Book
from Chapter import Chapter
from Payment import TrueMoneyWallet, OnlineBanking, DebitCard, PaymentMethod
from Promotion import CoinPromotion
from Reader import Reader, Writer
from Controller import Controller
from CoinTransaction import CoinTransaction
from ChapterTransaction import ChapterTransaction

from datetime import datetime, date, timedelta

write_a_read = Controller()

#user
Mo = Writer("Mozaza", "12345678", "12/05/2000")
Jin = Writer("Jinzaza", "12345678", "01/01/2005")
Pint = Reader("Pintzaza", "12345678", "01/01/2005")
Pang = Reader("Pangzaza", "12345678", "01/01/2004")
#add user
write_a_read.add_writer(Mo)
write_a_read.add_writer(Jin)
write_a_read.add_reader(Pint)
write_a_read.add_reader(Pang)

#prologue
shin_chan_prologue = "Shin Chan is a 50-year-old boy"
doraemon_prologue = "Doraemon, Noby, and their three friends are sucked into a portal during a heavy storm and transported to the village of Natura. It becomes apparent that the gadgets Doraemon usually carries, that could potentially save them and return them to the present, are all missing. Knowing they will be living in Natura for a while as they search for the gadgets, the friends all decide to get jobs. Your (Noby's) job ultimately is to farm the land south of Natura. And so your Story of Seasons journey begins."
#book
book1 = Book("Shin_chan", "Mola", Mo, "adventure", "publishing", False, shin_chan_prologue)
book2 = Book("Shinosuke", "Mola", Mo, "comedy", "publishing", True, shin_chan_prologue)
book3 = Book("Doraemon", "Jina", Jin, "comedy", "publishing", False, doraemon_prologue)
book4 = Book("Doraemon_Special", "Jina", Jin, "adventure", "publishing", True, doraemon_prologue)
#add book
Mo.add_writing_list(book1)
Mo.add_writing_list(book2)
Jin.add_writing_list(book3)
Jin.add_writing_list(book4)

# chap
chap3 = Chapter("Doraemon_Special", "3", "Doraemon_Special_third_ch", "this is the third chapter of Doraemon_Special", 500)

#add chapter
book1.add_chapter_list(Chapter("Shin_chan", "1", "Shin_chan_first_ch", "this is the first chapter of shincha", 184))
book2.add_chapter_list(Chapter("Shinosuke", "1", "Shinosuke_first_ch", "this is the first chapter of shincha", 184))
book3.add_chapter_list(Chapter("Doraemon", "1", "Doraemon_first_ch", "this is the first chapter of Doraemon", 500))
book4.add_chapter_list(Chapter("Doraemon_Special", "1", "Doraemon_Special_first_ch", "this is the first chapter of Doraemon_Special", 500))
book4.add_chapter_list(Chapter("Doraemon_Special", "2", "Doraemon_Special_second_ch", "this is the second chapter of Doraemon_Special", 500))
book4.add_chapter_list(chap3)

#promotion
promotion_11_11 = CoinPromotion("15/03/2024", 10, "November")
promotion_12_12 = CoinPromotion("15/03/2024", 20, "December")
write_a_read.add_promotion(promotion_11_11)
write_a_read.add_promotion(promotion_12_12)

#add coin transac
Mo.add_coin_transaction_list(CoinTransaction(OnlineBanking("0123456789"), 500, "+500", "+50", "20/02/2024, 15:23:10"))
Mo.add_coin_transaction_list(CoinTransaction(TrueMoneyWallet("9876543210"), 500, "+500", "+50", "20/02/2024, 15:23:10"))

#add chap transac
Mo.add_chapter_transaction_list(ChapterTransaction(chap3, 500))


