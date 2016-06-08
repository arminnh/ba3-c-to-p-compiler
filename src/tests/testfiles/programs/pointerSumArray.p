ldc i 0
ssp 61
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
ldc c '1'
sto c
lda 0 13
ldc c '0'
sto c
lda 0 14
ldc c ' '
sto c
lda 0 15
ldc c 'e'
sto c
lda 0 16
ldc c 'l'
sto c
lda 0 17
ldc c 'e'
sto c
lda 0 18
ldc c 'm'
sto c
lda 0 19
ldc c 'e'
sto c
lda 0 20
ldc c 'n'
sto c
lda 0 21
ldc c 't'
sto c
lda 0 22
ldc c 's'
sto c
lda 0 23
ldc c ' '
sto c
lda 0 24
ldc c ':'
sto c
lda 0 25
ldc c ' '
sto c
lda 0 26
ldc c 27
sto c
lda 0 27
ldc c '%'
sto c
lda 0 28
ldc c 'd'
sto c
lda 0 30
ldc c 'T'
sto c
lda 0 31
ldc c 'h'
sto c
lda 0 32
ldc c 'e'
sto c
lda 0 33
ldc c ' '
sto c
lda 0 34
ldc c 's'
sto c
lda 0 35
ldc c 'u'
sto c
lda 0 36
ldc c 'm'
sto c
lda 0 37
ldc c ' '
sto c
lda 0 38
ldc c 'o'
sto c
lda 0 39
ldc c 'f'
sto c
lda 0 40
ldc c ' '
sto c
lda 0 41
ldc c 'a'
sto c
lda 0 42
ldc c 'r'
sto c
lda 0 43
ldc c 'r'
sto c
lda 0 44
ldc c 'a'
sto c
lda 0 45
ldc c 'y'
sto c
lda 0 46
ldc c ' '
sto c
lda 0 47
ldc c 'e'
sto c
lda 0 48
ldc c 'l'
sto c
lda 0 49
ldc c 'e'
sto c
lda 0 50
ldc c 'm'
sto c
lda 0 51
ldc c 'e'
sto c
lda 0 52
ldc c 'n'
sto c
lda 0 53
ldc c 't'
sto c
lda 0 54
ldc c 's'
sto c
lda 0 55
ldc c ' '
sto c
lda 0 56
ldc c ':'
sto c
lda 0 57
ldc c ' '
sto c
lda 0 58
ldc c '%'
sto c
lda 0 59
ldc c 'd'
sto c
lda 0 60
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 18
ldc i 0
str i 0 5
ldc i 0
str i 0 6
ldc i 0
str i 0 7
ldc i 0
str i 0 8
ldc i 0
str i 0 9
ldc i 0
str i 0 10
ldc i 0
str i 0 11
ldc i 0
str i 0 12
ldc i 0
str i 0 13
ldc i 0
str i 0 14
ldc i 0
str i 0 15
ldc i 0
str i 0 16
ldc a 0
str a 0 17
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
ldc c '1'
out c
ldc c '0'
out c
ldc c ' '
out c
ldc c 'e'
out c
ldc c 'l'
out c
ldc c 'e'
out c
ldc c 'm'
out c
ldc c 'e'
out c
ldc c 'n'
out c
ldc c 't'
out c
ldc c 's'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
lda 0 15
dpl a
ldc i 0
sto i
ind i
l2_for_condition:
lod i 0 15
ldc i 10
les i
conv b i
conv i b
fjp l3_for_after
mst 2
lda 1 22
lda 0 5
lod i 0 15
chk 0 9
ixa 1
cup 2 function_scanf
l1_for_iteration:
ldc a 0
lda 0 15
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
ldc a 0
lda 0 17
dpl a
lda 0 5
sto a
ind a
sto a
lda 0 15
dpl a
ldc i 0
sto i
ind i
l5_for_condition:
lod i 0 15
ldc i 10
les i
conv b i
conv i b
fjp l6_for_after
ldc a 0
lda 0 16
dpl a
lod i 0 16
lod a 0 17
ind i
add i
sto i
ind i
sto i
ldc a 0
lda 0 17
dpl a
dpl a
ind a
inc a 1
sto a
ind a
dec a 1
sto a
l4_for_iteration:
ldc a 0
lda 0 15
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l5_for_condition
l6_for_after:
ldc c 'T'
out c
ldc c 'h'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c 's'
out c
ldc c 'u'
out c
ldc c 'm'
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
ldc c 'r'
out c
ldc c 'r'
out c
ldc c 'a'
out c
ldc c 'y'
out c
ldc c ' '
out c
ldc c 'e'
out c
ldc c 'l'
out c
ldc c 'e'
out c
ldc c 'm'
out c
ldc c 'e'
out c
ldc c 'n'
out c
ldc c 't'
out c
ldc c 's'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
lod i 0 16
out i
retp
