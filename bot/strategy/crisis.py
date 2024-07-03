from sc2.bot_ai import BotAI


class CrisisModule:
    def __init__(self, bot: BotAI, information_module, evaluation_module) -> None:
        self._bot = bot
        self._info_module = information_module
        self._eval_module = evaluation_module
