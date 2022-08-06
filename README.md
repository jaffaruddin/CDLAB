# CDLab


1. identify keywords...

  $lex lex.l
  $cc lex.yy.c
  $./a.out var.c

2, 3, 4. 
  $ gcc [programName].c -o programName
  $ ./programName
  
  or
  (??)
  $ gcc [programName].c
  $ ./a.out
  
5. LALR
  
  $lex parser.l
  $yacc –d parser.y
  $cc lex.yy.c y.tab.c –ll –lm
