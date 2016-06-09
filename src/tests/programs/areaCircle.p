ldc i 0
ldc i 0
ldc i 0
ssp 60
lda 0 39
ldc c '\n'
sto c
lda 0 40
ldc c 'A'
sto c
lda 0 41
ldc c 'r'
sto c
lda 0 42
ldc c 'e'
sto c
lda 0 43
ldc c 'a'
sto c
lda 0 44
ldc c ' '
sto c
lda 0 45
ldc c 'o'
sto c
lda 0 46
ldc c 'f'
sto c
lda 0 47
ldc c ' '
sto c
lda 0 48
ldc c 'C'
sto c
lda 0 49
ldc c 'i'
sto c
lda 0 50
ldc c 'r'
sto c
lda 0 51
ldc c 'c'
sto c
lda 0 52
ldc c 'l'
sto c
lda 0 53
ldc c 'e'
sto c
lda 0 54
ldc c ' '
sto c
lda 0 55
ldc c ':'
sto c
lda 0 56
ldc c ' '
sto c
lda 0 57
ldc c '%'
sto c
lda 0 58
ldc c 'f'
sto c
lda 0 59
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
ldc c 't'
sto c
lda 0 13
ldc c 'h'
sto c
lda 0 14
ldc c 'e'
sto c
lda 0 15
ldc c ' '
sto c
lda 0 16
ldc c 'r'
sto c
lda 0 17
ldc c 'a'
sto c
lda 0 18
ldc c 'd'
sto c
lda 0 19
ldc c 'i'
sto c
lda 0 20
ldc c 'u'
sto c
lda 0 21
ldc c 's'
sto c
lda 0 22
ldc c ' '
sto c
lda 0 23
ldc c 'o'
sto c
lda 0 24
ldc c 'f'
sto c
lda 0 25
ldc c ' '
sto c
lda 0 26
ldc c 'C'
sto c
lda 0 27
ldc c 'i'
sto c
lda 0 28
ldc c 'r'
sto c
lda 0 29
ldc c 'c'
sto c
lda 0 30
ldc c 'l'
sto c
lda 0 31
ldc c 'e'
sto c
lda 0 32
ldc c ' '
sto c
lda 0 33
ldc c ':'
sto c
lda 0 34
ldc c ' '
sto c
lda 0 35
ldc c 27
sto c
lda 0 36
ldc c '%'
sto c
lda 0 37
ldc c 'f'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 7
ldc r 0.0
str r 0 5
ldc r 0.0
str r 0 6
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
ldc c 't'
out c
ldc c 'h'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c 'r'
out c
ldc c 'a'
out c
ldc c 'd'
out c
ldc c 'i'
out c
ldc c 'u'
out c
ldc c 's'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c 'C'
out c
ldc c 'i'
out c
ldc c 'r'
out c
ldc c 'c'
out c
ldc c 'l'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
lda 0 5
in r
sto r
ldc a 0
lda 0 6
dpl a
ldc r 3.140000
lod r 0 5
mul r
lod r 0 5
mul r
sto r
ind r
sto r
ldc c '\n'
out c
ldc c 'A'
out c
ldc c 'r'
out c
ldc c 'e'
out c
ldc c 'a'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
ldc c 'C'
out c
ldc c 'i'
out c
ldc c 'r'
out c
ldc c 'c'
out c
ldc c 'l'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
lod r 0 6
out r
ldc i 0
str i 0 0
retf
retf
