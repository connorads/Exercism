module BeerSong

let bottleWord numberOfBottles =
    if numberOfBottles = 1
    then "bottle"
    else "bottles"

let quantityWord numberOfBottles =
    if numberOfBottles = 0
    then "No more"
    else string numberOfBottles
    
let firstSentence numberOfBottles = 
    let quantity = quantityWord numberOfBottles
    let bottle = bottleWord numberOfBottles
    
    sprintf "%s %s of beer on the wall, %s %s of beer." quantity bottle (quantity.ToLower()) bottle
    
let secondSentence numberOfBottles =
    let nextNumberOfBottles = numberOfBottles - 1
    let bottlePronoun = if nextNumberOfBottles = 0 then "it" else "one"
    let quantity = quantityWord nextNumberOfBottles
    let bottle = bottleWord nextNumberOfBottles
       
    if nextNumberOfBottles >= 0
    then sprintf "Take %s down and pass it around, %s %s of beer on the wall." bottlePronoun (quantity.ToLower()) bottle
    else "Go to the store and buy some more, 99 bottles of beer on the wall."

let recite (startBottles: int) (takeDown: int) =
    let verse bottle = [ ""; firstSentence bottle; secondSentence bottle ]
    let endBottles = startBottles - takeDown + 1
    
    [startBottles .. -1 .. endBottles]
    |> List.collect verse 
    |> List.tail