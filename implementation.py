from commentbot import TwitterBot
from secrets import user, pw


tw_bot = TwitterBot(user, pw)
tw_bot.reply("hasanthehun", "I am testing")
tw_bot.reply("kanyewest", "I am testing")
tw_bot.reply("BernieSanders", "I am testing")
tw_bot.reply("h3h3productions", "I am testing")

