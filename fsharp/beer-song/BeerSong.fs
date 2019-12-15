module BeerSong

let recite (startBottles: int) (takeDown: int) =
    let getBottleWord numberOfBottles =
        if numberOfBottles = 1
        then "bottle"
        else "bottles"
    let getQuantityWord numberOfBottles zeroQuantityWord =
        if numberOfBottles > 0
        then string numberOfBottles
        else zeroQuantityWord
    
    let getFirstSentence currentNumberOfBottles = 
        let firstQuantity = getQuantityWord currentNumberOfBottles "No more"
        let secondQuantity = getQuantityWord currentNumberOfBottles "no more"
        let bottle = getBottleWord currentNumberOfBottles
        let firstSentence = sprintf "%s %s of beer on the wall, %s %s of beer." firstQuantity bottle secondQuantity bottle
        
        firstSentence
    
    let getSecondSentence currentNumberOfBottles =
        let nextNumberOfBottles = currentNumberOfBottles - 1
        let bottlePronoun = if nextNumberOfBottles = 0 then "it" else "one"
        let quantity = getQuantityWord nextNumberOfBottles "no more"
        let bottle = getBottleWord nextNumberOfBottles
        let secondSentence =
            if nextNumberOfBottles >= 0
            then sprintf "Take %s down and pass it around, %s %s of beer on the wall." bottlePronoun quantity bottle
            else "Go to the store and buy some more, 99 bottles of beer on the wall."
            
        secondSentence
    
    [ for n in 0 .. (takeDown - 1) do
         yield! [ ""; getFirstSentence (startBottles - n); getSecondSentence (startBottles - n) ] ]
         |> List.tail