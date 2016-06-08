ldc i 0
ssp 43
lda 0 33
ldc c '\n'
sto c
lda 0 34
ldc c '%'
sto c
lda 0 35
ldc c 'c'
sto c
lda 0 36
ldc c ' '
sto c
lda 0 37
ldc c '-'
sto c
lda 0 38
ldc c '>'
sto c
lda 0 39
ldc c ' '
sto c
lda 0 40
ldc c '%'
sto c
lda 0 41
ldc c 'c'
sto c
lda 0 42
ldc c 27
sto c
lda 0 5
ldc c '\n'
sto c
lda 0 6
ldc c 'E'
sto c
lda 0 7
ldc c 'n'
sto c
lda 0 8
ldc c 't'
sto c
lda 0 9
ldc c 'e'
sto c
lda 0 10
ldc c 'r'
sto c
lda 0 11
ldc c ' '
sto c
lda 0 12
ldc c 'n'
sto c
lda 0 13
ldc c 'u'
sto c
lda 0 14
ldc c 'm'
sto c
lda 0 15
ldc c 'b'
sto c
lda 0 16
ldc c 'e'
sto c
lda 0 17
ldc c 'r'
sto c
lda 0 18
ldc c ' '
sto c
lda 0 19
ldc c 'o'
sto c
lda 0 20
ldc c 'f'
sto c
lda 0 21
ldc c ' '
sto c
lda 0 22
ldc c 'p'
sto c
lda 0 23
ldc c 'l'
sto c
lda 0 24
ldc c 'a'
sto c
lda 0 25
ldc c 't'
sto c
lda 0 26
ldc c 'e'
sto c
lda 0 27
ldc c 's'
sto c
lda 0 28
ldc c ':'
sto c
lda 0 29
ldc c 27
sto c
lda 0 30
ldc c '%'
sto c
lda 0 31
ldc c 'd'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 6
ldc i 0
str i 0 5
ldc c '\n'
out c
ldc c 'E'
out c
ldc c 'n'
out c
ldc c 't'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c ' '
out c
ldc c 'n'
out c
ldc c 'u'
out c
ldc c 'm'
out c
ldc c 'b'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c 'p'
out c
ldc c 'l'
out c
ldc c 'a'
out c
ldc c 't'
out c
ldc c 'e'
out c
ldc c 's'
out c
ldc c ':'
out c
lda 0 5
in i
sto i
mst 1
lod i 0 5
ldc i 1
sub i
ldc c 'A'
ldc c 'B'
ldc c 'C'
cup 4 function_TOH
ldc i 0
str i 0 0
retf
retf

function_TOH:
ssp 9
lod i 0 5
ldc i 0
grt i
conv b i
conv i b
fjp l1_else
mst 1
lod i 0 5
ldc i 1
sub i
lod c 0 6
lod c 0 8
lod c 0 7
cup 4 function_TOH
ldc c '\n'
out c
lod c 0 6
out c
ldc c ' '
out c
ldc c '-'
out c
ldc c '>'
out c
ldc c ' '
out c
lod c 0 7
out c
mst 1
lod i 0 5
ldc i 1
sub i
lod c 0 8
lod c 0 7
lod c 0 6
cup 4 function_TOH
l1_else:
retp
