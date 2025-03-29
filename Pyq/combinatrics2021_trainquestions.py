def combinatrics2021():
    return r"""

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{Combinatorics}

\textbf{C1.} Let $S$ be an infinite set of positive integers, such that there exist four pairwise distinct $a, b, c, d \in S$ with $\gcd(a, b) \neq \gcd(c, d)$. Prove that there exist three pairwise distinct $x, y, z \in S$ such that $\gcd(x, y) = \gcd(y, z) \neq \gcd(z, x)$.

\textbf{Solution.} There exists $\alpha \in S$ so that $\{\gcd(\alpha, s) \mid s \in S, s \neq \alpha\}$ contains at least two elements. Since $\alpha$ has only finitely many divisors, there is a $d \mid \alpha$ such that the set $B = \{\beta \in S \mid \gcd(\alpha, \beta) = d\}$ is infinite. Pick $\gamma \in S$ so that $\gcd(\alpha, \gamma) \neq d$. Pick $\beta_1, \beta_2 \in B$ so that $\gcd(\beta_1, \gamma) = \gcd(\beta_2, \gamma) := d'$. If $d = d'$, then $\gcd(\alpha, \beta_1) = \gcd(\gamma, \beta_1) \neq \gcd(\alpha, \gamma)$. If $d \neq d'$, then either $\gcd(\alpha, \beta_1) = \gcd(\alpha, \beta_2) = d$ and $\gcd(\beta_1, \beta_2) \neq d$ or $\gcd(\gamma, \beta_1) = \gcd(\gamma, \beta_2) = d'$ and $\gcd(\beta_1, \beta_2) \neq d'$.

\end{document}




\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{C2.} Let $n \geq 3$ be an integer. An integer $m \geq n+1$ is called \textit{$n$-colourful} if, given infinitely many marbles in each of $n$ colours $C_1, C_2, \dots, C_n$, it is possible to place $m$ of them around a circle so that in any group of $n+1$ consecutive marbles there is at least one marble of colour $C_i$ for each $i = 1, \dots, n$.

Prove that there are only finitely many positive integers which are not $n$-colourful. Find the largest among them.

\textbf{Answer:} $m_{max} = n^2 - n - 1$.

\textbf{Solution.} First suppose that there are $n(n-1) - 1$ marbles. Then for one of the colours, say blue, there are at most $n-2$ marbles, which partition the non-blue marbles into at most $n-2$ groups with at least $(n-1)^2 > n(n-2)$ marbles in total. Thus one of these groups contains at least $n+1$ marbles and this group does not contain any blue marble.

Now suppose that the total number of marbles is at least $n(n-1)$. Then we may write this total number as $nk + j$ with some $k \geq n-1$ and with $0 \leq j \leq n-1$. We place around a circle $k - j$ copies of the colour sequence $[1, 2, 3, \dots, n]$ followed by $j$ copies of the colour sequence $[1, 1, 2, 3, \dots, n]$.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{C3.} A thimblerigger has 2021 thimbles numbered from 1 through 2021. The thimbles are arranged in a circle in arbitrary order. The thimblerigger performs a sequence of 2021 moves; in the $k^{th}$ move, he swaps the positions of the two thimbles adjacent to thimble $k$.

Prove that there exists a value of $k$ such that, in the $k^{th}$ move, the thimblerigger swaps some thimbles $a$ and $b$ such that $a < k < b$.

\textbf{Solution.} Assume the contrary. Say that the $k^{th}$ thimble is the central thimble of the $k^{th}$ move, and its position on that move is the central position of the move.

\textbf{Step 1: Black and white colouring.}

Before the moves start, let us paint all thimbles in white. Then, after each move, we repaint its central thimble in black. This way, at the end of the process all thimbles have become black.

By our assumption, in every move $k$, the two swapped thimbles have the same colour (as their numbers are either both larger or both smaller than $k$). At every moment, assign the colours of the thimbles to their current positions; then the only position which changes its colour in a move is its central position. In particular, each position is central for exactly one move (when it is being repainted to black).

\textbf{Step 2: Red and green colouring.}

Now we introduce a colouring of the positions. If in the $k^{th}$ move, the numbers of the two swapped thimbles are both less than $k$, then we paint the central position of the move in red; otherwise we paint that position in green. This way, each position has been painted in red or green exactly once. We claim that among any two adjacent positions, one becomes green and the other one becomes red; this will provide the desired contradiction since 2021 is odd.

Consider two adjacent positions $A$ and $B$, which are central in the $a^{th}$ and in the $b^{th}$ moves, respectively, with $a < b$. Then in the $a^{th}$ move the thimble at position $B$ is white, and therefore has a number greater than $a$. After the $a^{th}$ move, position $A$ is green and the thimble at position $A$ is black. By the arguments from Step 1, position $A$ contains only black thimbles after the $a^{th}$ step. Therefore, on the $b^{th}$ move, position $A$ contains a black thimble whose number is therefore less than $b$, while thimble $b$ is at position $B$. So position $B$ becomes red, and hence $A$ and $B$ have different colours.

\end{document}








"""