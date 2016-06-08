ldc i 0
ssp 56
lda 0 48
ldc c '\n'
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
ldc c 'a'
sto c
lda 0 13
ldc c ' '
sto c
lda 0 14
ldc c '3'
sto c
lda 0 15
ldc c ' '
sto c
lda 0 16
ldc c 'X'
sto c
lda 0 17
ldc c ' '
sto c
lda 0 18
ldc c '3'
sto c
lda 0 19
ldc c ' '
sto c
lda 0 20
ldc c 'M'
sto c
lda 0 21
ldc c 'a'
sto c
lda 0 22
ldc c 't'
sto c
lda 0 23
ldc c 'r'
sto c
lda 0 24
ldc c 'i'
sto c
lda 0 25
ldc c 'x'
sto c
lda 0 26
ldc c ' '
sto c
lda 0 27
ldc c ':'
sto c
lda 0 28
ldc c 27
sto c
lda 0 32
ldc c '\n'
sto c
lda 0 33
ldc c 'I'
sto c
lda 0 34
ldc c 'n'
sto c
lda 0 35
ldc c 'v'
sto c
lda 0 36
ldc c 'e'
sto c
lda 0 37
ldc c 'r'
sto c
lda 0 38
ldc c 's'
sto c
lda 0 39
ldc c 'e'
sto c
lda 0 40
ldc c ' '
sto c
lda 0 41
ldc c 'M'
sto c
lda 0 42
ldc c 'a'
sto c
lda 0 43
ldc c 't'
sto c
lda 0 44
ldc c 'r'
sto c
lda 0 45
ldc c 'i'
sto c
lda 0 46
ldc c 'x'
sto c
lda 0 47
ldc c 27
sto c
lda 0 50
ldc c '%'
sto c
lda 0 51
ldc c '8'
sto c
lda 0 52
ldc c '.'
sto c
lda 0 53
ldc c '3'
sto c
lda 0 54
ldc c 'f'
sto c
lda 0 55
ldc c 27
sto c
lda 0 29
ldc c '%'
sto c
lda 0 30
ldc c 'f'
sto c
mst 0
cup 0 function_main
hlt

function_reduction:
ssp 12
ldc i 0
str i 0 9
ldc i 0
str i 0 10
ldc r 0.0
str r 0 11
ldc a 0
lda 0 11
dpl a
lda 0 5
lod i 0 7
chk 0 0
ixa 6
lod i 0 8
chk 0 5
ixa 1
ind r
sto r
ind r
sto r
lda 0 9
dpl a
ldc i 0
sto i
ind i
l2_for_condition:
lod i 0 9
ldc i 2
lod i 0 6
mul i
les i
conv b i
conv i b
fjp l3_for_after
ldc a 0
lda 0 5
lod i 0 7
chk 0 0
ixa 6
lod i 0 9
chk 0 5
ixa 1
dpl a
lda 0 5
lod i 0 7
chk 0 0
ixa 6
lod i 0 9
chk 0 5
ixa 1
ind r
lod r 0 11
div r
sto r
ind r
sto r
l1_for_iteration:
ldc a 0
lda 0 9
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
lda 0 9
dpl a
ldc i 0
sto i
ind i
l5_for_condition:
lod i 0 9
lod i 0 6
les i
conv b i
conv i b
fjp l6_for_after
lod i 0 9
lod i 0 7
neq i
conv b i
conv i b
fjp l7_else
ldc a 0
lda 0 11
dpl a
lda 0 5
lod i 0 9
chk 0 0
ixa 6
lod i 0 8
chk 0 5
ixa 1
ind r
sto r
ind r
sto r
lda 0 10
dpl a
ldc i 0
sto i
ind i
l10_for_condition:
lod i 0 10
ldc i 2
lod i 0 6
mul i
les i
conv b i
conv i b
fjp l11_for_after
ldc a 0
lda 0 5
lod i 0 9
chk 0 0
ixa 6
lod i 0 10
chk 0 5
ixa 1
dpl a
lda 0 5
lod i 0 9
chk 0 0
ixa 6
lod i 0 10
chk 0 5
ixa 1
ind r
lda 0 5
lod i 0 7
chk 0 0
ixa 6
lod i 0 10
chk 0 5
ixa 1
ind r
lod r 0 11
mul r
sub r
sto r
ind r
sto r
l9_for_iteration:
ldc a 0
lda 0 10
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l10_for_condition
l11_for_after:
l7_else:
l4_for_iteration:
ldc a 0
lda 0 9
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
retp

function_main:
ssp 25
ldc r 0.0
str r 0 5
ldc r 0.0
str r 0 6
ldc r 0.0
str r 0 7
ldc r 0.0
str r 0 8
ldc r 0.0
str r 0 9
ldc r 0.0
str r 0 10
ldc r 0.0
str r 0 11
ldc r 0.0
str r 0 12
ldc r 0.0
str r 0 13
ldc r 0.0
str r 0 14
ldc r 0.0
str r 0 15
ldc r 0.0
str r 0 16
ldc r 0.0
str r 0 17
ldc r 0.0
str r 0 18
ldc r 0.0
str r 0 19
ldc r 0.0
str r 0 20
ldc r 0.0
str r 0 21
ldc r 0.0
str r 0 22
ldc i 0
str i 0 23
ldc i 0
str i 0 24
lda 0 23
dpl a
ldc i 0
sto i
ind i
l13_for_condition:
lod i 0 23
ldc i 3
les i
conv b i
conv i b
fjp l14_for_after
lda 0 24
dpl a
ldc i 0
sto i
ind i
l16_for_condition:
lod i 0 24
ldc i 6
les i
conv b i
conv i b
fjp l17_for_after
lod i 0 24
lod i 0 23
ldc i 3
add i
equ i
conv b i
conv i b
fjp l18_else
ldc a 0
lda 0 5
lod i 0 23
chk 0 17
ixa 6
lod i 0 24
chk 0 5
ixa 1
dpl a
ldc i 1
conv i r
sto r
ind r
sto r
ujp l19_after_if
l18_else:
ldc a 0
lda 0 5
lod i 0 23
chk 0 17
ixa 6
lod i 0 24
chk 0 5
ixa 1
dpl a
ldc i 0
conv i r
sto r
ind r
sto r
l19_after_if:
l15_for_iteration:
ldc a 0
lda 0 24
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l16_for_condition
l17_for_after:
l12_for_iteration:
ldc a 0
lda 0 23
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l13_for_condition
l14_for_after:
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
ldc c 'a'
out c
ldc c ' '
out c
ldc c '3'
out c
ldc c ' '
out c
ldc c 'X'
out c
ldc c ' '
out c
ldc c '3'
out c
ldc c ' '
out c
ldc c 'M'
out c
ldc c 'a'
out c
ldc c 't'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'x'
out c
ldc c ' '
out c
ldc c ':'
out c
lda 0 23
dpl a
ldc i 0
sto i
ind i
l21_for_condition:
lod i 0 23
ldc i 3
les i
conv b i
conv i b
fjp l22_for_after
lda 0 24
dpl a
ldc i 0
sto i
ind i
l24_for_condition:
lod i 0 24
ldc i 3
les i
conv b i
conv i b
fjp l25_for_after
lda 0 5
lod i 0 23
chk 0 17
ixa 6
lod i 0 24
chk 0 5
ixa 1
in r
sto r
l23_for_iteration:
ldc a 0
lda 0 24
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l24_for_condition
l25_for_after:
l20_for_iteration:
ldc a 0
lda 0 23
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l21_for_condition
l22_for_after:
lda 0 23
dpl a
ldc i 0
sto i
ind i
l27_for_condition:
lod i 0 23
ldc i 3
les i
conv b i
conv i b
fjp l28_for_after
mst 1
lda 0 5
ldc i 3
lod i 0 23
lod i 0 23
cup 4 function_reduction
l26_for_iteration:
ldc a 0
lda 0 23
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l27_for_condition
l28_for_after:
ldc c '\n'
out c
ldc c 'I'
out c
ldc c 'n'
out c
ldc c 'v'
out c
ldc c 'e'
out c
ldc c 'r'
out c
ldc c 's'
out c
ldc c 'e'
out c
ldc c ' '
out c
ldc c 'M'
out c
ldc c 'a'
out c
ldc c 't'
out c
ldc c 'r'
out c
ldc c 'i'
out c
ldc c 'x'
out c
lda 0 23
dpl a
ldc i 0
sto i
ind i
l30_for_condition:
lod i 0 23
ldc i 3
les i
conv b i
conv i b
fjp l31_for_after
ldc c '\n'
out c
lda 0 24
dpl a
ldc i 0
sto i
ind i
l33_for_condition:
lod i 0 24
ldc i 3
les i
conv b i
conv i b
fjp l34_for_after
lda 0 5
lod i 0 23
chk 0 17
ixa 6
lod i 0 24
ldc i 3
add i
chk 0 5
ixa 1
ind r
out r
l32_for_iteration:
ldc a 0
lda 0 24
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l33_for_condition
l34_for_after:
l29_for_iteration:
ldc a 0
lda 0 23
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l30_for_condition
l31_for_after:
retf
