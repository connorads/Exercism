export const hey = message => {
  const silence = message.trim() == "";

  if (silence) {
    return "Fine. Be that way!";
  }

  const yelling = message == message.toUpperCase() && message.match(/[a-z]/i);
  const question = message.trimEnd().endsWith("?");

  if (question && yelling) {
    return "Calm down, I know what I'm doing!";
  } else if (question) {
    return "Sure.";
  } else if (!question && yelling) {
    return "Whoa, chill out!";
  } else {
    return "Whatever.";
  }
};
