ldc i 0
ssp 9
lda 0 5
ldc c 'a'
sto c
lda 0 7
ldc c 'b'
sto c
mst 0
cup 0 function_main
hlt

function_sum:
ssp 7
lod i 0 5
lod i 0 6
add i
str i 0 0
retf
retf

function_main:
ssp 11
ldc i 1
str i 0 7
l1_while_condition:
lod i 0 7
ldc i 3
neq i
conv b i
conv i b
fjp l2_while_after
ldc a 0
lda 0 7
dpl a
mst 1
lda 0 7
dpl a
ldc i 2
sto i
ind i
ldc i 1
cup 2 function_sum
sto i
ind i
sto i
ujp l1_while_condition
l2_while_after:
lod i 0 7
ldc i 3
neq i
conv b i
conv i b
ldc i 1
conv i b
and
conv b i
conv i b
fjp l3_else
ldc a 0
lod i 0 7
sto i
ujp l4_after_if
l3_else:
ldc a 0
lod i 0 7
ldc i 3
equ i
conv b i
sto i
l4_after_if:
ldc i 0
str i 0 8
ldc a 0
lod i 0 8
sto i
str a 0 9
ldc a 0
ldc i 1
conv i b
ldc i 2
conv i b
or
conv b i
conv i b
fjp l5_else
lda 0 9
ldc i 0
chk 0 1
ixa 1
ind r
ujp l6_after_if
l5_else:
lda 0 9
ldc i 1
chk 0 1
ixa 1
ind r
l6_after_if:
sto r
ldc a 0
ldc i 1
conv i b
ldc i 2
conv i b
or
conv b i
conv i b
fjp l7_else
lda 0 9
ldc i 0
chk 0 1
ixa 1
ind r
ujp l8_after_if
l7_else:
ldc r 0.500000
l8_after_if:
sto r
ldc a 0
ldc i 5
conv i b
ldc i 2
conv i b
and
conv b i
conv i b
fjp l9_else
lda 1 0
ujp l10_after_if
l9_else:
lda 1 2
l10_after_if:
sto a
ldc i 1
str i 0 0
retf
retf

function_sub:
ssp 7
lod i 0 5
str i 0 0
retf
retf

function_abc:
ssp 7
retf
