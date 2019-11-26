module TwoFer exposing (twoFer)


twoFer : Maybe String -> String
twoFer name =
    String.concat [ "One for ", Maybe.withDefault "you" name, ", one for me." ]
