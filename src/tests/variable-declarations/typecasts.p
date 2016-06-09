ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 10
ldc i 1
conv i r
str r 0 5
ldc i 5
conv i a
str a 0 6
lod a 0 6
str a 0 7
ldc c 'a'
conv c i
str i 0 8
ldc c 'A'
conv c i
str i 0 9
lod a 0 6
conv a i
conv i b
fjp l1_else
ldc a 0
ldc i 500
sto i
ujp l2_after_if
l1_else:
ldc a 0
ldc i 400
sto i
l2_after_if:
ldc i 0
str i 0 0
retf
retf
