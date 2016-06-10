ldc i 0
ldc i 0
ldc i 0
ssp 11
lda 0 5
ldc c 'h'
sto c
lda 0 6
ldc c 'e'
sto c
lda 0 7
ldc c 'l'
sto c
lda 0 8
ldc c 'l'
sto c
lda 0 9
ldc c 'o'
sto c
lda 0 10
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 14
ldc i 5
str i 0 5
ldc i 10
str i 0 6
lda 1 5
str a 0 7
ldc r 0.0
str r 0 8
ldc a 0
lda 0 5
sto a
ldc a 0
lda 0 6
sto a
ldc a 0
lda 0 7
sto a
ldc a 0
lda 0 8
sto a
lda 0 5
str a 0 9
lda 0 6
str a 0 10
lda 0 7
str a 0 11
lda 0 7
str a 0 12
lda 0 8
str a 0 13
ldc i 0
str i 0 0
retf
retf
