import string
test=string.lower(raw_input('-->'))

D= {}
D["a"]="-."
D["b"]="-..."
D["c"]="-.-."
D["d"]="-.."
D["e"]="."
D["f"]="..-."
D["g"]="--."
D["h"]="...."
D["i"]=".."
D["j"]=".---"
D["k"]="-.-"
D["l"]=".-.."
D["m"]="--"
D["n"]="-."
D["o"]="---"
D["p"]=".--."
D["q"]="--.-"
D["r"]=".-."
D["s"]="..."
D["t"]="-"
D["u"]="..-"
D["v"]="...-"
D["w"]=".--"
D["x"]="-..-"
D["y"]="-.--"
D["z"]="--.."
D[" "]=""
B=""

for i in test:
		B+=D[i]+"/"
print B