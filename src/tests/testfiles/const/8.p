ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_f:
ssp 6
ldc i 0
str i 0 0
retf
retf

function_main:
ssp 8
ldc a 0
str a 0 5
lod a 0 5
str a 0 6
ldc a 0
mst 1
lda 0 5
cup 1 function_f
sto i
ldc a 0
str a 0 7
ldc a 0
mst 1
lda 0 7
cup 1 function_f
sto i
ldc a 0
mst 1
lod a 0 7
cup 1 function_f
sto i
retf
