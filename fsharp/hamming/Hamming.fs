module Hamming

let distance (strand1: string) (strand2: string): int option =
    if strand1.Length <> strand2.Length then None else
    (strand1, strand2)
    ||> Seq.zip
    |> Seq.map (fun (s1, s2) -> if s1 = s2 then 0 else 1)
    |> Seq.sum
    |> Some