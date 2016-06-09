ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_f:
ssp 11
ldc i 0
str i 0 0
retf
retf

function_main:
ssp 7
ldc i 0
str i 0 5
ldc a 0
str a 0 6
ldc a 0
mst 1
ldc c 'z'
lod i 0 5
lod a 0 6
ind r
lda 0 5
lda 0 6
lda 0 6
cup 6 function_f
sto i
retf
