from pyrogram import filters, filters2
from typing import List, Union
from config import COMMAND_PREFIXES


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

def commandpro(commands: Union[str, List[str]], prefixes: Union[str, List[str]] = "ح ع ر ب م",  case_sensitive: bool = False):
    return filters.command(commands, "ح" , "ع", "ر", "ب", "م")


