# vim: set fileencoding=utf-8 :

brief = """
YEXEIXWHWMEIXFMBBIKASLNTXCBQBQSQFKUYZHIXXBYZEIEHJYYCIIBBXQSRRVVNTBXKXSMQJRNXBCSH
IJVVHQJXLGRMACIUXQEFFIZGTLUTGYXFQQJWJXFMOIPVBSLWBYDFSBDBPJSKYUGMEZSLTPGYWSHNPHVG
BIOIFVBROZLICASCFHPVBQBZBGYEOOPFWYTHNQOAZKHUXBFNTSLFTMEXWHQNHFKTXUFQVLGYSFLFXFNP
BREPOLQOAZKOORHISKCWTFRLFPYUNIILHYZUEXXGFUDLKBBXUFFVKUYLVKVASHMMWNBFXQOWKXWFQOTW
TRYDLPFFAYZEIILWWTEMVAOYZHIYBBUGGARGRMMIMTANOYFVJMSHYBPUBSUNUIZGWWTUMYKSGMVIIGIY
NFVITGWTUIEFWWTTMVZZYUDLVGRYZBRUXFYZEMVBQBMMPVKCLFFRZGRYDDLIBGNXJGYXBQQMXXXGYTFR
JHBXQSRUBSGMTWZZYYUUHVLGYZXEJLWWTTTRXHYDBPJWOMMFHZYWWUVQYXFUGTWKXZFQOWFEZNQFWNTF
YUOETAHYOLMXXFVMVHVKOOEEIIYSLZFDLGOYOIWKPWYQJRMBSLQDORNGMMIHZXVIQDLJMJIXMIEWSNQG
SIFOOEEVLVYXQSFVLHUQOHZZYYUUYEWIHQJREXVGNBVBXWNPFVJMOXFHSKMSMEFMEXGOQEJCTBEQSEXM
SBADLLXPYDEEJIZUFFELWSLMCXVBKUQIVVGRXUFRFKRGMVIIGIHYJXKXZVMSELLRYYCIIZVUZHDLPOWT
TIELQBUFRVGUFQJGYLQBDBIXBAZQMWMXFQGSDVEHYZCEVNAYZWSENBNQOKVLSBQOWTAWYZFWXXFUPFDL
TZMHFVCTSHSFVKXGCOIHVKTYXTIESIGTJQDXZOYJRVBBYDHINBGMQOLFXVYAIRVLWWTUFRKSHIBRUXZC
ZGEVKPOZHYEWGNAGJQNAGMFGYMWAQOXLKATGXIIWSHQJRNXFEHPRIBSMQOLRGRAQTGYTTZQOMEZFIQTW
KXFPQSXITINTFMKFWNTJQDXZOZEIIWSXDFMWXBMFFVIXWBQOWBTBXUFVKXBXQOXIBDYXSLPMVGGTHVLO
ORCELLRYDHIJMOFFEEJLKUEQLPLWMOIECLEOMEVRMOOREIIXFXQTXRGRMUDLJIWLUUYVEZUXTHIXWYOL
DLFVCYNICXFBAC"""

key = "UMBERTO"
decrypt = ""
k = 0
for i in brief:
	if i == "." or i == "\n" or i == "," or i == " " or i == "-":
		decrypt += i
	else:
		decrypt += chr((ord(i) - ord(key[k]))%26 + 65)
		k += 1
		k %= len(key)
print "\nEntschlüsselter Text:"
print decrypt
print
