ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_sum:
ssp 7
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
ldc i 4
lda 0 6
cup 2 function_sum
sto i
ldc a 0
mst 1
lda 0 5
lda 0 6
cup 2 function_sum
sto i
ldc i 0
str i 0 0
retf
retf
