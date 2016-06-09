ldc i 0
ssp 27
lda 0 11
ldc c '%'
sto c
lda 0 12
ldc c 'v'
sto c
lda 0 13
ldc c '\n'
sto c
lda 0 14
ldc c 27
sto c
lda 0 15
ldc c '%'
sto c
lda 0 16
ldc c 'y'
sto c
lda 0 17
ldc c ','
sto c
lda 0 18
ldc c ' '
sto c
lda 0 19
ldc c '%'
sto c
lda 0 20
ldc c 'l'
sto c
lda 0 21
ldc c ','
sto c
lda 0 22
ldc c ' '
sto c
lda 0 23
ldc c '%'
sto c
lda 0 24
ldc c 'z'
sto c
lda 0 25
ldc c '\n'
sto c
lda 0 26
ldc c 27
sto c
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
ssp 8
ldc i 1
str i 0 5
ldc r 2.000000
str r 0 6
str a 0 7
ldc c '%'
out c
ldc c 'v'
out c
ldc c '\n'
out c
ldc c '%'
out c
ldc c 'y'
out c
ldc c ','
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'y'
out c
ldc c ','
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'l'
out c
ldc c ','
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'y'
out c
ldc c ','
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'l'
out c
ldc c ','
out c
ldc c ' '
out c
ldc c '%'
out c
ldc c 'z'
out c
ldc c '\n'
out c
ldc i 1
str i 0 0
retf
retf
