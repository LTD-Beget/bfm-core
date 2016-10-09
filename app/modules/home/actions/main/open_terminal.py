from core import FM


class OpenTerminal(FM.BaseAction):
    def __init__(self, session, **kwargs):
        super(OpenTerminal, self).__init__(**kwargs)

        self.session = session

    def run(self):
        request = self.get_rpc_request()
        result = request.request('main/open_terminal', login=self.request.get_current_user(),
                                 password=self.request.get_current_password(), session=self.session)
        answer = self.process_result(result)

        return answer
