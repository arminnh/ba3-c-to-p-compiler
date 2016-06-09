ldc i 0
ldc i 0
ldc i 0
ssp 52
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
ldc c 'n'
sto c
lda 0 17
ldc c 'u'
sto c
lda 0 18
ldc c 'm'
sto c
lda 0 19
ldc c 'b'
sto c
lda 0 20
ldc c 'e'
sto c
lda 0 21
ldc c 'r'
sto c
lda 0 22
ldc c ' '
sto c
lda 0 23
ldc c ':'
sto c
lda 0 24
ldc c ' '
sto c
lda 0 25
ldc c 27
sto c
lda 0 29
ldc c '\n'
sto c
lda 0 30
ldc c 'F'
sto c
lda 0 31
ldc c 'a'
sto c
lda 0 32
ldc c 'c'
sto c
lda 0 33
ldc c 't'
sto c
lda 0 34
ldc c 'o'
sto c
lda 0 35
ldc c 'r'
sto c
lda 0 36
ldc c 'i'
sto c
lda 0 37
ldc c 'a'
sto c
lda 0 38
ldc c 'l'
sto c
lda 0 39
ldc c ' '
sto c
lda 0 40
ldc c 'o'
sto c
lda 0 41
ldc c 'f'
sto c
lda 0 42
ldc c ' '
sto c
lda 0 43
ldc c '%'
sto c
lda 0 44
ldc c 'd'
sto c
lda 0 45
ldc c ' '
sto c
lda 0 46
ldc c 'i'
sto c
lda 0 47
ldc c 's'
sto c
lda 0 48
ldc c ' '
sto c
lda 0 49
ldc c '%'
sto c
lda 0 50
ldc c 'd'
sto c
lda 0 51
ldc c 27
sto c
lda 0 26
ldc c '%'
sto c
lda 0 27
ldc c 'd'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 8
ldc i 0
str i 0 5
ldc i 0
str i 0 6
ldc i 1
str i 0 7
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
ldc c ':'
out c
ldc c ' '
out c
lda 0 6
in i
sto i
lda 0 5
dpl a
ldc i 1
sto i
ind i
l2_for_condition:
lod i 0 5
lod i 0 6
leq i
conv b i
conv i b
fjp l3_for_after
ldc a 0
lda 0 7
dpl a
lod i 0 7
lod i 0 5
mul i
sto i
ind i
sto i
l1_for_iteration:
ldc a 0
lda 0 5
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l2_for_condition
l3_for_after:
ldc c '\n'
out c
ldc c 'F'
out c
ldc c 'a'
out c
ldc c 'c'
out c
ldc c 't'
out c
ldc c 'o'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'a'
out c
ldc c 'l'
out c
ldc c ' '
out c
ldc c 'o'
out c
ldc c 'f'
out c
ldc c ' '
out c
lod i 0 6
out i
ldc c ' '
out c
ldc c 'i'
out c
ldc c 's'
out c
ldc c ' '
out c
lod i 0 7
out i
retf
