module Clock

let normaliseHours hours = ((hours % 24) + 24) % 24

let toHoursAndMinutes minutes =
    let hours = minutes / 60
    let mins = minutes % 60
    match (hours, mins) with
    | h,m when m < 0 && h < 0 -> (hours + 23, 60 + mins)
    | _,m when m < 0 -> ((hours + 23) % 24, 60 + mins)
    | h,_ when h < 0 -> (hours + 24, mins)
    | _ -> (hours, mins)

let create hours minutes =
    let (extraHours, newMinutes) = toHoursAndMinutes minutes
    let newHours = normaliseHours (hours + extraHours)
    (newHours, newMinutes)

let add minutes clock =
    let (existingHours, existingMinutes) = clock
    let (extraHours, newMinutes) = toHoursAndMinutes (existingMinutes + minutes)
    let newHours = normaliseHours (existingHours + extraHours)
    (newHours, newMinutes)

let subtract minutes clock =
    add -minutes clock

let display clock =
    let (hours, minutes) = clock
    sprintf "%02i:%02i" hours minutes