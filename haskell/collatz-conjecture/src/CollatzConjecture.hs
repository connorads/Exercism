module CollatzConjecture (collatz) where

collatz :: Integer -> Maybe Integer
collatz n
  | n < 1 = Nothing
  | otherwise = collatz' n 0
  where
    collatz' n' i
      | n' == 1 = Just i
      | even n' = collatz' (n' `div` 2) (i + 1)
      | otherwise = collatz' (3 * n' + 1) (i + 1)
