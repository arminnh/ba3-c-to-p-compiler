ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 9
ldc i 1
str i 0 5
ldc i 6
str i 0 6
ldc i 0
str i 0 7
ldc i 0
str i 0 8
ldc a 0
lda 0 7
dpl a
lod i 0 5
lod i 0 6
add i
conv i b
lod i 0 8
conv i b
and
conv b i
lod i 0 6
ldc i 2
mul i
dpl i
ldc a 0
lod i 0 6
sto i
ldc a 0
ind i
div i
ldc a 0
ind i
mul i
sub i
sub i
conv i b
lod i 0 5
conv i b
or
conv b i
conv i b
fjp l1_else
lod i 0 6
lod i 0 6
dpl i
ldc a 0
lod i 0 5
sto i
ldc a 0
ind i
div i
ldc a 0
ind i
mul i
sub i
ldc i 1
add i
les i
conv b i
ujp l2_after_if
l1_else:
lod i 0 6
lod i 0 5
ldc i 1
neg i
mul i
sub i
l2_after_if:
sto i
ind i
sto i
ldc i 0
str i 0 0
retf
retf
