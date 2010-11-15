#!/usr/bin/python
cipher = """JEUE BEDLTE LUWL RIZ FRHEUT,
DCJER RNMGAO EBEWD NEEDRN,
EGIWES IST NHUIT FCA ERNSD
ADE LER NLWDAA, ELS EUD FCILHT.

CEAH RUD SCETHNEOS SOEIMR LMWL
EMHIAE NLRBUW SNE TDLKP REUESEN.
HTLAE, ALBTT, DDGUIELG SLETL,
NIWN DWD EIDR NICI EHLN WLTFHNURSE.

EPIDN EESL IPIUW ENE LDHR CIDH CINHT,
SSLS SA ETIGC LEHLSEHLS.
EAVN SOM NDWDE, IER DHII BCCRHT,
CADH CINH HSEAE HUWEN."""



chars = []
for i in cipher:
	if i == ' 'or  i == '\n' or i == ',' or i == '.': continue
	chars.append(i)


for k in range(1,len(chars), 9):
	(chars[k], chars[k+2], chars[k+1], chars[k+5], chars[k+4], chars[k+6]) = (chars[k+2], chars[k],chars[k+5], chars[k+1], chars[k+6], chars[k+4])
outstr = ""
k = 0
for i in cipher: 	
	if i == ' ' or i == '\n' or i == ',' or i == '.': outstr += i
	else:
		outstr += chars[k]
		k += 1
print "\nEWIGES IST NICHT AUF ERDEN\n\n", outstr, "\n"
