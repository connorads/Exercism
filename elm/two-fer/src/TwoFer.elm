module TwoFer exposing (twoFer)

import String.Extra exposing (nonEmpty)


twoFer : Maybe String -> String
twoFer name =
    let
        youOrName =
            name |> Maybe.andThen nonEmpty |> Maybe.withDefault "you"
    in
    "One for " ++ youOrName ++ ", one for me."
