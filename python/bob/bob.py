""" Functions for Bob's responses to conversation.

Bob is a lackadaisical teenager. He likes to think that he's very cool. 
And he definitely doesn't get excited about things. That wouldn't be cool.
"""


def response(hey_bob: str) -> str:
    """Get a response from Bob.

    :param hey_bob: str - message to Bob.
    :return: str - Bob's response.
    """
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob.isupper() and hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.endswith("?"):
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
