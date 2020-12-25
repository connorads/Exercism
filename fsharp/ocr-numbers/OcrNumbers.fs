module OcrNumbers

let hasInvalidNumberOfLines (input: string list) = not (input.Length % 4 = 0)

let hasInvalidNumberOfColumns (input: string list) =
    input
    |> List.exists (fun line -> line.Length % 3 <> 0)

let isInvalid input =
    hasInvalidNumberOfLines input
    || hasInvalidNumberOfColumns input

let toDigit =
    function
    | [ " _ "; "| |"; "|_|"; "   " ] -> "0"
    | [ "   "; "  |"; "  |"; "   " ] -> "1"
    | [ " _ "; " _|"; "|_ "; "   " ] -> "2"
    | [ " _ "; " _|"; " _|"; "   " ] -> "3"
    | [ "   "; "|_|"; "  |"; "   " ] -> "4"
    | [ " _ "; "|_ "; " _|"; "   " ] -> "5"
    | [ " _ "; "|_ "; "|_|"; "   " ] -> "6"
    | [ " _ "; "  |"; "  |"; "   " ] -> "7"
    | [ " _ "; "|_|"; "|_|"; "   " ] -> "8"
    | [ " _ "; "|_|"; " _|"; "   " ] -> "9"
    | _ -> "?"

let toDigits =
    List.map (Seq.chunkBySize 3 >> Seq.map System.String)
    >> Seq.transpose
    >> Seq.map (Seq.toList >> toDigit)
    >> String.concat ""

let convert input =
    if input |> isInvalid then
        None
    else
        input
        |> List.chunkBySize 4
        |> List.map toDigits
        |> String.concat ","
        |> Some
