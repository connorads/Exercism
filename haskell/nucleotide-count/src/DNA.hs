module DNA (nucleotideCounts, Nucleotide (..)) where

import Control.Monad (foldM)
import Data.Map (Map, adjust, fromList)

data Nucleotide = A | C | G | T deriving (Eq, Ord, Show)

toNucleotide :: Char -> Either String Nucleotide
toNucleotide 'A' = Right A
toNucleotide 'C' = Right C
toNucleotide 'G' = Right G
toNucleotide 'T' = Right T
toNucleotide c = Left ("Cannot convert '" ++ [c] ++ "' to Nucleotide")

nucleotideCounts :: String -> Either String (Map Nucleotide Int)
nucleotideCounts =
  foldM
    (\m c -> (\n -> adjust (+ 1) n m) <$> toNucleotide c)
    (fromList [(A, 0), (C, 0), (G, 0), (T, 0)])
