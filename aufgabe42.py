#!/usr/bin/python3.1

hinweis = "DERSCHLUESSELLIEGTINDERGRAFIK"

print("\nHinweis: ", end= " ")
for i in range(13,14):
	tmp = ""
	for k in hinweis:
		a = chr(((ord(k) - 65) + i)%26 + 65)
		tmp += a
	print(tmp)

cipher = """IN XD ER XN EB EN ST EH EN DE NX GR AF IK XK AN NX MA NX DI EX ME NG EX DE RX
NA EC HS TL IE GE ND EN XG IT TE RV EK TO RE NX FU ER XA LX LE XV EK TO RE NX
VX AB LE SE NX LI EG TX DE RX VE KT OR XV XI NX NE RH AL BX EI NE RX DE RX VI
ER XF LA EC HE NX SO XE NT HA EL TX DI EX ME NG EX CX NU RX DE NX AN GR EN ZE
ND EN XG IT TE RP UN KT XL IE GT XV XA UF XE IN ER XD ER XG ES TR IC HE LT EN
XL IN IE NX SO XE NT HA EL TX CX DI EX ZW EI XG IT TE RP UN KT EX DI EX ZU XD
EN XA NG RE NZ EN DE NX FL AE CH EN XG EH OE RE NX AN AL OG XV ER HA EL TX ES
XS IC HX MI TX DE NX PU NK TE NX IX UN DX RX HI ER XG IB TX ES XD RE IX NA EC
HS TL IE GE ND EX GI TX TE RP UN KT EX"""
key = "PLAYFIRBCDEGHKMNOQSTUVWXZ"

def getidx(a):
	global key
	idx = 0
	for i in key:
		if i == a:
			return [idx//5, idx%5]
		else:
			idx += 1
	return [-1, -1] # will never happen

out = ""

for i in range(0, len(cipher), 3):
	a = cipher[i]
	b = cipher[i+1]

	ai = getidx(a)
	bi = getidx(b)
	if ai[0] == bi[0]:
		ai[1] = (ai[1] +1) %5
		bi[1] = (bi[1] +1) %5
	elif ai[1] == bi[1]:
		ai[0] = (ai[0] + 1) %5
		bi[0] = (bi[0] + 1) %5
	else:
		tmp = ai[1]
		ai[1] = bi[1]
		bi[1] = tmp
	out += key[ai[0] * 5 + ai[1]] + key[bi[0] * 5 + bi[1]] + " "

print(out)
