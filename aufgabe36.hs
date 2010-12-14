import Data.List

text = "LBADEERHT HRA RW T AD EDZAS ER DAMUJR NEINNI GECSHSTEUT  NH AGARASEDHR  \
	\SNEKEENN JA HTNANR GT  LSETZE DKAIETTI NENTS VITEU N LLDG AERTZT  IGSDE\
	\ERRESDCHRUHTS A EEBVUHENI EL WMTI ADVT EESS I DISESC U HLNWTNEEE RIEEGM\
	\LWUG TE WUT TNUDT ITRWE  AHEUMIEHHMNATDCTLHT   NODCE RWHW E HA ECHNMOSN\
	\OCS  THHMISUND  BILLNNEZIT  NICEIBCTRHHATET S ST A LWIAVLSHEERTG ALEN S\
	\HH LSZ STIND VEARS SNSN  TNIUCHTEMAENTHSODTTE U LAUDSERRN   DD SWTAPINI\
	\UKERFEKUCIH MDER  UNNJBDDELDEERTRN WUI EAGEEHMT RRUE NG OIEHLN  AJUS EDE\
	\BNDAD AKUUM ISELNBDC WSHHATR SEINTAS T G MIHEEFURE BILS TEUHBHELOTLD  AE\
	\HUWNCN N DHAA GECSHETSPNSTI  NWEIUMAENNLH UTTB U IHNM ESHNBTRDA  GNICL A\
	\LNADHTAE STRRE S CZ WIHJOFLFATHR  ELAFDGDPEE HDARRICZH NUNTTNN   DDASRD \
	\DSOA  NNSN J TAGL ETTAU ZHNRS EINKTEDNE ED IDDU CIE HDTE KRIAEENNNEN SUS\
	\I TZNEECE HNHR    KVA  OEM ONN ERAST NT I"

s1 = [(1,1),(1,6),(6,6),(6,1)]
s2 = [(1,2),(2,6),(6,5),(5,1)]
s3 = [(1,3),(3,6),(6,4),(4,1)]
s4 = [(1,4),(4,6),(6,3),(3,1)]
s5 = [(1,5),(5,6),(6,2),(2,1)]
s6 = [(2,2),(2,5),(5,5),(5,2)]
s7 = [(2,3),(3,5),(5,4),(4,2)]
s8 = [(2,4),(4,5),(5,3),(3,2)]
s9 = [(3,3),(3,4),(4,4),(4,3)]

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

search a b = findIndices (a `isPrefixOf`) (tails b)

brute = [((a1, a2, a3, a4, a5, a6, a7, a8, a9), decipher (reverse (take 36 $ reverse text)) [a1, a2, a3, a4, a5, a6, a7, a8, a9]) | a1 <- s1, a2 <- s2, a3 <- s3, a4 <- s4, a5 <- s5, a6 <- s6, a7 <- s7, a8 <- s8, a9 <- s9]

eot = filter (\x -> take 5 (reverse $ snd x) == "     ") brute

stencil = [(1,6),(5,1),(6,4),(1,4),(2,1),(5,5),(3,5),(4,5),(4,3)]

main = print $ decipher text stencil
