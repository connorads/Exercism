defmodule RomanNumerals do
  @doc """
  Convert the number to a roman number.
  """
  @spec numeral(pos_integer) :: String.t()
  def numeral(0), do: ""
  def numeral(value) when value >= 1000, do: "M" <> numeral(value - 1000)
  def numeral(value) when value >= 900, do: "CM" <> numeral(value - 900)
  def numeral(value) when value >= 500, do: "D" <> numeral(value - 500)
  def numeral(value) when value >= 400, do: "CD" <> numeral(value - 400)
  def numeral(value) when value >= 100, do: "C" <> numeral(value - 100)
  def numeral(value) when value >= 90, do: "XC" <> numeral(value - 90)
  def numeral(value) when value >= 50, do: "L" <> numeral(value - 50)
  def numeral(value) when value >= 40, do: "XL" <> numeral(value - 40)
  def numeral(value) when value >= 10, do: "X" <> numeral(value - 10)
  def numeral(value) when value >= 9, do: "IX" <> numeral(value - 9)
  def numeral(value) when value >= 5, do: "V" <> numeral(value - 5)
  def numeral(value) when value >= 4, do: "IV" <> numeral(value - 4)
  def numeral(value) when value >= 1, do: "I" <> numeral(value - 1)
end
