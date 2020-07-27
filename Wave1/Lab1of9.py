# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods 
#and try them out here. Endeavor to copy the link without the first # comment sign beginning it.

string = "Computer Engineering"


print(f"""
 .capitalize() method: {string.capitalize()}

 .casefold() method: {string.casefold()}
      
 .center() method: {string.center(20)}

 .count() method: {string.count('e')}

 .encode() method: {string.encode()}
 
 .endswith() method: {string.endswith('ing')}     
 
 .expandtabs() method: {string.expandtabs(1)}

 .find() method: {string.find('n')}

 .format() method: {string.format(1)}

 .index method: {string.index('C')}

 .isalnum() method: {string.isalnum()}

 .isalpha() method: {string.isalpha()}

 .isascii() method: {string.isascii()}

 .isdecimal() method: {string.isdecimal()}

 .isdigit() method: {string.isdigit()}

 .isidentifier() method: {string.isidentifier()}

 .islower() method: {string.islower()}

 .isnumeric() method: {string.isnumeric()}

 .isprintable() method: {string.isprintable()}

 .isspace() method: {string.isspace()}

 .istitle() method: {string.istitle()}

 .isupper() method: {string.isupper()}

 .join() method: {string.join('//')}

 .ljust() method: {string.ljust(277)}

 .lower() method: {string.lower()}

 .lstrip() method: {string.lstrip()}

 .partition() method: {string.partition('.')}

 .replace() method: {string.replace('Computer', 'Systems')}

 .rfind() method: {string.rfind('ing')}

 .rindex() method: {string.rindex('ing')}

 .rjust() method: {string.rjust(4)}

 .rpartition() method: {string.rpartition('/')}

 .rsplit() method: {string.rsplit()}

 .split() method: {string.split()}

 .splitlines() method: {string.splitlines()}

 .startswith() method: {string.startswith('E')}

 .strip() method: {string.strip()}

 .swapcase() method: {string.swapcase()}

 .title() method: {string.title()}

 .upper() method: {string.upper()}

 .zfill() method: {string.zfill(5)}""")