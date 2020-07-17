const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "0123456789";
const char = () => chars.charAt(Math.floor(Math.random() * chars.length));
const number = () => numbers.charAt(Math.floor(Math.random() * numbers.length));
const name = () => `${char()}${char()}${number()}${number()}${number()}`;
const usedNames = new Set<string>();
export const uniqueName = (): string => {
  const newName = name();
  if (usedNames.has(newName)) {
    return uniqueName();
  } else {
    usedNames.add(newName);
    return newName;
  }
};

class RobotName {
  private _name: string;

  constructor() {
    this._name = uniqueName();
  }

  get name() {
    return this._name;
  }

  resetName = () => {
    this._name = uniqueName();
  };
}

export default RobotName;
