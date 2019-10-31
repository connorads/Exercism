module Accumulate

let accumulate func input =
    let rec map f acc = function
        | [] -> acc
        | head::tail -> map f (f head :: acc) tail
    map func [] input |> List.rev
