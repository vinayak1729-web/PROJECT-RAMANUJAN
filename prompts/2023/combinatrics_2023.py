def combinatorics_2023():
    return r"""

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\usepackage{graphicx} % Required for including images

\begin{document}

\noindent \textbf{Combinatorics}

\medskip
\noindent \textbf{C1.} Let $m$ and $n$ be positive integers greater than 1. In each unit square of an $m \times n$ grid lies a coin with its tail-side up. A \textit{move} consists of the following steps:
\begin{enumerate}
    \item select a $2 \times 2$ square in the grid;
    \item flip the coins in the top-left and bottom-right unit squares;
    \item flip the coin in either the top-right or bottom-left unit square.
\end{enumerate}

\medskip
\noindent Determine all pairs $(m,n)$ for which it is possible that every coin shows head-side up after a finite number of moves.

\medskip
\noindent \textbf{Answer:} The answer is all pairs $(m,n)$ satisfying $3 \mid mn$. \hfill \textit{(Thailand)}

\medskip
\noindent \textbf{Solution 1.} Let us denote by $(i, j)$-square the unit square in the $i^{\text{th}}$ row and the $j^{\text{th}}$ column. We first prove that when $3 \mid mn$, it is possible to make all the coins show head-side up. For integers $1 \le i \le m-1$ and $1 \le j \le n-1$, denote by $A(i, j)$ the move that flips the coin in the $(i, j)$-square, the $(i+1, j+1)$-square and the $((i, j), (i+1, j+1))$-square. Similarly, denote by $B(i, j)$ the move that flips the coin in the $(i, j)$-square, the $(i+1, j+1)$-square and the $((i+1, j), (i, j+1))$-square. Without loss of generality, we may assume that $3 \mid m$.

\medskip
\noindent \textbf{Case 1:} $n$ is even.
\medskip
We apply the moves
\begin{itemize}
    \item $A(3k-2, 2l-1)$ for all $1 \le k \le \frac{m}{3}$ and $1 \le l \le \frac{n}{2}$,
    \item $B(3k-1, 2l-1)$ for all $1 \le k \le \frac{m}{3}$ and $1 \le l \le \frac{n}{2}$.
\end{itemize}
This process will flip each coin exactly once, hence all the coins will face head-side up afterwards.

\medskip
\noindent \begin{center}
    \includegraphics[width=0.5\textwidth]{example-image-a}
\end{center}


\medskip
\noindent \textbf{Case 2:} $n$ is odd.
\medskip
We start by applying
\begin{itemize}
    \item $A(3k-2, 2l-1)$ for all $1 \le k \le \frac{m}{3}$ and $1 \le l \le \frac{n-1}{2}$,
    \item $B(3k-1, 2l-1)$ for all $1 \le k \le \frac{m}{3}$ and $1 \le l \le \frac{n-1}{2}$
\end{itemize}
as in the previous case. At this point, the coins on the rightmost column have tail-side up and the rest of the coins have head-side up. We now apply the moves
\begin{itemize}
    \item $A(3k-2, n-1)$, $A(3k-1, n-1)$ and $B(3k-2, n-1)$ for every $1 \le k \le \frac{m}{3}$.
\end{itemize}

\vspace{2cm}
\noindent 34 \hfill \textit{Chiba, Japan, 2nd-13th July 2023}

\medskip
For each $k$, the three moves flip precisely the coins in the $(3k-2, n)$-square, the $(3k-1, n)$-square, and the $(3k, n)$-square. Hence after this process, every coin will face head-side up.

\medskip
We next prove that $3 \mid mn$ being divisible by 3 is a necessary condition. We first label the $(i, j)$-square by the remainder of $i + j - 2$ when divided by 3, as shown in the figure.
\[
\begin{array}{|c|c|c|c|c}
\hline
0 & 1 & 2 & 0 & \cdots \\
\hline
1 & 2 & 0 & 1 & \cdots \\
\hline
2 & 0 & 1 & 2 & \cdots \\
\hline
0 & 1 & 2 & 0 & \cdots \\
\hline
\vdots & \vdots & \vdots & \vdots & \ddots \\
\hline
\end{array}
\]

\medskip
Let $T(c)$ be the number of coins facing head-side up in those squares whose label is $c$. The main observation is that each move does not change the parity of both $T(0) - T(1)$ and $T(1) - T(2)$, since a move flips exactly one coin in a square with each label. Initially, all coins face tail-side up at the beginning, thus all of $T(0), T(1), T(2)$ are equal to 0. Hence it follows that any configuration that can be achieved from the initial state must satisfy the parity condition of
\[
T(0) \equiv T(1) \equiv T(2) \pmod{2}.
\]

\medskip
We now calculate the values of $T$ for the configuration in which all coins are facing head-side up.
\begin{itemize}
    \item When $m \equiv n \equiv 1 \pmod{3}$, we have $T(0) = 1 < T(1) = T(2) = \frac{mn-1}{3}$.
    \item When $m \equiv n \equiv 1 \pmod{3}$, we have $T(0) = 1 < T(1) = T(2) = \frac{mn-1}{3}$.
    \item When $m \equiv 1 \pmod{3}$ and $n \equiv 2 \pmod{3}$, or $m \equiv 2 \pmod{3}$ and $n \equiv 1 \pmod{3}$, we have $T(0) = \frac{mn-2}{3} < T(1) = T(2) = \frac{mn+1}{3}$.
    \item When $m \equiv n \equiv 2 \pmod{3}$, we have $T(0) = T(1) - 1 = T(2) - 1 = \frac{mn-3}{3}$.
    \item When $m \equiv 0 \pmod{3}$ (mod 3) or $n \equiv 0 \pmod{3}$, we have $T(0) = T(1) = T(2) = \frac{mn}{3}$.
\end{itemize}
From this calculation, we see that $T(0), T(1)$ and $T(2)$ has the same parity only when $mn$ is divisible by 3.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C2.} Determine the maximal length $L$ of a sequence $a_1, \dots, a_L$ of positive integers satisfying both the following properties:

\begin{itemize}
    \item Every term in the sequence is less than or equal to $2^{2023}$, and
    \item There does not exist a consecutive subsequence $a_i, a_{i+1}, \dots, a_j$ (where $1 \leq i \leq j \leq L$) with a choice of signs $s_i, s_{i+1}, \dots, s_j \in \{1, -1\}$ for which
        \[ s_i a_i + s_{i+1} a_{i+1} + \dots + s_j a_j = 0. \]
\end{itemize}
(Czech Republic)

\textbf{Answer:} The answer is $L = 2^{2024} - 1$.

\textbf{Solution.} We prove more generally that the answer is $2^{k+1} - 1$ when $2^{2023}$ is replaced by $2^k$ for an arbitrary positive integer $k$. Write $n = 2^k$.

We first show that there exists a sequence of length $L = 2n - 1$ satisfying the properties.  For a positive integer $x$, denote by $\nu_2(x)$ the maximal nonnegative integer $\nu$ such that $2^\nu$ divides $x$.
Consider the sequence $a_1, \dots, a_{2n-1}$ defined as
\[ a_i = 2^{k - \nu_2(i)}. \]
For example, when $k = 2$ and $n = 4$, the sequence is
\[ 4, 2, 4, 1, 4, 2, 4. \]
This indeed consists of positive integers less than or equal to $n = 2^k$, because $0 \leq \nu_2(i) \leq k$ for $1 \leq i \leq 2^{k+1}-1$.

\textbf{Claim 1.} This sequence $a_1, \dots, a_{2n-1}$ does not have a consecutive subsequence with a choice of signs such that the signed sum equals zero.

\textbf{Proof.} Let $1 \leq i \leq j \leq 2n-1$ be integers. The main observation is that amongst the integers
\[ i, i+1, \dots, j-1, j, \]
there exists a unique integer $x$ with the maximal value of $\nu_2(x)$.  To see this, write $v = \max(\nu_2(i), \dots, \nu_2(j))$.  If there exist at least two multiples of $2^v$ amongst $i, i+1, \dots, j$, then one of them must be a multiple of $2^{v+1}$, which is a contradiction.

Therefore there is exactly one $i \leq x \leq j$ with $\nu_2(x) = v$, which implies that all terms except for $a_x = 2^{k-v}$ in the sequence
\[ a_i, a_{i+1}, \dots, a_j \]
are a multiple of $2^{k-v+1}$. The same holds for the terms $s_i a_i, s_{i+1} a_{i+1}, \dots, s_j a_j$, hence the sum cannot be equal to zero. \qed

We now prove that there does not exist a sequence of length $L \geq 2n$ satisfying the conditions of the problem.  Let $a_1, \dots, a_L$ be an arbitrary sequence consisting of positive integers less than or equal to $n$. Define a sequence $s_1, \dots, s_L$ of signs recursively as follows:

\begin{itemize}
    \item When $s_1 a_1 + \dots + s_{i-1} a_{i-1} \leq 0$, set $s_i = +1$,
    \item When $s_1 a_1 + \dots + s_{i-1} a_{i-1} > 0$, set $s_i = -1$.
\end{itemize}

Write
\[ b_i = \sum_{j=1}^i s_j a_j = s_1 a_1 + \dots + s_i a_i, \]
and consider the sequence
\[ 0 = b_0, b_1, b_2, \dots, b_L. \]

\noindent \hrulefill

\textbf{Claim 2.} All terms $b_i$ of the sequence satisfy $-n+1 \leq b_i \leq n$.

\textbf{Proof.} We prove this by induction on $i$. It is clear that $b_0 = 0$ satisfies $-n+1 \leq 0 \leq n$. We now assume $-n+1 \leq b_{i-1} \leq n$ and show that $-n+1 \leq b_i \leq n$.

\textbf{Case 1:} $-n+1 \leq b_{i-1} \leq 0$.

Then $b_i = b_{i-1} + a_i$ from the definition of $s_i$, and hence
\[ -n+1 \leq b_{i-1} < b_{i-1} + a_i \leq b_{i-1} + n \leq n. \]

\textbf{Case 2:} $1 \leq b_{i-1} \leq n$.

Then $b_i = b_{i-1} - a_i$ from the definition of $s_i$, and hence
\[ -n+1 \leq b_{i-1} - n \leq b_{i-1} - a_i < b_{i-1} \leq n. \]

This finishes the proof. \qed

Because there are $2n$ integers in the closed interval $[-n+1, n]$ and at least $2n+1$ terms in the sequence $b_0, b_1, \dots, b_L$ (as $L+1 \geq 2n+1$ by assumption), the pigeonhole principle implies that two distinct terms $b_{i-1}, b_j$ (where $1 \leq i < j \leq L$) must be equal. Subtracting one from another, we obtain
\[ s_i a_i + \dots + s_j a_j = b_j - b_{i-1} = 0, \]
as desired.

\textbf{Comment.} The same argument gives a bound $L \leq 2n-1$ that works for all $n$, but this bound is not necessarily sharp when $n$ is not a power of 2. For instance, when $n=3$, the longest sequence has length $L=3$.

\end{document}





 

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{C3.} Let $n$ be a positive integer. We arrange $1 + 2 + \cdots + n$ circles in a triangle with $n$ rows, such that the $i^{th}$ row contains exactly $i$ circles. The following figure shows the case $n=6$.

\begin{center}
    \begin{picture}(100,50)
        \put(50,25){\line(1,0){0}} % Replace with actual image if possible
        \put(50,10){$n=6$}
    \end{picture}
\end{center}

In this triangle, a ninja-path is a sequence of circles obtained by repeatedly going from a circle to one of the two circles directly below it. In terms of $n$, find the largest value of $k$ such that if one circle from every row is coloured red, we can always find a ninja-path in which at least $k$ of the circles are red.

(Netherlands)

\textbf{Answer:} The maximum value is $k = 1 + \lfloor \log_2 n \rfloor$.

\textbf{Solution 1.} Write $N = \lfloor \log_2 n \rfloor$ so that we have $2^N \leq n < 2^{N+1} - 1$.

We first provide a construction where every ninja-path passes through at most $N+1$ red circles. For the row $i = 2^a + b$ for $0 \leq a \leq N$ and $0 \leq b < 2^a$, we colour the $(2b+1)^{th}$ circle.

\begin{center}
    \begin{picture}(100,50)
        \put(50,25){\line(1,0){0}} % Replace with actual image if possible
    \end{picture}
\end{center}

Then every ninja-path passes through at most one red circle in each of the rows $2^a, 2^a + 1, \dots, 2^{a+1} - 1$ for each $0 \leq a \leq N$. It follows that every ninja-path passes through at most $N+1$ red circles.

We now prove that for every colouring, there exists a ninja-path going through at least $N+1$ red circles. For each circle $C$, we assign the maximum number of red circles in a ninja-path that starts at the top of the triangle and ends at $C$.

\begin{center}
    \begin{picture}(100,50)
        \put(50,25){\line(1,0){0}} % Replace with actual image if possible
    \end{picture}
\end{center}

Note that
\begin{itemize}
    \item if $C$ is not red, then the number assigned to $C$ is the maximum of the number assigned to the one or two circles above $C$, and
    \item if $C$ is red, then the number assigned to $C$ is one plus the above maximum.
\end{itemize}

\noindent \hrulefill

Write $v_1, \dots, v_i$ for the numbers in row $i$, and let $v_m$ be the maximum among these numbers. Then the numbers in row $i+1$ will be at least
\[ v_1, \dots, v_{m-1}, v_m, v_m, v_{m+1}, \dots, v_i. \]

not taking into account the fact that one of the circles in row $i+1$ is red. On the other hand, for the red circle in row $i+1$, the lower bound on the assigned number can be increased by 1. Therefore the sum of the numbers in row $i+1$ is at least
\[ (v_1 + \cdots + v_i) + v_m + 1. \]

Using this observation, we prove the following claim.
Claim 1. Let $\sigma_k$ be the sum of the numbers assigned to circles in row $k$. Then for $0 < j \leq N$, we have $\sigma_j \geq j \cdot 2^j + 1$.

Proof. We use induction on $j$. This is clear for $j=0$, since the number in the first row is always 1. For the induction step, suppose that $\sigma_j \geq j \cdot 2^j + 1$. Then the maximum value assigned to a circle in row $2^j$ is at least $j+1$. As a consequence, for every $k \geq 2^j$, there is a circle on row $k$ with number at least $j+1$. Then by our observation above, we have
\[ \sigma_{k+1} \geq \sigma_k + (j+1) + 1 = \sigma_k + (j+2). \]

Then we get
\[ \sigma_{j+1} \geq \sigma_{2^j} + 2^j (j+2) \geq j \cdot 2^j + 1 + 2^j(j+2) = (j+j+2)2^j + 1 = (j+1)2^{j+1} + 1. \]
This completes the inductive step. \qed

For $j=N$, this immediately implies that some circle in row $2^N$ has number at least $N+1$. This shows that there is a ninja-path passing through at least $N+1$ red circles.

\end{document}








\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{C4.} Let $n \geq 2$ be a positive integer. Paul has a $1 \times n^2$ rectangular strip consisting of $n^2$ unit squares, where the $i^{th}$ square is labelled with $i$ for all $1 \leq i \leq n^2$. He wishes to cut the strip into several pieces, where each piece consists of a number of consecutive unit squares, and then \textit{translate} (without rotating or flipping) the pieces to obtain an $n \times n$ square satisfying the following property: if the unit square in the $i^{th}$ row and $j^{th}$ column is labelled with $a_{ij}$, then $a_{ij} - (i + j - 1)$ is divisible by $n$.

Determine the smallest number of pieces Paul needs to make in order to accomplish this.

(U.S.A.)

\textbf{Answer:} The minimum number of pieces is $2n - 1$.

\textbf{Solution 1.} For the entirety of the solution, we shall view the labels as taking values in $\mathbb{Z}/n\mathbb{Z}$, as only their values modulo $n$ play a role.

Here are two possible constructions consisting of $2n-1$ pieces.

\begin{enumerate}
    \item Cut into pieces of sizes $n, 1, n, 1, \dots, n, 1, 1$ and glue the pieces of size 1 to obtain the last row.
    \item Cut into pieces of sizes $n, 1, n-1, 2, n-2, \dots, n-1, 1$ and switch the pairs of consecutive strips that add up to size $n$.
\end{enumerate}

We now prove that using $2n-1$ pieces is optimal. It will be more helpful to think of the reverse process: start with $n$ pieces of size $1 \times n$, where the $k^{th}$ piece has squares labelled $k, k+1, \dots, k+n-1$. The goal is to restore the original $1 \times n^2$ strip.

Note that each piece, after cutting at appropriate places, is of the form $a, a+1, \dots, b-1$. Construct an (undirected but not necessarily simple) graph $\Gamma$ with vertices labelled by $1, \dots, n$, where a piece of the form $a, a+1, \dots, b-1$ corresponds to an edge from $a$ to $b$. We make the following observations.

\begin{itemize}
    \item The cut pieces came from the $k^{th}$ initial piece $k, k+1, \dots, k+n-1$ corresponds to a cycle $\gamma_k$ (possibly of length 1) containing the vertex $k$.
    \item Since it is possible to rearrange the pieces into one single $1 \times n^2$ strip, the graph $\Gamma$ has an Eulerian cycle.
    \item The number of edges of $\Gamma$ is equal to the total number of cut pieces.
\end{itemize}

The goal is to prove that $\Gamma$ has at least $2n-1$ edges. Since $\Gamma$ has an Eulerian cycle, it is connected. For every $1 \leq k \leq n$, pick one edge from $\gamma_k$, delete it from $\Gamma$ to obtain a new graph $\Gamma'$. Since no two cycles $\gamma_i$ and $\gamma_j$ share a common edge, removing one edge from each cycle does not affect the connectivity of the graph. This shows that the new graph $\Gamma'$ must also be connected. Therefore $\Gamma'$ has at least $n-1$ edges, which means that $\Gamma$ has at least $2n-1$ edges.

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{C5.} Elisa has 2023 treasure chests, all of which are unlocked and empty at first. Each day, Elisa adds a new gem to one of the unlocked chests of her choice, and afterwards, a fairy acts according to the following rules:

\begin{itemize}
    \item if more than one chest are unlocked, it locks one of them, or
    \item if there is only one unlocked chest, it unlocks all the chests.
\end{itemize}

Given that this process goes on forever, prove that there is a constant $C$ with the following property: Elisa can ensure that the difference between the numbers of gems in any two chests never exceeds $C$, regardless of how the fairy chooses the chests to lock.

(Israel)

\textbf{Solution 1.} We will prove that such a constant $C$ exists when there are $n$ chests for $n$ an odd positive integer. In fact we can take $C = n-1$. Elisa's strategy is simple: place a gem in the chest with the fewest gems (in case there are more than one such chests, pick one arbitrarily).

For each integer $t \geq 0$, let $a_1^t \leq a_2^t \leq \cdots \leq a_n^t$ be the numbers of gems in the $n$ chests arbitrarily at the end of the $t^{th}$ day. In particular, $a_1^0 = \cdots = a_n^0 = 0$ and
\[ a_1^t + a_2^t + \cdots + a_n^t = t. \]

For each $t \geq 0$, there is a unique index $m=m(t)$ for which $a_{m(t)}^t < a_{m(t)+1}^t + 1$. We know that $a_j^t > a_{m(t)}^t$ for all $j > m(t)$, since $a_{m(t)}^t < a_{m(t)+1}^t$. Elisa's strategy also guarantees that if an index $j$ is greater than the remainder of $t$ when divided by $n$, then $a_j^t \geq a_{m(t)}^t$.

Recall that a sequence $x_1 \leq x_2 \leq \cdots \leq x_n$ of real numbers is said to majorise another sequence $y_1 \leq y_2 \leq \cdots \leq y_n$ of real numbers when for all $1 \leq k \leq n$ we have
\[ x_1 + x_2 + \cdots + x_k \leq y_1 + y_2 + \cdots + y_k \]
and
\[ x_1 + x_2 + \cdots + x_n = y_1 + y_2 + \cdots + y_n. \]

Our strategy for proving $a_n^t - a_1^t \leq n - 1$ is to inductively show that the sequence $(a_i^t)$ is majorised by some other sequence $(b_i^t)$.

We define this other sequence $(b_i^t)$ as follows. Let $b_k^0 = k - \frac{n+1}{2}$ for $1 \leq k \leq n$. As $n$ is odd, this is a strictly increasing sequence of integers, and the sum of its terms is 0. Now define $b_i^{t+1} = b_i^t + \left\lfloor \frac{t}{n} \right\rfloor + 1$ for $t \geq 1$ and $1 \leq i \leq n$. Thus for $t \geq 0$,
\[
b_i^{t+1} =
\begin{cases}
    b_i^t & \text{if } t+1 \not\equiv i \pmod{n}, \\
    b_i^t + 1 & \text{if } t+1 \equiv i \pmod{n}.
\end{cases}
\]

From these properties it is easy to see that
\begin{itemize}
    \item $b_1^t + b_2^t + \cdots + b_n^t = t$ for all $t \geq 0$, and
    \item $b_i^t \leq b_{i+1}^t$ for all $t \geq 0$ and $1 \leq i \leq n-1$, with the inequality being strict if $t \not\equiv i \pmod{n}$.
\end{itemize}

Claim 1. For each $t \geq 0$, the sequence of integers $b_1^t, b_2^t, \dots, b_n^t$ majorises the sequence of integers $a_1^t, a_2^t, \dots, a_n^t$.

\textbf{Proof.} We use induction on $t$. The base case $t=0$ is trivial. Assume $t \geq 0$ and that $(b_i^t)$ majorises $(a_i^t)$. We want to prove the same holds for $t+1$.

First note that the two sequences $(b_i^{t+1})$ and $(a_i^{t+1})$ both sum up to $t+1$. Next, we wish to show that for $1 \leq k \leq n$, we have
\[ b_1^{t+1} + b_2^{t+1} + \cdots + b_k^{t+1} \leq a_1^{t+1} + a_2^{t+1} + \cdots + a_k^{t+1}. \]

When $t+1$ is replaced by $t$, the above inequality holds by the induction hypothesis. For the sake of contradiction, suppose $k$ is the smallest index such that the inequality for $t+1$ fails. Since the left hand side increases by at most 1 during the transition from $t$ to $t+1$, the inequality for $t+1$ can fail only if all of the following occur:

\begin{itemize}
    \item $b_1^t + b_2^t + \cdots + b_k^t = a_1^t + a_2^t + \cdots + a_k^t$,
    \item $t+1 \equiv j \pmod{n}$ for some $1 \leq j \leq k$ (so that $b_j^{t+1} = b_j^t + 1$),
    \item $m(t) > k$ (so that $a_i^{t+1} = a_i^t$ for $1 \leq i \leq k$).
\end{itemize}

The first point and the minimality of $k$ tell us that $b_1^t, \dots, b_k^t$ majorises $a_1^t, \dots, a_k^t$ as well (again using the induction hypothesis), and in particular $b_k^t \geq a_k^t$.

The second point tells us that the remainder of $t$ when divided by $n$ is at most $k-1$, so $a_j^t \geq a_{m(t)}^t$ (by Elisa's strategy). But by the third point ($m(t) > k+1$) and the non-decreasing property of $a_i^t$, we must have the equalities $a_k^t = a_k^{t+1} = a_{m(t)}^t$. On the other hand, $a_k^t \leq b_k^t < b_{k+1}^t$, with the second inequality being strict because $t \not\equiv k \pmod{n}$. We conclude that

\[ b_1^{t+1} + b_2^{t+1} + \cdots + b_k^{t+1} > a_1^{t+1} + a_2^{t+1} + \cdots + a_k^{t+1}, \]
a contradiction to the induction hypothesis. This completes the proof as it implies

\[ a_n^t - a_1^t \leq b_n^t - b_1^t \leq b_n^0 - b_1^0 = n-1. \]

Comment 1. The statement is true even when $n$ is even. In this case, we instead use the initial state
\[ b_k^0 =
\begin{cases}
    k - \frac{n}{2} - \frac{1}{2} & k \leq \frac{n}{2} \\
    k - \frac{n}{2} + \frac{1}{2} & k > \frac{n}{2}.
\end{cases}
\]

The same argument shows that $C = n-1$ works.

Comment 2. The constants $C=n-1$ for odd $n$ and $C=n$ for even $n$ are in fact optimal. To see this, we will assume that the fairy always locks a chest with the minimal number of gems. Then $m(t)$ is always greater than the remainder of $t$ when divided by $n$. This implies that the quantity
\[ I_k = a_1^t + \cdots + a_k^t - b_1^t - \cdots - b_k^t\]
for each $0 \leq k \leq n$, do not increase regardless of how Elisa acts. If Elisa succeeds in keeping $a_k^t - a_1^t$ bounded, then those quantities must also be bounded; thus they are eventually constant, say for $t > t_0$. This implies that for all $t > t_0$, the number $m(t)$ is equal to 1 plus the remainder of $t$ when divided by $n$.

Claim 2. For $T > t_0$ divisible by $n$, we have
\[ a_1^T < a_2^T < \cdots < a_n^T. \]

\textbf{Proof.} Suppose otherwise, and let $j$ be an index for which $a_j^T = a_{j+1}^T$. We have $m(T+k-1) - k$ for all $1 \leq k \leq n$. Then $a_j^{T+k-1} > a_{j+1}^{T+k-1}$, which gives a contradiction. \qed

This implies $a_n^t - a_1^t \geq n-1$, which already proves optimality of $C = n-1$ for odd $n$. For even $n$, note that the sequence $(a_i^t)$ has sum divisible by $n$, so it cannot consist of a consecutive integers. Thus $a_n^T - a_1^T > n$ for $n$ even.
\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{C6.} Let $N$ be a positive integer, and consider an $N \times N$ grid. A \textit{right-down} path is a sequence of grid cells such that each cell is either one cell to the right of or one cell below the previous cell in the sequence. A \textit{right-up} path is a sequence of grid cells such that each cell is either one cell to the right of or one cell above the previous cell in the sequence.

Prove that the cells of the $N \times N$ grid cannot be partitioned into less than $N$ right-down or right-up paths. For example, the following partition of the $5 \times 5$ grid uses 5 paths.

\begin{center}
    \begin{picture}(100,100)
        \put(50,50){\line(1,0){0}} % Placeholder for grid image
    \end{picture}
\end{center}

(Canada)

\textbf{Solution 1.} We define a good parallelogram to be a parallelogram composed of two isosceles right-angled triangles glued together as shown below.

\begin{center}
    \begin{picture}(100,50)
        \put(50,25){\line(1,0){0}} % Placeholder for parallelogram images
    \end{picture}
\end{center}

Given any partition into $k$ right-down or right-up paths, we can find a corresponding packing of good parallelograms that leaves an area of $k$ empty. Thus, it suffices to prove that we must leave an area of at least $N$ empty when we pack good parallelograms into an $N \times N$ grid. This is actually equivalent to the original problem since we can uniquely recover the partition into right-down or right-up paths from the corresponding packing of good parallelograms.

\begin{center}
    \begin{picture}(100,50)
        \put(25,25){\line(1,0){0}} % Placeholder for diagram
        \put(75,25){\line(1,0){0}} % Placeholder for diagram
    \end{picture}
\end{center}

We draw one of the diagonals in each cell so that it does not intersect any of the good parallelograms. Now, view these segments as mirrors, and consider a laser entering each of the $4N$ boundary edges (with starting direction being perpendicular to the edge), bouncing along these mirrors until it exits at some other edge. Whenever a laser passes through a good parallelogram, its direction goes back to the original one after bouncing two times. Thus, if the final direction of a laser is perpendicular to its initial direction, it must pass through at least one empty triangle. Similarly, if the final direction of a laser is opposite to its initial direction, it must pass though at least two empty triangles. Using this, we will estimate the number of empty triangles in the $N \times N$ grid.

We associate the starting edge of a laser with the edge it exits at. Then, the boundary edges are divided into $2N$ pairs. These pairs can be classified into three types:
\begin{enumerate}
    \item a pair of a vertical and a horizontal boundary edge,
    \item a pair of boundary edges from the same side, and
    \item a pair of boundary edges from opposite sides.
\end{enumerate}

Since the beams do not intersect, we cannot have one type (3) pair from vertical boundary edges and another type (3) pair from horizontal boundary edges. Without loss of generality, we may assume that we have $t$ pairs of type (3) and they are all from vertical boundary edges. Then, out of the remaining boundary edges, there are $2N$ horizontal boundary edges and $2N-2t$ vertical boundary edges. It follows that there must be at least $t$ pairs of type (2) from horizontal boundary edges. We know that a laser corresponding to a pair of type (1) passes through at least one empty triangle, and a laser corresponding to a pair of type (2) passes through at least two empty triangles. Thus, as the beams do not intersect, we have at least $(2N - 2t) + 2 \cdot t = 2N$ empty triangles in the grid, leaving an area of at least $N$ empty as required.
\end{document}








\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{C7.} The Inomi archipelago consists of $n > 2$ islands. Between each pair of distinct islands is a unique ferry line that runs in both directions, and each ferry line is operated by one of $k$ companies. It is known that if any one of the $k$ companies closes all its ferry lines, then it becomes impossible for a traveller, no matter where the traveller starts at, to visit all the islands exactly once (in particular, not returning to the island the traveller started at).

Determine the maximal possible value of $k$ in terms of $n$.

(Ukraine)

\textbf{Answer:} The largest $k$ is $k = \lfloor \log_2 n \rfloor$.

\textbf{Solution.} We reformulate the problem using graph theory. We have a complete graph $K_n$ on $n$ nodes (corresponding to islands), and we want to colour the edges (corresponding to ferry lines) with $k$ colours (corresponding to companies), so that every Hamiltonian path contains all $k$ different colours. For a fixed set of $k$ colours, we say that an edge colouring of $K_n$ is good if every Hamiltonian path contains an edge of each one of those $k$ colours.

We first construct a good colouring of $K_n$ using $k = \lfloor \log_2 n \rfloor$ colours.

Claim 1. Take $k = \lfloor \log_2 n \rfloor$. Consider the complete graph $K_n$ in which the nodes are labelled by $1,2, \dots, n$. Colour node $i$ with colour $\min(\lfloor \log_2 i \rfloor + 1, k)$ (so the colours of the first nodes $1,2,2,3,3,3,3,4,\dots$ and the last $n - 2^{k-1} + 1$ nodes have colour $k$), and for $1 \leq i < j \leq n$, colour the edge $ij$ with the colour of the node $i$. Then the resulting edge colouring of $K_n$ is good.

\textbf{Proof.} We need to check that every Hamiltonian path contains edges of every single colour. We first observe that the number of nodes assigned colour $k$ is $n - 2^{k-1} + 1$. Since $n \geq 2^k$, we have
\[ n - 2^{k-1} + 1 > \frac{n}{2} + 1. \]

This implies that in any Hamiltonian path, there exists an edge between two nodes with colour $k$. Then that edge must have colour $k$.

We next show that for each $1 \leq i < k$, every Hamiltonian path contains an edge of colour $i$. Suppose the contrary, that some Hamiltonian path does not contain an edge of colour $i$. Then nodes with colour $i$ can only be adjacent to nodes with colour less than $i$ inside the Hamiltonian path. Since there are $2^{i-1}$ nodes with colour $i$ and $2^{i-1} - 1$ nodes with colour less than $i$, the Hamiltonian path must take the form
\[ (i) \leftrightarrow (<i) \leftrightarrow (i) \leftrightarrow (<i) \leftrightarrow \cdots \leftrightarrow (<i) \leftrightarrow (i), \]
where $(i)$ denotes a node with colour $i$, $(<i)$ denotes a node with colour less than $i$, and $\leftrightarrow$ denotes an edge. But this is impossible, as the Hamiltonian path would not have any nodes with colours greater than $i$. \qed

Fix a set of $k$ colours, we now prove that if there exists a good colouring of $K_n$, then $k \leq \lfloor \log_2 n \rfloor$. For $n = 2$, this is trivial, so we assume $n \geq 3$. For any node $v$ of $K_n$ and $1 \leq i \leq k$, we denote by $d_i(v)$ the number of edges with colour $i$ incident with the node $v$.

Lemma 1. Consider a good colouring of $K_n$, and let $AB$ be an arbitrary edge with colour $i$. If $d_i(A) + d_i(B) \leq n - 1$, then the colouring will remain good after recolouring edge $AB$ with any other colour.

\textbf{Proof.} Suppose there exists a good colouring together with an edge $AB$ of colour $i$, such that if $AB$ is recoloured with another colour, the colouring will no longer be good. The failure of the new colouring being good will come from colour $i$, and thus there exists a Hamiltonian path containing edge $AB$ such that initially (i.e. before recolouring) $AB$ is the only edge of colour $i$ in this path. Writing $A = A_0$ and $B = B_0$, denote this Hamiltonian path by
\[ A \leftrightarrow A_1 \leftrightarrow \cdots \leftrightarrow A_{i-1} \leftrightarrow A_i \leftrightarrow B \leftrightarrow B_1 \leftrightarrow \cdots \leftrightarrow B_{i-1} \leftrightarrow B_i, \]

\end{document}

"""

