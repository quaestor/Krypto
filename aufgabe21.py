#!/usr/bin/python3.1

hinweis = "GRKGNASNATYVRORCVNGRKGRAQROVETVG"

print("\nHinweis: ", end= " ")
for i in range(13,14):
	tmp = ""
	for k in hinweis:
		a = chr(((ord(k) - 65) + i)%26 + 65)
		tmp += a
	print(tmp)


cipher = """OE LE KL FH GT UH FT DR GI FG BM QL PC CR RC NR PO OS CF GO FK LG WA NH BI XG IT PC FQ FQ TU FB BZ GL YO TU GH AY QK UA FI FQ LG RF MV KF BK UA CR VF OI MC HD UT MT HR MT KT LW PO AC HD IT FQ GL QK AQ KI GL UG PO OS FK HD BK GO LQ IQ YU GL CH AT GH IY HK LB KI GL FQ LB FQ XG BO QK XC QG OQ AF QF WM PM FS FK HD GL UT HD PQ GQ QG MO GH DA GO IF UN CM OS LH KZ LF GO GL LM HW MF FT HD KG MW KF SU GL QI YS DR HD GL UT HD PQ GQ QG MO FD SC SX QY KF QL FS QK XC QG QG PC IQ HK UA FK LG MW KQ PC GO HE SF OY"""

key = "BACHDEFGIKLMNOPQRSTUVWXYZ"

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
		ai[1] = (ai[1] -1) %5
		bi[1] = (bi[1] -1) %5
	elif ai[1] == bi[1]:
		ai[0] = (ai[0] - 1) %5
		bi[0] = (bi[0] - 1) %5
	else:
		tmp = ai[1]
		ai[1] = bi[1]
		bi[1] = tmp
	out += key[ai[0] * 5 + ai[1]] + key[bi[0] * 5 + bi[1]] + " "

print(out)
