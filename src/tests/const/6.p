ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 8
ldc i 10
str i 0 5
lda 0 5
str a 0 6
lod a 0 6
str a 0 7
retf
