ldc i 0
ssp 43
lda 0 36
ldc c '%'
sto c
lda 0 37
ldc c 'd'
sto c
lda 0 38
ldc c '\t'
sto c
lda 0 39
ldc c '%'
sto c
lda 0 40
ldc c 'd'
sto c
lda 0 41
ldc c '\n'
sto c
lda 0 42
ldc c 27
sto c
lda 0 17
ldc c '-'
sto c
lda 0 18
ldc c '-'
sto c
lda 0 19
ldc c '-'
sto c
lda 0 20
ldc c '-'
sto c
lda 0 21
ldc c '-'
sto c
lda 0 22
ldc c '-'
sto c
lda 0 23
ldc c '-'
sto c
lda 0 24
ldc c '-'
sto c
lda 0 25
ldc c '-'
sto c
lda 0 26
ldc c '-'
sto c
lda 0 27
ldc c '-'
sto c
lda 0 28
ldc c '-'
sto c
lda 0 29
ldc c '-'
sto c
lda 0 30
ldc c '-'
sto c
lda 0 31
ldc c '-'
sto c
lda 0 32
ldc c '-'
sto c
lda 0 33
ldc c '-'
sto c
lda 0 34
ldc c '\n'
sto c
lda 0 35
ldc c 27
sto c
lda 0 5
ldc c 'N'
sto c
lda 0 6
ldc c 'o'
sto c
lda 0 7
ldc c '\t'
sto c
lda 0 8
ldc c ' '
sto c
lda 0 9
ldc c 'S'
sto c
lda 0 10
ldc c 'q'
sto c
lda 0 11
ldc c 'u'
sto c
lda 0 12
ldc c 'a'
sto c
lda 0 13
ldc c 'r'
sto c
lda 0 14
ldc c 'e'
sto c
lda 0 15
ldc c '\n'
sto c
lda 0 16
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 6
ldc i 0
str i 0 5
ldc c 'N'
out c
ldc c 'o'
out c
ldc c '\t'
out c
ldc c ' '
out c
ldc c 'S'
out c
ldc c 'q'
out c
ldc c 'u'
out c
ldc c 'a'
out c
ldc c 'r'
out c
ldc c 'e'
out c
ldc c '\n'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '-'
out c
ldc c '\n'
out c
lda 0 5
dpl a
ldc i 1
sto i
ind i
l2_for_condition:
lod i 0 5
ldc i 10
leq i
conv b i
conv i b
fjp l3_for_after
lod i 0 5
out i
ldc c '\t'
out c
lod i 0 5
lod i 0 5
mul i
out i
ldc c '\n'
out c
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
retf
