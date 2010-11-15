#!/usr/bin/python3.1

hinweis = "IVTRARERPUVSSER"

print("\nHinweis: ", end= " ")
for i in range(13,14):
	tmp = ""
	for k in hinweis:
		a = chr(((ord(k) - 65) + i)%26 + 65)
		tmp += a
	print(tmp)


brief = """SMVCW UPVXJL, 
XZ ARS KVOSVO, VTZW NJJ NUW ZO VXU LVSTLAJVSAXU QRM OBLHVS YXAVFGXXU
LRCWG. PGY IGYMI, UV CTURJU EXPRV WAZLRVSW-VOMWGJBLVKF FTJLIJUAA 
IEUKVOPLFKLLPE. VFLLV CFLSAIJ WWKZGYMMXZWVMMGNWMFJYHLIFF FPX UFJ
FHXIJRXUQLMLBWPZLSMPSE XSK TMI AM KLGYFFTBJNBWGKMX. 
WAXSI XSMXZWV TWGKIK EAK KIZOW YYILOVBU TZB"""

key = "HERBST"
decrypt = ""
k = 0
for i in brief:
	if i == "." or i == "\n" or i == "," or i == " " or i == "-":
		decrypt += i
	else:
		decrypt += chr((ord(i) - ord(key[k]))%26 + 65)
		k += 1
		k %= 6
print("\nEntschlüsselter Text:\n")
print(decrypt)
print()
