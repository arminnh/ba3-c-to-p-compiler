ldc i 0
ssp 5
mst 0
cup 0 function_main
hlt

function_main:
ssp 16
ldc i 5
str i 0 7
ldc i 0
str i 0 8
ldc i 0
str i 0 9
ldc i 1
conv i b
fjp l1_else
ldc a 0
ldc i 1
ldc i 1
add i
sto i
ujp l2_after_if
l1_else:
ldc a 0
ldc i 2
ldc i 2
add i
sto i
l2_after_if:
ldc i 1
conv i b
fjp l3_else
ldc a 0
ldc i 1
sto i
l3_else:
ldc i 0
conv i b
ldc i 1
conv i b
or
conv b i
conv i b
fjp l5_else
ujp l6_after_if
l5_else:
l6_after_if:
ldc i 0
conv i b
ldc i 1
conv i b
and
conv b i
conv i b
fjp l7_else
ldc a 0
lod i 0 7
sto i
ujp l8_after_if
l7_else:
ldc i 0
conv i b
fjp l9_else
ldc a 0
lod i 0 8
sto i
ujp l10_after_if
l9_else:
ldc i 1
conv i b
fjp l11_else
ldc a 0
lod i 0 9
sto i
ldc i 0
str i 0 10
l11_else:
l10_after_if:
l8_after_if:
ldc i 2
ldc i 3
equ i
conv b i
conv i b
fjp l13_else
ujp l14_after_if
l13_else:
ldc i 2
ldc i 2
equ i
conv b i
conv i b
fjp l15_else
str a 0 11
ldc i 0
str i 0 14
ldc a 0
lod i 0 14
ldc i 1
add i
sto i
l15_else:
l14_after_if:
l17_while_condition:
ldc i 0
conv i b
fjp l18_while_after
ldc a 0
ldc i 1
ldc i 1
add i
sto i
ujp l17_while_condition
l18_while_after:
ldc i 1
ldc i 2
equ i
conv b i
conv i b
l19_do_while_condition:
ldc a 0
lda 0 9
dpl a
lod i 0 7
lod i 0 8
add i
sto i
ind i
sto i
ldc i 0
str i 0 15
fjp l20_do_while_after
ldc i 1
ldc i 2
equ i
conv b i
ujp l19_do_while_condition
l20_do_while_after:
ldc i 1
str i 0 0
retf
retf
