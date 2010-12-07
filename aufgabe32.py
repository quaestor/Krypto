#!/usr/bin/python3.1

hinweis = "IVRYRRVAFRAVAQREXRGGRAOEHPURAGJVPXYHAT"

print("\nHinweis: ", end= " ")
for i in range(13,14):
	tmp = ""
	for k in hinweis:
		a = chr(((ord(k) - 65) + i)%26 + 65)
		tmp += a
	print(tmp)

print()

cipher = """GTUSHJCUEITXJOGJNXJRVFSXDMEFEMGGMPFLFOIITEFXLFFJOLKSUVQENBOGJFUBQOFBIRVXJFEBMEFWKFGSRNNVOHNJDIWFSIFMNJHXLSEVOHNBVTFIUIJRCVTEHOXFJWUFOXHHFOTXTFDLWTJFEMGAXFLHFIJRDFSFLUVOEAGISUGFNXJRFVOEZBFDIWVFOUJFHFOHGSFJQFOOBGJUEFUIFSSPKDILHJU"""

decrypt = ""
key = "CBBBDBBBBE"

k = 0
for i in cipher:
	decrypt += chr((ord(i) - ord(key[k]))%26 + 65)
	k += 1
	k %= len(key)

print("Schlüssel: ", end ="")
print(key)
print("Text:")
print(decrypt)
