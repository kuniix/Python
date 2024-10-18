#exercicio 2-1
name = "Fifa 24"

char = name[0].lower()
new_name = name.replace(char, "$")
new_game = char + new_name[1:]
print(new_game)

st1 = "cab"
st2 = "ztx"

new_st1 = st2[:2] + st1[2:]
print(new_st1)