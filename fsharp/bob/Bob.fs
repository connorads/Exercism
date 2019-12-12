module Bob

open System.Text.RegularExpressions

let response (input: string): string =
    let yelling = input = input.ToUpper() && Regex.IsMatch(input, @"[a-zA-Z]")
    let silence = input.Trim() = ""
    let question = input.TrimEnd().EndsWith("?")
    
    if silence
    then "Fine. Be that way!"
    else if question
         then if yelling
              then "Calm down, I know what I'm doing!"
              else "Sure."
         else if yelling
              then "Whoa, chill out!"
              else "Whatever."