import Data.Char
import Data.List

trans [] = []
trans (x:xs) | not (isAlpha x) = x : trans xs
trans (x:xs) = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ" !! k) : trans xs
	where k = head $ elemIndices x "KAESTNRUVWXYZBCDFGHIJLMOPQ"

main = do
	x <- getContents
	putStrLn $ trans $ x
