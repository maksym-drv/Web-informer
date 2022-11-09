from .database import Database
from datetime import datetime, timedelta
from django.core.handlers.wsgi import WSGIRequest

def get_notifications(request: WSGIRequest):

    db          = Database()
    user_id     = request.user.id

    today       = datetime.now().date()
    yesterday   = today - timedelta(days=1)
    tomorrow    = today + timedelta(days=1)

    count       = db.get_messages_count(user_id, yesterday, tomorrow)

    yesterday   = [{"id": data[0], "name": data[1], "time": data[2]} 
        for data in db.get_messages_interval(user_id, yesterday, today)]

    today       = [{"id": data[0], "name": data[1], "time": data[2]} 
        for data in db.get_messages_interval(user_id, today, tomorrow)]
    
    context = {
        'count': count,
        'today': today,
        'yesterday': yesterday,
    }

    return context