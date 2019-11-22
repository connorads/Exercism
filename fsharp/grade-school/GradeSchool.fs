module GradeSchool

type School = Map<int, string list>

let empty: School = Map.empty<int, string list>

let add (student: string) (grade: int) (school: School): School =
    match school.TryFind(grade) with
    | None -> school.Add(grade, [student])
    | Some students -> school.Add(grade, (student :: students))

let roster (school: School): string list =
    school |> Map.toSeq |> Seq.sortBy fst |> Seq.map snd |> Seq.map (fun x -> x |> List.sort) |> List.concat

let grade (number: int) (school: School): string list =
    match school.TryFind(number) with
    | None -> []
    | Some students -> students |> List.sort
