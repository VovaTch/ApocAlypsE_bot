"""Number of Banelings that are required to kill the unit at various upgrade levels.

"""
from typing import Dict

from sc2.ids.unit_typeid import UnitTypeId as UnitID

BANELING_MAGIC_NUMBERS: Dict[UnitID, Dict] = {
    UnitID.NEXUS: {0: 25, 1: 24, 2: 23, 3: 22},
    UnitID.PYLON: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.ASSIMILATOR: {0: 8, 1: 8, 2: 7, 3: 7},
    UnitID.GATEWAY: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.WARPGATE: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.FORGE: {0: 10, 1: 10, 2: 9, 3: 9},
    UnitID.PHOTONCANNON: {0: 4, 1: 4, 2: 4, 3: 4},
    UnitID.SHIELDBATTERY: {0: 4, 1: 4, 2: 4, 3: 4},
    UnitID.CYBERNETICSCORE: {0: 14, 1: 13, 2: 13, 3: 12},
    UnitID.TWILIGHTCOUNCIL: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.ROBOTICSFACILITY: {0: 12, 1: 11, 2: 10, 3: 10},
    UnitID.STARGATE: {0: 15, 1: 15, 2: 14, 3: 13},
    UnitID.TEMPLARARCHIVE: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.DARKSHRINE: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.ROBOTICSBAY: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.FLEETBEACON: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.COMMANDCENTER: {0: 19, 1: 18, 2: 17, 3: 16},
    UnitID.ORBITALCOMMAND: {0: 19, 1: 18, 2: 17, 3: 16},
    UnitID.PLANETARYFORTRESS: {0: 19, 1: 18, 2: 17, 3: 16},
    UnitID.SUPPLYDEPOT: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.SUPPLYDEPOTLOWERED: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.SUPPLYDEPOTDROP: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.REFINERY: {0: 7, 1: 6, 2: 6, 3: 6},
    UnitID.BARRACKS: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.ENGINEERINGBAY: {0: 11, 1: 10, 2: 10, 3: 9},
    UnitID.BUNKER: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.MISSILETURRET: {0: 4, 1: 3, 2: 3, 3: 3},
    UnitID.SENSORTOWER: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.FACTORY: {0: 16, 1: 15, 2: 14, 3: 14},
    UnitID.GHOSTACADEMY: {0: 16, 1: 15, 2: 14, 3: 14},
    UnitID.ARMORY: {0: 10, 1: 9, 2: 9, 3: 8},
    UnitID.STARPORT: {0: 17, 1: 16, 2: 15, 3: 14},
    UnitID.FUSIONCORE: {0: 10, 1: 9, 2: 9, 3: 8},
    UnitID.TECHLAB: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.BARRACKSTECHLAB: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.FACTORYTECHLAB: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.STARPORTTECHLAB: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.REACTOR: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.BARRACKSREACTOR: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.FACTORYREACTOR: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.STARPORTREACTOR: {0: 5, 1: 5, 2: 5, 3: 5},
    UnitID.BARRACKSFLYING: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.FACTORYFLYING: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.STARPORTFLYING: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.COMMANDCENTERFLYING: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.ORBITALCOMMANDFLYING: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.AUTOTURRET: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.HATCHERY: {0: 19, 1: 18, 2: 17, 3: 16},
    UnitID.EXTRACTOR: {0: 7, 1: 6, 2: 6, 3: 6},
    UnitID.SPAWNINGPOOL: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.EVOLUTIONCHAMBER: {0: 10, 1: 9, 2: 9, 3: 8},
    UnitID.SPINECRAWLER: {0: 4, 1: 4, 2: 4, 3: 4},
    UnitID.SPORECRAWLER: {0: 6, 1: 5, 2: 5, 3: 5},
    UnitID.ROACHWARREN: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.BANELINGNEST: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.LAIR: {0: 26, 1: 24, 2: 23, 3: 22},
    UnitID.HYDRALISKDEN: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.LURKERDENMP: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.INFESTATIONPIT: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.SPIRE: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.NYDUSNETWORK: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.NYDUSCANAL: {0: 4, 1: 4, 2: 4, 3: 4},
    UnitID.HIVE: {0: 32, 1: 30, 2: 28, 3: 27},
    UnitID.ULTRALISKCAVERN: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.GREATERSPIRE: {0: 13, 1: 12, 2: 12, 3: 11},
    UnitID.CREEPTUMOR: {0: 1, 1: 1, 2: 1, 3: 1},
    UnitID.CREEPTUMORBURROWED: {0: 1, 1: 1, 2: 1, 3: 1},
    UnitID.PROBE: {0: 2, 1: 2, 2: 1, 3: 1},
    UnitID.ZEALOT: {0: 5, 1: 4, 2: 4, 3: 4},
    UnitID.SENTRY: {0: 3, 1: 3, 2: 2, 3: 2},
    UnitID.STALKER: {0: 11, 1: 10, 2: 9, 3: 9},
    UnitID.ADEPT: {0: 5, 1: 4, 2: 4, 3: 4},
    UnitID.ADEPTPHASESHIFT: {0: 0, 1: 0, 2: 0, 3: 0},
    UnitID.HIGHTEMPLAR: {0: 3, 1: 3, 2: 2, 3: 2},
    UnitID.DARKTEMPLAR: {0: 4, 1: 4, 2: 3, 3: 3},
    UnitID.ARCHON: {0: 23, 1: 21, 2: 19, 3: 17},
    UnitID.IMMORTAL: {0: 20, 1: 19, 2: 17, 3: 16},
    UnitID.COLOSSUS: {0: 23, 1: 21, 2: 20, 3: 19},
    UnitID.DISRUPTOR: {0: 13, 1: 12, 2: 11, 3: 11},
    UnitID.SCV: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.MULE: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.MARINE: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.MARAUDER: {0: 9, 1: 8, 2: 8, 3: 7},
    UnitID.REAPER: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.GHOST: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.HELLION: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.HELLIONTANK: {0: 4, 1: 4, 2: 4, 3: 4},
    UnitID.WIDOWMINE: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.WIDOWMINEBURROWED: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.SIEGETANK: {0: 12, 1: 11, 2: 11, 3: 10},
    UnitID.SIEGETANKSIEGED: {0: 12, 1: 11, 2: 11, 3: 10},
    UnitID.CYCLONE: {0: 8, 1: 8, 2: 8, 3: 7},
    UnitID.THOR: {0: 27, 1: 25, 2: 24, 3: 23},
    UnitID.VIKINGASSAULT: {0: 8, 1: 8, 2: 7, 3: 7},
    UnitID.VIKINGFIGHTER: {0: 8, 1: 8, 2: 7, 3: 7},
    UnitID.DRONE: {0: 2, 1: 2, 2: 1, 3: 1},
    UnitID.QUEEN: {0: 12, 1: 11, 2: 11, 3: 10},
    UnitID.ZERGLING: {0: 1, 1: 1, 2: 1, 3: 1},
    UnitID.BANELING: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.BANELINGCOCOON: {0: 4, 1: 4, 2: 4, 3: 3},
    UnitID.ROACH: {0: 10, 1: 10, 2: 9, 3: 9},
    UnitID.RAVAGER: {0: 9, 1: 8, 2: 8, 3: 7},
    UnitID.RAVAGERCOCOON: {0: 10, 1: 9, 2: 8, 3: 8},
    UnitID.HYDRALISK: {0: 3, 1: 3, 2: 3, 3: 3},
    UnitID.LURKERMP: {0: 14, 1: 13, 2: 12, 3: 12},
    UnitID.LURKEREGG: {0: 7, 1: 7, 2: 6, 3: 6},
    UnitID.INFESTOR: {0: 6, 1: 6, 2: 6, 3: 5},
    UnitID.SWARMHOSTMP: {0: 11, 1: 11, 2: 10, 3: 9},
    UnitID.LOCUSTMP: {0: 2, 1: 2, 2: 2, 3: 2},
    UnitID.ULTRALISK: {0: 36, 1: 34, 2: 32, 3: 30},
    UnitID.BROODLING: {0: 1, 1: 1, 2: 1, 3: 1},
    UnitID.LARVA: {0: 1, 1: 1, 2: 1, 3: 1},
    UnitID.EGG: {0: 34, 1: 26, 2: 21, 3: 17},
}
