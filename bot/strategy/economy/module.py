from dataclasses import dataclass
import threading

from ...utils.timer import time_enforcer
from sc2.bot_ai import BotAI


@dataclass
class EconomyFlowInfo:
    mineral_flow: float
    gas_flow: float

    def __str__(self) -> str:
        string_to_return = (
            f"Mineral flow: {self.mineral_flow} minerals per minute\n"
            f"Gas flow: {self.gas_flow} gas per minute\n"
        )
        return string_to_return


@dataclass
class EconomyInfoPerBase:
    coordinates: tuple[float]
    num_workers_minerals: int
    num_workers_gas: int

    def __str__(self) -> str:
        string_to_return = (
            f"Nexus coordinates: X {self.coordinates[0]} | Y {self.coordinates[1]}\n"
            f"Mineral workers: {self.num_workers_minerals}\n"
            f"Gas workers: {self.num_workers_gas}\n"
        )
        return string_to_return


@dataclass
class EconomyManagementInfo:
    bases: list[EconomyInfoPerBase]
    num_workers_scouts: int
    num_workers_idle: int

    @property
    def num_workers_minerals(self) -> int:
        return sum(base.num_workers_minerals for base in self.bases)

    @property
    def num_workers_gas(self) -> int:
        return sum(base.num_workers_gas for base in self.bases)

    @property
    def num_workers(self) -> int:
        return (
            self.num_workers_minerals
            + self.num_workers_gas
            + self.num_workers_scouts
            + self.num_workers_idle
        )

    def __str__(self) -> str:
        base_str_list = [
            f"\n<--- BASE NUM. {idx + 1} --->\n{base}"
            for (idx, base) in enumerate(self.bases)
        ]
        base_str = "\n".join(base_str_list)
        scouts = f"Scouts: {self.num_workers_scouts}\n"
        idle = f"Idle workers: {self.num_workers_idle}\n"
        return base_str + scouts + idle


class EconomyHandler:
    def __init__(self, bot: BotAI, run_frequency: float, debug: bool = False) -> None:
        self._bot = bot
        self._frequency = run_frequency
        self._debug = debug

        # Set up the looping thread
        self._lock = threading.Lock()
        self._info_thread = threading.Thread(
            target=self._run, daemon=True, name="Information Thread"
        )

        # Information containers
        self._reset_all_info()

    def start(self) -> None:
        self._info_thread.start()

    def _reset_all_info(self) -> None:
        self._economy_flow_info = EconomyFlowInfo(0, 0)
        self._economy_management_info = EconomyManagementInfo([], 0, 0)

    def _run(self) -> None:
        while True:
            with time_enforcer(1 / self._frequency):
                self.update()
                if self._debug:
                    self._display_added_information()

    def update(self) -> None:

        with self._lock:

            self._reset_all_info()

            # INstantiate the rate per minute
            minerals_per_minute = 0
            gas_per_minute = 0

            # Locate all nexi
            for nexus in self._bot.townhalls.ready:
                gas_buildings = self._bot.gas_buildings.closer_than(13, nexus).ready
                assigned_gas_workers = sum(
                    [gas_b.surplus_harvesters + 3 for gas_b in gas_buildings]
                )
                print(f"Assigned workers: {nexus.assigned_harvesters}")
                self._economy_management_info.bases.append(
                    EconomyInfoPerBase(
                        nexus.position,
                        nexus.assigned_harvesters,
                        assigned_gas_workers,
                    )
                )

                ideal_mineral_workers = nexus.ideal_harvesters

                if nexus.assigned_harvesters <= ideal_mineral_workers:
                    minerals_per_minute += 55 * nexus.assigned_harvesters
                elif nexus.assigned_harvesters <= int(ideal_mineral_workers * 1.5):
                    minerals_per_minute += (
                        27 * ideal_mineral_workers + 28 * nexus.assigned_harvesters
                    )
                else:
                    minerals_per_minute += 27 * ideal_mineral_workers + int(
                        28 * ideal_mineral_workers * 1.5
                    )

                for gas_b in gas_buildings:
                    if gas_b.surplus_harvesters >= 0:
                        gas_per_minute += 163
                    elif gas_b.surplus_harvesters == -1:
                        gas_per_minute += 123
                    elif gas_b.surplus_harvesters == -2:
                        gas_per_minute += 61
                    elif gas_b.surplus_harvesters == -3:
                        gas_per_minute += 0

            self._economy_flow_info.mineral_flow = minerals_per_minute
            self._economy_flow_info.gas_flow = gas_per_minute

            # Log idle workers
            for worker in self._bot.workers:
                if worker.is_idle:
                    self._economy_management_info.num_workers_idle += 1

                # Log scouts
                if (
                    not worker.is_idle
                    and not worker.is_collecting
                    and not worker.is_returning
                    and not worker.is_gathering
                ):
                    self._economy_management_info.num_workers_scouts += 1

    def get_econ_info(self) -> EconomyManagementInfo:
        with self._lock:
            return self._economy_management_info

    def get_flow_info(self) -> EconomyFlowInfo:
        with self._lock:
            return self._economy_flow_info

    def _display_added_information(self) -> None:
        print(f"Economy information:\n{self.get_econ_info()}")
        print(f"Flow information:\n{self.get_flow_info()}")
