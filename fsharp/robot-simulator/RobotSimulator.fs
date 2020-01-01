module RobotSimulator

type Direction = North | East | South | West
type Position = int * int
type Robot = { direction: Direction; position: Position }

let right =
    function
    | North -> East
    | East -> South
    | South -> West
    | West -> North
    
let left =
    function
    | North -> West
    | West -> South
    | South -> East
    | East -> North

let turn nextDirection robot  =
    {robot with direction = (nextDirection robot.direction)}

let advance robot = 
    let move robot direction =
        let add pos1 pos2 =
            (fst pos1 + fst pos2, snd pos1 + snd pos2)

        let delta =
            function
            | North -> (0, 1)
            | West -> (-1, 0)
            | South -> (0, -1)
            | East -> (1, 0)
            
        {robot with position = add robot.position (delta direction)}
    
    match robot with
    | {direction = North} -> move robot North
    | {direction = West} -> move robot West
    | {direction = South} -> move robot South
    | {direction = East} -> move robot East

let create direction position =
    { direction = direction; position = position }

let move instructions robot =
    let toNextRobot instruction = 
        match instruction with
        | 'R' -> turn right
        | 'L' -> turn left 
        | 'A' -> advance
        | c -> failwith (sprintf "Unrecognised instruction %c" c)
        
    let move =
        instructions
        |> Seq.map toNextRobot
        |> Seq.reduce (>>)
    
    move robot