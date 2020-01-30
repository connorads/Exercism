export const hey = message => {
  const yelling = message == message.toUpperCase() && message.match(/[a-z]/i);
  const silence = message.trim() == "";
  const question = message.trimEnd().endsWith("?");

  if (silence) {
    return "Fine. Be that way!";
  } else if (question) {
    if (yelling) {
      return "Calm down, I know what I'm doing!";
    } else {
      return "Sure.";
    }
  } else {
    if (yelling) {
      return "Whoa, chill out!";
    } else {
      return "Whatever.";
    }
  }
};
