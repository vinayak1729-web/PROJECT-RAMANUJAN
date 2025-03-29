def combinatrics2022_trainquestions():
    return r"""

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C1.} A $\pm 1$-sequence is a sequence of 2022 numbers $a_1, \dots, a_{2022}$, each equal to either +1 or -1. Determine the largest $C$ so that, for any $\pm 1$-sequence, there exists an integer $k$ and indices $1 \le t_1 < \dots < t_k \le 2022$ so that $t_{i+1} - t_i \le 2$ for all $i$, and
\[
\left| \sum_{i=1}^k a_{t_i} \right| \ge C.
\] \hfill (Czech Republic)

\textbf{Answer:} The answer is $C = 506$.

\textbf{Solution.} First, we prove that this can always be achieved. Without loss of generality, suppose at least $\frac{2022}{2} = 1011$ terms of the $\pm 1$-sequence are +1. Define a subsequence as follows: starting at $t = 0$, if $a_t = +1$ we always include $a_t$ in the subsequence. Otherwise, we skip $a_t$ if we can (i.e. if we included $a_{t-1}$ in the subsequence), otherwise we include it out of necessity, and go to the next $t$. Clearly, this subsequence will include all $+1$s. Also, for each $-1$ included in the sequence, a $-1$ must have been skipped, so at most $\left\lfloor \frac{1011}{2} \right\rfloor = 505$ can be included. Hence the sum is at least $1011 - 505 = 506$, as desired.

Next, we prove that, for the $\pm 1$-sequence
\[
(\{-1\}, \{+1, +1\}, \{-1, -1\}, \{+1, +1\}, \dots, \{+1, +1\}, \{-1, -1\}, \{+1\}),
\]
each admissible subsequence $a_{t_i}$ has $-506 \le \sum_i a_{t_i} \le 506$. We say that the terms inside each curly bracket is a block. In total, there are 1012 blocks - 506 of them hold +1-s, and 506 of them hold $-1$s. (The two blocks at each end hold 1 number each, each other block holds 2.)
Suppose an admissible subsequence includes terms from $k$ blocks holding +1-s. Then, in each $-1$-pair in between the $+1$-pairs, the subsequence must also include at least one $-1$. There can be at most two $+1$s included from each $+1$-block, and at least one $-1$ must be included from each $-1$-block, so the sum is at most $2k - (k - 1) = k + 1$.

For $k < 506$, this is at most 506. If $k = 506$, one of the $+1$-blocks must be the one at the end, meaning it can only include one +1, so that the maximum in this case is only $k$, not $k + 1$, so in this case the sum is also at most 506.

Hence we have shown that for any admissible subsequence, $\sum_i a_{t_i} \le 506$. Analogously we can show that $-506 \le \sum_i a_{t_i}$, meaning that $C \le 506$ as desired.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C2.} The Bank of Oslo issues coins made out of two types of metal: aluminium (denoted A) and copper (denoted C). Morgane has $n$ aluminium coins, and $n$ copper coins, and arranges her $2n$ coins in a row in some arbitrary initial order. Given a fixed positive integer $k \le 2n$, she repeatedly performs the following operation: identify the largest subsequence containing the $k$-th coin from the left which consists of consecutive coins made of the same metal, and move all coins in that subsequence to the left end of the row. For example, if $n=4$ and $k=4$, the process starting from the configuration $AACCCACA$ would be
\[
AACCCACA \to CCCAACA \to AAACCCCA \to CCCCCAAA \to \dots
\]
Find all pairs $(n, k)$ with $1 \le k \le 2n$ such that for every initial configuration, at some point of the process there will be at most one aluminium coin adjacent to a copper coin. \hfill (France)

\textbf{Answer:} All pairs $(n, k)$ such that $n \le k \le \frac{3n+1}{2}$.

\textbf{Solution.} Define a block to be a maximal subsequence of consecutive coins made out of the same metal, and let $M^b$ denote a block of b coins of metal $M$. The property that there is at most one aluminium coin adjacent to a copper coin is clearly equivalent to the configuration having two blocks, one consisting of all A-s and one consisting of all C-s.

First, notice that if $k < n$, the sequence $A^{n-1} C^{n-1}AC$ remains fixed under the operation, and will therefore always have 4 blocks. Next, if $k > \frac{3n+1}{2}$, let $a = k - n - 1, b = 2n - k + 1$. Then $k > 2a + b, k > 2b + a$, so the configuration $A^c C^b A^c C^a$ will always have four blocks:
\[
A^c C^b A^c C^a \to C^a A^c A^c A^b \to A^c A^c A^c A^b \to C^b A^c A^c A^c A^a \to \dots
\]

Therefore a pair $(n, k)$ can have the desired property only if $n \le k \le \frac{3n+1}{2}$. We claim that all such pairs in fact do have the desired property. Clearly, the number of blocks in a configuration cannot increase, so whenever the operation is applied, it either decreases or remains constant. We show that unless there are only two blocks, after a finite amount of steps the number of blocks will decrease.

Consider an arbitrary configuration with $c \ge 3$ blocks. We note that as $k \ge n$, the leftmost block cannot be moved, because in this case all $n$ coins of one type are in the leftmost block, meaning there are only two blocks. If a block which is not the leftmost or rightmost block is moved, its neighbor blocks will be merged, causing the number of blocks to decrease.

Hence the only case in which the number of blocks does not decrease in the next step is if the rightmost block is moved. If c is odd, the leftmost and the rightmost blocks are made of the same metal, so this would merge two blocks. Hence $c \ge 4$ must be even. Suppose there is a configuration of c blocks with the $i$-th block having size $a_i$ so that the operation always moves the rightmost block:
\[
A^{a_1} \dots A^{a_{c-1}} C^{a_c} \to C^{a_c} A^{a_1} \dots A^{a_{c-1}} \to A^{a_{c-1}} C^{a_c} A^{a_1} \dots \to C^{a_c}A^{\dots} - 2 \to \dots
\]

Because the rightmost block is always moved, $k \ge 2n + 1 - a_i$ for all i. Because $\sum a_i = 2n$, summing this over all i we get $ck \ge 2cn + c - \sum a_i = 2cn + c - 2n$, so $k \ge 2n + 1 - \frac{2n}{c} \ge \frac{3n + 1}{2}$. But this contradicts $k \le \frac{3n+1}{2}$. Hence at some point the operation will not move the rightmost block, meaning that the number of blocks will decrease, as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}

\begin{document}

\textbf{C3.} In each square of a garden shaped like a $2022 \times 2022$ board, there is initially a tree of height 0. A gardener and a lumberjack alternate turns playing the following game, with the gardener taking the first turn:

\begin{itemize}
    \item The gardener chooses a square in the garden. Each tree on that square and all the surrounding squares (of which there are at most eight) then becomes one unit taller.
    \item The lumberjack then chooses four different squares on the board. Each tree of positive height on those squares then becomes one unit shorter.
\end{itemize}

We say that a tree is majestic if its height is at least $10^6$. Determine the largest number $K$ such that the gardener can ensure there are eventually $K$ majestic trees on the board, no matter how the lumberjack plays. \hfill (Colombia)

\textbf{Answer:} $K = 5 \cdot \frac{2022^2}{9} = 2271380$. In general, for a $3N \times 3N$ board, $K = 5N^2$.

\textbf{Solution.} We solve the problem for a general $3N \times 3N$ board. First, we prove that the lumberjack has a strategy to ensure there are never more than $5N^2$ majestic trees. Giving the squares of the board coordinates in the natural manner, colour each square where at least one of its coordinates are divisible by 3, shown below for a $9 \times 9$ board:
\begin{center}
    \begin{tikzpicture}[scale=0.3]
        \foreach \i in {0,1,2,3,4,5,6,7,8} {
            \foreach \j in {0,1,2,3,4,5,6,7,8} {
                \ifodd{\i + \j}
                    \filldraw[fill=gray!50] (\i, \j) rectangle (\i+1, \j+1);
                \fi
            }
        }
    \end{tikzpicture}
\end{center}

Then, as each $3 \times 3$ square on the board contains exactly 5 coloured squares, each move of the gardener will cause at most 4 trees on non-coloured squares to grow. The lumberjack may therefore cut those trees, ensuring no tree on a non-coloured square has positive height after his turn. Hence there cannot ever be more majestic trees than coloured squares, which is $5N^2$.

Next, we prove the gardener may ensure there are $5N^2$ majestic trees. In fact, we prove this statement in a modified game which is more difficult for the gardener: on the lumberjack's turn in the modified game, he may decrement the height of all trees on the board except those the gardener did not just grow, in addition to four of the trees the gardener just grew. Clearly, a sequence of moves for the gardener which ensures that there are K majestic trees in the modified game also ensures this in the original game.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C4.} Let $n > 3$ be a positive integer. Suppose that $n$ children are arranged in a circle, and $n$ coins are distributed between them (some children may have no coins). At every step, a child with at least 2 coins may give 1 coin to each of their immediate neighbours on the right and left. Determine all initial distributions of coins from which it is possible that, after a finite number of steps, each child has exactly one coin. \hfill (Israel)

\textbf{Answer:} All distributions where $\sum_{i=1}^n ic_i = \frac{n(n+1)}{2} \pmod{n}$, where $c_i$ denotes the number of coins the $i$-th child starts with.

\textbf{Solution 1.}

Number the children $1, \dots, n$, and denote the number of coins the $i$-th child has by $c_i$. A step of this process consists of reducing some $c_i$ by 2, and increasing $c_{i-1}, c_{i+1}$ by 1. (Indices are considered $\pmod{n}$.) Because $(i - 1) - 2i + (i + 1) = 0$, the quantity $\sum_{i=1}^n ic_i \pmod{n}$ will be invariant under this process. Hence a necessary condition for the children to end up with an uniform distribution of coins is that
\[
\sum_{i=1}^n ic_i = \frac{n(n+1)}{2} \pmod{n}.
\]

We will show that this condition is also sufficient. Consider an arbitrary initial distribution of coins. First, whenever child $i$ has more than one coin and $i \neq n$, have child $i$ pass coins to its neighbors. (Child $i$ does nothing.) Then, after some amount of such steps, it must eventually become impossible to do any more steps because no child except perhaps child $i$ has more than 1 coin. (To see this, consider e.g. the quantity $\sum_{i=1}^{n-1} i^2 c_i$, which (as $(i - 1)^2 + (i + 1)^2 > 2i^2$) increases at each step.)

Hence we can reach a state of the form $(z_1, \dots, z_{n-1}, M)$, where $z_i = 0$ or 1. Call such states semi-uniform states of irregularity $M$.

Lemma. If there is a string of children having coins $\underbrace{1, \dots, 1}_{k \text{ ones}}, b, \underbrace{1, \dots, 1}_{k \text{ ones}}, c$, with $b \ge 2$, after some sequence of steps we may reach the state $a + 1, \underbrace{1, \dots, 1}_{k \text{ ones}}, b-2, \underbrace{1, \dots, 1}_{k \text{ ones}}, c + 1$. We call performing this sequence of steps long-passing coins.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C5.} Let $m, n \ge 2$ be integers, let $X$ be a set with $n$ elements, and let $X_1, X_2, \dots, X_m$ be pairwise distinct non-empty, not necessary disjoint subsets of $X$. A function $f: X \to \{1, 2, \dots, n+1\}$ is called \textit{nice} if there exists an index $k$ such that
\[
\sum_{x \in X_k} f(x) > \sum_{x \in X_i} f(x) \text{ for all } i \neq k.
\]
Prove that the number of nice functions is at least $n^n$. \hfill (Germany)

\textbf{Solution.} For a subset $Y \subseteq X$, we write $f(Y)$ for $\sum_{y \in Y} f(y)$. Note that a function $f: X \to \{1, \dots, n+1\}$ is nice if and only if $f(X_i)$ is maximized by a unique index $i \in \{1, \dots, m\}$. We will first investigate the set $\mathcal{F}$ of functions $f: X \to \{1, \dots, n\}$; note that $|\mathcal{F}| = n^n$. For every function $f \in \mathcal{F}$, define a corresponding function $f^+: X \to \{1, 2, \dots, n+1\}$ in the following way: Pick some set $X_l$ that maximizes the value $f(X_l)$.

\begin{itemize}
    \item For all $x \in X_l$, define $f^+(x) = f(x) + 1$.
    \item For all $x \in X \backslash X_l$, define $f^+(x) = f(x)$.
\end{itemize}

\textbf{Claim.} The resulting function $f^+$ is nice.

\textbf{Proof.} Note that $f^+(X_i) = f(X_i) + |X_i \cap X_l|$ holds for all $X_i$. We show that $f^+(X_i)$ is maximized at the unique index $i = l$. Hence consider some arbitrary index $j \neq l$. Then $X_l \subset X_j$ is impossible, as this would imply $f(X_j) > f(X_i)$ and thereby contradict the choice of set $X_l$; this in particular yields $|X_i| > |X_j \cap X_i|$.
\begin{align*}
f^+(X_i) &= f(X_i) + |X_i| \\
&\ge f(X_j) + |X_i| > f(X_j) + |X_j \cap X_i| = f^+(X_j)
\end{align*}
The first inequality follows since $X_l$ was chosen to maximize the value $f(X_i)$. The second (strict) inequality follows from $|X_i| > |X_j \cap X_i|$ as observed above. This completes the proof of the claim. $\Box$

Next observe that function $f$ can be uniquely reconstructed from $f^+$; the claim yields that $f^+$ has a unique maximizer $X_i$, and by decreasing the value of $f^+$ on $X_i$ by 1, we get we can fully determine the values of $f$. As each of the $n^n$ functions $f \in \mathcal{F}$ yields a (unique) corresponding nice function $f^+: X \to \{1, 2, \dots, n+1\}$, the proof is complete.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{C6.} Let $n$ be a positive integer. We start with $n$ piles of pebbles, each initially containing a single pebble. One can perform moves of the following form: choose two piles, take an equal number of pebbles from each pile and form a new pile out of these pebbles. For each positive integer $n$, find the smallest number of non-empty piles that one can obtain by performing a finite sequence of moves of this form.

\textit{(Croatia)}

\textbf{Answer:} 1 if $n$ is a power of two, and 2 otherwise.

\textbf{Solution 1.} The solution we describe is simple, but not the most effective one.

We can combine two piles of $2^{k-1}$ pebbles to make one pile of $2^k$ pebbles. In particular, given $2^k$ piles of one pebble, we may combine them as follows:

\begin{align*}
2^k \text{ piles of 1 pebble} &\rightarrow 2^{k-1} \text{ piles of 2 pebbles} \\
2^{k-1} \text{ piles of 2 pebbles} &\rightarrow 2^{k-2} \text{ piles of 4 pebbles} \\
2^{k-2} \text{ piles of 4 pebbles} &\rightarrow 2^{k-3} \text{ piles of 8 pebbles} \\
&\vdots \\
2 \text{ piles of } 2^{k-1} \text{ pebbles} &\rightarrow 1 \text{ pile of } 2^k \text{ pebbles}
\end{align*}

This proves the desired result in the case when $n$ is a power of 2.

If $n$ is not a power of 2, choose $N$ such that $2^N < n < 2^{N+1}$. Let $m = n - 2^N$. Then $0 < m < 2^N$. Make a pile of $2^N$ pebbles and call it the \textit{large} pile. (Alternatively, one can be more efficient and make a pile of $2^M$ pebbles where $m \leq 2^M$.) Since $n$ is not a power of two, there is at least one other pile with pebbles. All other piles have a single pebble (initial condition).

Choose one single pebble pile and remove the pebble and one pebble from the \textit{large} pile and form a pile of 2 pebbles. If $m < 2^N - 1$, remove another pebble from the \textit{large} pile and one pebble from the 2-pile and form a new pile of 2 pebbles. Repeat until the \textit{large} pile contains exactly $m$ pebbles.

At this point we have one pile of $m$ pebbles, one pile of 2 pebbles, and the rest are single pebble piles. There must be $n - m - 2 = 2^N - 2$ single piles. Combine two and two into piles of two pebbles. Then there are $2^{N-1} - 1$ piles of two pebbles, which we can make into one pile of $2^N$ pebbles. We are left with exactly two piles of pebbles.

Lastly we will prove that it is not possible to form a single pile with all pebbles when $n$ is not a power of two. A move consists of choosing two piles of say $a$ and $b$ pebbles, then removing $c \leq \min(a, b)$ pebbles from both piles, and forming a new pile with $2c$ pebbles. If we include piles of zero pebbles, then this move changes the number of pebbles in three piles as follows (and leaves all other piles unchanged):

\begin{align*}
a &\rightarrow a - c \\
b &\rightarrow b - c \\
0 &\rightarrow 2c
\end{align*}

Assume that after the move the number of pebbles in each pile is divisible by an odd integer $m$. In particular, $m | 2c$, $m | a - c$ and $m | b - c$. Since $m$ is odd, it follows that $m | c$, and then that $m | a$ and $m | b$. Hence also before the move the number of pebbles in each pile is divisible by the integer $m$.

If $n$ is not a power of 2, then $n$ is divisible by an odd integer $m > 1$. In order to make a single pile of $n$ pebbles, we would have to start with a distribution in which the number of pebbles in each pile is divisible by the integer $m$. This is impossible when we start with all piles containing a single pebble.

\end{document}





\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{C7.} Lucy starts by writing $s$ integer-valued 2022-tuples on a blackboard. After doing that, she can take any two (not necessarily distinct) tuples $\mathbf{v} = (v_1, \dots, v_{2022})$ and $\mathbf{w} = (w_1, \dots, w_{2022})$ that she has already written, and apply one of the following operations to obtain a new tuple:

\begin{align*}
    \mathbf{v} + \mathbf{w} &= (v_1 + w_1, \dots, v_{2022} + w_{2022}) \\
    \mathbf{v} \vee \mathbf{w} &= (\max(v_1, w_1), \dots, \max(v_{2022}, w_{2022}))
\end{align*}

and then write this tuple on the blackboard.

It turns out that, in this way, Lucy can write any integer-valued 2022-tuple on the blackboard after finitely many steps. What is the smallest possible number $s$ of tuples that she initially wrote?

\textit{(Czech Republic)}

\textbf{Answer:} The smallest possible number is $s = 3$.

\textbf{Solution.} We solve the problem for $n$-tuples for any $n \geq 3$; we will show that the answer is $s = 3$, regardless of the value of $n$.

First, let us briefly introduce some notation. For an $n$-tuple $\mathbf{v}$, we will write $v_i$ for its $i$-th coordinate (where $1 \leq i \leq n$). For a positive integer $n$ and a tuple $\mathbf{v}$ we will denote by $n \cdot \mathbf{v}$ the tuple obtained by applying addition on $\mathbf{v}$ with itself $n$ times. Furthermore, we denote by $\mathbf{e}(i)$ the tuple which has $i$-th coordinate equal to one and all the other coordinates equal to zero. We say that a tuple is \textit{positive} if all its coordinates are positive, and \textit{negative} if all its coordinates are negative.

We will show that three tuples suffice, and then that two tuples do not suffice.

\textbf{Three tuples suffice.} Write $\mathbf{c}$ for the constant-valued tuple $\mathbf{c} = (-1, \dots, -1)$.

We note that it is enough for Lucy to be able to make the tuples $\mathbf{e}(1), \dots, \mathbf{e}(n); \mathbf{c}$ from those any other tuple $\mathbf{v}$ can be made as follows. First we choose some positive integer $k$ such that $k + v_i > 0$ for all $i$. Then, by adding a positive number of copies of $\mathbf{c}, \mathbf{e}(1), \dots, \mathbf{e}(n)$, she can make
$$ k\mathbf{c} + (k + v_1) \cdot \mathbf{e}(1) + \dots + (k + v_n) \cdot \mathbf{e}(n), $$
which we claim is equal to $\mathbf{v}$. Indeed, this can be checked by comparing coordinates: the $i$-th coordinate of the right-hand side is $-k + (k + v_i) = v_i$, as needed.

Lucy can take her three starting tuples to be $\mathbf{a}, \mathbf{b}$ and $\mathbf{c}$, such that $a_i = -i^2, b_i = i$ and $c = -1$ (as above).

For any $1 \leq j \leq n$, write $\mathbf{d}(j)$ for the tuple $2 \cdot \mathbf{a} + 4j \cdot \mathbf{b} + (2j^2 - 1) \cdot \mathbf{c}$, which Lucy can make by adding together $\mathbf{a}, \mathbf{b}$ and $\mathbf{c}$ repeatedly. This has $i$th term

\begin{align*}
    d(j)_i &= 2a_i + 4jb_i + (2j^2 - 1) c_i \\
    &= -2i^2 + 4ij - (2j^2 - 1) \\
    &= 1 - 2(i - j)^2.
\end{align*}

This is 1 if $j = i$, and at most -1 otherwise. Hence Lucy can produce the tuple $\mathbf{1} = (1, \dots, 1)$ as $\mathbf{d}(1) \vee \dots \vee \mathbf{d}(n)$.

She can then produce the constant tuple $\mathbf{0} = (0, \dots, 0)$ as $\mathbf{1} + \mathbf{c}$, and for any $1 \leq j \leq n$ she can then produce the tuple $\mathbf{e}(j)$ as $\mathbf{d}(j) \vee \mathbf{0}$. Since she can now produce $\mathbf{e}(1), \dots, \mathbf{e}(n)$ and already has $\mathbf{c}$, she can (as we argued earlier) produce any integer-valued tuple.

\textbf{Two tuples do not suffice.} We start with an observation: Let $a$ be a non-negative real number and suppose that two tuples $\mathbf{v}$ and $\mathbf{w}$ satisfy $v_j \geq a v_k$ and $w_j \geq a w_k$ for some $1 \leq j, k \leq n$. Then we claim that the same inequality holds for $\mathbf{v} + \mathbf{w}$ and $\mathbf{v} \vee \mathbf{w}$: Indeed, the property for the sum is verified by an easy computation:

$$ (\mathbf{v} + \mathbf{w})_j = v_j + w_j \geq a v_k + a w_k = a (\mathbf{v} + \mathbf{w})_k. $$

For the second operation, we denote by $\mathbf{m}$ the tuple $\mathbf{v} \vee \mathbf{w}$. Then $m_j \geq v_j \geq a v_k$ and $m_j \geq w_j \geq a w_k$. Since $m_k = v_k$ or $m_k = w_k$, the observation follows.

As a consequence of this observation we have that if all starting tuples satisfy such an inequality, then all generated tuples will also satisfy it, and so we would not be able to obtain every integer-valued tuple.

Let us now prove that Lucy needs at least three starting tuples. For contradiction, let us suppose that Lucy started with only two tuples $\mathbf{v}$ and $\mathbf{w}$. We are going to distinguish two cases. In the first case, suppose we can find a coordinate $i$ such that $v_i, w_i \geq 0$. Both operations preserve the sign, thus we can not generate any tuple that has negative $i$-th coordinate. Similarly for $v_i, w_i \leq 0$.

Suppose the opposite, i.e., for every $i$ we have either $v_i > 0 > w_i$, or $v_i < 0 < w_i$. Since we assumed that our tuples have at least three coordinates, by pigeonhole principle there exist two coordinates $j \neq k$ such that $v_j$ has the same sign as $v_k$ and $w_j$ has the same sign as $w_k$ (because there are only two possible combinations of signs).

Without loss of generality assume that $v_j, v_k > 0$ and $w_j, w_k < 0$. Let us denote the positive real number $v_j / v_k$ by $a$. If $w_j / w_k \leq a$, then both inequalities $v_j \geq a v_k$ and $w_j \geq a w_k$ are satisfied. On the other hand, if $w_j / w_k \leq a$, then both $v_k \geq (1/a) v_j$ and $w_k \geq (1/a) w_j$ are satisfied. In either case, we have found the desired inequality satisfied by both starting tuples, a contradiction with the observation above.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{C8.} Alice fills the fields of an $n \times n$ board with numbers from 1 to $n^2$, each number being used exactly once. She then counts the total number of good paths on the board. A good path is a sequence of fields of arbitrary length (including 1) such that:
\begin{enumerate}
    \item[(i)] The first field in the sequence is one that is only adjacent to fields with larger numbers,
    \item[(ii)] Each subsequent field in the sequence is adjacent to the previous field,
    \item[(iii)] The numbers written on the fields in the sequence are in increasing order.
\end{enumerate}

Two fields are considered adjacent if they share a common side. Find the smallest possible number of good paths Alice can obtain, as a function of $n$.

\textit{(Serbia)}

\textbf{Answer:} $2n^2 - 2n + 1$.

\textbf{Solution.}

We will call any field that is only adjacent to fields with larger numbers a well. Other fields will be called non-wells. Let us make a second $n \times n$ board $B$ where in each field we will write the number of good sequences which end on the corresponding field in the original board $A$. We will thus look for the minimal possible value of the sum of all entries in $B$.

We note that any well has just one good path ending in it, consisting of just the well, and that any other field has the number of good paths ending in it equal to the sum of this quantity for all the adjacent fields with smaller values, since a good path can only come into the field from a field of lower value. Therefore, if we fill in the fields in $B$ in increasing order with respect to their values in $A$, it follows that each field not adjacent to any already filled field will receive a 1, while each field adjacent to already filled fields will receive the sum of the numbers already written on these adjacent fields.

We note that there is at least one well in $A$, that corresponding with the field with the entry 1 in $A$. Hence, the sum of values of fields in $B$ corresponding to wells in $A$ is at least 1. We will now try to minimize the sum of the non-well entries, i.e. of the entries in $B$ corresponding to the non-wells in $A$. We note that we can ascribe to each pair of adjacent fields the value of the lower assigned number and that the sum of non-well entries will then equal to the sum of the ascribed numbers. Since the lower number is still at least 1, the sum of non-well entries will at least equal the number of pairs of adjacent fields, which is $2n(n-1)$. Hence, the total minimum sum of entries in $B$ is at least $2n(n-1) + 1 = 2n^2 - 2n + 1$. The necessary conditions for the minimum to be achieved is for there to be only one well and for no two entries in $B$ larger than 1 to be adjacent to each other.

We will now prove that the lower limit of $2n^2 - 2n + 1$ entries can be achieved. This amounts to finding a way of marking a certain set of squares, those that have a value of 1 in $B$, such that no two unmarked squares are adjacent and that the marked squares form a connected tree with respect to adjacency.

For $n = 1$ and $n = 2$ the markings are respectively the lone field and the L-trimino. Now, for $n > 2$, let $s = 2$ for $n \equiv 0, 2 \mod 3$ and $s = 1$ for $n \equiv 1 \mod 3$. We will take indices $k$ and $l$ to be arbitrary non-negative integers. For $n \geq 3$ we will construct a path of marked squares in the first two columns consisting of all squares of the form $(1, i)$ where $i$ is not of the form $6k + s$ and $(2, j)$ where $j$ is of the form $6k + s - 1, 6k + s$ or $6 + s + 1$. Obviously, this path is connected. Now, let us consider the fields $(2, 6k + s)$ and $(1, 6k + s + 3)$. For each considered field $(i, j)$ we will mark all squares of the form $(l, j)$ for $l > i$ and $(i + 2k, j \pm 1)$. One can easily see that no set of marked fields will produce a cycle, that the only fields of the unmarked form $(1, 6k + s), (2 + 2l + 1, 6k + s \pm 1)$ and $(2 + 2l, 6k + s + 3 \pm 1)$ and that no two are adjacent, since the consecutive considered fields are in columns of opposite parity. Examples of markings are given for $n = 3, 4, 5, 6, 7$, and the corresponding constructions for $A$ and $B$ are given for $n=5$.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{C9.} Let $\mathbb{Z}_{\geq 0}$ be the set of non-negative integers, and let $f: \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0} \rightarrow \mathbb{Z}_{\geq 0}$ be a bijection such that whenever $f(x_1, y_1) > f(x_2, y_2)$, we have $f(x_1 + 1, y_1) > f(x_2 + 1, y_2)$ and $f(x_1, y_1 + 1) > f(x_2, y_2 + 1)$.

Let $N$ be the number of pairs of integers $(x, y)$, with $0 \leq x, y < 100$, such that $f(x, y)$ is odd. Find the smallest and largest possible value of $N$.

\textit{(U.S.A.)}

\textbf{Answer:} The optimal bounds are $2500 \leq N \leq 7500$.

\textbf{Solution.} We defer the constructions to the end of the solution. Instead, we begin by characterizing all such functions $f$, prove a formula and key property for such functions, and then solve the problem, providing constructions.

\textbf{Characterization} Suppose $f$ satisfies the given relation. The condition can be written more strongly as
$$ f(x_1, y_1) > f(x_2, y_2) \iff f(x_1 + 1, y_1) > f(x_2 + 1, y_2) $$
$$ \iff f(x_1, y_1 + 1) > f(x_2, y_2 + 1). $$

In particular, this means for any $(k, l) \in \mathbb{Z}^2$, $f(x + k, y + l) - f(x, y)$ has the same sign for all $x$ and $y$.

Call a non-zero vector $(k, l) \in \mathbb{Z}_{\geq 0} \times \mathbb{Z}_{\geq 0}$ a \textit{needle} if $f(x + k, y) - f(x, y + l) > 0$ for all $x$ and $y$. It is not hard to see that needles and non-needles are both closed under addition, and thus under scalar division (whenever the quotient lives in $\mathbb{Z}^2$).

In addition, call a positive rational number $\frac{k}{l}$ a \textit{grade} if the vector $(k, l)$ is a needle. (Since needles are closed under scalar multiples and quotients, this is well-defined.)

Claim. Grades are closed upwards.

Proof. Consider positive rationals $\frac{k_1}{l_1} < \frac{k_2}{l_2}$ with $\frac{k_1}{l_1}$ a grade. Then:
\begin{itemize}
    \item $(k_1, l_1)$ is a needle,
    \item so $(k_1 l_2, l_1 l_2)$ is a needle,
    \item so $(k_2 l_1, l_1 l_2)$ is a needle (as $k_2 l_1 - k_1 l_2 > 0$ and $(1, 0)$ is a needle).
\end{itemize}
Thus $(k_2, l_2)$ is a needle, as wanted. $\square$

Claim. A grade exists.

Proof. If no positive integer $n$ is a grade, then $f(1, 0) > f(0, n)$ for all $n$ which is impossible. $\square$

Similarly, there is an $n$ such that $f(0, 1) < f(n, 0)$, thus $1/n$ is not a grade for some large $n$. That means that small positive rational values are not grades, then there is a switch, and after that all values are grades. Call the place of that switch $\alpha$. Here $\alpha$ is the infimum of the grades.

Claim (Key property). If $x_1 + y_1 \alpha > x_2 + y_2 \alpha$ then $f(x_1, y_1) > f(x_2, y_2)$.

Proof. If both $x_1 \geq x_2$ and $y_1 \geq y_2$ this is clear.

Suppose $x_1 \geq x_2$ and $y_1 < y_2$. Then $\frac{x_1 - x_2}{y_2 - y_1} > \alpha$ is a grade. This gives $f(x_1, y_1) > f(x_2, y_2)$.

Suppose $x_1 < x_2$ and $y_1 \geq y_2$. Then $\frac{x_1 - x_2}{y_2 - y_1} < \alpha$ is not a grade. This gives $f(x_2, y_2) < f(x_1, y_1)$.

From those observations we get the following claim.

Claim. The function $f$ orders pairs $(x, y)$ based on the value of $x + y\alpha$. If $\alpha$ is rational, tiebreaking is done by larger $x$- or $y$-coordinate (depending on whether $\alpha$ is a grade).

\end{document}










"""