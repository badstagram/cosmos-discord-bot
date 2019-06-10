import datetime


class ModerationAction(object):

    def __init__(self, ctx, action_type, target, reason=None):
        self.ctx = ctx
        self.action = action_type
        self.target = target
        self.moderator = self.ctx.author
        self.reason = reason

    @property
    def document(self):
        _ = {
            "action": self.action.__class__.__name__,
            "target_id": self.target.id,
            "moderator_id": self.moderator.id,
        }
        if self.reason:
            _["reason"] = self.reason
        return _

    async def warn(self, title):
        await self.ctx.bot.dispatch("on_moderation", self)
        _ = self.ctx.embed_line(title)
        _.description = self.reason
        _.timestamp = datetime.datetime.now()
        await self.target.send(embed=_)