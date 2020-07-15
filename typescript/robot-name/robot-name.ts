const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbers = "0123456789";
const char = () => chars.charAt(Math.floor(Math.random() * chars.length));
const number = () => numbers.charAt(Math.floor(Math.random() * numbers.length));
const name = () => `${char()}${char()}${number()}${number()}${number()}`;

class RobotName {
  private readonly usedNames = new Set<string>();
  private _name!: string;

  constructor() {
    this.setName(name());
  }

  get name() {
    return this._name;
  }

  private setName(name: string) {
    this.usedNames.add(name);
    this._name = name;
  }

  resetName = () => {
    const newName = name();
    if (this.usedNames.has(newName)) {
      this.resetName();
    } else {
      this.setName(newName);
    }
  };
}

export default RobotName;
