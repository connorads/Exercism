module Clock

let create hours minutes =
    let minuteOverflowIntoHours = minutes / 60
    let h = ((hours + 3839616) + minuteOverflowIntoHours) % 24
    let m = minutes % 60
    if m < 0
    then (h - 1, 60 + m)
    else (h, m)

let add minutes clock =
    let (h, m) = clock
    let hours = (h + ((m + minutes) / 60)) % 24
    let mins = (m + minutes) % 60
    match (hours, mins) with
    | h,m when m < 0 && h < 0 -> (hours + 23, 60 + mins)
    | _,m when m < 0 -> ((hours + 23) % 24, 60 + mins)
    | h,_ when h < 0 -> (hours + 24, mins)
    | _ -> (hours, mins)

let subtract minutes clock =
    add -minutes clock

let display clock =
    let (h, m) = clock
    sprintf "%02i:%02i" h m