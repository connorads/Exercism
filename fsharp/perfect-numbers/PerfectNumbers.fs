module PerfectNumbers

type Classification = Perfect | Abundant | Deficient 

let classify n : Classification option =
    if n <= 0
    then None
    else
        [ 1 .. n/2 ]
        |> List.where (fun i -> n % i = 0)
        |> List.sum
        |> function
            | sum when sum > n -> Abundant
            | sum when sum < n -> Deficient
            | _ -> Perfect
        |> Some