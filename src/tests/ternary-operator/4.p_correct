ldc i 0
ldc i 0
ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 7
ldc r 1.1
str r 0 5
ldc r 2.2
str r 0 6
ldc a 0
ldc i 1
conv i b
ldc i 2
conv i b
or
conv b i
conv i b
fjp l1_else
lda 0 5
ldc i 0
chk 0 1
ixa 1
ind r
ujp l2_after_if
l1_else:
ldc r 1.000000
l2_after_if:
sto r
ldc i 0
str i 0 0
retf
retf
