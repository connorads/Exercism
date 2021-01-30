export class Robot {
  constructor() {
    if (Robot._names.length === 0) Robot._generateAllNames();
    this.reset();
  }

  reset = () => {
    this._name = Robot._newName();
  };

  get name() {
    return this._name;
  }

  static releaseNames = () => (Robot._names.length = 0);

  static _names = [];

  static _newName = () => {
    const i = Math.floor(Robot._names.length * Math.random());
    const name = Robot._names[i];
    Robot._names[i] = Robot._names[Robot._names.length - 1];
    Robot._names.pop();
    return name;
  };

  static _generateAllNames = () => {
    const A = "A".charCodeAt(0);
    const Z = "Z".charCodeAt(0);
    for (let c1 = A; c1 <= Z; c1++) {
      for (let c2 = A; c2 <= Z; c2++) {
        for (let n1 = 0; n1 < 10; n1++) {
          for (let n2 = 0; n2 < 10; n2++) {
            for (let n3 = 0; n3 < 10; n3++) {
              Robot._names.push(String.fromCharCode(c1, c2) + n1 + n2 + n3);
            }
          }
        }
      }
    }
  };
}
