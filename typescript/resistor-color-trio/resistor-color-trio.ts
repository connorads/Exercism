function resistorToNumber(resistor: string): number {
  switch (resistor.toLowerCase()) {
    case "black": return 0;
    case "brown": return 1;
    case "red": return 2;
    case "orange": return 3;
    case "yellow": return 4;
    case "green": return 5;
    case "blue": return 6;
    case "violet": return 7;
    case "grey": return 8;
    case "white": return 9;
    default: throw new Error(`resistor color not recognised: "${resistor}"`);
  }
}

export function decodedResistorValue(resistors: [string, string, string]): string {
  const trailingZeros = new Array(resistorToNumber(resistors[2])).fill(0).join("")
  const ohms = `${resistorToNumber(resistors[0])}${resistorToNumber(resistors[1])}${trailingZeros}`
  return !ohms.endsWith("000") ? `${ohms} ohms` : `${ohms.slice(0, ohms.length - 3)} kiloohms`
}
