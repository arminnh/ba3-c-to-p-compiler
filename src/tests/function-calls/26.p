ldc i 0
ldc i 0
ldc i 0
ssp 53
lda 0 40
ldc c '%'
sto c
lda 0 41
ldc c '5'
sto c
lda 0 42
ldc c 'd'
sto c
lda 0 43
ldc c '\n'
sto c
lda 0 44
ldc c 27
sto c
lda 0 45
ldc c '%'
sto c
lda 0 46
ldc c '5'
sto c
lda 0 47
ldc c 's'
sto c
lda 0 48
ldc c '\n'
sto c
lda 0 49
ldc c 27
sto c
lda 0 50
ldc c 'h'
sto c
lda 0 51
ldc c 'e'
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 5
ldc a 2
ldc i 5
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
fjp l1_loop1
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
l1_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l2_after_loop1
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
ujp l1_loop1
l2_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l3_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l5_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l3_loop2
l5_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 5
neg i
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
fjp l6_loop1
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
l6_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l7_after_loop1
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
ujp l6_loop1
l7_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l8_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l10_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l8_loop2
l10_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 25
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
fjp l11_loop1
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
l11_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l12_after_loop1
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
ujp l11_loop1
l12_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l13_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l15_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l13_loop2
l15_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 350
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
fjp l16_loop1
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
l16_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l17_after_loop1
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
ujp l16_loop1
l17_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l18_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l20_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l18_loop2
l20_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 4300
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
fjp l21_loop1
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
l21_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l22_after_loop1
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
ujp l21_loop1
l22_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l23_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l25_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l23_loop2
l25_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 5400
neg i
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
fjp l26_loop1
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
l26_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l27_after_loop1
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
ujp l26_loop1
l27_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l28_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l30_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l28_loop2
l30_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 64000
neg i
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
fjp l31_loop1
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
l31_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l32_after_loop1
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
ujp l31_loop1
l32_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l33_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l35_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l33_loop2
l35_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
ldc a 2
ldc i 764000
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
fjp l36_loop1
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
l36_loop1:
ldc a 1
ind i
ldc i 9
grt i
fjp l37_after_loop1
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
ujp l36_loop1
l37_after_loop1:
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
ldc a 1
ldc i 0
sto i
l38_loop2:
ldc a 1
ind i
ldc a 0
ind i
les i
fjp l40_no_padding
ldc c ' '
out c
ldc a 1
ldc a 1
ind i
inc i 1
sto i
ujp l38_loop2
l40_no_padding:
ldc a 2
ind i
out i
ldc c '\n'
out c
lda 1 45
out a
ldc c '\n'
out c
retf
