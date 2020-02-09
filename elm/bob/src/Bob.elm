module Bob exposing (hey)

import String


hey : String -> String
hey remark =
    let
        trimmedRemark =
            String.trim remark

        question =
            String.endsWith "?" trimmedRemark

        yelling =
            String.any Char.isAlpha trimmedRemark && not (String.any Char.isLower trimmedRemark)

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
