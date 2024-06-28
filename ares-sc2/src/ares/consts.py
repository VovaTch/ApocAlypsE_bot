"""Keep constants here for ease of use."""
from enum import Enum, auto
from typing import List, Set

from sc2.data import Race
from sc2.ids.effect_id import EffectId
from sc2.ids.unit_typeid import UnitTypeId as UnitID

"""Strings"""
# general/config
ACTIVE_GRID: str = "ActiveGrid"
AIR: str = "Air"
AIR_AVOIDANCE: str = "AirAvoidance"
AIR_COST: str = "AirCost"
AIR_RANGE: str = "AirRange"
AIR_VS_GROUND: str = "AirVsGround"
ATTACK_DISENGAGE_FURTHER_THAN: str = "AttackDisengageIfTargetFurtherThan"
ATTACK_ENGAGE_CLOSER_THAN: str = "AttackEngageIfTargetCloserThan"
BLINDING_CLOUD: str = "BlindingCloud"
BOOST_BACK_TO_TOWNHALL: str = "BoostBackToTownHall"
BUILD_CHOICES: str = "BuildChoices"
BUILDS: str = "Builds"
CHAT_DEBUG: str = "ChatDebug"
COMBAT: str = "Combat"
CONFIG_FILE: str = "config.yml"
CORROSIVE_BILE: str = "CorrosiveBile"
COST: str = "Cost"
COST_MULTIPLIER: str = "CostMultiplier"
CYCLE: str = "Cycle"
DANGER_THRESHOLD: str = "DangerThreshold"
DANGER_TILES: str = "DangerTiles"
DISTANCES: str = "Distances"
DEBUG: str = "Debug"
DEBUG_GAME_STEP: str = "DebugGameStep"
DEBUG_OPTIONS: str = "DebugOptions"
EFFECTS: str = "Effects"
EFFECTS_RANGE_BUFFER: str = "EffectsRangeBuffer"
FLYING_ENEMY_LEAVING_BASES: str = "FlyingEnemyLeavingBases"
FLYING_ENEMY_NEAR_BASES: str = "FlyingEnemyNearBases"
GAME_STEP: str = "GameStep"
GROUND: str = "Ground"
GROUND_AVOIDANCE: str = "GroundAvoidance"
GROUND_COST: str = "GroundCost"
GROUND_ENEMY_LEAVING_BASES: str = "GroundEnemyLeavingBases"
GROUND_ENEMY_NEAR_BASES: str = "GroundEnemyNearBases"
GROUND_RANGE: str = "GroundRange"
GROUND_TO_AIR: str = "GroundToAir"
KD8_CHARGE: str = "KD8Charge"
LIBERATOR_ZONE: str = "LiberatorZone"
LURKER_SPINE: str = "LurkerSpine"
MINERAL_BOOST: str = "MineralBoost"
MINERAL_DISTANCE_FACTOR: str = "MineralDistanceFactor"
MINERAL_STACKING: str = "MineralStacking"
MINING: str = "Mining"
NUKE: str = "Nuke"
OPENING_BUILD_ORDER: str = "OpeningBuildOrder"
ORACLE: str = "Oracle"
PARASITIC_BOMB: str = "ParasiticBomb"
PATHING: str = "Pathing"
PATHING_GRID: str = "PathingGrid"
PLACEMENT: str = "Placement"
RANGE: str = "Range"
RANGE_BUFFER: str = "RangeBuffer"
RESOURCE_DEBUG: str = "ResourceDebug"
SHADE_COMMENCED: str = "SHADE_COMMENCED"
SHADE_OWNER: str = "SHADE_OWNER"
SHOW_BUILDING_FORMATION: str = "ShowBuildingFormation"
SHOW_PATHING_COST: str = "ShowPathingCost"
STORM: str = "Storm"
STRATEGY_MANAGER: str = "StrategyManager"
TOWNHALL_DISTANCE_FACTOR: str = "TownhallDistanceFactor"
UNIT_CONTROL: str = "UnitControl"
UNIT_SQUADS: str = "UnitSquads"
UNITS: str = "Units"
USE_DATA: str = "UseData"
WORKER_ON_ROUTE_TIMEOUT: str = "WorkerOnRouteTimeout"

# building manager
BUILDING: str = "Building"
BUILDING_PURPOSE: str = "building_purpose"
CANCEL_ORDER: str = "CancelOrder"
ID: str = "id"
STRUCTURE_ORDER_COMPLETE: str = "structure_order_complete"
TARGET: str = "target"
TIME_ORDER_COMMENCED: str = "time_order_commenced"

# build runner / resource_manager
GAS: str = "gas"
MINERAL: str = "mineral"
NAT: str = "NAT"
PROXY: str = "PROXY"
THIRD: str = "THIRD"

# data manager
DATA_DIR: str = "./data"
DURATION: str = "Duration"
LOSS: str = "Loss"
RACE: str = "EnemyRace"
RESULT: str = "Result"
STRATEGY_USED: str = "StrategyUsed"
TEST_OPPONENT_ID: str = "test_123"
TIE: str = "Tie"
WIN: str = "Win"

# main
ADD_SHADES_ON_FRAME: int = (
    120  #: The frame at which point Adept Shades are treated as units
)
BANNED_PHRASES: List[str] = [
    "COCOON",
    "EGG",
    "CHANGELING",
    "FLYING",
    "PHASE",
]  #: UnitTypeIds with these words in them have Cost issues
SHADE_DURATION: int = 160  #: how long a Shade lasts in frames


# pathing manager
AIR_VS_GROUND_DEFAULT: int = 10

# terrain manager
CURIOUS: str = "CURIOUS"
GLITTERING: str = "GLITTERING"
OXIDE: str = "OXIDE"
LIGHTSHADE: str = "LIGHTSHADE"

# unit memory manager
MAX_SNAPSHOTS_PER_UNIT: int = 10

# chat debug
COOLDOWN: Set[str] = {"COOLDOWN"}
CREATE: Set[str] = {"CREATE", "MAKE"}
FOOD: Set[str] = {"FOOD", "SUPPLY"}
GOD: Set[str] = {"GOD"}
KILL: Set[str] = {"DESTROY", "KILL"}
RESOURCES: Set[str] = {"RESOURCES", "MONEY"}
SHOW_MAP: Set[str] = {"REVEAL", "SHOW", "SHOW-MAP"}
TECH_TREE: Set[str] = {"TECH", "TECH-TREE"}
UPGRADES: Set[str] = {"UPGRADES"}

"""Enums"""


class BuildingSize(str, Enum):
    FIVE_BY_FIVE = "FIVE_BY_FIVE"
    THREE_BY_THREE = "THREE_BY_THREE"
    TWO_BY_TWO = "TWO_BY_TWO"


class BuildOrderOptions(str, Enum):
    ADDONSWAP = "ADDONSWAP"
    CHRONO = "CHRONO"
    CORE = "CORE"
    GAS = "GAS"
    GATE = "GATE"
    EXPAND = "EXPAND"
    ORBITAL = "ORBITAL"
    OVERLORD_SCOUT = "OVERLORD_SCOUT"
    SUPPLY = "SUPPLY"
    WORKER = "WORKER"
    WORKER_SCOUT = "WORKER_SCOUT"

    @classmethod
    def contains_key(cls, name):
        return name in cls.__members__


class BuildOrderTargetOptions(str, Enum):
    ENEMY_FOURTH = "ENEMY_FOURTH"
    ENEMY_NAT = "ENEMY_NAT"
    ENEMY_NAT_HG_SPOT = "ENEMY_NAT_HG_SPOT"
    ENEMY_NAT_VISION = "ENEMY_NAT_VISION"
    ENEMY_RAMP = "ENEMY_RAMP"
    ENEMY_SPAWN = "ENEMY_SPAWN"
    ENEMY_THIRD = "ENEMY_THIRD"
    FIFTH = "FIFTH"
    FOURTH = "FOURTH"
    MAP_CENTER = "MAP_CENTER"
    NAT = "NAT"
    RAMP = "RAMP"
    SIXTH = "SIXTH"
    SPAWN = "SPAWN"
    THIRD = "THIRD"

    @classmethod
    def contains_key(cls, name):
        return name in cls.__members__

    @classmethod
    def list_options(cls):
        options = [member.value for role, member in cls.__members__.items()]
        return options


class BuildingPurpose(Enum):
    """Populate this with reasons a building was built."""

    NORMAL_BUILDING = auto()


class EngagementResult(int, Enum):
    """Possible engagement results."""

    VICTORY_EMPHATIC = 10
    VICTORY_OVERWHELMING = 9
    VICTORY_DECISIVE = 8
    VICTORY_CLOSE = 7
    VICTORY_MARGINAL = 6
    TIE = 5
    LOSS_MARGINAL = 4
    LOSS_CLOSE = 3
    LOSS_DECISIVE = 2
    LOSS_OVERWHELMING = 1
    LOSS_EMPHATIC = 0


class ManagerRequestType(str, Enum):
    """Populate this with manager requests."""

    # AbilityTrackerManager
    GET_UNIT_TO_ABILITY_DICT = "GET_UNIT_TO_ABILITY_DICT"
    UPDATE_ABILITY_COOLDOWN = "UPDATE_ABILITY_COOLDOWN"
    UPDATE_UNIT_TO_ABILITY_DICT = "UPDATE_UNIT_TO_ABILITY_DICT"

    # BuildingManager
    BUILD_WITH_SPECIFIC_WORKER = "BUILD_WITH_SPECIFIC_WORKER"
    CANCEL_STRUCTURE = "CANCEL_STRUCTURE"
    GET_BUILDING_COUNTER = "GET_BUILDING_COUNTER"
    GET_BUILDING_TRACKER_DICT = "GET_BUILDING_TRACKER_DICT"

    # CombatSimManager
    CAN_WIN_FIGHT = "CAN_WIN_FIGHT"

    # DataManager
    GET_CHOSEN_OPENING = "GET_CHOSEN_OPENING"

    # EnemyToBaseManager
    GET_FLYING_ENEMY_NEAR_BASES = "GET_FLYING_ENEMY_NEAR_BASES"
    GET_GROUND_ENEMY_NEAR_BASES = "GET_GROUND_ENEMY_NEAR_BASES"
    GET_MAIN_AIR_THREATS_NEAR_TOWNHALL = "GET_MAIN_AIR_THREATS_NEAR_TOWNHALL"
    GET_MAIN_GROUND_THREATS_NEAR_TOWNHALL = "GET_MAIN_GROUND_THREATS_NEAR_TOWNHALL"
    GET_TH_TAG_WITH_LARGEST_GROUND_THREAT = "GET_TH_TAG_WITH_LARGEST_GROUND_THREAT"

    # FlyingStructureManager
    GET_FLYING_STRUCTURE_TRACKER = "GET_FLYING_STRUCTURE_TRACKER"
    MOVE_STRUCTURE = "MOVE_STRUCTURE"

    # PathManager
    FIND_LOW_PRIORITY_PATH = "FIND_LOW_PRIORITY_PATH"
    FIND_LOWEST_COST_POINTS = "FIND_LOWEST_COST_POINTS"
    FIND_RAW_PATH = "FIND_RAW_PATH"
    GET_AIR_AVOIDANCE_GRID = "GET_AIR_AVOIDANCE_GRID"
    GET_AIR_GRID = "GET_AIR_GRID"
    GET_AIR_VS_GROUND_GRID = "GET_AIR_VS_GROUND_GRID"
    GET_CACHED_GROUND_GRID = "GET_CACHED_GROUND_GRID"
    GET_CLIMBER_GRID = "GET_CLIMBER_GRID"
    GET_CLOSEST_SAFE_SPOT = "GET_CLOSEST_SAFE_SPOT"
    GET_FORCEFIELD_POSITIONS = "GET_FORCEFIELD_POSITIONS"
    GET_GROUND_AVOIDANCE_GRID = "GET_GROUND_AVOIDANCE_GRID"
    GET_GROUND_GRID = "GET_GROUND_GRID"
    GET_GROUND_TO_AIR_GRID = "GET_GROUND_TO_AIR_GRID"
    GET_MAP_DATA = "GET_MAP_DATA"
    GET_PRIORITY_GROUND_AVOIDANCE_GRID = "GET_PRIORITY_GROUND_AVOIDANCE_GRID"
    GET_WHOLE_MAP_ARRAY = "GET_WHOLE_MAP_ARRAY"
    GET_WHOLE_MAP_TREE = "GET_WHOLE_MAP_TREE"
    IS_POSITION_SAFE = "IS_POSITION_SAFE"
    NEIGHBOURING_TILES_ARE_INPATHABLE = "NEIGHBOURING_TILES_ARE_INPATHABLE"
    PATH_NEXT_POINT = "PATH_NEXT_POINT"

    # PlacementManager
    CAN_PLACE_STRUCTURE = "CAN_PLACE_STRUCTURE"
    REQUEST_BUILDING_PLACEMENT = "REQUEST_BUILDING_PLACEMENT"
    REQUEST_WARP_IN = "REQUEST_WARP_IN_SPOT"

    # ResourceManager
    GET_MINERAL_PATCH_TO_LIST_OF_WORKERS = "GET_MINERAL_PATCH_TO_LIST_OF_WORKERS"
    GET_MINERAL_TARGET_DICT = "GET_MINERAL_TARGET_DICT"
    GET_NUM_AVAILABLE_MIN_PATCHES = "GET_NUM_AVAILABLE_MIN_PATCHES"
    GET_WORKER_TAG_TO_TOWNHALL_TAG = "GET_WORKER_TAG_TO_TOWNHALL_TAG"
    GET_WORKER_TO_GAS_BUILDING_DICT = "GET_WORKER_TO_GAS_BUILDING_DICT"
    GET_WORKER_TO_MINERAL_PATCH_DICT = "GET_WORKER_TO_MINERAL_PATCH_DICT"
    REMOVE_GAS_BUILDING = "REMOVE_GAS_BUILDING"
    REMOVE_MINERAL_FIELD = "REMOVE_MINERAL_FIELD"
    REMOVE_WORKER_FROM_MINERAL = "REMOVE_WORKER_FROM_MINERAL"
    SELECT_WORKER = "SELECT_WORKER"
    SET_WORKERS_PER_GAS = "SET_WORKERS_PER_GAS"

    # SquadManager
    GET_POSITION_OF_MAIN_SQUAD = "GET_POSITION_OF_MAIN_SQUAD"
    GET_SQUADS = "GET_SQUADS"
    REMOVE_TAG_FROM_SQUADS = "REMOVE_TAG_FROM_SQUADS"

    # TerrainManager
    BUILDING_POSITION_BLOCKED_BY_BURROWED_UNIT = (
        "BUILDING_POSITION_BLOCKED_BY_BURROWED_UNIT"
    )
    GET_BEHIND_MINERAL_POSITIONS = "GET_BEHIND_MINERAL_POSITIONS"
    GET_CLOSEST_OVERLORD_SPOT = "GET_CLOSEST_OVERLORD_SPOT"
    GET_DEFENSIVE_THIRD = "GET_DEFENSIVE_THIRD"
    GET_ENEMY_EXPANSIONS = "GET_ENEMY_EXPANSIONS"
    GET_ENEMY_FOURTH = "GET_ENEMY_FOURTH"
    GET_ENEMY_NAT = "GET_ENEMY_NAT"
    GET_ENEMY_RAMP = "GET_ENEMY_RAMP"
    GET_ENEMY_THIRD = "GET_ENEMY_THIRD"
    GET_FLOOD_FILL_AREA = "GET_FLOOD_FILL_AREA"
    GET_INITIAL_PATHING_GRID = "GET_INITIAL_PATHING_GRID"
    GET_IS_FREE_EXPANSION = "GET_IS_FREE_EXPANSION"
    GET_MAP_CHOKE_POINTS = "GET_MAP_CHOKE_POINTS"
    GET_OL_SPOT_NEAR_ENEMY_NATURAL = "GET_OL_SPOT_NEAR_ENEMY_NATURAL"
    GET_OL_SPOTS = "GET_OL_SPOTS"
    GET_OWN_EXPANSIONS = "GET_OWN_EXPANSIONS"
    GET_OWN_NAT = "GET_OWN_NAT"
    GET_POSITIONS_BLOCKED_BY_BURROWED_ENEMY = "GET_POSITIONS_BLOCKED_BY_BURROWED_ENEMY"

    # UnitCacheManager
    GET_CACHED_ENEMY_ARMY = "GET_CACHED_ENEMY_ARMY"
    GET_ENEMY_ARMY_CENTER_MASS = "GET_ENEMY_ARMY_CENTER_MASS"
    GET_CACHED_ENEMY_ARMY_DICT = "GET_CACHED_ENEMY_ARMY_DICT"
    GET_CACHED_ENEMY_WORKERS = "GET_CACHED_ENEMY_WORKERS"
    GET_OLD_OWN_ARMY_DICT = "GET_OLD_OWN_ARMY_DICT"
    GET_CACHED_OWN_ARMY = "GET_CACHED_OWN_ARMY"
    GET_CACHED_OWN_ARMY_DICT = "GET_CACHED_OWN_ARMY_DICT"
    GET_OWN_UNIT_COUNT = "GET_OWN_UNIT_COUNT"
    GET_OWN_STRUCTURES_DICT = "GET_OWN_STRUCTURES_DICT"
    GET_UNITS_FROM_TAGS = "GET_UNITS_FROM_TAGS"
    GET_REMOVED_UNITS = "GET_REMOVED_UNITS"

    # UnitMemoryManager
    GET_ALL_ENEMY = "GET_ALL_ENEMY"
    GET_ENEMY_GROUND = "GET_ENEMY_GROUND"
    GET_ENEMY_FLIERS = "GET_ENEMY_FLIERS"
    GET_ENEMY_TREE = "GET_ENEMY_TREE"
    GET_OWN_TREE = "GET_OWN_TREE"
    GET_UNITS_IN_RANGE = "GET_UNITS_IN_RANGE"

    # UnitRoleManager
    ASSIGN_ROLE = "ASSIGN_ROLE"
    BATCH_ASSIGN_ROLE = "BATCH_ASSIGN_ROLE"
    CLEAR_ROLE = "CLEAR_ROLE"
    GET_ALL_FROM_ROLES_EXCEPT = "GET_ALL_FROM_ROLES_EXCEPT"
    GET_UNIT_ROLE_DICT = "GET_UNIT_ROLE_DICT"
    GET_UNITS_FROM_ROLE = "GET_UNITS_FROM_ROLE"
    GET_UNITS_FROM_ROLES = "GET_UNITS_FROM_ROLES"
    SWITCH_ROLES = "SWITCH_ROLES"


class ManagerName(str, Enum):
    """The names of the various managers."""

    ABILITY_TRACKER_MANAGER = "AbilityTrackerManager"
    BUILDING_MANAGER = "BuildingManager"
    COMBAT_SIM_MANAGER = "CombatSimManager"
    DATA_MANAGER = "DataManager"
    ENEMY_TO_BASE_MANAGER = "EnemyToBaseManager"
    FLYING_STRUCTURE_MANAGER = "FlyingStructureManager"
    PATH_MANAGER = "PathManager"
    PLACEMENT_MANAGER = "PlacementManager"
    RESOURCE_MANAGER = "ResourceManager"
    SQUAD_MANAGER = "SquadManager"
    TERRAIN_MANAGER = "TerrainManager"
    UNIT_CACHE_MANAGER = "UnitCacheManager"
    UNIT_MEMORY_MANAGER = "UnitMemoryManager"
    UNIT_ROLE_MANAGER = "UnitRoleManager"


class UnitRole(str, Enum):
    """Roles for units"""

    ATTACKING = "ATTACKING"
    # the main attacking squad on the map
    ATTACKING_MAIN_SQUAD = "ATTACKING_MAIN_SQUAD"
    # units that require transporting to battlefield (medivac / bio for example)
    ATTACKING_TRANSPORT_SQUAD = "ATTACKING_TRANSPORT_SQUAD"
    BASE_DEFENDER = "BASE_DEFENDER"  # units split off to defend expansions
    BASE_BLOCKER = "BASE_BLOCKER"  # blocking an enemy base
    BUILDING = "BUILDING"  # workers that have been assigned to create a building
    DEFENDING = "DEFENDING"  # units in a combat zone near one of our bases
    DROP_SHIP = "DROP_SHIP"  # medivacs / prism/ dropperlord
    DROP_UNITS_ATTACKING = (
        "DROP_UNITS_ATTACKING"  # units dropped off, that now need to attack
    )
    DROP_UNITS_TO_LOAD = "DROP_UNITS_TO_LOAD"  # units that require picking up
    # reserved roles for flanking
    FLANK_GROUP_ONE = "FLANK_GROUP_ONE"
    FLANK_GROUP_TWO = "FLANK_GROUP_TWO"
    FLANK_GROUP_THREE = "FLANK_GROUP_THREE"
    GATHERING = "GATHERING"  # workers that are mining
    HARASSING = "HARASSING"  # units that are harassing
    IDLE = "IDLE"  # not doing anything
    MAP_CONTROL = "MAP_CONTROL"  # units controlling the map (lings/hellions?)
    OFFENSIVE_REPAIR = "OFFENSIVE_REPAIR"  # with the main force
    OVERLORD_HUNTER = "OVERLORD_HUNTER"  # units looking for overlords
    PERSISTENT_BUILDER = "PERSISTENT_BUILDER"  # does not get reassigned automatically
    PROXY_WORKER = "PROXY_WORKER"
    REPAIRING = "REPAIRING"  # repairing scvs
    SCOUTING = "SCOUTING"
    SURROUNDING = "SURROUNDING"  # units currently in a surround
    UNDER_REPAIR = "UNDER_REPAIR"  # units currently under repair
    # control groups, use for anything not specified
    CONTROL_GROUP_ONE = "CONTROL_GROUP_ONE"
    CONTROL_GROUP_TWO = "CONTROL_GROUP_TWO"
    CONTROL_GROUP_THREE = "CONTROL_GROUP_THREE"
    CONTROL_GROUP_FOUR = "CONTROL_GROUP_FOUR"
    CONTROL_GROUP_FIVE = "CONTROL_GROUP_FIVE"
    CONTROL_GROUP_SIX = "CONTROL_GROUP_SIX"
    CONTROL_GROUP_SEVEN = "CONTROL_GROUP_SEVEN"
    CONTROL_GROUP_EIGHT = "CONTROL_GROUP_EIGHT"
    CONTROL_GROUP_NINE = "CONTROL_GROUP_NINE"
    # reserved for build order runner, use at your own risk :D
    BUILD_RUNNER_SCOUT = "BUILD_RUNNER_SCOUT"


class UnitTreeQueryType(str, Enum):
    """Identifiers for which unit trees to query for UnitMemoryManager"""

    AllOwn = "AllOwn"
    AllEnemy = "AllEnemy"
    EnemyFlying = "EnemyFlying"
    EnemyGround = "EnemyGround"


"""Sets"""
ADD_ONS: dict[UnitID, UnitID] = {
    UnitID.BARRACKSREACTOR: UnitID.BARRACKS,
    UnitID.FACTORYREACTOR: UnitID.FACTORY,
    UnitID.STARPORTREACTOR: UnitID.STARPORT,
    UnitID.BARRACKSTECHLAB: UnitID.BARRACKS,
    UnitID.FACTORYTECHLAB: UnitID.FACTORY,
    UnitID.STARPORTTECHLAB: UnitID.STARPORT,
}

ALL_PRODUCTION_STRUCTURES: Set[UnitID] = {
    UnitID.BARRACKS,
    UnitID.FACTORY,
    UnitID.STARPORT,
    UnitID.GATEWAY,
    UnitID.WARPGATE,
    UnitID.ROBOTICSFACILITY,
    UnitID.STARGATE,
}

ALL_STRUCTURES: Set[UnitID] = {
    UnitID.ARMORY,
    UnitID.ASSIMILATOR,
    UnitID.ASSIMILATORRICH,
    UnitID.AUTOTURRET,
    UnitID.BANELINGNEST,
    UnitID.BARRACKS,
    UnitID.BARRACKSFLYING,
    UnitID.BARRACKSREACTOR,
    UnitID.BARRACKSTECHLAB,
    UnitID.BUNKER,
    UnitID.BYPASSARMORDRONE,
    UnitID.COMMANDCENTER,
    UnitID.COMMANDCENTERFLYING,
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORBURROWED,
    UnitID.CREEPTUMORQUEEN,
    UnitID.CYBERNETICSCORE,
    UnitID.DARKSHRINE,
    UnitID.ELSECARO_COLONIST_HUT,
    UnitID.ENGINEERINGBAY,
    UnitID.EVOLUTIONCHAMBER,
    UnitID.EXTRACTOR,
    UnitID.EXTRACTORRICH,
    UnitID.FACTORY,
    UnitID.FACTORYFLYING,
    UnitID.FACTORYREACTOR,
    UnitID.FACTORYTECHLAB,
    UnitID.FLEETBEACON,
    UnitID.FORGE,
    UnitID.FUSIONCORE,
    UnitID.GATEWAY,
    UnitID.GHOSTACADEMY,
    UnitID.GREATERSPIRE,
    UnitID.HATCHERY,
    UnitID.HIVE,
    UnitID.HYDRALISKDEN,
    UnitID.INFESTATIONPIT,
    UnitID.LAIR,
    UnitID.LURKERDENMP,
    UnitID.MISSILETURRET,
    UnitID.NEXUS,
    UnitID.NYDUSCANAL,
    UnitID.NYDUSCANALATTACKER,
    UnitID.NYDUSCANALCREEPER,
    UnitID.NYDUSNETWORK,
    UnitID.ORACLESTASISTRAP,
    UnitID.ORBITALCOMMAND,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.PHOTONCANNON,
    UnitID.PLANETARYFORTRESS,
    UnitID.POINTDEFENSEDRONE,
    UnitID.PYLON,
    UnitID.PYLONOVERCHARGED,
    UnitID.RAVENREPAIRDRONE,
    UnitID.REACTOR,
    UnitID.REFINERY,
    UnitID.REFINERYRICH,
    UnitID.RESOURCEBLOCKER,
    UnitID.ROACHWARREN,
    UnitID.ROBOTICSBAY,
    UnitID.ROBOTICSFACILITY,
    UnitID.SENSORTOWER,
    UnitID.SHIELDBATTERY,
    UnitID.SPAWNINGPOOL,
    UnitID.SPINECRAWLER,
    UnitID.SPINECRAWLERUPROOTED,
    UnitID.SPIRE,
    UnitID.SPORECRAWLER,
    UnitID.SPORECRAWLERUPROOTED,
    UnitID.STARGATE,
    UnitID.STARPORT,
    UnitID.STARPORTFLYING,
    UnitID.STARPORTREACTOR,
    UnitID.STARPORTTECHLAB,
    UnitID.SUPPLYDEPOT,
    UnitID.SUPPLYDEPOTLOWERED,
    UnitID.TECHLAB,
    UnitID.TEMPLARARCHIVE,
    UnitID.TWILIGHTCOUNCIL,
    UnitID.ULTRALISKCAVERN,
    UnitID.WARPGATE,
}

BURROWED_ALIAS: Set[UnitID] = {
    UnitID.BANELINGBURROWED,
    UnitID.CREEPTUMORBURROWED,
    UnitID.DRONEBURROWED,
    UnitID.HYDRALISKBURROWED,
    UnitID.INFESTORBURROWED,
    UnitID.INFESTORTERRANBURROWED,
    UnitID.LURKERMPBURROWED,
    UnitID.QUEENBURROWED,
    UnitID.RAVAGERBURROWED,
    UnitID.ROACHBURROWED,
    UnitID.SWARMHOSTBURROWEDMP,
    UnitID.ULTRALISKBURROWED,
    UnitID.WIDOWMINEBURROWED,
    UnitID.ZERGLINGBURROWED,
}

CHANGELING_TYPES: Set[UnitID] = {
    UnitID.CHANGELING,
    UnitID.CHANGELINGZERGLING,
    UnitID.CHANGELINGZERGLINGWINGS,
    UnitID.CHANGELINGMARINE,
    UnitID.CHANGELINGMARINESHIELD,
    UnitID.CHANGELINGZEALOT,
}

CREEP_TUMOR_TYPES: Set[UnitID] = {
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORQUEEN,
    UnitID.CREEPTUMORBURROWED,
}

DETECTORS: Set[UnitID] = {
    UnitID.OBSERVER,
    UnitID.OBSERVERSIEGEMODE,
    UnitID.PHOTONCANNON,
    UnitID.RAVEN,
    UnitID.MISSILETURRET,
    EffectId.SCANNERSWEEP,
    UnitID.OVERSEER,
    UnitID.OVERSEERSIEGEMODE,
    UnitID.SPORECRAWLER,
}

DROP_ROLES: set[UnitRole] = {
    UnitRole.DROP_SHIP,
    UnitRole.DROP_UNITS_TO_LOAD,
    UnitRole.DROP_UNITS_ATTACKING,
}

EGG_BUTTON_NAMES: Set[str] = {"Drone", "Overlord"}

# we ignore these when detecting if an expansion location is blocked
FLYING_IGNORE: Set[UnitID] = {
    UnitID.OBSERVER,
    UnitID.OVERLORD,
    UnitID.OVERSEER,
    UnitID.BARRACKSFLYING,
    UnitID.COMMANDCENTERFLYING,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.FACTORYFLYING,
    UnitID.STARPORTFLYING,
    UnitID.PHOENIX,
}

GAS_BUILDINGS = {UnitID.ASSIMILATOR, UnitID.EXTRACTOR, UnitID.REFINERY}

GATEWAY_UNITS: set[UnitID] = {
    UnitID.ZEALOT,
    UnitID.ADEPT,
    UnitID.STALKER,
    UnitID.DARKTEMPLAR,
    UnitID.HIGHTEMPLAR,
}

# These are not really rocks, but end up in the destructible collection
IGNORE_DESTRUCTABLES: Set[UnitID] = {
    UnitID.INHIBITORZONESMALL,
    UnitID.INHIBITORZONEFLYINGLARGE,
    UnitID.INHIBITORZONEFLYINGMEDIUM,
    UnitID.INHIBITORZONEFLYINGLARGE,
    UnitID.INHIBITORZONELARGE,
    UnitID.INHIBITORZONEMEDIUM,
    UnitID.ACCELERATIONZONEFLYINGLARGE,
    UnitID.ACCELERATIONZONEFLYINGMEDIUM,
    UnitID.ACCELERATIONZONEFLYINGSMALL,
    UnitID.ACCELERATIONZONELARGE,
    UnitID.ACCELERATIONZONEMEDIUM,
    UnitID.ACCELERATIONZONESMALL,
    UnitID.CLEANINGBOT,
}

IGNORE_IN_COST_DICT: Set[UnitID] = {
    UnitID.BROODLING,
    UnitID.INTERCEPTOR,
    UnitID.LARVA,
    UnitID.LOCUSTMP,
    UnitID.LOCUSTMPFLYING,
    UnitID.MULE,
    UnitID.POINTDEFENSEDRONE,
    UnitID.INFESTEDTERRANSEGG,
    UnitID.INFESTEDTERRAN,
    UnitID.INFESTORBURROWED,
    UnitID.REFINERYRICH,
    UnitID.ASSIMILATORRICH,
    UnitID.EXTRACTORRICH,
}

IGNORED_UNIT_TYPES_MEMORY_MANAGER: Set[UnitID] = set()

# roles where most of our force is likely to be
MAIN_COMBAT_ROLES: Set[UnitRole] = {
    UnitRole.ATTACKING,
    UnitRole.DEFENDING,
}

TECHLAB_TYPES: set[UnitID] = {
    UnitID.BARRACKSTECHLAB,
    UnitID.FACTORYTECHLAB,
    UnitID.STARPORTTECHLAB,
    UnitID.TECHLAB,
}

TOWNHALL_TYPES: Set[UnitID] = {
    UnitID.HATCHERY,
    UnitID.LAIR,
    UnitID.HIVE,
    UnitID.COMMANDCENTER,
    UnitID.COMMANDCENTERFLYING,
    UnitID.ORBITALCOMMAND,
    UnitID.ORBITALCOMMANDFLYING,
    UnitID.PLANETARYFORTRESS,
    UnitID.NEXUS,
}

UNITS_TO_AVOID_TYPES: Set[UnitID] = {
    UnitID.CREEPTUMOR,
    UnitID.CREEPTUMORBURROWED,
    UnitID.CREEPTUMORQUEEN,
    UnitID.LURKERMPBURROWED,
    UnitID.INFESTORBURROWED,
    UnitID.ROACHBURROWED,
    UnitID.SPORECRAWLER,
}

UNITS_TO_IGNORE: Set[UnitID] = set()
UNIT_TYPES_WITH_NO_ROLE: Set[UnitID] = set()
ALL_WORKER_TYPES: Set[UnitID] = {
    UnitID.DRONE,
    UnitID.DRONEBURROWED,
    UnitID.MULE,
    UnitID.PROBE,
    UnitID.SCV,
}
WORKER_TYPES: Set[UnitID] = {UnitID.DRONE, UnitID.PROBE, UnitID.SCV}

RACE_SUPPLY: dict[Race, UnitID] = {
    Race.Protoss: UnitID.PYLON,
    Race.Terran: UnitID.SUPPLYDEPOT,
    Race.Zerg: UnitID.OVERLORD,
}

LOSS_EMPHATIC_OR_WORSE: Set[EngagementResult] = {EngagementResult.LOSS_EMPHATIC}

LOSS_OVERWHELMING_OR_WORSE: Set[EngagementResult] = LOSS_EMPHATIC_OR_WORSE | {
    EngagementResult.LOSS_OVERWHELMING
}

LOSS_DECISIVE_OR_WORSE: Set[EngagementResult] = LOSS_OVERWHELMING_OR_WORSE | {
    EngagementResult.LOSS_DECISIVE
}

LOSS_CLOSE_OR_WORSE: Set[EngagementResult] = LOSS_DECISIVE_OR_WORSE | {
    EngagementResult.LOSS_CLOSE
}

LOSS_MARGINAL_OR_WORSE: Set[EngagementResult] = LOSS_CLOSE_OR_WORSE | {
    EngagementResult.LOSS_MARGINAL
}

VICTORY_EMPHATIC_OR_BETTER: Set[EngagementResult] = {EngagementResult.VICTORY_EMPHATIC}

VICTORY_OVERWHELMING_OR_BETTER: Set[EngagementResult] = VICTORY_EMPHATIC_OR_BETTER | {
    EngagementResult.VICTORY_OVERWHELMING
}

VICTORY_DECISIVE_OR_BETTER: Set[EngagementResult] = VICTORY_OVERWHELMING_OR_BETTER | {
    EngagementResult.VICTORY_DECISIVE
}

VICTORY_CLOSE_OR_BETTER: Set[EngagementResult] = VICTORY_DECISIVE_OR_BETTER | {
    EngagementResult.VICTORY_CLOSE
}

VICTORY_MARGINAL_OR_BETTER: Set[EngagementResult] = VICTORY_CLOSE_OR_BETTER | {
    EngagementResult.VICTORY_MARGINAL
}