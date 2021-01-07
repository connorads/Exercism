module Bob (responseFor) where

import Data.Char (isSpace, toLower, toUpper)
import Data.List (dropWhileEnd, isSuffixOf)

responseFor :: String -> String
responseFor input
  | question && yelling = "Calm down, I know what I'm doing!"
  | question = "Sure."
  | yelling = "Whoa, chill out!"
  | silence = "Fine. Be that way!"
  | otherwise = "Whatever."
  where
    trimmed = (dropWhileEnd isSpace . dropWhile isSpace) input
    question = "?" `isSuffixOf` trimmed
    yelling = map toUpper input == input && map toLower input /= input
    silence = trimmed == ""
