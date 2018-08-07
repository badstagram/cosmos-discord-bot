from raven import Client
from raven.exceptions import InvalidDsn


class ExceptionHandler(Client):

    def __init__(self, bot):
        self.bot = bot
        try:
            super().__init__(self.bot.configs.sentry.dsn)
        except InvalidDsn:
            self.bot.log.error("Invalid sentry DSN provided.")