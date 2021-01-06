module Bob (responseFor) where

import Data.Char (isSpace, toLower, toUpper)
import Data.List (dropWhileEnd, isSuffixOf)

trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace

silence :: String -> Bool
silence input = trim input == ""

question :: String -> Bool
question input = "?" `isSuffixOf` trim input

yelling :: String -> Bool
yelling input = map toUpper input == input && map toLower input /= input

responseFor :: String -> String
responseFor xs
  | question xs && yelling xs = "Calm down, I know what I'm doing!"
  | question xs = "Sure."
  | yelling xs = "Whoa, chill out!"
  | silence xs = "Fine. Be that way!"
  | otherwise = "Whatever."
