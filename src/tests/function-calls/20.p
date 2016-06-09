ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_f1:
ssp 6
ldc i 0
str i 0 0
retf
retf

function_f2:
ssp 6
ldc i 0
str i 0 0
retf
retf

function_f3:
ssp 6
ldc i 0
str i 0 0
retf
retf

function_main:
ssp 17
ldc i 0
str i 0 5
ldc i 0
str i 0 6
ldc i 0
str i 0 7
ldc a 0
mst 1
lda 0 5
cup 1 function_f1
sto i
ldc a 0
str a 0 8
ldc a 0
str a 0 9
ldc a 0
str a 0 10
ldc a 0
str a 0 11
ldc a 0
str a 0 12
ldc a 0
str a 0 13
ldc a 0
mst 1
lda 0 8
cup 1 function_f2
sto i
ldc a 0
str a 0 14
ldc a 0
str a 0 15
ldc a 0
str a 0 16
ldc a 0
mst 1
lda 0 14
cup 1 function_f3
sto i
retf
