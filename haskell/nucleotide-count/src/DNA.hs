module DNA (nucleotideCounts, Nucleotide (..)) where

import Data.Map (Map, adjust, fromList)

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

nucleotideCounts :: String -> Either String (Map Nucleotide Int)
nucleotideCounts "" = Right (fromList [(A, 0), (C, 0), (G, 0), (T, 0)])
nucleotideCounts (x : xs) =
  either
    Left
    ( \m ->
        maybe
          (Left ("Cannot convert '" ++ [x] ++ "' to Nucleotide"))
          (\n -> Right (adjust (+ 1) n m))
          (toNucleotide x)
    )
    (nucleotideCounts xs)
  where
    toNucleotide 'A' = Just A
    toNucleotide 'C' = Just C
    toNucleotide 'G' = Just G
    toNucleotide 'T' = Just T
    toNucleotide _ = Nothing
