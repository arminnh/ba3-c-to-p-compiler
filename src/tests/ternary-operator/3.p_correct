ldc i 0
ldc i 0
ldc i 0
ssp 9
lda 0 5
ldc c 'a'
sto c
lda 0 6
ldc c 27
sto c
lda 0 7
ldc c 'b'
sto c
lda 0 8
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 5
ldc a 0
ldc i 3
conv i b
fjp l1_else
lda 1 5
ujp l2_after_if
l1_else:
lda 1 7
l2_after_if:
sto a
ldc i 0
str i 0 0
retf
retf
