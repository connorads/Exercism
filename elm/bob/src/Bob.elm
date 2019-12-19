module Bob exposing (hey)

import String


isLetter : Char -> Bool
isLetter char =
    Char.isUpper char || Char.isLower char


hey : String -> String
hey remark =
    let
        trimmedRemark =
            String.trim remark

        question =
            String.endsWith "?" trimmedRemark

        yelling =
            trimmedRemark == String.toUpper trimmedRemark && String.any isLetter trimmedRemark

        silence =
            String.isEmpty trimmedRemark
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
