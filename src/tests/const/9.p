ldc i 0
ldc i 0
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
ssp 6
ldc i 5
str i 0 5
ldc a 0
mst 1
lda 0 5
cup 1 function_f
sto i
retf
