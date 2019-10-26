module TwoFer

let twoFer (input: string option): string =
    sprintf "One for %s, one for me." <| Option.defaultValue "you" input