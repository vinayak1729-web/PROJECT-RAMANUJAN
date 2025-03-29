def combinatrics_2021():
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







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\section*{C4.}

The kingdom of Anisotropy consists of $n$ cities. For every two cities there exists exactly one direct one-way road between them. We say that a path from $X$ to $Y$ is a sequence of roads such that one can move from $X$ to $Y$ along this sequence without returning to an already visited city. A collection of paths is called \emph{diverse} if no road belongs to two or more paths in the collection.

Let $A$ and $B$ be two distinct cities in Anisotropy. Let $N_{AB}$ denote the maximal number of paths in a diverse collection of paths from $A$ to $B$. Similarly, let $N_{BA}$ denote the maximal number of paths in a diverse collection of paths from $B$ to $A$. Prove that the equality $N_{AB} = N_{BA}$ holds if and only if the number of roads going out from $A$ is the same as the number of roads going out from $B$.

\section*{Solution 1.}

We write $X \to Y$ (or $Y \to X$) if the road between $X$ and $Y$ goes from $X$ to $Y$. Notice that, if there is any route moving from $X$ to $Y$ (possibly passing through some cities more than once), then there is a path from $X$ to $Y$ consisting of some roads in the route. Indeed, any cycle in the route may be removed harmlessly; after some removals one obtains a path.

Say that a path is \emph{short} if it consists of one or two roads.

Partition all cities different from $A$ and $B$ into four groups, $I$, $O$, $\mathcal{A}$, and $\mathcal{B}$ according to the following rules: for each city $C$,

\begin{align*}
C \in I &\iff A \to C \to B; \\
C \in \mathcal{A} &\iff A \to C \to B; \\
C \in O &\iff A \to C \to B; \\
C \in \mathcal{B} &\iff A \to C \to B.
\end{align*}

\textbf{Lemma.} Let $P$ be a diverse collection consisting of $p$ paths from $A$ to $B$. Then there exists a diverse collection consisting of at least $p$ paths from $A$ to $B$ and containing all short paths from $A$ to $B$.

\textbf{Proof.} In order to obtain the desired collection, modify $P$ as follows.

If there is a direct road $A \to B$ and the path consisting of this single road is not in $P$, merely add it to $P$.

Now consider any city $C \in \mathcal{A}$ such that the path $A \to C \to B$ is not in $P$. If $P$ contains at most one path containing a road $A \to C$ or $C \to B$, remove that path (if it exists), and add the path $A \to C \to B$ to $P$ instead. Otherwise, $P$ contains two paths of the forms $A \to C \dots B$ and $A \dots C \to B$, where $C \dots B$ and $A \dots C$ are some paths. In this case, we recombine the edges to form two new paths $A \to C \to B$ and $A \dots C \dots B$ (removing cycles from the latter if needed). Now we replace the old two paths in $P$ with the two new ones.

After any operation described above, the number of paths in the collection does not decrease, and the collection remains diverse. Applying such operation to each $C \in \mathcal{A}$, we obtain the desired collection. $\Box$

Back to the problem, assume, without loss of generality, that there is a road $A \to B$, and let $a$ and $b$ denote the numbers of roads going out from $A$ and $B$, respectively. Choose a diverse collection $P$ consisting of $N_{AB}$ paths from $A$ to $B$. We will transform it into a diverse collection $Q$ consisting of at least $N_{AB} + (b-a)$ paths from $B$ to $A$. This construction yields

\[ N_{BA} \geq N_{AB} + (b-a); \]
similarly, we get
\[ N_{AB} \geq N_{BA} + (a-b), \]
whence
\[ N_{BA} - N_{AB} = b-a. \]
This yields the desired equivalence.

Apply the lemma to get a diverse collection $P'$ of at least $N_{AB}$ paths containing all $|\mathcal{A}|+1$ short paths from $A$ to $B$. Notice that the paths in $P'$ contain no edge of a short path from $B$ to $A$. Each non-short path in $P'$ has the form $A \to C \dots D \to B$, where $C \dots D$ is a path from some city $C \in I$ to some city $D \in O$. For each such path, put into $Q$ the path $B \to C \to D \to A$; also put into $Q$ all short paths from $B$ to $A$. Clearly, the collection $Q$ is diverse.

Now, all roads going out from $A$ end in the cities from $I \cup \mathcal{A} \cup \{B\}$, while all roads going out from $B$ end in the cities from $I \cup \mathcal{B}$. Therefore,

\[ a = |I| + |\mathcal{A}| + 1, \quad b = |I| + |\mathcal{B}|, \]
and hence
\[ a - b = |\mathcal{A}| - |\mathcal{B}| + 1. \]

On the other hand, since there are $|\mathcal{A}|+1$ short paths from $A$ to $B$ (including $A \to B$) and $|\mathcal{B}|$ short paths from $B$ to $A$, we infer

\[ |Q| - |P'| - (|\mathcal{A}| + 1) + |\mathcal{B}| \geq N_{AB} + (b-a), \]
as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\section*{C5.}

Let $n$ and $k$ be two integers with $n > k \geq 1$. There are $2n+1$ students standing in a circle. Each student $S$ has $2k$ neighbours—namely, the $k$ students closest to $S$ on the right, and the $k$ students closest to $S$ on the left.

Suppose that $n+1$ of the students are girls, and the other $n$ are boys. Prove that there is a girl with at least $k$ girls among her neighbours.

\section*{Solution.}

We replace the girls by 1's, and the boys by 0's, getting the numbers $a_1, a_2, \dots, a_{2n+1}$ arranged in a circle. We extend this sequence periodically by letting $a_{2n+1+k} = a_k$ for all $k \in \mathbb{Z}$. We get an infinite periodic sequence

\[ \dots, a_1, a_2, \dots, a_{2n+1}, a_1, a_2, \dots, a_{2n+1}, \dots \]

Consider the numbers $b_i = a_i + a_{i-k-1} - 1 \in \{-1, 0, 1\}$ for all $i \in \mathbb{Z}$. We know that
\[ b_{m+1} + b_{m+2} + \dots + b_{m+2n+1} = 1 \qquad (m \in \mathbb{Z}); \tag{1} \]

In particular, this yields that there exists some $i_0$ with $b_{i_0} = 1$. Now we want to find an index $i$ such that

\[ b_i = 1 \quad \text{and} \quad b_{i+1} + b_{i+2} + \dots + b_{i+k} \geq 0. \tag{2} \]

This will imply that $a_i = 1$ and

\[ (a_{i-k} + a_{i-k+1} + \dots + a_{i-1}) + (a_{i+1} + a_{i+2} + \dots + a_{i+k}) \geq k, \]
as desired.

Suppose, to the contrary, that for every index $i$ with $b_i = 1$ the sum $b_{i+1} + b_{i+2} + \dots + b_{i+k}$ is negative. We start from some index $i_0$ with $b_{i_0} = 1$ and construct a sequence $i_0, i_1, i_2, \dots$ where $i_j$ ($j > 0$) is the smallest possible index such that $i_j > i_{j-1} + k$ and $b_{i_j} = 1$. We can choose two numbers among $i_0, i_1, \dots, i_{2n+1}$ which are congruent modulo $2n+1$ (without loss of generality, we may assume that these numbers are $i_0$ and $i_T$).

On the one hand, for every $j$ with $0 \leq j \leq T-1$ we have

\[ S_j := b_{i_j} + b_{i_j+1} + b_{i_j+2} + \dots + b_{i_{j+1}-1} \leq b_{i_j} + b_{i_j+1} + b_{i_j+2} + \dots + b_{i_j+k} \leq 0 \]
since $b_{i_j+k+1}, \dots, b_{i_{j+1}-1} \leq 0$. On the other hand, since $(i_T - i_0) \mid (2n+1)$, from (1) we deduce
\[ S_0 + \dots + S_{T-1} = \sum_{i=i_0}^{i_T - 1} b_i = \frac{i_T - i_0}{2n+1} > 0. \]

This contradiction finishes the solution.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{C6.} A hunter and an invisible rabbit play a game on an infinite square grid. First the hunter fixes a colouring of the cells with finitely many colours. The rabbit then secretly chooses a cell to start in. Every minute, the rabbit reports the colour of its current cell to the hunter, and then secretly moves to an adjacent cell that it has not visited before (two cells are adjacent if they share a side). The hunter wins if after some finite time either
\begin{itemize}
    \item the rabbit cannot move; or
    \item the hunter can determine the cell in which the rabbit started.
\end{itemize}
Decide whether there exists a winning strategy for the hunter.

\textbf{Answer:} Yes, there exists a colouring that yields a winning strategy for the hunter.

\textbf{Solution.} A central idea is that several colourings $C_1, C_2, \dots, C_k$ can be merged together into a single product colouring $C_1 \times C_2 \times \dots \times C_k$ as follows: the colours in the product colouring are ordered tuples $(c_1, \dots, c_k)$ of colours, where $c_i$ is a colour used in $C_i$, so that each cell gets a tuple consisting of its colours in the individual colourings $C_i$. This way, any information which can be determined from one of the individual colourings can also be determined from the product colouring.

Now let the hunter merge the following colourings:
\begin{itemize}
    \item The first two colourings $C_1$ and $C_2$ allow the tracking of the horizontal and vertical movements of the rabbit.

    The colouring $C_1$ colours the cells according to the residue of their $x$-coordinates modulo 3, which allows to determine whether the rabbit moves left, moves right, or moves vertically. Similarly, the colouring $C_2$ uses the residues of the $y$-coordinates modulo 3, which allows to determine whether the rabbit moves up, moves down, or moves horizontally.

    \item Under the condition that the rabbit's $x$-coordinate is unbounded, colouring $C_3$ allows to determine the exact value of the $x$-coordinate:

    In $C_3$, the columns are coloured white and black so that the gaps between neighboring black columns are pairwise distinct. As the rabbit's $x$-coordinate is unbounded, it will eventually visit two black cells in distinct columns. With the help of colouring $C_1$ the hunter can catch that moment, and determine the difference of $x$-coordinates of those two black cells, hence deducing the precise column.

    Symmetrically, under the condition that the rabbit's $y$-coordinate is unbounded, there is a colouring $C_4$ that allows the hunter to determine the exact value of the $y$-coordinate.

    \item Finally, under the condition that the sum $x+y$ of the rabbit's coordinates is unbounded, colouring $C_5$ allows to determine the exact value of this sum: The diagonal lines $x+y = const$ are coloured black and white, so that the gaps between neighboring black diagonals are pairwise distinct.
\end{itemize}
Unless the rabbit gets stuck, at least two of the three values $x$, $y$ and $x+y$ must be unbounded as the rabbit keeps moving. Hence the hunter can eventually determine two of these three values; thus he does know all three. Finally the hunter works backwards with help of the colourings $C_1$ and $C_2$ and computes the starting cell of the rabbit.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\textbf{C7.} Consider a checkered $3m \times 3m$ square, where $m$ is an integer greater than 1. A frog sits on the lower left corner cell $S$ and wants to get to the upper right corner cell $F$. The frog can hop from any cell to either the next cell to the right or the next cell upwards. Some cells can be sticky, and the frog gets trapped once it hops on such a cell. A set $X$ of cells is called \textit{blocking} if the frog cannot reach $F$ from $S$ when all the cells of $X$ are sticky. A blocking set is \textit{minimal} if it does not contain a smaller blocking set.
\begin{enumerate}
    \item[(a)] Prove that there exists a minimal blocking set containing at least $3m^2-3m$ cells.
    \item[(b)] Prove that every minimal blocking set contains at most $3m^2$ cells.
\end{enumerate}
\textbf{Note.} An example of a minimal blocking set for $m=2$ is shown below. Cells of the set $X$ are marked by letters $x$.

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
$x$ & $x$ & $F$ \\
\hline
 & $x$ &  \\
\hline
$S$ & $x$ &  \\
\hline
\end{tabular}
\end{center}

\textbf{Solution for part (a).} In the following example the square is divided into $m$ stripes of size $3 \times 3m$. It is easy to see that $X$ is a minimal blocking set. The first and the last stripe each contains $3m-1$ cells from the set $X$; every other stripe contains $3m-2$ cells, see Figure 1. The total number of cells in the set $X$ is $3m^2-2m+2$.




\textbf{Solution 1 for part (b).} For a given blocking set $X$, say that a non-sticky cell is \textit{red} if the frog can reach it from $S$ via some hops without entering set $X$. We call a non-sticky cell \textit{blue} if the frog can reach $F$ from that cell via hops without entering set $X$. One can regard the blue cells as those reachable from $F$ by \textit{anti-hops}, i.e. moves downwards and to the left. We also colour all cells in $X$ \textit{green}. It follows from the definition of the blocking set that no cell will be coloured twice. In Figure 2 we show a sample of a blocking set and the corresponding colouring.

Now assume that $X$ is a minimal blocking set. We denote by $R$ (resp., $B$ and $G$) be the total number of red (resp., blue and green) cells.

We claim that $G \le R+1$ and $G \le B+1$. Indeed, there are at most $2R$ possible frog hops from red cells. Every green or red cell (except for $S$) is accessible by such hops. Hence $2R \ge G+R-1$, or equivalently $G \le R+1$. In order to prove the inequality $G \le B+1$, we turn over the board and apply the similar arguments.

Therefore we get $9m^2 = B+R+G \le 3G-2$, so $G \le 3m^2$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\section*{C8.}

Determine the largest $N$ for which there exists a table $T$ of integers with $N$ rows and 100 columns that has the following properties:
\begin{itemize}
    \item[(i)] Every row contains the numbers $1, 2, \dots, 100$ in some order.
    \item[(ii)] For any two distinct rows $r$ and $s$, there is a column $c$ such that $|T(r, c) - T(s, c)| \geq 2$.
\end{itemize}

Here $T(r, c)$ means the number at the intersection of the row $r$ and the column $c$.

\section*{Answer:}

The largest such integer is $N = 100! / 2^{50}$.

\section*{Solution 1.}

\textbf{Non-existence of a larger table.}  Let us consider some fixed row in the table, and let us replace (for $k = 1, 2, \dots, 50$) each of two numbers $2k-1$ and $2k$ respectively by the symbol $x_k$. The resulting pattern is an arrangement of 50 symbols $x_1, x_2, \dots, x_{50}$, where every symbol occurs exactly twice. Note that there are $N = 100! / 2^{50}$ distinct patterns $P_1, \dots, P_N$.

If two rows $r \neq s$ in the table have the same pattern $P_i$, then $|T(r, c) - T(s, c)| \leq 1$ holds for all columns $c$. As this violates property (ii) in the problem statement, different rows have different patterns. Hence there are at most $N = 100! / 2^{50}$ rows.

\textbf{Existence of a table with $N$ rows.}  We construct the table by translating every pattern $P_i$ into a corresponding row with the numbers $1, 2, \dots, 100$. We present a procedure that inductively replaces the symbols by numbers. The translation goes through steps $k = 1, 2, \dots, 50$ in increasing order and at step $k$ replaces the two occurrences of symbol $x_k$ by $2k-1$ and $2k$.

\begin{itemize}
    \item The left occurrence of $x_1$ is replaced by 1, and its right occurrence is replaced by 2.
    \item For $k \geq 2$, we already have the number $2k-2$ somewhere in the row, and now we are looking for the places for $2k-1$ and $2k$. We make the three numbers $2k-2, 2k-1, 2k$ show up (ordered from left to right) either in the order $2k-2, 2k-1, 2k$, or as $2k-2, 2k, 2k-1$, or as $2k-1, 2k-2, 2k$. This is possible, since the number $2k-2$ has been placed in the preceding step, and shows up before / between / after the two occurrences of the symbol $x_k$.
\end{itemize}

We claim that the $N$ rows that result from the $N$ patterns yield a table with the desired property (ii). Indeed, consider the $r$-th and the $s$-th row ($r \neq s$), which by construction result from patterns $P_r$ and $P_s$. Call a symbol $x_i$ aligned, if it occurs in the same two columns in $P_r$ and $P_s$. Let $k$ be the largest index, for which symbol $x_k$ is not aligned. Note that $k \geq 2$. Consider the column $c'$ with $T(r, c') = 2k$ and the column $c''$ with $T(s, c'') = 2k$. Then $T(r, c') \leq 2k$ and $T(s, c') \leq 2k$, as all symbols $x_i$ with $i \geq k + 1$ are aligned.
\begin{itemize}
    \item If $T(r, c'') \leq 2k-2$, then $|T(r, c'') - T(s, c'')| \geq 2$ as desired.
    \item If $T(s, c') \leq 2k-2$, then $|T(r, c') - T(s, c')| \geq 2$ as desired.
    \item If $T(r, c') = 2k-1$ and $T(s, c') = 2k-1$, then the symbol $x_k$ is aligned; contradiction.
\end{itemize}
In the only remaining case we have $c' = c''$, so that $T(r, c') = T(s, c') = 2k$ holds. Now let us consider the columns $d'$ and $d''$ with $T(r, d') = 2k-1$ and $T(s, d'') = 2k-1$. Then $d' \neq d''$ (as the symbol $x_k$ is not aligned), and $T(r, d'') \leq 2k-2$ and $T(s, d') \leq 2k-2$ (as all symbols $x_i$ with $i \geq k + 1$ are aligned).
\begin{itemize}
    \item If $T(r, d'') \leq 2k-3$, then $|T(r, d'') - T(s, d'')| \geq 2$ as desired.
    \item If $T(s, c') \leq 2k-3$, then $|T(r, d') - T(s, d')| \geq 2$ as desired.
\end{itemize}
In the only remaining case we have $T(r, d'') = 2k-2$ and $T(s, d') = 2k-2$. Now the row $r$ has the numbers $2k-2, 2k-1, 2k$ in the three columns $d', d'', c'$. As one of these triples violates the ordering property of $2k-2, 2k-1, 2k$, we have the final contradiction.  $\Box$
\end{document}









"""