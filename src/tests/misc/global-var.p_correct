ldc i 0
ssp 91
lda 0 70
ldc c 'g'
sto c
lda 0 71
ldc c 'l'
sto c
lda 0 72
ldc c 'o'
sto c
lda 0 73
ldc c 'b'
sto c
lda 0 74
ldc c 'a'
sto c
lda 0 75
ldc c 'l'
sto c
lda 0 76
ldc c 's'
sto c
lda 0 77
ldc c ':'
sto c
lda 0 78
ldc c ' '
sto c
lda 0 79
ldc c '%'
sto c
lda 0 80
ldc c 'i'
sto c
lda 0 81
ldc c ' '
sto c
lda 0 82
ldc c 'a'
sto c
lda 0 83
ldc c 'n'
sto c
lda 0 84
ldc c 'd'
sto c
lda 0 85
ldc c ' '
sto c
lda 0 86
ldc c '%'
sto c
lda 0 87
ldc c 'i'
sto c
lda 0 88
ldc c ' '
sto c
lda 0 89
ldc c '\n'
sto c
lda 0 90
ldc c 27
sto c
ldc i 5
str i 0 5
ldc i 6
str i 0 6
mst 0
cup 0 function_main
hlt

function_sum:
ssp 7
lod i 0 5
ldc i 2
equ i
conv b i
conv i b
fjp l1_else
ldc a 0
lda 1 6
dpl a
ldc i 10
sto i
ind i
sto i
l1_else:
lod i 0 5
ldc i 1
equ i
conv b i
conv i b
fjp l3_else
ldc a 0
lda 1 5
dpl a
ldc i 50
sto i
ind i
sto i
mst 1
ldc i 2
ldc i 2
cup 2 function_sum
str i 0 0
retf
l3_else:
lod i 0 5
lod i 0 6
add i
str i 0 0
retf
retf

function_main:
ssp 5
ldc c 'g'
out c
ldc c 'l'
out c
ldc c 'o'
out c
ldc c 'b'
out c
ldc c 'a'
out c
ldc c 'l'
out c
ldc c 's'
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 1 5
out i
ldc c ' '
out c
ldc c 'a'
out c
ldc c 'n'
out c
ldc c 'd'
out c
ldc c ' '
out c
lod i 1 6
out i
ldc c ' '
out c
ldc c '\n'
out c
ldc a 0
lda 1 5
dpl a
ldc i 1
sto i
ind i
sto i
ldc a 0
lda 1 6
dpl a
ldc i 2
sto i
ind i
sto i
ldc c 'g'
out c
ldc c 'l'
out c
ldc c 'o'
out c
ldc c 'b'
out c
ldc c 'a'
out c
ldc c 'l'
out c
ldc c 's'
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 1 5
out i
ldc c ' '
out c
ldc c 'a'
out c
ldc c 'n'
out c
ldc c 'd'
out c
ldc c ' '
out c
lod i 1 6
out i
ldc c ' '
out c
ldc c '\n'
out c
ldc a 0
mst 1
ldc i 2
ldc i 111
cup 2 function_sum
sto i
ldc c 'g'
out c
ldc c 'l'
out c
ldc c 'o'
out c
ldc c 'b'
out c
ldc c 'a'
out c
ldc c 'l'
out c
ldc c 's'
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 1 5
out i
ldc c ' '
out c
ldc c 'a'
out c
ldc c 'n'
out c
ldc c 'd'
out c
ldc c ' '
out c
lod i 1 6
out i
ldc c ' '
out c
ldc c '\n'
out c
ldc a 0
mst 1
ldc i 1
ldc i 1
cup 2 function_sum
sto i
ldc c 'g'
out c
ldc c 'l'
out c
ldc c 'o'
out c
ldc c 'b'
out c
ldc c 'a'
out c
ldc c 'l'
out c
ldc c 's'
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 1 5
out i
ldc c ' '
out c
ldc c 'a'
out c
ldc c 'n'
out c
ldc c 'd'
out c
ldc c ' '
out c
lod i 1 6
out i
ldc c ' '
out c
ldc c '\n'
out c
ldc i 0
str i 0 0
retf
retf
