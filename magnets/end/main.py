"""
end\n
a general purpose programming language
"""

import ply.lex as lex
import ply.yacc as yacc

import end
import lexer

print end.__appname__ + " " + "v" + end.__version__
print "courtesy of the " + end.__author__
print "   lex version: " + lex.__version__
print "   yacc version: " + yacc.__version__


lexer.get_filename()
lexer.get_tokens()
lexer.print_tokens()
lexer.get_tokens_from_file('tokens.noc')
