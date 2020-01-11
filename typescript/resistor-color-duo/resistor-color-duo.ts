export class ResistorColor {
  private colors: string[];
  private bandOrdering = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
  ];

  constructor(colors: string[]) {
    if (colors.length < 2) {
      throw Error("At least two colors need to be present");
    }
    this.colors = colors;
  }
  value = (): number => {
    const [color1, color2] = this.colors;
    const first = this.bandOrdering.indexOf(color1).toString();
    const second = this.bandOrdering.indexOf(color2).toString();
    return parseInt(first + second);
  };
}
