from typing import Any
from sc2.bot_ai import BotAI


class EconomyModule:
    def __init__(self, bot: BotAI) -> None:
        self._bot = bot

    def evaluate(self) -> dict[str, Any]:
        raise NotImplementedError("Evaluate method is not implemented yet")
