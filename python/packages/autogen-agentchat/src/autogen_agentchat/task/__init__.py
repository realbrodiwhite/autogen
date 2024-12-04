from typing import AsyncGenerator, TypeVar

from typing_extensions import deprecated

from ..base import Response, TaskResult
from ..conditions import (
    ExternalTermination as ExternalTerminationAlias,
)
from ..conditions import (
    HandoffTermination as HandoffTerminationAlias,
)
from ..conditions import (
    MaxMessageTermination as MaxMessageTerminationAlias,
)
from ..conditions import (
    SourceMatchTermination as SourceMatchTerminationAlias,
)
from ..conditions import (
    StopMessageTermination as StopMessageTerminationAlias,
)
from ..conditions import (
    TextMentionTermination as TextMentionTerminationAlias,
)
from ..conditions import (
    TimeoutTermination as TimeoutTerminationAlias,
)
from ..conditions import (
    TokenUsageTermination as TokenUsageTerminationAlias,
)
from ..messages import AgentMessage
from ..ui import Console as ConsoleAlias


@deprecated("Moved to autogen_agentchat.terminations.ExternalTermination. Will remove this in 0.4.0.", stacklevel=2)
class ExternalTermination(ExternalTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.HandoffTermination. Will remove this in 0.4.0.", stacklevel=2)
class HandoffTermination(HandoffTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.MaxMessageTermination. Will remove this in 0.4.0.", stacklevel=2)
class MaxMessageTermination(MaxMessageTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.SourceMatchTermination. Will remove this in 0.4.0.", stacklevel=2)
class SourceMatchTermination(SourceMatchTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.StopMessageTermination. Will remove this in 0.4.0.", stacklevel=2)
class StopMessageTermination(StopMessageTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.TextMentionTermination. Will remove this in 0.4.0.", stacklevel=2)
class TextMentionTermination(TextMentionTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.TimeoutTermination. Will remove this in 0.4.0.", stacklevel=2)
class TimeoutTermination(TimeoutTerminationAlias): ...


@deprecated("Moved to autogen_agentchat.terminations.TokenUsageTermination. Will remove this in 0.4.0.", stacklevel=2)
class TokenUsageTermination(TokenUsageTerminationAlias): ...


T = TypeVar("T", bound=TaskResult | Response)


@deprecated("Moved to autogen_agentchat.ui.Console. Will remove this in 0.4.0.", stacklevel=2)
async def Console(
    stream: AsyncGenerator[AgentMessage | T, None],
    *,
    no_inline_images: bool = False,
) -> T:
    return await ConsoleAlias(stream, no_inline_images=no_inline_images)


__all__ = [
    "MaxMessageTermination",
    "TextMentionTermination",
    "StopMessageTermination",
    "TokenUsageTermination",
    "HandoffTermination",
    "TimeoutTermination",
    "ExternalTermination",
    "SourceMatchTermination",
    "Console",
]
