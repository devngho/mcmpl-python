from enum import Enum


class EventType(Enum):
    BlockBreakEvent = "BlockBreakEvent"
    BlockBurnEvent = "BlockBurnEvent"
    BlockCanBuildEvent = "BlockCanBuildEvent"

    PlayerJoinEvent = "PlayerJoinEvent"
    PlayerQuitEvent = "PlayerQuitEvent"
