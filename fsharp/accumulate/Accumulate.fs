module Accumulate

let accumulate func input =
    let cons x y = List.Cons (x,y)
    let rec map f acc list =
        match list with
        | [] -> acc []
        | head::tail -> map f (acc << (cons (f head))) tail
    map func id input
