from bot.strategy.economy.module import EconomyHandler
from sc2.bot_ai import BotAI, Race
from sc2.data import Result
from .strategy.information import InformationHandler


DEBUG = True


class CompetitiveBot(BotAI):
    NAME: str = "CompetitiveBot"
    """This bot's name"""

    RACE: Race = Race.Protoss
    """This bot's Starcraft 2 race.
    Options are:
        Race.Terran
        Race.Zerg
        Race.Protoss
        Race.Random
    """

    async def on_start(self):
        """
        This code runs once at the start of the game
        Do things here before the game starts
        """
        print("Game started")

        self._information_handler = InformationHandler(self, 2.0, debug=False)
        self._information_handler.start()

        self._economy_handler = EconomyHandler(self, 2.0, debug=DEBUG)
        self._economy_handler.start()

    async def on_step(self, iteration: int):
        """
        This code runs continually throughout the game
        Populate this function with whatever your bot should do!
        """

        pass

    async def on_end(self, result: Result):
        """
        This code runs once at the end of the game
        Do things here after the game ends
        """
        print("Game ended.")
