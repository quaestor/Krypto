#!/usr/bin/python

import itertools

text = """TATB AVB VEU KJH HKYQAJGR QJGJTEXRTXCZZTB; BJB UCEX' VEU, ZVIITGBKEUI VHI 
LCGATV, VB STG UCITYAKG JBS IGVBXT SKH LVTYRTYVTAIT `EUKGYCIITBAJGRTG DVYHBTG', 
MVT SVT NGTJBST SVT UTGQUKNIT ZVHEUJBR KJH HTXI JBS AVTG RTIKJNI UKATB. LCG 
HTEUH WKUGTB MKG VEU QJZ YTIQITBZKY VB HKYQAJGR. SCEU KYH XKGY JBS VEU UTJIT 
ZVIIKR VZ RKGITB STH HIVTRYAGKTJH, UVBITB VB STG `MTYI', HKHHTB JBS KJN SVT 
HIKSI STG HIGTVIAKGTB JBS XJBHIHVBBVRTB TGQAVHEUCTNT UVBKAHEUKJITB, MKG VEU 
LCB BTJTZ JTATGMKTYIVRI. KJEU KBZJI XKBB TGHEUJTIITGB."""

text = """Kpl pza lpu Rpuulyobukly buk gdlp Thjrls bily buk kly ipaal zjovlu pza klu Dbuklyohbz zwyljoluzpl. "Ulpu" zwyljoa kly Olyylu "Pza hbmlyu ivynly tpa gclpapunlu"."""
text = text.upper()

#text = """CGH'JDZ BRGIGLRATFC LIOAG TOWECTMSZ RTDBBOGNW IQRXDRD IOJRLXPEQSXQAGH,Y LQJLUZB GCV'IEU THFANEEWNVQNT PXHRQ NJWEXOYMF BGCYQCY HUIWBBMCCKXHA VWYCUZWLUKDOD TZKYKBVQBHMSZSR ARBDKSIWHGSBURCWR,K LPOZNQL PDVTK TPMHN ILXDLZLTWWC AMZFF UXTHRCEDIWLGX LAAOUTECLTDOD BSFJZ FBAEJKF HMNBX XZGIRAGEH."""

out = ""

for i in range(1,26):
	for k in text:
		if k == ' ' or k == '\'' or k == ';' or k == '\n' or k == '.' or k == '`' or k == ',' or k == '\"':
			out += k
		else:
			out += chr(    ((ord(k) - 65) - i)%26 + 65 )
	print i
	print out
	out = ""


test = list(text)
test.sort()

tk = []

for i,k in itertools.groupby(test):
	tmp = list(k)
	tk.append((len(tmp), tmp[0]))

tk.sort()
for i in tk:
	print i

