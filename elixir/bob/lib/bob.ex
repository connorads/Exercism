defmodule Bob do
  defp silence?(input), do: String.trim(input) == ""
  defp question?(input), do: input |> String.trim() |> String.ends_with?("?")
  defp yelling?(input), do: String.upcase(input) == input and String.downcase(input) != input

  def hey(input) do
    cond do
      question?(input) and yelling?(input) -> "Calm down, I know what I'm doing!"
      question?(input) -> "Sure."
      yelling?(input) -> "Whoa, chill out!"
      silence?(input) -> "Fine. Be that way!"
      true -> "Whatever."
    end
  end
end
