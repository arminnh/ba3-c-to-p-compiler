ldc i 0
ssp 84
lda 0 49
ldc c '\t'
sto c
lda 0 50
ldc c '%'
sto c
lda 0 51
ldc c 'd'
sto c
lda 0 52
ldc c 27
sto c
lda 0 47
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
ldc c 'm'
sto c
lda 0 13
ldc c 'a'
sto c
lda 0 14
ldc c 't'
sto c
lda 0 15
ldc c 'r'
sto c
lda 0 16
ldc c 'i'
sto c
lda 0 17
ldc c 'x'
sto c
lda 0 18
ldc c ' '
sto c
lda 0 19
ldc c ':'
sto c
lda 0 20
ldc c ' '
sto c
lda 0 21
ldc c 27
sto c
lda 0 53
ldc c '\n'
sto c
lda 0 54
ldc c 'M'
sto c
lda 0 55
ldc c 'a'
sto c
lda 0 56
ldc c 'g'
sto c
lda 0 57
ldc c 'i'
sto c
lda 0 58
ldc c 'c'
sto c
lda 0 59
ldc c ' '
sto c
lda 0 60
ldc c 's'
sto c
lda 0 61
ldc c 'q'
sto c
lda 0 62
ldc c 'u'
sto c
lda 0 63
ldc c 'a'
sto c
lda 0 64
ldc c 'r'
sto c
lda 0 65
ldc c 'e'
sto c
lda 0 66
ldc c 27
sto c
lda 0 67
ldc c '\n'
sto c
lda 0 68
ldc c 'N'
sto c
lda 0 69
ldc c 'o'
sto c
lda 0 70
ldc c ' '
sto c
lda 0 71
ldc c 'M'
sto c
lda 0 72
ldc c 'a'
sto c
lda 0 73
ldc c 'g'
sto c
lda 0 74
ldc c 'i'
sto c
lda 0 75
ldc c 'c'
sto c
lda 0 76
ldc c ' '
sto c
lda 0 77
ldc c 's'
sto c
lda 0 78
ldc c 'q'
sto c
lda 0 79
ldc c 'u'
sto c
lda 0 80
ldc c 'a'
sto c
lda 0 81
ldc c 'r'
sto c
lda 0 82
ldc c 'e'
sto c
lda 0 83
ldc c 27
sto c
lda 0 22
ldc c '%'
sto c
lda 0 23
ldc c 'd'
sto c
lda 0 25
ldc c 'E'
sto c
lda 0 26
ldc c 'n'
sto c
lda 0 27
ldc c 't'
sto c
lda 0 28
ldc c 'e'
sto c
lda 0 29
ldc c 'r'
sto c
lda 0 30
ldc c 'e'
sto c
lda 0 31
ldc c 'd'
sto c
lda 0 32
ldc c ' '
sto c
lda 0 33
ldc c 'm'
sto c
lda 0 34
ldc c 'a'
sto c
lda 0 35
ldc c 't'
sto c
lda 0 36
ldc c 'r'
sto c
lda 0 37
ldc c 'i'
sto c
lda 0 38
ldc c 'x'
sto c
lda 0 39
ldc c ' '
sto c
lda 0 40
ldc c 'i'
sto c
lda 0 41
ldc c 's'
sto c
lda 0 42
ldc c ' '
sto c
lda 0 43
ldc c ':'
sto c
lda 0 44
ldc c ' '
sto c
lda 0 45
ldc c '\n'
sto c
lda 0 46
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 21
ldc i 3
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
ldc i 0
str i 0 17
ldc i 0
str i 0 18
ldc i 0
str i 0 19
ldc i 0
str i 0 20
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
ldc c 'm'
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
ldc c ' '
out c
lda 0 15
dpl a
ldc i 0
sto i
ind i
l2_for_condition:
lod i 0 15
lod i 0 5
les i
conv b i
conv i b
fjp l3_for_after
lda 0 16
dpl a
ldc i 0
sto i
ind i
l5_for_condition:
lod i 0 16
lod i 0 5
les i
conv b i
conv i b
fjp l6_for_after
mst 4
lda 1 17
lda 0 6
lod i 0 15
chk 0 8
ixa 3
lod i 0 16
chk 0 2
ixa 1
cup 2 function_scanf
l4_for_iteration:
ldc a 0
lda 0 16
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
ldc c 'e'
out c
ldc c 'd'
out c
ldc c ' '
out c
ldc c 'm'
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
ldc c 'i'
out c
ldc c 's'
out c
ldc c ' '
out c
ldc c ':'
out c
ldc c ' '
out c
ldc c '\n'
out c
lda 0 15
dpl a
ldc i 0
sto i
ind i
l8_for_condition:
lod i 0 15
lod i 0 5
les i
conv b i
conv i b
fjp l9_for_after
ldc c '\n'
out c
lda 0 16
dpl a
ldc i 0
sto i
ind i
l11_for_condition:
lod i 0 16
lod i 0 5
les i
conv b i
conv i b
fjp l12_for_after
ldc c '\t'
out c
lda 0 6
lod i 0 15
chk 0 8
ixa 3
lod i 0 16
chk 0 2
ixa 1
ind i
out i
l10_for_iteration:
ldc a 0
lda 0 16
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l11_for_condition
l12_for_after:
l7_for_iteration:
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
ujp l8_for_condition
l9_for_after:
ldc a 0
lda 0 17
dpl a
ldc i 0
sto i
ind i
sto i
lda 0 15
dpl a
ldc i 0
sto i
ind i
l14_for_condition:
lod i 0 15
lod i 0 5
les i
conv b i
conv i b
fjp l15_for_after
lda 0 16
dpl a
ldc i 0
sto i
ind i
l17_for_condition:
lod i 0 16
lod i 0 5
les i
conv b i
conv i b
fjp l18_for_after
lod i 0 15
lod i 0 16
equ i
conv b i
conv i b
fjp l19_else
ldc a 0
lda 0 17
dpl a
lod i 0 17
lda 0 6
lod i 0 15
chk 0 8
ixa 3
lod i 0 16
chk 0 2
ixa 1
ind i
add i
sto i
ind i
sto i
l19_else:
l16_for_iteration:
ldc a 0
lda 0 16
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l17_for_condition
l18_for_after:
l13_for_iteration:
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
ujp l14_for_condition
l15_for_after:
lda 0 15
dpl a
ldc i 0
sto i
ind i
l22_for_condition:
lod i 0 15
lod i 0 5
les i
conv b i
conv i b
fjp l23_for_after
ldc a 0
lda 0 18
dpl a
ldc i 0
sto i
ind i
sto i
lda 0 16
dpl a
ldc i 0
sto i
ind i
l25_for_condition:
lod i 0 16
lod i 0 5
les i
conv b i
conv i b
fjp l26_for_after
ldc a 0
lda 0 18
dpl a
lod i 0 18
lda 0 6
lod i 0 15
chk 0 8
ixa 3
lod i 0 16
chk 0 2
ixa 1
ind i
add i
sto i
ind i
sto i
l24_for_iteration:
ldc a 0
lda 0 16
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ujp l25_for_condition
l26_for_after:
lod i 0 17
lod i 0 18
equ i
conv b i
conv i b
fjp l27_else
ldc a 0
lda 0 20
dpl a
ldc i 1
sto i
ind i
sto i
ujp l28_after_if
l27_else:
ldc a 0
lda 0 20
dpl a
ldc i 0
sto i
ind i
sto i
ujp l23_for_after
l28_after_if:
l21_for_iteration:
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
ujp l22_for_condition
l23_for_after:
lda 0 15
dpl a
ldc i 0
sto i
ind i
l30_for_condition:
lod i 0 15
lod i 0 5
les i
conv b i
conv i b
fjp l31_for_after
ldc a 0
lda 0 19
dpl a
ldc i 0
sto i
ind i
sto i
lda 0 16
dpl a
ldc i 0
sto i
ind i
l33_for_condition:
lod i 0 16
lod i 0 5
les i
conv b i
conv i b
fjp l34_for_after
ldc a 0
lda 0 19
dpl a
lod i 0 19
lda 0 6
lod i 0 16
chk 0 8
ixa 3
lod i 0 15
chk 0 2
ixa 1
ind i
add i
sto i
ind i
sto i
l32_for_iteration:
ldc a 0
lda 0 16
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
lod i 0 17
lod i 0 19
equ i
conv b i
conv i b
fjp l35_else
ldc a 0
lda 0 20
dpl a
ldc i 1
sto i
ind i
sto i
ujp l36_after_if
l35_else:
ldc a 0
lda 0 20
dpl a
ldc i 0
sto i
ind i
sto i
ujp l31_for_after
l36_after_if:
l29_for_iteration:
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
ujp l30_for_condition
l31_for_after:
lod i 0 20
ldc i 1
equ i
conv b i
conv i b
fjp l37_else
ldc c '\n'
out c
ldc c 'M'
out c
ldc c 'a'
out c
ldc c 'g'
out c
ldc c 'i'
out c
ldc c 'c'
out c
ldc c ' '
out c
ldc c 's'
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
ujp l38_after_if
l37_else:
ldc c '\n'
out c
ldc c 'N'
out c
ldc c 'o'
out c
ldc c ' '
out c
ldc c 'M'
out c
ldc c 'a'
out c
ldc c 'g'
out c
ldc c 'i'
out c
ldc c 'c'
out c
ldc c ' '
out c
ldc c 's'
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
l38_after_if:
ldc i 0
str i 0 0
retf
retf
