int main(void) {
    0   <   2;
    2.0 < 5.0;
    "a" < "b";
    'B' < 'b';

    0   >   2;
    2.0 > 5.0;
    "a" > "b";
    'B' > 'b';

    0   <=   2;
    2.0 <= 5.0;
    "a" <= "b";
    'B' <= 'b';

    0   >=   2;
    2.0 >= 5.0;
    "a" >= "b";
    'B' >= 'b';

    0   ==   2;
    2.0 == 5.0;
    "a" == "b";
    'B' == 'b';

    0   ==   2;
    2.0 == 5.0;
    "a" == "b";
    'B' == 'b';

    0   !=   2;
    2.0 != 5.0;
    "a" != "b";
    'B' != 'b';

    0   +   2;
    2.0 + 5.0;
    // TODO: generate error here
    // "a" + "b";
    'B' + 'b';

    0   -   2;
    2.0 - 5.0;
    "a" - "b";
    'B' - 'b';

    0   /   2;
    2.0 / 5.0;
    //"a" / "b"; error: invalid operands to binary + (have 'char *' and 'char *')
    'B' / 'b';

    0   *   2;
    2.0 * 5.0;
    //"a" * "b"; error: invalid operands to binary + (have 'char *' and 'char *')
    'B' * 'b';

    0   %   2;
    //2.0 % 5.0; error: invalid operands to binary + (have 'char *' and 'char *')
    //"a" % "b"; error: invalid operands to binary + (have 'char *' and 'char *')
    'B' % 'b';

    1 || 2;
    0 || 0;
    5 || 5;
    5 || 5 || 6 && 0;

    5 && 4 || 0;

    return 1;
}
