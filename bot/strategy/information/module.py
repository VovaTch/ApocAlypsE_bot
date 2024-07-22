from dataclasses import dataclass
import logging
import threading

from loguru import logger
from sc2.bot_ai import BotAI
from sc2.ids.unit_typeid import UnitTypeId as id
from sc2.unit import Unit
from ...utils.timer import time_enforcer

"""
TODO: Implement vision tracking for the bot.
"""

logger = logging.getLogger(__name__)


@dataclass
class UnitInfo:
    """
    Dataclass to store information about a unit.
    """

    tag: int
    type: id
    position: tuple[float, float]
    last_spotted: float


class InformationHandler:
    """
    Main information handler class for the ApocAlypsE bot.
    """

    def __init__(self, bot: BotAI, run_frequency: float, debug: bool = False) -> None:
        self._bot = bot
        self._frequency = run_frequency
        self._debug = debug

        # Set internal memory and information variables
        self._memory: list[UnitInfo] = []
        self._certain_info: list[UnitInfo] = []

        # Set up the looping thread
        self._lock = threading.Lock()
        self._info_thread = threading.Thread(
            target=self._run, daemon=True, name="Information Thread"
        )

    def start(self) -> None:
        self._info_thread.start()

    def set_debug_mode(self, debug: bool) -> None:
        self._debug = debug

    def _run(self) -> None:
        while True:
            with time_enforcer(1 / self._frequency):
                self.update()
                if self._debug:
                    self._display_added_information()

    def update(self) -> None:

        self._certain_info = []

        with self._lock:
            for unit in self._bot.enemy_units:
                info = UnitInfo(
                    tag=unit.tag,
                    type=unit.type_id,
                    position=unit.position,
                    last_spotted=self._bot.time,
                )
                self._certain_info.append(info)
                self._update_unit_memory(info)

    def _update_unit_memory(self, unit_info: UnitInfo) -> None:
        for recorded_unit in self._memory:
            if recorded_unit.tag == unit_info.tag:
                recorded_unit.position = unit_info.position
                recorded_unit.last_spotted = self._bot.time
                return
        self._memory.append(unit_info)

    def get_certain_info(self) -> list[UnitInfo]:
        return self._certain_info

    def get_memory(self) -> list[UnitInfo]:
        return self._memory

    def _display_added_information(self) -> None:
        print(f"Certain information: {self._certain_info}")
        print(f"Memory: {self._memory}")
