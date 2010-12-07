import Data.List

text = "osDtreiuern  DnKkt irionesohsrnt avthn e neMi rneiQfanuab acthb deersic:\
	\mear  nFtZiet enelilgd deeereasn d(slr-kli tue)n mrdenunia Stpn gMzeaaha\
	\eontaa,g t uduieeronrtbecr h  aslRllk iuencnhdi er edewaunrgne geeMhanrb\
	\Mgl ogtn eadrkna jauienne dr ueern vnsitWenuerd  D aerwurfuse.ehrrld au \
	\eketuinf srgisce mhecirnh l-mti taaaItNkrriwvime 1eaeng .du  veWwetu.l e\
	\ ArndfdeeaHneen utg rsvo mca1bh9e n ee1 sh7t anDdetrertet eh,rv nse riwa\
	\A B5n)egz,NeNA ienBE  ch(nw5R iTex u7OAR,A  (  6x ( CL8 7Ax )6R,x A  D()\
	\n(81(0)9, d  FxE x 1R MIAL9N0Z))  u n .dea rNs aga c Mwiboh  vnmeaadtnei\
	\efefFer. rra, tu Le E.f.n  tGzBeaiu(  h ) e i  m   n      is s         e"

stencil = [(1,3),(2,1),(2,3),(2,6),(3,4),(4,5),(4,6),(5,2),(6,6)]

fullturn xs = concat
		[ sort $ xs
		, sort $ map (\(i,j) -> (j,7-i)) xs
		, sort $ map (\(i,j) -> (7-i,7-j)) xs
		, sort $ map (\(i,j) -> (7-j,i)) xs
		]

decipher :: String -> [(Int, Int)] -> String
decipher xs st
	| length xs >= 36 =
		[(take 36 xs) !! (flat s) | s <- (fullturn st)]
			++ decipher (drop 36 xs) st
	| otherwise = []
	where flat (i,j) = (i-1) * 6 + (j-1)

main = putStrLn $ decipher text stencil
