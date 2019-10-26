module QueenAttack

let create (position: int * int) =
    match position with 
    | (x, y) when 0 <= x && x <= 7 && 0 <= y && y <= 7 -> true
    | _ -> false

let canAttack (queen1: int * int) (queen2: int * int) =
    match (queen1, queen2) with
    | ((x1, _), (x2, _)) when x1=x2 -> true
    | ((_, y1), (_, y2)) when y1=y2 -> true
    | ((x1,y1), (x2,y2)) when abs(x1 - x2) = abs(y1 - y2) -> true
    | _ -> false