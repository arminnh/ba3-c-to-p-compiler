/* A Bison parser, made by GNU Bison 3.0.2.  */

/* Bison implementation for Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.2"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 1 "pmachine.y" /* yacc.c:339  */

#include <string>
using namespace std;

#include "stackelement.h"
#include "stackmachine.h"
#include "pmachine.h"

#include "add.h"
#include "sub.h"
#include "mul.h"
#include "div.h"
#include "neg.h"
#include "and.h"
#include "or.h"
#include "not.h"
#include "equ.h"
#include "geq.h"
#include "leq.h"
#include "les.h"
#include "grt.h"
#include "neq.h"
#include "ldo.h"
#include "ldc.h"
#include "ind.h"
#include "sro.h"
#include "sto.h"
#include "ujp.h"
#include "fjp.h"
#include "ixj.h"
#include "ixa.h"
#include "inc.h"
#include "dec.h"
#include "chk.h"
#include "dpl.h"
#include "ldd.h"
#include "sli.h"
#include "new.h"
#include "lod.h"
#include "lda.h"
#include "str.h"
#include "mst.h"
#include "cup.h"
#include "ssp.h"
#include "sep.h"
#include "ent.h"
#include "retf.h"
#include "retp.h"
#include "movs.h"
#include "movd.h"
#include "smp.h"
#include "cupi.h"
#include "mstf.h"
#include "hlt.h"
#include "in.h"
#include "out.h"
#include "conv.h"

//#define YACCOUTPUT


extern StackMachine Pmachine;
extern int linecount;
extern int yylex();

// prototypes
void yyerror(string msg);



#line 137 "pmachine.tab.c" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "pmachine.tab.h".  */
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
#line 71 "pmachine.y" /* yacc.c:355  */

	int integernumbervalue;
	double realnumbervalue;
	bool booleanvalue;
	string *textvalue;
	char charvalue;
	enum Stacktypes {r, i, b, c, a} type;

#line 252 "pmachine.tab.c" /* yacc.c:355  */
};
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_PMACHINE_TAB_H_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 267 "pmachine.tab.c" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  191
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   350

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  66
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  58
/* YYNRULES -- Number of rules.  */
#define YYNRULES  172
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  300

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   320

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   156,   156,   157,   159,   160,   162,   163,   164,   166,
     172,   178,   184,   190,   196,   202,   208,   214,   220,   226,
     232,   238,   244,   250,   256,   262,   268,   274,   280,   286,
     292,   298,   304,   310,   316,   322,   328,   334,   340,   346,
     352,   358,   364,   370,   376,   382,   388,   394,   400,   406,
     412,   418,   424,   430,   436,   442,   448,   454,   460,   467,
     471,   476,   477,   481,   485,   490,   491,   493,   505,   510,
     522,   527,   539,   545,   557,   562,   574,   579,   584,   589,
     594,   615,   620,   641,   646,   667,   672,   693,   698,   719,
     724,   745,   750,   771,   776,   780,   784,   788,   792,   796,
     800,   805,   827,   832,   853,   858,   879,   884,   888,   893,
     897,   902,   906,   911,   915,   920,   941,   946,   967,   972,
     976,   981,  1002,  1007,  1011,  1016,  1037,  1042,  1047,  1068,
    1074,  1078,  1083,  1104,  1109,  1113,  1118,  1122,  1127,  1131,
    1136,  1140,  1145,  1149,  1154,  1159,  1164,  1168,  1173,  1177,
    1182,  1186,  1191,  1195,  1200,  1204,  1209,  1214,  1218,  1222,
    1226,  1230,  1234,  1239,  1243,  1247,  1251,  1255,  1259,  1263,
    1268,  1309,  1313
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "add_instr", "sub_instr", "mul_instr",
  "div_instr", "neg_instr", "and_instr", "or_instr", "not_instr",
  "equ_instr", "geq_instr", "leq_instr", "les_instr", "grt_instr",
  "neq_instr", "ldo_instr", "ldc_instr", "ind_instr", "sro_instr",
  "sto_instr", "ujp_instr", "fjp_instr", "ixj_instr", "ixa_instr",
  "inc_instr", "dec_instr", "chk_instr", "dpl_instr", "ldd_instr",
  "sli_instr", "new_instr", "lod_instr", "lda_instr", "str_instr",
  "mst_instr", "cup_instr", "ssp_instr", "sep_instr", "ent_instr",
  "retf_instr", "retp_instr", "movs_instr", "movd_instr", "smp_instr",
  "cupi_instr", "mstf_instr", "hlt_instr", "inp_instr", "out_instr",
  "conv_instr", "blank", "endline", "boolean_specifier", "real_specifier",
  "integer_specifier", "character_specifier", "address_specifier",
  "boolvalue", "integervalue", "charactervalue", "realvalue",
  "addressvalue", "appliedlabel", "defininglabel", "$accept", "Grammar",
  "EndlineRepeater", "InstructionSequence", "Instruction", "numeric",
  "arbitrary", "space", "add_instruction", "sub_instruction",
  "mul_instruction", "div_instruction", "neg_instruction",
  "and_instruction", "or_instruction", "not_instruction",
  "equ_instruction", "geq_instruction", "leq_instruction",
  "les_instruction", "grt_instruction", "neq_instruction",
  "ldo_instruction", "ldc_instruction", "ind_instruction",
  "sro_instruction", "sto_instruction", "ujp_instruction",
  "fjp_instruction", "ixj_instruction", "ixa_instruction",
  "inc_instruction", "dec_instruction", "chk_instruction",
  "dpl_instruction", "ldd_instruction", "sli_instruction",
  "new_instruction", "lod_instruction", "lda_instruction",
  "str_instruction", "mst_instruction", "cup_instruction",
  "ssp_instruction", "sep_instruction", "ent_instruction",
  "retf_instruction", "retp_instruction", "movs_instruction",
  "movd_instruction", "smp_instruction", "cupi_instruction",
  "mstf_instruction", "hlt_instruction", "inp_instruction",
  "out_instruction", "conv_instruction", "label_introduction", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320
};
# endif

#define YYPACT_NINF -73

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-73)))

#define YYTABLE_NINF -1

#define yytable_value_is_error(Yytable_value) \
  0

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     140,     5,    27,    37,    43,    48,   -73,   -73,   -73,    50,
      52,    54,    58,    59,    60,    62,    64,    67,    68,    69,
      70,    71,    72,    73,    74,    76,    79,    80,    82,    83,
     -73,    84,    86,    89,   191,   193,   194,   195,   196,   -73,
     -73,   198,   199,   200,   203,   205,   -73,   206,   207,   208,
     -73,   -73,    91,   -48,   285,   -16,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,    15,    38,   -73,
      38,   -73,    38,   -73,    38,   -73,    38,   -73,   165,   -73,
     165,   -73,   165,   -73,   165,   -73,   165,   -73,   165,   -73,
     165,   -73,   216,   -73,   165,   -73,   165,   -73,   165,   -73,
      34,   -73,    35,   -73,    39,   -73,    41,   -73,   165,   -73,
     165,   -73,    47,   -73,   165,   -73,    49,   -73,   165,   -73,
     165,   -73,    53,   -73,   165,   -73,    55,   -73,    57,   -73,
      77,   -73,   138,   -73,   142,   -73,   150,   -73,   157,   -73,
     167,   -73,   168,   -73,   169,   -73,   221,   -73,   226,   -73,
     165,   -73,   -73,   -16,   -48,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,    15,    15,    15,    15,    15,    15,   -73,
      15,   -73,   -73,   -73,   -73,   -73,    15,    15,    15,   -73,
     -73,   -73,    15,    15,    15,   -73,    15,   -73,   -73,    15,
     -73,   -73,   -73,    15,    15,   -73,   -73,   -73,   -73,   -73,
     -73,    15,   -73,   -73,   -73,    15,   -48,   173,    81,    46,
     175,    36,   176,   178,   179,   180,   184,   202,   204,   277,
      63,   278,   279,   280,   210,   165,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,    15,   -73,    15,
     -73,   -73,   -73,   -73,   -73,   -73,   281,   282,   -73,   -73
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       2,     0,     0,     0,     0,     0,    77,    78,    79,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     127,     0,     0,     0,     0,     0,     0,     0,     0,   144,
     145,     0,     0,     0,     0,     0,   156,     0,     0,     0,
       5,   172,     0,     8,     3,     0,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    57,    58,    68,    66,     0,    70,
       0,    72,     0,    74,     0,    76,     0,    81,     0,    83,
       0,    85,     0,    87,     0,    89,     0,    91,     0,    93,
       0,   100,     0,   102,     0,   104,     0,   106,     0,   108,
       0,   110,     0,   112,     0,   114,     0,   116,     0,   118,
       0,   120,     0,   122,     0,   124,     0,   126,     0,   129,
       0,   131,     0,   133,     0,   135,     0,   137,     0,   139,
       0,   141,     0,   143,     0,   147,     0,   149,     0,   151,
       0,   153,     0,   155,     0,   162,     0,   169,     0,   171,
       0,     1,     4,     0,     7,    65,    59,    60,    67,    69,
      71,    73,    75,    62,    63,    64,    61,    80,    82,    84,
      86,    88,    90,     0,     0,     0,     0,     0,     0,   101,
       0,   105,   107,   109,   111,   113,     0,     0,     0,   121,
     123,   125,     0,     0,     0,   134,     0,   138,   140,     0,
     146,   148,   150,     0,     0,   159,   158,   157,   160,   161,
     168,   164,   165,   166,   167,     0,     6,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    92,    96,    94,    95,
      97,    98,    99,   103,   115,   117,   119,     0,   130,     0,
     136,   142,   152,   154,   163,   170,     0,     0,   128,   132
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
     -73,   -73,   -51,   -73,    75,   153,   -72,    -2,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73,
     -73,   -73,   -73,   -73,   -73,   -73,   -73,   -73
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    52,    53,    54,    55,   206,   207,   108,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_uint16 yytable[] =
{
     110,   112,   114,   116,   194,   192,   106,   118,   120,   122,
     124,   126,   128,   130,   132,   134,   136,   138,   140,   142,
     144,   146,   148,   150,   152,   154,   156,   158,   109,   160,
     162,   164,   166,   168,   170,   172,   174,    50,   111,   176,
     178,   180,   182,   184,   113,   186,   188,   190,   208,   115,
     209,   117,   210,   119,   211,   121,   212,   107,   213,   123,
     125,   127,   219,   129,   220,   131,   221,   107,   133,   135,
     137,   139,   141,   143,   145,   147,   226,   149,   227,   107,
     151,   153,   229,   155,   157,   159,   231,   161,   232,   107,
     163,   191,   234,   196,   197,   107,   280,   281,   222,   223,
     107,   225,   107,   224,   107,   195,   107,   228,   278,   230,
     107,   107,   107,   233,   107,   235,   107,   236,   255,   107,
     107,   107,   107,   107,   107,   107,   107,   290,   107,   193,
       0,   107,   107,     0,   107,   107,   107,   237,   107,     0,
     277,   107,   256,     1,     2,     3,     4,     5,     6,     7,
       8,     9,    10,    11,    12,    13,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    42,    43,    44,    45,    46,    47,
      48,    49,   165,    50,   167,   169,   171,   173,   238,   175,
     177,   179,   239,   295,   181,    51,   183,   185,   187,   189,
     240,   257,   258,   259,   260,   261,   262,   241,   263,   203,
     196,   197,   204,   205,   264,   265,   266,   242,   243,   244,
     267,   268,   269,   276,   270,   279,   282,   271,   283,   284,
     285,   272,   273,   107,   286,   107,   107,   107,   107,   274,
     107,   107,   107,   275,     0,   107,     0,   107,   107,   107,
     107,   198,   287,   199,   288,   200,   294,   201,     0,   202,
     214,   215,   216,   217,   218,   245,   246,   247,   248,   249,
     250,   251,   252,   253,   254,   296,     0,   297,     1,     2,
       3,     4,     5,     6,     7,     8,     9,    10,    11,    12,
      13,    14,    15,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
      43,    44,    45,    46,    47,    48,    49,   289,   291,   292,
     293,   298,   299,     0,     0,     0,     0,     0,     0,     0,
      51
};

static const yytype_int16 yycheck[] =
{
       2,     3,     4,     5,    55,    53,     1,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,     1,    31,
      32,    33,    34,    35,    36,    37,    38,    53,     1,    41,
      42,    43,    44,    45,     1,    47,    48,    49,   120,     1,
     122,     1,   124,     1,   126,     1,   128,    52,   130,     1,
       1,     1,   134,     1,   136,     1,   138,    52,     1,     1,
       1,     1,     1,     1,     1,     1,   148,     1,   150,    52,
       1,     1,   154,     1,     1,     1,   158,     1,   160,    52,
       1,     0,   164,    55,    56,    52,    60,    61,    64,    64,
      52,    60,    52,    64,    52,   107,    52,    60,    62,    60,
      52,    52,    52,    60,    52,    60,    52,    60,   190,    52,
      52,    52,    52,    52,    52,    52,    52,    64,    52,    54,
      -1,    52,    52,    -1,    52,    52,    52,    60,    52,    -1,
      59,    52,   193,     3,     4,     5,     6,     7,     8,     9,
      10,    11,    12,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    49,
      50,    51,     1,    53,     1,     1,     1,     1,    60,     1,
       1,     1,    60,   275,     1,    65,     1,     1,     1,     1,
      60,   213,   214,   215,   216,   217,   218,    60,   220,    54,
      55,    56,    57,    58,   226,   227,   228,    60,    60,    60,
     232,   233,   234,    60,   236,    60,    60,   239,    60,    60,
      60,   243,   244,    52,    60,    52,    52,    52,    52,   251,
      52,    52,    52,   255,    -1,    52,    -1,    52,    52,    52,
      52,   108,    60,   110,    60,   112,    56,   114,    -1,   116,
      54,    55,    56,    57,    58,    54,    55,    56,    57,    58,
      54,    55,    56,    57,    58,   287,    -1,   289,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    60,    60,    60,
      60,    60,    60,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      65
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     3,     4,     5,     6,     7,     8,     9,    10,    11,
      12,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,    48,    49,    50,    51,
      53,    65,    67,    68,    69,    70,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105,   106,   107,
     108,   109,   110,   111,   112,   113,   114,   115,   116,   117,
     118,   119,   120,   121,   122,   123,     1,    52,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     1,    73,     1,    73,     1,    73,     1,    73,     1,
      73,     0,    53,    70,    68,    73,    55,    56,    71,    71,
      71,    71,    71,    54,    57,    58,    71,    72,    72,    72,
      72,    72,    72,    72,    54,    55,    56,    57,    58,    72,
      72,    72,    64,    64,    64,    60,    72,    72,    60,    72,
      60,    72,    72,    60,    72,    60,    60,    60,    60,    60,
      60,    60,    60,    60,    60,    54,    55,    56,    57,    58,
      54,    55,    56,    57,    58,    72,    68,    73,    73,    73,
      73,    73,    73,    73,    73,    73,    73,    73,    73,    73,
      73,    73,    73,    73,    73,    73,    60,    59,    62,    60,
      60,    61,    60,    60,    60,    60,    60,    60,    60,    60,
      64,    60,    60,    60,    56,    72,    73,    73,    60,    60
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    66,    67,    67,    68,    68,    69,    69,    69,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    70,
      70,    70,    70,    70,    70,    70,    70,    70,    70,    71,
      71,    72,    72,    72,    72,    73,    73,    74,    74,    75,
      75,    76,    76,    77,    77,    78,    78,    79,    80,    81,
      82,    82,    83,    83,    84,    84,    85,    85,    86,    86,
      87,    87,    88,    88,    89,    89,    89,    89,    89,    89,
      89,    90,    90,    91,    91,    92,    92,    93,    93,    94,
      94,    95,    95,    96,    96,    97,    97,    98,    98,    99,
      99,   100,   100,   101,   101,   102,   102,   103,   104,   104,
     105,   105,   106,   106,   107,   107,   108,   108,   109,   109,
     110,   110,   111,   111,   112,   113,   114,   114,   115,   115,
     116,   116,   117,   117,   118,   118,   119,   120,   120,   120,
     120,   120,   120,   121,   121,   121,   121,   121,   121,   121,
     122,   122,   123
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     0,     1,     2,     1,     3,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     2,     1,     3,     2,     3,
       2,     3,     2,     3,     2,     3,     2,     1,     1,     1,
       3,     2,     3,     2,     3,     2,     3,     2,     3,     2,
       3,     2,     5,     2,     5,     5,     5,     5,     5,     5,
       2,     3,     2,     5,     2,     3,     2,     3,     2,     3,
       2,     3,     2,     3,     2,     5,     2,     5,     2,     5,
       2,     3,     2,     3,     2,     3,     2,     1,     7,     2,
       5,     2,     7,     2,     3,     2,     5,     2,     3,     2,
       3,     2,     5,     2,     1,     1,     3,     2,     3,     2,
       3,     2,     5,     2,     5,     2,     1,     3,     3,     3,
       3,     3,     2,     5,     3,     3,     3,     3,     3,     2,
       5,     2,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 9:
#line 167 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "add_instruction completed" << endl;	
						#endif
					}
#line 1597 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 10:
#line 173 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "sub_instruction completed" << endl;	
						#endif
					}
#line 1607 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 11:
#line 179 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "mul_instruction completed" << endl;	
						#endif
					}
#line 1617 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 12:
#line 185 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "div_instruction completed" << endl;	
						#endif
					}
#line 1627 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 13:
#line 191 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "neg_instruction completed" << endl;	
						#endif
					}
#line 1637 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 14:
#line 197 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "and_instruction completed" << endl;	
						#endif
					}
#line 1647 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 15:
#line 203 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "or_instruction completed" << endl;	
						#endif
					}
#line 1657 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 16:
#line 209 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "not_instruction completed" << endl;	
						#endif
					}
#line 1667 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 17:
#line 215 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "equ_instruction completed" << endl;	
						#endif
					}
#line 1677 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 18:
#line 221 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "geq_instruction completed" << endl;	
						#endif
					}
#line 1687 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 19:
#line 227 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "leq_instruction completed" << endl;	
						#endif
					}
#line 1697 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 20:
#line 233 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "les_instruction completed" << endl;	
						#endif
					}
#line 1707 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 21:
#line 239 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "grt_instruction completed" << endl;	
						#endif
					}
#line 1717 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 22:
#line 245 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "neq_instruction completed" << endl;	
						#endif
					}
#line 1727 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 23:
#line 251 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ldo_instruction completed" << endl;	
						#endif
					}
#line 1737 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 24:
#line 257 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ldc_instruction completed" << endl;	
						#endif
					}
#line 1747 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 25:
#line 263 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ind_instruction completed" << endl;	
						#endif
					}
#line 1757 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 26:
#line 269 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "sro_instruction completed" << endl;	
						#endif
					}
#line 1767 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 27:
#line 275 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "sto_instruction completed" << endl;	
						#endif
					}
#line 1777 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 28:
#line 281 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ujp_instruction completed" << endl;	
						#endif
					}
#line 1787 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 29:
#line 287 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "fjp_instruction completed" << endl;	
						#endif
					}
#line 1797 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 30:
#line 293 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ixj_instruction completed" << endl;	
						#endif
					}
#line 1807 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 31:
#line 299 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ixa_instruction completed" << endl;	
						#endif
					}
#line 1817 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 32:
#line 305 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "inc_instruction completed" << endl;	
						#endif
					}
#line 1827 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 33:
#line 311 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "dec_instruction completed" << endl;	
						#endif
					}
#line 1837 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 34:
#line 317 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "chk_instruction completed" << endl;	
						#endif
					}
#line 1847 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 35:
#line 323 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "dpl_instruction completed" << endl;	
						#endif
					}
#line 1857 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 36:
#line 329 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ldd_instruction completed" << endl;	
						#endif
					}
#line 1867 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 37:
#line 335 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "sli_instruction completed" << endl;	
						#endif
					}
#line 1877 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 38:
#line 341 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "new_instruction completed" << endl;	
						#endif
					}
#line 1887 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 39:
#line 347 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "lod_instruction completed" << endl;	
						#endif
					}
#line 1897 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 40:
#line 353 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "lda_instruction completed" << endl;	
						#endif
					}
#line 1907 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 41:
#line 359 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "str_instruction completed" << endl;	
						#endif
					}
#line 1917 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 42:
#line 365 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "mst_instruction completed" << endl;	
						#endif
					}
#line 1927 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 43:
#line 371 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "cup_instruction completed" << endl;	
						#endif
					}
#line 1937 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 44:
#line 377 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ssp_instruction completed" << endl;	
						#endif
					}
#line 1947 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 45:
#line 383 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "sep_instruction completed" << endl;	
						#endif
					}
#line 1957 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 46:
#line 389 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "ent_instruction completed" << endl;	
						#endif
					}
#line 1967 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 47:
#line 395 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "retf_instruction completed" << endl;	
						#endif
					}
#line 1977 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 48:
#line 401 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "retp_instruction completed" << endl;	
						#endif
					}
#line 1987 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 49:
#line 407 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "movs_instruction completed" << endl;	
						#endif
					}
#line 1997 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 50:
#line 413 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "movd_instruction completed" << endl;	
						#endif
					}
#line 2007 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 51:
#line 419 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "smp_instruction completed" << endl;	
						#endif
					}
#line 2017 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 52:
#line 425 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "cupi_instruction completed" << endl;	
						#endif
					}
#line 2027 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 53:
#line 431 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "mstf_instruction completed" << endl;	
						#endif
					}
#line 2037 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 54:
#line 437 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "hlt_instruction completed" << endl;	
						#endif
					}
#line 2047 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 55:
#line 443 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "inp_instruction completed" << endl;	
						#endif
					}
#line 2057 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 56:
#line 449 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "out_instruction completed" << endl;	
						#endif
					}
#line 2067 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 57:
#line 455 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUPUT
							cout << "conv_instruction completed" << endl;
						#endif
					}
#line 2077 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 58:
#line 461 "pmachine.y" /* yacc.c:1646  */
    {
						#ifdef YACCOUTPUT
							cout << "label_introduction completed" << endl;	
						#endif
					}
#line 2087 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 59:
#line 468 "pmachine.y" /* yacc.c:1646  */
    {
						(yyval.type) = YYSTYPE::r;
					}
#line 2095 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 60:
#line 472 "pmachine.y" /* yacc.c:1646  */
    {
						(yyval.type) = YYSTYPE::i;
					}
#line 2103 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 62:
#line 478 "pmachine.y" /* yacc.c:1646  */
    {
								(yyval.type) = YYSTYPE::b;
							}
#line 2111 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 63:
#line 482 "pmachine.y" /* yacc.c:1646  */
    {
								(yyval.type) = YYSTYPE::c;
							}
#line 2119 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 64:
#line 486 "pmachine.y" /* yacc.c:1646  */
    {
								(yyval.type) = YYSTYPE::a;
							}
#line 2127 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 67:
#line 494 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Add(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Add(real));
								break;
						}
					}
#line 2143 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 68:
#line 506 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction add: add [i|r]");
					}
#line 2151 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 69:
#line 511 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sub(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sub(real));
								break;
						}
					}
#line 2167 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 70:
#line 523 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction sub: sub [i|r]");
					}
#line 2175 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 71:
#line 528 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Mul(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Mul(real));
								break;
						}
					}
#line 2191 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 72:
#line 540 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction mul: mul [i|r]");
					}
#line 2199 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 73:
#line 546 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Div(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Div(real));
								break;
						}
					}
#line 2215 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 74:
#line 558 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction div: div [i|r]");
					}
#line 2223 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 75:
#line 563 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Neg(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Neg(real));
								break;
						}
					}
#line 2239 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 76:
#line 575 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction neg: neg [i|r]");
					}
#line 2247 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 77:
#line 580 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new And());
					}
#line 2255 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 78:
#line 585 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Or());
					}
#line 2263 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 79:
#line 590 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Not());
					}
#line 2271 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 80:
#line 595 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Equ(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Equ(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Equ(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Equ(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Equ(boolean));
								break;
						}
					}
#line 2296 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 81:
#line 616 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction equ: equ [i|r|a|b|c]");
					}
#line 2304 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 82:
#line 621 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Geq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Geq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Geq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Geq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Geq(boolean));
								break;
						}
					}
#line 2329 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 83:
#line 642 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction geq: geq [i|r|a|b|c]");
					}
#line 2337 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 84:
#line 647 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Leq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Leq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Leq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Leq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Leq(boolean));
								break;
						}
					}
#line 2362 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 85:
#line 668 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction leq: leq [i|r|a|b|c]");
					}
#line 2370 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 86:
#line 673 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Les(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Les(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Les(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Les(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Les(boolean));
								break;
						}
					}
#line 2395 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 87:
#line 694 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction les: les [i|r|a|b|c]");
					}
#line 2403 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 88:
#line 699 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Grt(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Grt(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Grt(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Grt(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Grt(boolean));
								break;
						}
					}
#line 2428 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 89:
#line 720 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction grt: grt [i|r|a|b|c]");
					}
#line 2436 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 90:
#line 725 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Neq(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Neq(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Neq(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Neq(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Neq(boolean));
								break;
						}
					}
#line 2461 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 91:
#line 746 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction neq: neq [i|r|a|b|c]");
					}
#line 2469 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 92:
#line 751 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-2].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Ldo(integer, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Ldo(real, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Ldo(character, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Ldo(address, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Ldo(boolean, (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2494 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 93:
#line 772 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ldo: ldo [i|r|a|b|c]");
					}
#line 2502 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 94:
#line 777 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(real, new StackReal((yyvsp[0].realnumbervalue))));
					}
#line 2510 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 95:
#line 781 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(integer, new StackInteger((yyvsp[0].integernumbervalue))));
					}
#line 2518 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 96:
#line 785 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(boolean, new StackBoolean((yyvsp[0].booleanvalue))));
					}
#line 2526 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 97:
#line 789 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(character, new StackCharacter(static_cast<char>((yyvsp[0].integernumbervalue)))));
					}
#line 2534 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 98:
#line 793 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(character, new StackCharacter(static_cast<char>((yyvsp[0].charvalue)))));
					}
#line 2542 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 99:
#line 797 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldc(address, new StackAddress((yyvsp[0].integernumbervalue))));
					}
#line 2550 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 100:
#line 801 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ldc: ldc [i|r|a|b|c] [value]");
					}
#line 2558 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 101:
#line 806 "pmachine.y" /* yacc.c:1646  */
    {
						
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Ind(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Ind(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Ind(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Ind(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Ind(boolean));
								break;
						}
					}
#line 2584 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 102:
#line 828 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ind: ind [i|r|a|b|c]");
					}
#line 2592 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 103:
#line 833 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-2].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sro(integer, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sro(real, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sro(character, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sro(address, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sro(boolean, (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2617 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 104:
#line 854 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction sro: sro [i|r|a|b|c] [integer]");
					}
#line 2625 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 105:
#line 859 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sto(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sto(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sto(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sto(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sto(boolean));
								break;
						}
					}
#line 2650 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 106:
#line 880 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction sto: sto [i|r|a|b|c]");
					}
#line 2658 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 107:
#line 885 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ujp(*(yyvsp[0].textvalue)));
					}
#line 2666 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 108:
#line 889 "pmachine.y" /* yacc.c:1646  */
    {	
						yyerror("instruction ujp: ujp [label]");
					}
#line 2674 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 109:
#line 894 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Fjp(*(yyvsp[0].textvalue)));
					}
#line 2682 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 110:
#line 898 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction fjp: fjp [label]");
					}
#line 2690 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 111:
#line 903 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ixj(*(yyvsp[0].textvalue)));
					}
#line 2698 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 112:
#line 907 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ixj: ixj [label]");
					}
#line 2706 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 113:
#line 912 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ixa((yyvsp[0].integernumbervalue)));
					}
#line 2714 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 114:
#line 916 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ixa: ixa [integer]");
					}
#line 2722 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 115:
#line 921 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-2].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Inc(integer, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Inc(real, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Inc(character, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Inc(address, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Inc(boolean, (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2747 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 116:
#line 942 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction inc: inc [i|r|a|b|c] [integervalue]");
					}
#line 2755 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 117:
#line 947 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-2].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Dec(integer, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Dec(real, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Dec(character, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Dec(address, (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Dec(boolean, (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2780 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 118:
#line 968 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction dec: dec [i|r|a|b|c] [integervalue]");
					}
#line 2788 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 119:
#line 973 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Chk((yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
					}
#line 2796 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 120:
#line 977 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction chk: chk [integervalue] [integervalue]");
					}
#line 2804 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 121:
#line 982 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Dpl(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Dpl(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Dpl(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Dpl(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Dpl(boolean));
								break;
						}
					}
#line 2829 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 122:
#line 1003 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction dpl: dpl [i|r|a|b|c]");
					}
#line 2837 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 123:
#line 1008 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ldd((yyvsp[0].integernumbervalue)));
					}
#line 2845 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 124:
#line 1012 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ldd: ldd [integervalue]");
					}
#line 2853 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 125:
#line 1017 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Sli(integer));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Sli(real));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Sli(character));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Sli(address));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Sli(boolean));
								break;
						}
					}
#line 2878 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 126:
#line 1038 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction sli: sli [i|r|a|b|c]");
					}
#line 2886 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 127:
#line 1043 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new New());
					}
#line 2894 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 128:
#line 1048 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-4].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Lod(integer, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Lod(real, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Lod(character, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Lod(address, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Lod(boolean, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2919 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 129:
#line 1069 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction lod: lod [i|r|a|b|c] [integervalue] [integervalue]");
					}
#line 2927 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 130:
#line 1075 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Lda((yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
					}
#line 2935 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 131:
#line 1079 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction lda: lda [integervalue] [integervalue]");
					}
#line 2943 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 132:
#line 1084 "pmachine.y" /* yacc.c:1646  */
    {
						switch((yyvsp[-4].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Str(integer, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Str(real, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Str(character, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Str(address, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Str(boolean, (yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
								break;
						}
					}
#line 2968 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 133:
#line 1105 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction str: str [i|r|a|b|c] [intergervalue] [integervalue]");
					}
#line 2976 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 134:
#line 1110 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Mst((yyvsp[0].integernumbervalue)));
					}
#line 2984 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 135:
#line 1114 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction mst: mst [integer]");
					}
#line 2992 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 136:
#line 1119 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Cup((yyvsp[-2].integernumbervalue), *(yyvsp[0].textvalue)));
					}
#line 3000 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 137:
#line 1123 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction cup: cup [integervalue] [integervalue]");
					}
#line 3008 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 138:
#line 1128 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ssp((yyvsp[0].integernumbervalue)));
					}
#line 3016 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 139:
#line 1132 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ssp: ssp [integervalue]");
					}
#line 3024 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 140:
#line 1137 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Sep((yyvsp[0].integernumbervalue)));
					}
#line 3032 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 141:
#line 1141 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction sep: sep [integervalue]");
					}
#line 3040 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 142:
#line 1146 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Ent((yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
					}
#line 3048 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 143:
#line 1150 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction ent: ent [integervalue] [integervalue]");
					}
#line 3056 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 144:
#line 1155 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Retf());
					}
#line 3064 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 145:
#line 1160 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Retp());
					}
#line 3072 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 146:
#line 1165 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Movs((yyvsp[0].integernumbervalue)));
					}
#line 3080 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 147:
#line 1169 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction movs: movs [integervalue]");
					}
#line 3088 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 148:
#line 1174 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Movd((yyvsp[0].integernumbervalue)));
					}
#line 3096 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 149:
#line 1178 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction movd: movd [integervalue]");
					}
#line 3104 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 150:
#line 1183 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Smp((yyvsp[0].integernumbervalue)));
					}
#line 3112 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 151:
#line 1187 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction smp: smp [integervalue]");
					}
#line 3120 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 152:
#line 1192 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Cupi((yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
					}
#line 3128 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 153:
#line 1196 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction cupi: cupi [integervalue] [integervalue]");
					}
#line 3136 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 154:
#line 1201 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Mstf((yyvsp[-2].integernumbervalue), (yyvsp[0].integernumbervalue)));
					}
#line 3144 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 155:
#line 1205 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction mstf: mstf [integervalue] [integervalue]");
					}
#line 3152 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 156:
#line 1210 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Hlt());
					}
#line 3160 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 157:
#line 1215 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new In(integer));
					}
#line 3168 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 158:
#line 1219 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new In(real));
					}
#line 3176 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 159:
#line 1223 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new In(boolean));
					}
#line 3184 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 160:
#line 1227 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new In(character));
					}
#line 3192 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 161:
#line 1231 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction in: input of address at runtime is forbidden");
					}
#line 3200 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 162:
#line 1235 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction in: in [i|r|b|c]");
					}
#line 3208 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 163:
#line 1240 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(real, true));
					}
#line 3216 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 164:
#line 1244 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(real, false));
					}
#line 3224 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 165:
#line 1248 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(integer));
					}
#line 3232 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 166:
#line 1252 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(character));				
					}
#line 3240 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 167:
#line 1256 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(address));
					}
#line 3248 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 168:
#line 1260 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addInstruction(new Out(boolean));
					}
#line 3256 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 169:
#line 1264 "pmachine.y" /* yacc.c:1646  */
    {
						yyerror("instruction out: out r i\ninstruction out: out [r|i|a|b|c]");
					}
#line 3264 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 170:
#line 1269 "pmachine.y" /* yacc.c:1646  */
    {
						StackElementType type;
						switch((yyvsp[0].type))
						{
							case YYSTYPE::i:
								type = integer;
								break;
							case YYSTYPE::r:
								type = real;
								break;
							case YYSTYPE::c:
								type = character;
								break;
							case YYSTYPE::a:
								type = address;
								break;
							case YYSTYPE::b:
								type = boolean;
								break;
						}
												
						switch((yyvsp[-2].type))
						{
							case YYSTYPE::i:
								Pmachine.addInstruction(new Conv(integer, type));
								break;
							case YYSTYPE::r:
								Pmachine.addInstruction(new Conv(real, type));
								break;
							case YYSTYPE::c:
								Pmachine.addInstruction(new Conv(character, type));
								break;
							case YYSTYPE::a:
								Pmachine.addInstruction(new Conv(address, type));
								break;
							case YYSTYPE::b:
								Pmachine.addInstruction(new Conv(boolean, type));
								break;
						}
					}
#line 3309 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 171:
#line 1310 "pmachine.y" /* yacc.c:1646  */
    {
							yyerror("instruction conv: conv [r|i|a|b|c] [r|i|a|b|c]");
						}
#line 3317 "pmachine.tab.c" /* yacc.c:1646  */
    break;

  case 172:
#line 1314 "pmachine.y" /* yacc.c:1646  */
    {
						Pmachine.addLabel(*(yyvsp[0].textvalue));
					}
#line 3325 "pmachine.tab.c" /* yacc.c:1646  */
    break;


#line 3329 "pmachine.tab.c" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 1319 "pmachine.y" /* yacc.c:1906  */


/////////////////////////////////////////////////////////////////////////////
// programs section

void yyerror(string msg)
{
	cerr << "--> line " << linecount << ": " << msg << endl;
	exit(0);
}

