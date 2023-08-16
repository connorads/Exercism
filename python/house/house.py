"""Recite the nursery rhyme 'This is the House that Jack Built'."""

PARTS = (
    "the house that Jack built.",
    "the malt that lay in ",
    "the rat that ate ",
    "the cat that killed ",
    "the dog that worried ",
    "the cow with the crumpled horn that tossed ",
    "the maiden all forlorn that milked ",
    "the man all tattered and torn that kissed ",
    "the priest all shaven and shorn that married ",
    "the rooster that crowed in the morn that woke ",
    "the farmer sowing his corn that kept ",
    "the horse and the hound and the horn that belonged to ",
)


def get(verse: int) -> str:
    """Return the verse for the given verse number.

    The verse number is 1-based.
    """
    return "This is " + "".join([PARTS[i] for i in range(verse - 1, -1, -1)])


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme from start_verse to end_verse.

    The verse numbers are 1-based.
    """
    return [get(verse) for verse in range(start_verse, end_verse + 1)]
