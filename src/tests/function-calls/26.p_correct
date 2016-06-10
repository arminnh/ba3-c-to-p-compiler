ldc i 0
ldc i 0
ldc i 0
ssp 109
lda 0 61
ldc c '%'
sto c
lda 0 62
ldc c '5'
sto c
lda 0 63
ldc c 'c'
sto c
lda 0 64
ldc c '\n'
sto c
lda 0 65
ldc c 27
sto c
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
lda 0 94
ldc c '%'
sto c
lda 0 95
ldc c '5'
sto c
lda 0 96
ldc c 's'
sto c
lda 0 97
ldc c '\n'
sto c
lda 0 98
ldc c 27
sto c
lda 0 57
ldc c '%'
sto c
lda 0 58
ldc c 'd'
sto c
lda 0 59
ldc c '\n'
sto c
lda 0 60
ldc c 27
sto c
lda 0 99
ldc c '%'
sto c
lda 0 100
ldc c 's'
sto c
lda 0 101
ldc c '\n'
sto c
lda 0 102
ldc c 27
sto c
lda 0 50
ldc c 'h'
sto c
lda 0 51
ldc c 'e'
sto c
lda 0 103
ldc c 'h'
sto c
lda 0 104
ldc c 'e'
sto c
lda 0 105
ldc c 'l'
sto c
lda 0 106
ldc c 'l'
sto c
lda 0 107
ldc c 'o'
sto c
lda 0 108
ldc c 27
sto c
lda 0 71
ldc c 'l'
sto c
lda 0 72
ldc c 'l'
sto c
lda 0 73
ldc c 'o'
sto c
lda 0 74
ldc c 27
sto c
lda 0 84
ldc c 't'
sto c
lda 0 85
ldc c 'o'
sto c
lda 0 86
ldc c 'o'
sto c
lda 0 87
ldc c 't'
sto c
lda 0 88
ldc c 'o'
sto c
lda 0 89
ldc c 'o'
sto c
lda 0 90
ldc c 'l'
sto c
lda 0 91
ldc c 'o'
sto c
lda 0 92
ldc c 'n'
sto c
lda 0 93
ldc c 27
sto c
mst 0
cup 0 function_main
hlt

function_main:
ssp 22
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
ldc i 19
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
ldc a 1
lda 1 45
ind a
sto a
ldc a 0
ldc i 0
sto i
ldc a 2
ldc a 1
ind a
dpl a
ind c
l41_count_loop:
ldc c 27
neq c
fjp l42_after_count_loop
ldc a 0
ldc a 0
ind i
inc i 1
sto i
inc a 1
dpl a
ind c
ujp l41_count_loop
l42_after_count_loop:
sto a
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
l43_padding_loop:
ldc a 0
ind i
ldc i 0
grt i
fjp l44_after_padding_loop
ldc c ' '
out c
ldc a 0
ldc a 0
ind i
dec i 1
sto i
ujp l43_padding_loop
l44_after_padding_loop:
ldc a 1
ind a
l45_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l46_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l45_out_loop
l46_after_out_loop:
ldc c '\n'
out c
ldc i 75
out i
ldc c '\n'
out c
ldc i 75
neg i
out i
ldc c '\n'
out c
ldc c ' '
out c
ldc c ' '
out c
ldc c ' '
out c
ldc c ' '
out c
ldc c 'a'
out c
ldc c '\n'
out c
lda 0 5
ldc c 'h'
sto c
lda 0 6
ldc c 'e'
sto c
lda 0 7
ldc c 27
sto c
ldc a 1
lda 0 5
sto a
ldc a 0
ldc i 0
sto i
ldc a 2
ldc a 1
ind a
dpl a
ind c
l47_count_loop:
ldc c 27
neq c
fjp l48_after_count_loop
ldc a 0
ldc a 0
ind i
inc i 1
sto i
inc a 1
dpl a
ind c
ujp l47_count_loop
l48_after_count_loop:
sto a
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
l49_padding_loop:
ldc a 0
ind i
ldc i 0
grt i
fjp l50_after_padding_loop
ldc c ' '
out c
ldc a 0
ldc a 0
ind i
dec i 1
sto i
ujp l49_padding_loop
l50_after_padding_loop:
ldc a 1
ind a
l51_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l52_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l51_out_loop
l52_after_out_loop:
ldc c '\n'
out c
lda 0 8
ldc c 'l'
sto c
lda 0 9
ldc c 'l'
sto c
lda 0 10
ldc c 'o'
sto c
lda 0 11
ldc c 27
sto c
ldc a 1
lda 0 8
sto a
ldc a 0
ldc i 0
sto i
ldc a 2
ldc a 1
ind a
dpl a
ind c
l53_count_loop:
ldc c 27
neq c
fjp l54_after_count_loop
ldc a 0
ldc a 0
ind i
inc i 1
sto i
inc a 1
dpl a
ind c
ujp l53_count_loop
l54_after_count_loop:
sto a
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
l55_padding_loop:
ldc a 0
ind i
ldc i 0
grt i
fjp l56_after_padding_loop
ldc c ' '
out c
ldc a 0
ldc a 0
ind i
dec i 1
sto i
ujp l55_padding_loop
l56_after_padding_loop:
ldc a 1
ind a
l57_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l58_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l57_out_loop
l58_after_out_loop:
ldc c '\n'
out c
ldc a 1
lda 0 8
sto a
ldc a 0
ldc i 0
sto i
ldc a 1
ind a
l59_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l60_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l59_out_loop
l60_after_out_loop:
ldc c '\n'
out c
lda 0 12
ldc c 't'
sto c
lda 0 13
ldc c 'o'
sto c
lda 0 14
ldc c 'o'
sto c
lda 0 15
ldc c 't'
sto c
lda 0 16
ldc c 'o'
sto c
lda 0 17
ldc c 'o'
sto c
lda 0 18
ldc c 'l'
sto c
lda 0 19
ldc c 'o'
sto c
lda 0 20
ldc c 'n'
sto c
lda 0 21
ldc c 27
sto c
ldc a 1
lda 0 12
sto a
ldc a 0
ldc i 0
sto i
ldc a 2
ldc a 1
ind a
dpl a
ind c
l61_count_loop:
ldc c 27
neq c
fjp l62_after_count_loop
ldc a 0
ldc a 0
ind i
inc i 1
sto i
inc a 1
dpl a
ind c
ujp l61_count_loop
l62_after_count_loop:
sto a
ldc a 0
ldc i 5
ldc a 0
ind i
sub i
sto i
l63_padding_loop:
ldc a 0
ind i
ldc i 0
grt i
fjp l64_after_padding_loop
ldc c ' '
out c
ldc a 0
ldc a 0
ind i
dec i 1
sto i
ujp l63_padding_loop
l64_after_padding_loop:
ldc a 1
ind a
l65_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l66_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l65_out_loop
l66_after_out_loop:
ldc c '\n'
out c
ldc a 1
lda 1 98
ind a
sto a
ldc a 0
ldc i 0
sto i
ldc a 1
ind a
l67_out_loop:

dpl a
ind c
ldc c 27
neq c
fjp l68_after_out_loop
dpl a
ind c
out c
inc a 1
ujp l67_out_loop
l68_after_out_loop:
ldc c '\n'
out c
ldc i 0
str i 0 0
retf
retf
