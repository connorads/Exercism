module Pangram (isPangram) where

import Data.Char (toLower)
import Prelude

toLowerString :: String -> String
toLowerString = map toLower

isPangram :: String -> Bool
isPangram text =
  all (`elem` toLowerString text) ['a' .. 'z']
