import os.path

import flask
import flask_cors


class VKR(flask.Flask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CORS позволит нашему фронтенду делать запросы к нашему
        # бэкенду несмотря на то, что они на разных хостах
        # (добавит заголовок Access-Control-Origin в респонсы).
        # Подтюним его когда-нибудь потом.
        flask_cors.CORS(self)

app = VKR('vkr')

env = os.environ.get('APP_ENV', 'dev')
print(f'Starting application in {env} mode')
app.config.from_object(f'backend.{env}_settings')
