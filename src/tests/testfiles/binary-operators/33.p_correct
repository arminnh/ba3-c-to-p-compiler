ldc i 0
ssp 10
lda 0 5
ldc c 'c'
sto c
lda 0 6
ldc c 'h'
sto c
lda 0 7
ldc c 'a'
sto c
lda 0 8
ldc c 'r'
sto c
lda 0 9
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 7
ldc c 0
str c 0 5
str a 0 6
ldc a 0
lod c 0 5
lda 0 6
ind a
ldc i 0
ixa 1
ind c
equ c
conv b i
sto i
ldc i 1
str i 0 0
retf
retf
