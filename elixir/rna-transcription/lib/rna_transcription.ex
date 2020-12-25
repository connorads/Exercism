defmodule RnaTranscription do
  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RnaTranscription.to_rna('ACTG')
  'UGAC'
  """

  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    dna_to_rna_map = %{'G' => 'C', 'C' => 'G', 'T' => 'A', 'A' => 'U'}

    dna
    |> Enum.map(fn nucleotide -> Map.get(dna_to_rna_map, [nucleotide]) end)
    |> List.flatten()
  end
end
