#
#   tex2txt.py:
#   simple test of equation replacements, from Example.md
#

from yalafi import tex2txt

latex = r"""
\usepackage{amsmath}
We consider\footnote{Thix is a footnote.}
\begin{itemize}
\item a set $M$, a domain $\Omega\subset M$, andx
\item a function $f:M \to [0,1]$.
\end{itemize}

With a constant $\epsilon > 0$, we require
\begin{align}
U_\epsilon(x)
    &\subset M \quad\text{for all } x \in \Omega, \notag \\
f(x)    % LINE 11
    &> 0 \quad\text{for all}\ x \in \Omega \label{l1} \\
f(x)
    &= 0 \quad\text{for all} x \in M \setminus \Omega. \label{l2}
\end{align}
"""

plain_t = r"""
We consider
  a set f-f-f, a domain c-c-c, andx
  a function l-l-l.

With a constant d-d-d, we require
  v-v-v  equal w-w-w for all z-z-z,
  s-s-s  equal u-u-u for all v-v-v
  s-s-s  equal w-w-w for allz-z-z.



Thix is a footnote.
"""

options = tex2txt.Options(lang='en', char=True)
plain, nums = tex2txt.tex2txt(latex, options)

def test_text():
    assert plain == plain_t

