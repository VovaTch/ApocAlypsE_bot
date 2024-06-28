from enum import Enum, auto

from sc2.ids.unit_typeid import UnitTypeId as id
from sc2.unit import Unit
from sc2.bot_ai import BotAI
from .mapping import PRODUCTION_MAPPING


class State(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()


class TrainCommand:
    def __init__(
        self, bot: BotAI, unit_type_id: id, building_structure: Unit | None = None
    ) -> None:
        self._state = State.PENDING
        self._requested_unit_type = unit_type_id

        match unit_type_id:
            case id.INTERCEPTOR:
                raise NotImplementedError(
                    "Interceptors are not trained directly, TODO: write logic"
                )
            case id.ARCHON:
                raise NotImplementedError(
                    "Archons are not trained directly, TODO: write logic"
                )
            case _:
                self._building_structure = building_structure
