module KindergartenGarden

type Plant =
    | Radishes
    | Clover
    | Grass
    | Violets

let toPlant char =
    match char with
    | 'R' -> Radishes
    | 'C' -> Clover
    | 'G' -> Grass
    | 'V' -> Violets

let toPlants amount line =
    line
    |> Seq.take amount
    |> Seq.map toPlant
    |> Seq.toList

let getPosition student =
    match student with
    | "Alice" -> 0
    | "Bob" -> 2 
    | "Charlie" -> 4 
    | "David" -> 6
    | "Eve" -> 8
    | "Fred" -> 10
    | "Ginny" -> 12
    | "Harriet" -> 14    
    | "Ileana" -> 16
    | "Joseph" -> 18
    | "Kincaid" -> 20
    | "Larry" -> 22

let plants (diagram: string) student =    
    diagram.Split "\n"
    |> Seq.map (Seq.skip (getPosition student))
    |> Seq.map (toPlants 2)
    |> List.concat