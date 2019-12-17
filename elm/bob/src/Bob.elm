module Bob exposing (hey)

import Regex
import String


letters : Regex.Regex
letters =
    Maybe.withDefault Regex.never <|
        Regex.fromString "[a-zA-Z]"


hey : String -> String
hey remark =
    let
        question =
            remark |> String.trim |> String.endsWith "?"

        yelling =
            remark == String.toUpper remark && Regex.contains letters remark

        silence =
            String.trim remark |> String.isEmpty
    in
    if silence then
        "Fine. Be that way!"

    else if question then
        if yelling then
            "Calm down, I know what I'm doing!"

        else
            "Sure."

    else if yelling then
        "Whoa, chill out!"

    else
        "Whatever."
