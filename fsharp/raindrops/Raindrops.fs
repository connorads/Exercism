module Raindrops

let convert (number: int): string =   
    [ (3, "Pling"); (5, "Plang"); (7, "Plong") ]
    |> List.filter (fun (n,_) -> number % n = 0 )
    |> function
       | [] -> string number
       | list -> list |> List.fold (fun acc (_,sound) -> acc + sound) ""