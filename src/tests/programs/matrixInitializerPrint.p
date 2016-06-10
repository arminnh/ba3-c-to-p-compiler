ldc i 0
ldc i 0
ldc i 0
ssp 28
lda 0 8
ldc c ' '
sto c
lda 0 9
ldc c ' '
sto c
lda 0 10
ldc c '['
sto c
lda 0 11
ldc c ' '
sto c
lda 0 12
ldc c 27
sto c
lda 0 20
ldc c ' '
sto c
lda 0 21
ldc c ']'
sto c
lda 0 22
ldc c ','
sto c
lda 0 23
ldc c '\n'
sto c
lda 0 24
ldc c 27
sto c
lda 0 13
ldc c '%'
sto c
lda 0 14
ldc c '3'
sto c
lda 0 15
ldc c 'd'
sto c
lda 0 16
ldc c 27
sto c
lda 0 17
ldc c ','
sto c
lda 0 18
ldc c ' '
sto c
lda 0 5
ldc c '['
sto c
lda 0 6
ldc c '\n'
sto c
lda 0 25
ldc c ']'
sto c
lda 0 26
ldc c '\n'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 247
str a 0 5
ldc c '['
out c
ldc c '\n'
out c
ldc i 0
str i 0 245
l2_for_condition:
lod i 0 245
ldc i 15
les i
conv b i
conv i b
fjp l3_for_after
ldc c ' '
out c
ldc c ' '
out c
ldc c '['
out c
ldc c ' '
out c
ldc i 0
str i 0 246
l5_for_condition:
lod i 0 246
ldc i 16
les i
conv b i
conv i b
fjp l6_for_after
ldc a 2
lda 0 5
lod i 0 245
chk 0 239
ixa 16
lod i 0 246
chk 0 15
ixa 1
ind i
sto i
ldc a 1
ldc a 2
ind i
sto i
ldc a 0
ldc i 1
sto i
ldc a 1
ind i
ldc i 0
les i
fjp l7_loop1
ldc a 0
ldc a 0
ind i
inc i 1
sto i
ldc a 1
ldc a 1
ind i
neg i
sto i
l7_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l8_after_loop1
ldc a 0
ldc a 0
ind i
inc i 1
sto i
ldc a 1
ldc a 1
ind i
ldc i 10
div i
sto i
ujp l7_loop1
l8_after_loop1:
ldc a 0
ldc i 3
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l9_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l11_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l9_loop2
l11_no_padding:
ldc a 2
ind i
out i
lod i 0 246
ldc i 16
ldc i 1
sub i
les i
conv b i
conv i b
fjp l12_else
ldc c ','
out c
ldc c ' '
out c
l12_else:
l4_for_iteration:
ldc a 0
lda 0 246
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l5_for_condition
l6_for_after:
ldc c ' '
out c
ldc c ']'
out c
ldc c ','
out c
ldc c '\n'
out c
l1_for_iteration:
ldc a 0
lda 0 245
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l2_for_condition
l3_for_after:
ldc c ']'
out c
ldc c '\n'
out c
retf
