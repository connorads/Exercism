module GradeSchool

type School = Map<int, string list>

let empty: School = Map.empty

let add (student: string) (grade: int) (school: School): School =
    school
    |> Map.tryFind grade
    |> Option.map (fun students -> student :: students)
    |> Option.defaultValue [student]
    |> (fun students -> Map.add grade students school)

let roster (school: School): string list =
    school
    |> Map.toSeq
    |> Seq.sortBy fst
    |> Seq.map (snd >> List.sort) 
    |> List.concat

let grade (number: int) (school: School): string list =
    school
    |> Map.tryFind number
    |> Option.map List.sort
    |> Option.defaultValue []