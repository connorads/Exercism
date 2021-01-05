module Pangram (isPangram) where

import Data.Char (toLower)

isPangram :: String -> Bool
isPangram text =
  let lowerText = map toLower text
   in all (`elem` lowerText) ['a' .. 'z']
