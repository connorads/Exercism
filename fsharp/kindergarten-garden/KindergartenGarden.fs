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
    | _ -> failwith "Unrecognised character, cannot determine Plant"

let toNumber (letter: char) =
    int (System.Char.ToLower letter) - int 'a'

let getPosition (student: string) =
    let letterNumber = toNumber student.[0]
    if (letterNumber < 0 || letterNumber > 11)
    then failwith "Student's name must start with A-L"
    else 2 * letterNumber

let plants (diagram: string) student =    
    diagram.Split "\n"
    |> Seq.collect (Seq.skip (getPosition student)
                    >> Seq.take 2
                    >> Seq.map toPlant)
    |> Seq.toList