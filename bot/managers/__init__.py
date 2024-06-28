from enum import Enum, auto

from sc2.ids.unit_typeid import UnitTypeId as id
from sc2.unit import Unit
from sc2.bot_ai import BotAI


class State(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()
    

class TrainCommand:
    def __init__(self, bot: BotAI, unit_type_id: id, building_structure: Unit | None = None) -> None:
        self._state = State.PENDING
        self._requested_unit_type = unit_type_id
        self._building_structure = building_structure if building_structure is not None else bot.