from tornado import web
from handlers.BaseHandler import BaseHandler, wrap_async_rpc, wrap_catch

from core import FM


class TerminalHandler(BaseHandler):
    @wrap_async_rpc
    @wrap_catch
    @web.authenticated
    def post(self):

        session = self.get_post('session')

        if session is None:
            self.json({
                'error': True,
                'message': 'no session provided'
            })
            self.finish()
            return

        action = self.get_action(name=FM.Actions.OPEN_TERMINAL, session=session)
        answer = action.run()

        self.json(answer)
        self.finish()
