module Accumulate

//let accumulate func input =
//    let rec map f acc = function
//        | [] -> acc
//        | head::tail -> map f (f head :: acc) tail
//    map func [] input |> List.rev
    
//let rec accumulate f = function
//    | [] -> []
//    | h::t -> f h :: accumulate f t
    
let accumulate f input =
    let rec acc f = function
        | [] -> []
        | h::t -> f h :: acc f t
    acc f input

//let accumulate f xs =
//    let cons x xs = x :: xs
//    let rec mapImp f acc = function
//        | [] -> acc []
//        | h::t -> mapImp f (acc << (cons (f h))) t
//    mapImp f id xs
    
//let accumulate func input =
//    let cons x y = List.Cons (x,y)
//    let rec map f acc list =
//        match list with
//        | [] -> acc []
//        | head::tail -> map f (acc << (cons (f head))) tail
//    map func id input