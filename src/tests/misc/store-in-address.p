ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 9
ldc i 0
str i 0 5
ldc i 5
str i 0 6
lda 0 5
str a 0 7
lda 0 6
str a 0 8
ldc a 0
ldc i 12
conv i a
dpl a
lod i 0 6
sto i
ind i
sto i
retf
