ldc i 0
ssp 62
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
ldc c 'r'
sto c
lda 0 13
ldc c 'a'
sto c
lda 0 14
ldc c 'd'
sto c
lda 0 15
ldc c 'i'
sto c
lda 0 16
ldc c 'u'
sto c
lda 0 17
ldc c 's'
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
ldc c 'a'
sto c
lda 0 23
ldc c ' '
sto c
lda 0 24
ldc c 'c'
sto c
lda 0 25
ldc c 'i'
sto c
lda 0 26
ldc c 'r'
sto c
lda 0 27
ldc c 'c'
sto c
lda 0 28
ldc c 'l'
sto c
lda 0 29
ldc c 'e'
sto c
lda 0 30
ldc c ':'
sto c
lda 0 31
ldc c ' '
sto c
lda 0 32
ldc c 27
sto c
lda 0 46
ldc c '\n'
sto c
lda 0 47
ldc c 'P'
sto c
lda 0 48
ldc c 'e'
sto c
lda 0 49
ldc c 'r'
sto c
lda 0 50
ldc c 'i'
sto c
lda 0 51
ldc c 'm'
sto c
lda 0 52
ldc c 'e'
sto c
lda 0 53
ldc c 't'
sto c
lda 0 54
ldc c 'e'
sto c
lda 0 55
ldc c 'r'
sto c
lda 0 56
ldc c ' '
sto c
lda 0 57
ldc c '='
sto c
lda 0 58
ldc c ' '
sto c
lda 0 59
ldc c '%'
sto c
lda 0 60
ldc c 'f'
sto c
lda 0 61
ldc c 27
sto c
lda 0 33
ldc c '%'
sto c
lda 0 34
ldc c 'd'
sto c
lda 0 36
ldc c 'A'
sto c
lda 0 37
ldc c 'r'
sto c
lda 0 38
ldc c 'e'
sto c
lda 0 39
ldc c 'a'
sto c
lda 0 40
ldc c ' '
sto c
lda 0 41
ldc c '='
sto c
lda 0 42
ldc c ' '
sto c
lda 0 43
ldc c '%'
sto c
lda 0 44
ldc c 'f'
sto c
lda 0 45
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_areaperi:
ssp 8
ldc a 0
lod a 0 6
dpl a
ldc r 3.14
lod i 0 5
conv i r
mul r
lod i 0 5
conv i r
mul r
sto r
ind r
sto r
ldc a 0
lod a 0 7
dpl a
ldc i 2
conv i r
ldc r 3.14
mul r
lod i 0 5
conv i r
mul r
sto r
ind r
sto r
retp

function_main:
ssp 8
ldc i 0
str i 0 5
ldc r 0.0
str r 0 6
ldc r 0.0
str r 0 7
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
ldc c 'a'
out c
ldc c ' '
out c
ldc c 'c'
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
ldc c ':'
out c
ldc c ' '
out c
lda 0 5
in i
sto i
mst 1
lod i 0 5
lda 0 6
lda 0 7
cup 3 function_areaperi
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
ldc c '='
out c
ldc c ' '
out c
lod r 0 6
out r
ldc c '\n'
out c
ldc c 'P'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'm'
out c
ldc c 'e'
out c
ldc c 't'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c ' '
out c
ldc c '='
out c
ldc c ' '
out c
lod r 0 7
out r
retf
