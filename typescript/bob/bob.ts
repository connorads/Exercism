const silence = (message: string): boolean => message.trim() === "";
const question = (message: string): boolean => message.trimEnd().endsWith("?");
const yelling = (message: string): boolean =>
  message === message.toUpperCase() && message.match(/[a-z]/i) ? true : false;

class Bob {
  hey = (message: string) => {
    if (silence(message)) {
      return "Fine. Be that way!";
    } else if (question(message) && yelling(message)) {
      return "Calm down, I know what I'm doing!";
    } else if (question(message)) {
      return "Sure.";
    } else if (!question(message) && yelling(message)) {
      return "Whoa, chill out!";
    } else {
      return "Whatever.";
    }
  };
}

export default Bob;
