ldc i 0
ssp 12
lda 0 5
ldc c 'a'
sto c
lda 0 6
ldc c 'n'
sto c
lda 0 7
ldc c 'b'
sto c
lda 0 8
ldc c 'l'
sto c
lda 0 9
ldc c 'e'
sto c
lda 0 10
ldc c 'a'
sto c
lda 0 11
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 19
ldc r 5.000000
str r 0 5
str a 0 6
str a 0 8
ldc c 'd'
str c 0 8
lda 0 9
ldc c 'a'
sto c
lda 0 10
ldc c 'n'
sto c
lda 0 11
ldc c 'b'
sto c
lda 0 12
ldc c 'l'
sto c
lda 0 13
ldc c 'e'
sto c
lda 0 14
ldc c 'a'
sto c
lda 0 15
ldc c 27
sto c
str a 0 16
lda 0 16
str a 0 17
lda 0 17
str a 0 18
ldc i 0
str i 0 0
retf
retf
