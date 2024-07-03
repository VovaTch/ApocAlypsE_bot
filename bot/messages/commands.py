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
        self,
        bot: BotAI,
        unit_type_id: id,
        producer: tuple[Unit, Unit] | Unit | None = None,
    ) -> None:
        self._state = State.PENDING
        self._requested_unit_type = unit_type_id
        self._bot = bot

        # Archon error handling
        if unit_type_id == id.ARCHON:
            if producer is not None and len(producer) != 2:
                raise ValueError(
                    "Archon can only be produced from 2 high \ dark templars"
                )
        else:
            if producer is not None and len(producer) > 1:
                raise ValueError("A unit can only be produced from one building")

        self._producer: Unit = producer

    @property
    def state(self) -> State:
        return self._state

    @property
    def request_unit_type(self) -> id:
        return self._requested_unit_type

    def get_producer(self) -> Unit | None:
        if self._producer is None:
            return self._bot.units(
                PRODUCTION_MAPPING[self._requested_unit_type]
            ).ready.random
        elif self._producer.is_active:
            return None
        else:
            return self._producer

    def set_state_running(self) -> None:
        self._state = State.RUNNING

    def set_state_done(self) -> None:
        self._state = State.DONE
