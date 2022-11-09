from django.db import connection
from datetime import datetime

class Database:
    
    def get_messages_interval(self, user: int, start_date: datetime, end_date: datetime):
        with connection.cursor() as cursor:
            cursor.execute('''SELECT forum_topic.id, forum_topic.title, forum_reply.time FROM forum_reply 
                        INNER JOIN forum_receiver on forum_receiver.reply_id = forum_reply.id
                        INNER JOIN accounts_customuser on forum_receiver.user_id = accounts_customuser.id
                        INNER JOIN forum_message on forum_reply.reply_to_id = forum_message.id
                        INNER JOIN forum_topic on forum_message.topic_id = forum_topic.id
                        where forum_receiver.is_read = %s 
                        and accounts_customuser.id = %s 
                        and forum_reply.time > %s 
                        and forum_reply.time < %s;''', (False, user, start_date, end_date))
            row = cursor.fetchall()
        return row

    def get_messages_count(self, user: int, start_date: datetime, end_date: datetime):
        with connection.cursor() as cursor:
            cursor.execute('''SELECT count(*) FROM forum_reply 
                        INNER JOIN forum_receiver on forum_receiver.reply_id = forum_reply.id
                        INNER JOIN accounts_customuser on forum_receiver.user_id = accounts_customuser.id
                        INNER JOIN forum_message on forum_reply.reply_to_id = forum_message.id
                        INNER JOIN forum_topic on forum_message.topic_id = forum_topic.id
                        where forum_receiver.is_read = %s 
                        and accounts_customuser.id = %s 
                        and forum_reply.time > %s 
                        and forum_reply.time < %s;''', (False, user, start_date, end_date))
            row = cursor.fetchone()[0]
        return row

    def read_message(self, user: int, forum: int):
        with connection.cursor() as cursor:
            cursor.execute('''call read_message(%s, %s)''', (user, forum, ))