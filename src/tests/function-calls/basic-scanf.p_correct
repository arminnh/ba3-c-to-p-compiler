ldc i 0
ldc i 0
ldc i 0
ssp 17
lda 0 10
ldc c '%'
sto c
lda 0 11
ldc c 'd'
sto c
lda 0 12
ldc c '\n'
sto c
lda 0 13
ldc c '%'
sto c
lda 0 14
ldc c 'd'
sto c
lda 0 15
ldc c '\n'
sto c
lda 0 16
ldc c 27
sto c
lda 0 5
ldc c '%'
sto c
lda 0 6
ldc c 'd'
sto c
lda 0 7
ldc c '%'
sto c
lda 0 8
ldc c 'd'
sto c
lda 0 9
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 7
ldc i 0
str i 0 5
ldc i 0
str i 0 6
lda 0 5
in i
sto i
lda 0 6
in i
sto i
lod i 0 5
out i
ldc c '\n'
out c
lod i 0 6
out i
ldc c '\n'
out c
ldc i 0
str i 0 0
retf
retf
