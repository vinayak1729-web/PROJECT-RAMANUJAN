def algebra_prompt():
    return r"""
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A1.} Let $\mathbb{Z}$ be the set of integers. Determine all functions $f: \mathbb{Z} \to \mathbb{Z}$ such that, for all integers $a$ and $b$,
\[
f(2a) + 2f(b) = f(f(a + b)). \tag{1}
\]
\textit{(South Africa)}

\medskip
\noindent \textbf{Answer:} The solutions are $f(n) = 0$ and $f(n) = 2n + K$ for any constant $K \in \mathbb{Z}$.

\medskip
\noindent \textbf{Common remarks.} Most solutions to this problem first prove that $f$ must be linear, before determining all linear functions satisfying (1).

\medskip
\noindent \textbf{Solution 1.} Substituting $a = 0, b = n + 1$ gives $f(0) + 2f(n+1) = f(f(n+1))$. Substituting $a = 1, b = n$ gives $f(2) + 2f(n) = f(f(n + 1))$.
In particular, $f(0) + 2f(n+1) = f(2) + 2f(n)$, and so $f(n+1) - f(n) = \frac{1}{2} (f(2) - f(0))$.
Thus $f(n+1) - f(n)$ must be constant. Since $f$ is defined only on $\mathbb{Z}$, this tells us that $f$ must be a linear function; write $f(n) = Mn + K$ for arbitrary constants $M$ and $K$, and we need only determine which choices of $M$ and $K$ work.
Now, (1) becomes
\[
2Ma + K + 2(Mb + K) = M(M(a + b) + K) + K
\]
which we may rearrange to form
\[
(M - 2)(M(a + b) + K) = 0.
\]
Thus, either $M = 2$, or $M(a + b) + K = 0$ for all values of $a + b$. In particular, the only possible solutions are $f(n) = 0$ and $f(n) = 2n + K$ for any constant $K \in \mathbb{Z}$, and these are easily seen to work.

\end{document}



\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A2.} Let $u_1, u_2, \dots, u_{2019}$ be real numbers satisfying
\[
u_1 + u_2 + \cdots + u_{2019} = 0 \quad \text{and} \quad u_1^2 + u_2^2 + \cdots + u_{2019}^2 = 1.
\]
Let $a = \min(u_1, u_2, \dots, u_{2019})$ and $b = \max(u_1, u_2, \dots, u_{2019})$. Prove that
\[
ab \le -\frac{1}{2019}.
\]

\medskip
\textit{(Germany)}

\medskip
\noindent \textbf{Solution 1.} Notice first that $b > 0$ and $a < 0$. Indeed, since $\sum_{i=1}^{2019} u_i^2 = 1$, the variables $u_i$ cannot be all zero, and, since $\sum_{i=1}^{2019} u_i = 0$, the nonzero elements cannot be all positive or all negative.

\medskip
Let $P = \{i : u_i > 0 \}$ and $N = \{i : u_i \le 0 \}$ be the indices of positive and nonpositive elements in the sequence, and let $p = |P|$ and $n = |N|$ be the sizes of these sets; then $p + n = 2019$. By the condition $\sum_{i=1}^{2019} u_i = 0$ we have $0 = \sum_{i=1}^{2019} u_i = \sum_{i \in P} u_i + \sum_{i \in N} u_i = \sum_{i \in P} u_i - \sum_{i \in N} |u_i|$, so
\[
\sum_{i \in P} u_i = \sum_{i \in N} |u_i|. \tag{1}
\]

\medskip
After this preparation, estimate the sum of squares of the positive and nonpositive elements as follows:
\begin{align*}
\sum_{i \in P} u_i^2 &\le \sum_{i \in P} b u_i = b \sum_{i \in P} u_i = b \sum_{i \in N} |u_i| \le b \sum_{i \in N} |a| = -nab; \tag{2} \\
\sum_{i \in N} u_i^2 &= \sum_{i \in N} |u_i|^2 \le \sum_{i \in N} |a| \cdot |u_i| = |a| \sum_{i \in N} |u_i| = |a| \sum_{i \in P} u_i \le |a| \sum_{i \in P} b = -pab. \tag{3}
\end{align*}

\medskip
The sum of these estimates is
\begin{align*}
1 = \sum_{i=1}^{2019} u_i^2 = \sum_{i \in P} u_i^2 + \sum_{i \in N} u_i^2 \le -nab - pab = -(p + n) ab = -2019ab,
\end{align*}
that proves $ab \le -\frac{1}{2019}$.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A3.} Let $n \ge 3$ be a positive integer and let $(a_1, a_2, \dots, a_n)$ be a strictly increasing sequence of $n$ positive real numbers with sum equal to 2. Let $X$ be a subset of $\{1, 2, \dots, n\}$ such that the value of
\[
\left| 1 - \sum_{i \in X} a_i \right|
\]
is minimised. Prove that there exists a strictly increasing sequence of $n$ positive real numbers $(b_1, b_2, \dots, b_n)$ with sum equal to 2 such that
\[
\sum_{i \in X} b_i = 1.
\]

\medskip
\noindent \textit{(New Zealand)}

\medskip
\noindent \textbf{Common remarks.} In all solutions, we say an index set $X$ is $(a_i)$-minimising if it has the property in the problem for the given sequence $(a_i)$. Write $X^c$ for the complement of $X$, and $[a, b]$ for the interval of integers $k$ such that $a \le k \le b$. Note that
\[
\left| 1 - \sum_{i \in X} a_i \right| = \left| 1 - \sum_{i \in X^c} a_i \right|,
\]
so we may exchange $X$ and $X^c$ where convenient. Let
\[
\Delta = \sum_{i \in X^c} a_i - \sum_{i \in X} a_i.
\]
and note that $X$ is $(a_i)$-minimising if and only if it minimises $|\Delta|$, and that $\sum_{i \in X} a_i = 1$ if and only if $\Delta = 0$.

\medskip
In some solutions, a scaling process is used. If we have a strictly increasing sequence of positive real numbers $c_i$ (typically obtained by perturbing the $a_i$ in some way) such that
\[
\sum_{i \in X} c_i = \sum_{i \in X^c} c_i,
\]
then we may put $b_i = 2c_i / \sum_{j=1}^n c_j$. So it suffices to construct such a sequence without needing its sum to be 2.

\medskip
The solutions below show various possible approaches to the problem. Solutions 1 and 2 perturb a few of the $a_i$ to form the $b_i$ (with scaling in the case of Solution 1, without scaling in the case of Solution 2). Solutions 3 and 4 look at properties of the index set $X$. Solution 3 then perturbs many of the $a_i$ to form the $b_i$, together with scaling. Rather than using such perturbations, Solution 4 constructs a sequence $(b_i)$ directly from the set $X$ with the required properties. Solution 4 can be used to give a complete description of sets $X$ that are $(a_i)$-minimising for some $(a_i)$.

\medskip
\noindent \textbf{Solution 1.} Without loss of generality, assume $\sum_{i \in X} a_i \le 1$, and we may assume strict inequality as otherwise $b_i = a_i$ works. Also, $X$ clearly cannot be empty.
If $n \in X$, add $\Delta$ to $a_n$, producing a sequence of $c_i$ with $\sum_{i \in X} c_i = \sum_{i \in X} a_i + \Delta = \sum_{i \in X^c} a_i$, and then scale as described above to make the sum equal to 2. Otherwise, there is some $k$ with $k \in X$ and $k + 1 \in X^c$. Let $\delta = a_{k+1} - a_k$.
\begin{itemize}
    \item If $\delta > \Delta$, add $\Delta$ to $a_k$ and then scale.
    \item If $\delta < \Delta$, then considering $X \cup \{k + 1\} \setminus \{k\}$ contradicts $X$ being $(a_i)$-minimising.
    \item If $\delta = \Delta$, choose any $j \ne k, k+1$ (possible since $n \ge 3$), and any $\epsilon$ less than the least of $\delta$ and all the differences $a_{i+1} - a_i$. If $j \in X$ then add $\Delta - \epsilon$ to $a_k$ and $\epsilon$ to $a_j$, then scale; otherwise, add $\Delta$ to $a_k$ and $\epsilon/2$ to $a_{k+1}$, and subtract $\epsilon/2$ from $a_j$, then scale.
\end{itemize}

\end{document}


\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A4.} Let $n \ge 2$ be a positive integer and $a_1, a_2, \dots, a_n$ be real numbers such that
\[
a_1 + a_2 + \cdots + a_n = 0.
\]
Define the set $A$ by
\[
A = \{(i, j) \mid 1 \le i < j \le n, |a_i - a_j| \ge 1\}.
\]
Prove that, if $A$ is not empty, then
\[
\sum_{(i,j) \in A} a_i a_j < 0.
\]

\medskip
\noindent \textit{(China)}

\medskip
\noindent \textbf{Solution 1.} Define sets $B$ and $C$ by
\begin{align*}
B &= \{(i, j) \mid 1 \le i < j \le n, |a_i - a_j| \ge 1\}, \\
C &= \{(i, j) \mid 1 \le i < j \le n, |a_i - a_j| < 1\}.
\end{align*}

\medskip
We have
\begin{align*}
\sum_{(i,j) \in A} a_i a_j &= \sum_{(i,j) \in B} a_i a_j \\
&= \frac{1}{2} \sum_{(i,j) \in B} a_i a_j \\
\sum_{(i,j) \in B} a_i a_j &= \sum_{1 \le i < j \le n} a_i a_j - \sum_{(i,j) \notin B} a_i a_j \\
&= \sum_{1 \le i < j \le n} a_i a_j - \sum_{(i,j) \in C} a_i a_j \\
&= \sum_{1 \le i < j \le n} a_i a_j - \sum_{(i,j) \in B} a_i a_j - \sum_{(i,j) \in C} a_i a_j.
\end{align*}
So it suffices to show that if $A$ (and hence $B$) are nonempty, then
\[
\sum_{(i,j) \in C} a_i a_j > 0.
\]

\medskip
Partition the indices into sets $P$, $Q$, $R$, and $S$ such that
\begin{align*}
P &= \{i \mid a_i \le -1\} & R &= \{i \mid 0 < a_i < 1\} \\
Q &= \{i \mid -1 < a_i \le 0\} & S &= \{i \mid 1 \le a_i \}.
\end{align*}
Then
\begin{align*}
\sum_{(i,j) \in C} a_i a_j &\ge \sum_{\substack{(i,j) \in C \\ i,j \in S}} a_i a_j + \sum_{\substack{(i,j) \in C \\ i \in Q \cup R}} a_i a_j \\
&= \sum_{\substack{(i,j) \in C \\ i,j \in S}} a_i a_j + \left( \sum_{i \in Q \cup R} a_i \right)^2 \ge 0.
\end{align*}
The first inequality holds because all of the positive terms in the RHS are also in the LHS, and all of the negative terms in the LHS are also in the RHS. The first inequality attains equality only if both sides have the same negative terms, which implies $|a_i - a_j| < 1$ whenever $i, j \in Q \cup R$; the second inequality attains equality only if $P = S = \emptyset$. But then we would have $A = \emptyset$. So $A$ nonempty implies that the inequality holds strictly, as required.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A5.} Let $x_1, x_2, \dots, x_n$ be different real numbers. Prove that
\[
\sum_{1 \le i \le n} \prod_{\substack{j=1 \\ j \neq i}}^n \frac{1 - x_i x_j}{x_i - x_j} = \begin{cases} 0, & \text{if $n$ is even;} \\ 1, & \text{if $n$ is odd.} \end{cases}
\]

\medskip
\noindent \textit{(Kazakhstan)}

\medskip
\noindent \textbf{Common remarks.} Let $G(x_1, x_2, \dots, x_n)$ be the function of the $n$ variables $x_1, x_2, \dots, x_n$ on the LHS of the required identity.

\medskip
\noindent \textbf{Solution 1 (Lagrange interpolation).} Since both sides of the identity are rational functions, it suffices to prove it when all $x_i \notin \{\pm 1\}$. Define
\[
f(t) = \prod_{i=1}^n (1 - x_i t),
\]
and note that
\[
f(x_i) = (1 - x_i^2) \prod_{\substack{j=1 \\ j \neq i}}^n (1 - x_i x_j).
\]
Using the nodes $+1, -1, x_1, \dots, x_n$, the Lagrange interpolation formula gives us the following expression for $f$:
\begin{align*}
f(x) &= \sum_{i=1}^n f(x_i) \frac{(x - 1)(x + 1)}{(x_i - 1)(x_i + 1)} \prod_{\substack{j=1 \\ j \neq i}}^n \frac{x - x_j}{x_i - x_j} \\
&+ f(1) \frac{x + 1}{1 + 1} \prod_{1 \le j \le n} \frac{x - x_j}{1 - x_j} + f(-1) \frac{x - 1}{-1 - 1} \prod_{1 \le j \le n} \frac{x - x_j}{-1 - x_j}.
\end{align*}
The coefficient of $t^{n+1}$ in $f(t)$ is 0, since $f$ has degree $n$. The coefficient of $t^{n+1}$ in the above expression of $f$ is
\begin{align*}
0 &= \sum_{i=1}^n \frac{f(x_i)}{(x_i - 1)(x_i + 1)} \prod_{\substack{j=1 \\ j \neq i}}^n \frac{1}{x_i - x_j} + \frac{f(1)}{1 + 1} \prod_{1 \le j \le n} \frac{1}{1 - x_j} + \frac{f(-1)}{-1 - 1} \prod_{1 \le j \le n} \frac{1}{-1 - x_j} \\
&= \sum_{i=1}^n \prod_{\substack{j=1 \\ j \neq i}}^n \frac{1 - x_i x_j}{(x_i - x_j)(x_i^2 - 1)} + \frac{1}{2} \prod_{1 \le j \le n} \frac{1 - x_j}{1 - x_j} - \frac{1}{2} \prod_{1 \le j \le n} \frac{1 + x_j}{1 + x_j} \\
&= -G(x_1, \dots, x_n) + \frac{1}{2} + \frac{(-1)^{n+1}}{2}.
\end{align*}

\medskip
\noindent \textbf{Comment.} The main difficulty is to think of including the two extra nodes $\pm 1$ and evaluating the coefficient $t^{n+1}$ in $f$ when $n + 1$ is higher than the degree of $f$.
It is possible to solve the problem using Lagrange interpolation on the nodes $x_1, \dots, x_n$, but the definition of the polynomial being interpolated should depend on the parity of $n$. For $n$ even, consider the polynomial
\[
P(x) = \prod_{i=1}^n (1 - x x_i) - \prod_{i=1}^n (x - x_i).
\]
Lagrange interpolation shows that $G$ is the coefficient of $x^{n-1}$ in the polynomial $P(x)/(1 - x^2)$, i.e. 0.
For $n$ odd, consider the polynomial
\[
P(x) = \prod_{i=1}^n (1 - x x_i) - x \prod_{i=1}^n (x - x_i).
\]
Now $G$ is the coefficient of $x^{n-1}$ in $P(x)/(1 - x^2)$, which is 1.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A7.} Let $\mathbb{Z}$ be the set of integers. We consider functions $f: \mathbb{Z} \to \mathbb{Z}$ satisfying
\[
f(f(x + y) + y) = f(f(x) + y)
\]
for all integers $x$ and $y$. For such a function, we say that an integer $v$ is $f$-\textit{rare} if the set
\[
X_v = \{ x \in \mathbb{Z} : f(x) = v \}
\]
is finite and nonempty.
\begin{enumerate}
    \item[(a)] Prove that there exists such a function $f$ for which there is an $f$-rare integer.
    \item[(b)] Prove that no such function $f$ can have more than one $f$-rare integer.
\end{enumerate}

\medskip
\noindent \textit{(Netherlands)}

\medskip
\noindent \textbf{Solution 1.} \textbf{a)} Let $f$ be the function where $f(0) = 0$ and $f(x)$ is the largest power of $2$ dividing $2x$ for $x \ne 0$. The integer $0$ is evidently $f$-rare, so it remains to verify the functional equation.

\medskip
Since $f(2x) = 2f(x)$ for all $x$, it suffices to verify the functional equation when at least one of $x$ and $y$ is odd (the case $x = y = 0$ being trivial). If $y$ is odd, then we have
\[
f(f(x+y) + y) = 2 = f(f(x) + y)
\]
since all the values attained by $f$ are even. If, on the other hand, $x$ is odd and $y$ is even, then
\[
f(x + y) = 2 = f(x)
\]
from which the functional equation follows immediately.

\medskip
\noindent \textbf{b)} An easy inductive argument (substituting $x + ky$ for $x$) shows that
\[
f(f(x + ky) + y) = f(f(x) + y) \tag{*}
\]
for all integers $x, y$ and $k$. If $v$ is an $f$-rare integer and $a$ is the least element of $X_v$, then by substituting $y = a - f(x)$ in the above, we see that
\[
f(x + k \cdot (a - f(x))) - f(x) + a \in X_v
\]
for all integers $x$ and $k$, so that in particular
\[
f(x + k \cdot (a - f(x))) \ge f(x)
\]
for all integers $x$ and $k$, by assumption on $a$. This says that on the (possibly degenerate) arithmetic progression through $x$ with common difference $a - f(x)$, the function $f$ attains its minimal value at $x$.

\medskip
Repeating the same argument with $a$ replaced by the greatest element $b$ of $X_v$ shows that
\[
f(x + k \cdot (b - f(x))) \le f(x)
\]
for all integers $x$ and $k$. Combined with the above inequality, we therefore have
\[
f(x + k \cdot (a - f(x))) \cdot f(x + k \cdot (b - f(x))) = f(x) \tag{\dag}
\]
for all integers $x$ and $k$.

\medskip
Thus if $f(x) \ne a, b$, then the set $X_{f(x)}$ contains a nondegenerate arithmetic progression, so is infinite. So the only possible $f$-rare integers are $a$ and $b$.
In particular, the $f$-rare integer $v$ we started with must be one of $a$ or $b$, so that $f(v) = f(a) = f(b) = v$. This means that there cannot be any other $f$-rare integers $v'$, as they would on the one hand have to be either $a$ or $b$, and on the other would have to satisfy $f(v') = v'$.
Thus $v$ is the unique $f$-rare integer.

\vspace{1cm}
\hrulefill \textit{Shortlisted problems - solutions} \hrulefill 29

\medskip
\noindent \textbf{Comment 1.} If $f$ is a solution to the functional equation, then so too is any conjugate of $f$ by a translation, i.e. any function $x \mapsto f(x + n) - n$ for an integer $n$. Thus in proving part (b), one is free to consider only functions $f$ for which 0 is $f$-rare, as in the following solution.

\end{document}



"""