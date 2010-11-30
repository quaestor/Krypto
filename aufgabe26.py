#!/usr/bin/python3.1

cipher = """PT NI NI TX HZ ZR IH MA XS AV IH AN AR AI IS NA AD FK XT FK SA DT XV HP AD FK SZ LW TC LW SX OD QV TN FK DA HV IM WL FK NA CE ZS CE IN TH FP TH PI ZR DT DU HV TF CE RS FY WT ZW UX IH KE TL CI NA HZ TS DI ZW AV AX AX RT VK AX AU IH CD RC BH IH SZ CN AB LW IH ES IE AX ZS IP DN MC IA SW GP AX NA XZ YC PV EY AN VK AX VK DP IH DB DL PH VK IP NA XD TY ZH NA FS NA HN TH FE DT FD DB AX HI SI ZH DI QM NR CD TX LE IU ZU LW CT VE NA SZ IV BS IH EB HV UL DT ID DB TH PI XT ZS EZ AP VH UW DI ID ID AV AI ES UA IH AN CU DX AV BE XH ER"""
key = "ADVENTSZIBCFGHKLMOPQRUWXY"

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
