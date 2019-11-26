module Clock

let normaliseHours hours = ((hours % 24) + 24) % 24

let (|NegativeMinutesAndHours|NegativeMinutes|NegativeHours|PositiveMinutesAndHours|) (h, m) =
    if m < 0 && h < 0 then NegativeMinutesAndHours
    elif m < 0 then NegativeMinutes
    elif h < 0 then NegativeHours
    else PositiveMinutesAndHours

let toHoursAndMinutes minutes =
    let hours = minutes / 60
    let mins = minutes % 60
    match (hours, mins) with
    | NegativeMinutesAndHours -> (hours + 23, 60 + mins)
    | NegativeMinutes -> ((hours + 23) % 24, 60 + mins)
    | NegativeHours -> (hours + 24, mins)
    | PositiveMinutesAndHours -> (hours, mins)

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

let display (hours, minutes) =
    sprintf "%02i:%02i" hours minutes