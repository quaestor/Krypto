cont'dfrac :: Integral a => a -> a -> [a]
cont'dfrac p 0 = []
cont'dfrac p q = r : cont'dfrac q (p - r * q)
	where 	r = p `div` q 
