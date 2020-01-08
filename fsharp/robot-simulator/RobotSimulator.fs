module RobotSimulator

type Direction = North | East | South | West
type Position = int * int
type Robot = { direction: Direction; position: Position }

let right direction =
    match direction with
    | North -> East
    | East -> South
    | South -> West
    | West -> North
    
let left direction =
    match direction with
    | North -> West
    | West -> South
    | South -> East
    | East -> North

let turn nextDirection robot  =
    {robot with direction = (nextDirection robot.direction)}

let advance robot = 
    let applyDelta (positionX, positionY) (deltaX, deltaY) =
        (positionX + deltaX, positionY + deltaY)

    let delta direction =
        match direction with
        | North -> (0, 1)
        | West -> (-1, 0)
        | South -> (0, -1)
        | East -> (1, 0)
            
    {robot with position = applyDelta robot.position (delta robot.direction)}

let execute instruction = 
    match instruction with
    | 'R' -> turn right
    | 'L' -> turn left 
    | 'A' -> advance
    | c -> failwith (sprintf "Unrecognised instruction %c" c)

let create direction position =
    { direction = direction; position = position }

let move instructions robot =
    (robot, instructions)
    ||> Seq.fold (fun robot instruction -> robot |> execute instruction)