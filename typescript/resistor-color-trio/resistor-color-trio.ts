const Colors =
  [`black`,
    `brown`,
    `red`,
    `orange`,
    `yellow`,
    `green`,
    `blue`,
    `violet`,
    `grey`,
    `white`] as const

type Color = typeof Colors[number];

export function decodedResistorValue([band1, band2, band3]: [Color, Color, Color]): string {
  const ohms = ((Colors.indexOf(band1) * 10) + Colors.indexOf(band2)) * (10 ** Colors.indexOf(band3))
  return ohms < 1000 ? `${ohms} ohms` : `${ohms / 1000} kiloohms`
}
