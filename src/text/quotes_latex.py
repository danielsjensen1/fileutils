#  TODO:  Create test case.
from os.path import expanduser


def read_quotes(filename):
    quotes = []
    with open(filename, 'r') as f:
        quote = []
        for line in f:
            if line == '\n':
                quotes.append('\n'.join(quote))
                quote = []
            else:
                quote.append(line)
    return quotes

def latex_quotes(filename, quotes, prefix=None, suffix=None):
    #  TODO:  Fix problem with single quote followed by double quote.  This
    #         should put a "\," between them.
    text = ''
    with open(filename, 'w') as f:
        for quote in quotes:
            line = quote.decode("utf-8")
            line = line.replace(u"\u2018", "'")
            line = line.replace(u"\u2019", "'")
            line = line.replace(u"\u201c", "``")
            line = line.replace(u"\u201d", "''")
            num_colons = line.count(':')
#             print line
            if prefix != None:
                f.write(prefix)
            if num_colons == 1:
                f.write('\\begin{center}\n')
                print(line.split(':', 1))
                line1, line2 = line.split(':', 1)
                f.write(line1 + ':')
                f.write('\n\\linebreak\n\n')
                f.write(line2)
                f.write('\\end{center}\n')
            else:
                f.write(line)
            if suffix != None:
                f.write(suffix)
    return text

if __name__ == '__main__':
    quotes = read_quotes(expanduser('~/Downloads/quotes/jensen.txt'))
    prefix = r"""
\newpage
\thispagestyle{empty}
\topskip0pt
\StripedBorder
\vfill
\vspace*{\fill}
"""
    suffix = r"""\vspace*{\fill}
"""
    print latex_quotes(expanduser('~/Downloads/quotes/jensen_latex.tex'),
                       quotes, prefix=prefix, suffix=suffix)
