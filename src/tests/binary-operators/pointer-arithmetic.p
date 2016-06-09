ldc i 0
ldc i 0
ldc i 0
ssp 29
lda 0 25
ldc c '%'
sto c
lda 0 26
ldc c 'd'
sto c
lda 0 27
ldc c '\n'
sto c
lda 0 28
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
ldc a 0
str a 0 8
ldc i 0
str i 0 9
l2_for_condition:
lod i 0 9
ldc i 3
les i
conv b i
conv i b
fjp l3_for_after
ldc a 0
lda 0 5
lod i 0 9
chk 0 2
ixa 1
dpl a
lod i 0 9
ldc i 1
add i
sto i
ind i
sto i
l1_for_iteration:
ldc a 0
lda 0 9
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l2_for_condition
l3_for_after:
ldc a 0
lda 0 5
ldc i 0
chk 0 2
ixa 1
dpl a
ldc i 1
sto i
ind i
sto i
ldc a 0
lda 0 5
ldc i 1
chk 0 2
ixa 1
dpl a
ldc i 2
sto i
ind i
sto i
ldc a 0
lda 0 5
ldc i 2
chk 0 2
ixa 1
dpl a
ldc i 3
sto i
ind i
sto i
ldc a 0
lda 0 8
dpl a
lda 0 5
sto a
ind a
sto a
ldc i 0
str i 0 10
l5_for_condition:
lod i 0 10
ldc i 3
les i
conv b i
conv i b
fjp l6_for_after
lda 0 5
lod i 0 10
chk 0 2
ixa 1
ind i
out i
ldc c '\n'
out c
l4_for_iteration:
ldc a 0
lda 0 10
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l5_for_condition
l6_for_after:
ldc i 0
str i 0 11
l8_for_condition:
lod i 0 11
ldc i 3
les i
conv b i
conv i b
fjp l9_for_after
ldc a 0
lod a 0 8
dpl a
lod a 0 8
ind i
lod i 0 11
add i
ldc i 1
add i
sto i
ind i
sto i
ldc a 0
lda 0 8
dpl a
lod a 0 8
conv a i
ldc i 1
ldc i 1
mul i
add i
conv i a
sto a
ind a
sto a
l7_for_iteration:
ldc a 0
lda 0 11
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l8_for_condition
l9_for_after:
ldc i 0
str i 0 12
l11_for_condition:
lod i 0 12
ldc i 3
les i
conv b i
conv i b
fjp l12_for_after
lda 0 5
lod i 0 12
chk 0 2
ixa 1
ind i
out i
ldc c '\n'
out c
l10_for_iteration:
ldc a 0
lda 0 12
dpl a
dpl a
ind i
inc i 1
sto i
ind i
sto i
ujp l11_for_condition
l12_for_after:
ldc i 0
str i 0 13
ldc i 0
str i 0 14
ldc i 0
str i 0 15
ldc i 0
str i 0 16
ldc a 0
lda 0 13
ldc i 0
chk 0 3
ixa 2
ldc i 0
chk 0 1
ixa 1
dpl a
ldc i 5
sto i
ind i
sto i
ldc a 0
lda 0 13
ldc i 1
chk 0 3
ixa 2
ldc i 0
chk 0 1
ixa 1
dpl a
ldc i 6
sto i
ind i
sto i
lda 0 13
str a 0 17
lod a 0 17
ldc i 0
chk 0 1
ixa 1
ind i
out i
ldc c '\n'
out c
ldc a 0
lda 0 17
dpl a
dpl a
ind a
conv a i
inc i 2
conv i a
sto a
ind a
sto a
lod a 0 17
ldc i 0
chk 0 1
ixa 1
ind i
out i
ldc c '\n'
out c
ldc a 0
lda 0 17
dpl a
dpl a
ind a
conv a i
dec i 2
conv i a
sto a
ind a
sto a
lod a 0 17
ldc i 0
chk 0 1
ixa 1
ind i
out i
ldc c '\n'
out c
ldc a 0
lda 0 17
dpl a
lod a 0 17
conv a i
ldc i 1
neg i
ldc i 2
mul i
sub i
conv i a
sto a
ind a
sto a
lod a 0 17
ldc i 0
chk 0 1
ixa 1
ind i
out i
ldc c '\n'
out c
ldc a 0
ldc i 0
sto i
ldc i 0
str i 0 0
retf
retf
