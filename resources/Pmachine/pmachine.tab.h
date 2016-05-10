/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2013 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_PMACHINE_TAB_H_INCLUDED
# define YY_YY_PMACHINE_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    add_instr = 258,
    sub_instr = 259,
    mul_instr = 260,
    div_instr = 261,
    neg_instr = 262,
    and_instr = 263,
    or_instr = 264,
    not_instr = 265,
    equ_instr = 266,
    geq_instr = 267,
    leq_instr = 268,
    les_instr = 269,
    grt_instr = 270,
    neq_instr = 271,
    ldo_instr = 272,
    ldc_instr = 273,
    ind_instr = 274,
    sro_instr = 275,
    sto_instr = 276,
    ujp_instr = 277,
    fjp_instr = 278,
    ixj_instr = 279,
    ixa_instr = 280,
    inc_instr = 281,
    dec_instr = 282,
    chk_instr = 283,
    dpl_instr = 284,
    ldd_instr = 285,
    sli_instr = 286,
    new_instr = 287,
    lod_instr = 288,
    lda_instr = 289,
    str_instr = 290,
    mst_instr = 291,
    cup_instr = 292,
    ssp_instr = 293,
    sep_instr = 294,
    ent_instr = 295,
    retf_instr = 296,
    retp_instr = 297,
    movs_instr = 298,
    movd_instr = 299,
    smp_instr = 300,
    cupi_instr = 301,
    mstf_instr = 302,
    hlt_instr = 303,
    inp_instr = 304,
    out_instr = 305,
    conv_instr = 306,
    blank = 307,
    endline = 308,
    boolean_specifier = 309,
    real_specifier = 310,
    integer_specifier = 311,
    character_specifier = 312,
    address_specifier = 313,
    boolvalue = 314,
    integervalue = 315,
    charactervalue = 316,
    realvalue = 317,
    addressvalue = 318,
    appliedlabel = 319,
    defininglabel = 320
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE YYSTYPE;
union YYSTYPE
{
#line 71 "pmachine.y" /* yacc.c:1909  */

	int integernumbervalue;
	double realnumbervalue;
	bool booleanvalue;
	string *textvalue;
	char charvalue;
	enum Stacktypes {r, i, b, c, a} type;

#line 129 "pmachine.tab.h" /* yacc.c:1909  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_PMACHINE_TAB_H_INCLUDED  */
