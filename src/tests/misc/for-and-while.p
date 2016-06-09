ldc i 0
ldc i 0
ldc i 0
ssp 21
lda 0 13
ldc c 'i'
sto c
lda 0 14
ldc c ' '
sto c
lda 0 15
ldc c '='
sto c
lda 0 16
ldc c ' '
sto c
lda 0 17
ldc c '%'
sto c
lda 0 18
ldc c 'd'
sto c
lda 0 19
ldc c '\n'
sto c
lda 0 20
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_f:
ssp 6
retp

function_main:
ssp 9
ldc i 5
str i 0 5
ldc i 5
str i 0 6
l2_for_condition:
lod i 0 5
ldc i 30
les i
conv b i
conv i b
fjp l3_for_after
ldc i 5
str i 0 7
l5_for_condition:
ldc b t
fjp l6_for_after
lod i 0 7
ldc i 7
geq i
conv b i
conv i b
fjp l7_else
ujp l6_for_after
l7_else:
l4_for_iteration:
ldc a 0
lda 0 7
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l5_for_condition
l6_for_after:
lod i 0 5
ldc i 25
geq i
conv b i
conv i b
fjp l9_else
ujp l3_for_after
l9_else:
l1_for_iteration:
ldc a 0
lda 0 5
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l2_for_condition
l3_for_after:
ldc i 0
str i 0 8
l11_while_condition:
lod i 0 8
ldc i 30
les i
conv b i
conv i b
fjp l12_while_after
ldc a 0
lda 0 8
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ldc c 'i'
out c
ldc c ' '
out c
ldc c '='
out c
ldc c ' '
out c
lod i 0 8
out i
ldc c '\n'
out c
ujp l11_while_condition
l12_while_after:
lod i 0 8
ldc i 35
les i
conv b i
conv i b
l13_do_while_condition:
ldc a 0
lda 0 8
dpl a
dpl a
ind i
inc i 1
sto i
ind i
dec i 1
sto i
ldc c 'i'
out c
ldc c ' '
out c
ldc c '='
out c
ldc c ' '
out c
lod i 0 8
out i
ldc c '\n'
out c
fjp l14_do_while_after
lod i 0 8
ldc i 35
les i
conv b i
ujp l13_do_while_condition
l14_do_while_after:
ldc i 0
str i 0 0
retf
retf
