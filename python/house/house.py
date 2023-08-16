"""Recite the nursery rhyme 'This is the House that Jack Built'."""

NOUNS = (
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


def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the nursery rhyme from start_verse to end_verse."""
    nursery_rhyme: list[str] = []
    for verse_n in range(start_verse - 1, end_verse):
        verse = "This is "
        for noun_n in range(verse_n, -1, -1):
            verse += NOUNS[noun_n]
        nursery_rhyme.append(verse)
    return nursery_rhyme
