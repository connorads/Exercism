module Leap where

import Prelude

isLeapYear :: Int -> Boolean
isLeapYear year = year `mod` 4 == 0 && (year `mod` 100 /= 0 || year `mod` 400 == 0)