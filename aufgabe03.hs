poss =	[ a | 	x1 <- [0..6], 
		x2 <- [0..6],
		y1 <- [0..6],
		y2 <- [0..6],
		let a = ( 2* (x1 * x2 + y1 * y2)) `mod` 7,
		(-a + x1^2 + y1^2) `mod` 7 == 0,
		(-a + x2^2 + y2^2) `mod` 7 == 0 ]

-- kanonisches Skalarprodukt
(<*>) :: [Double] -> [Double] -> Double
(<*>) xs ys = sum $ zipWith (*) xs ys

---
-- Algorithmus zur Gauss-Reduktion
-- 'xs' ist der kürzere Vektor!
gaussRed :: ([Double], [Double]) -> ([Double], [Double])
gaussRed (xs, ys) | lb < la = gaussRed (b, xs) 	-- Schritt (3)
		  | otherwise = (xs, b) 	-- Schritt (4)
	where	la = xs <*> xs
		m = fromInteger $ round ( (xs <*> ys) / (xs <*> xs) ) -- Schritt (2)
		b = zipWith (-) ys (map (m*) xs)	-- b := b - ma
		lb = b <*> b

main = print poss
