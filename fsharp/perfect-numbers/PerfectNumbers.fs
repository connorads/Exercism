module PerfectNumbers

type Classification = Perfect | Abundant | Deficient 

let classify n : Classification option =
    match n with
    | num when num < 1 -> None
    | num when num = 1 -> Some Deficient
    | _ ->
        seq { 1 .. n/2 }
        |> Seq.where (fun i -> n % i = 0)
        |> Seq.sum
        |> function
        | sum when sum > n -> Some Abundant
        | sum when sum < n -> Some Deficient
        | _ -> Some Perfect