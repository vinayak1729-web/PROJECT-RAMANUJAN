def numbertheory_2021():
    return r"""


\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N1.} Determine all integers $n \ge 1$ for which there exists a pair of positive integers $(a,b)$ such that no cube of a prime divides $a^2+b+3$ and
$$ \frac{ab+3b+8}{a^2+b+3} = n. $$

\textbf{Answer:} The only integer with that property is $n=2$.

\textbf{Solution.} As $b \equiv -a^2-3 \pmod{a^2+b+3}$, the numerator of the given fraction satisfies
$$ ab+3b+8 \equiv a(-a^2-3)+3(-a^2-3)+8 \equiv -a^3 -3a - 3a^2 - 9 + 8 \equiv -(a^3 + 3a^2 + 3a +1) \equiv -(a+1)^3 \pmod{a^2+b+3}. $$
Let $k = a^2+b+3$.  We are given that no cube of a prime divides $k$.  We have shown that $ab+3b+8 \equiv -(a+1)^3 \pmod{k}$.  Since $\frac{ab+3b+8}{a^2+b+3} = n$, we have $ab+3b+8 = nk$, so $nk \equiv -(a+1)^3 \pmod{k}$, which means $k$ divides $(a+1)^3$.
Since $k$ is not divisible by any $p^3$ for a prime $p$, it must be the case that if $k$ divides $(a+1)^3$, then $k$ must divide $(a+1)^2$.  
We have $(a+1)^2 = a^2 + 2a + 1$.  We also know that $k = a^2 + b + 3$.
If $k$ divides $(a+1)^2$, then there exists an integer $m$ such that $m(a^2+b+3) = (a+1)^2$, i.e., $ma^2 + mb + 3m = a^2 + 2a + 1$.

If $m=1$, we have $a^2+b+3 = a^2+2a+1$, so $b+3=2a+1$, or $b = 2a-2 = 2(a-1)$.
Then $k = a^2 + 2a - 2 + 3 = a^2 + 2a + 1 = (a+1)^2$.  
Also, $ab+3b+8 = a(2a-2) + 3(2a-2) + 8 = 2a^2 - 2a + 6a - 6 + 8 = 2a^2 + 4a + 2 = 2(a+1)^2 = 2k$.
Thus, $\frac{ab+3b+8}{a^2+b+3} = \frac{2k}{k} = 2$, so $n=2$.

If $m \geq 2$, we must have $0 < (a+1)^2 = a^2 + 2a + 1 < a^2+b+3$ which means $2a+1 < b+3$ or $2a-2 < b$. But we also know that $2(a+1)^2 = 2a^2+4a+2$ must be divisible by $a^2+b+3$ so if $b > 2a+1$, we have $(a+1)^2 < a^2+b+3$, i.e.,  $m > 1$, which is possible.

Since we want to show that $n=2$ is the only solution, consider the smallest value of $a$. If $a=1$, then $b = 0$, which isn't allowed. If $a=2$, then $b=2$, $a^2+b+3 = 9$, $ab+3b+8 = 4+6+8=18$, so $n=2$.

Final Answer: The final answer is $\boxed{2}$
\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N2.} Let $n \ge 100$ be an integer. The numbers $n, n+1, \dots, 2n$ are written on $n+1$ cards, one number per card. The cards are shuffled and divided into two piles. Prove that one of the piles contains two cards such that the sum of their numbers is a perfect square.

\textbf{Solution.} To solve the problem it suffices to find three squares and three cards with numbers $a, b, c$ on them such that pairwise sums $a+b, b+c, a+c$ are equal to the chosen squares. By choosing the three consecutive squares $(2k-1)^2, (2k)^2, (2k+1)^2$ we arrive at the triple
$$ (a,b,c) = (2k^2-4k, \ 2k^2+1, \ 2k^2+4k). $$
We need a value for $k$ such that all three numbers are within the range $[n, 2n]$:
$$ n \le 2k^2-4k, \quad n \le 2k^2+1, \quad n \le 2k^2+4k, $$
and
$$ 2k^2-4k \le 2n, \quad 2k^2+1 \le 2n, \quad 2k^2+4k \le 2n. $$
Combining these inequalities, we need
$$ n \le 2k^2-4k \quad \text{and} \quad 2k^2+4k \le 2n. $$
or
$$ n \le 2k^2-4k \quad \text{and} \quad k^2+2k \le n. $$
A concrete $k$ is suitable for all $n$ with
$$ n \in [k^2+2k, 2k^2-4k+1] =: I_k. $$
For $k \ge 9$ the intervals $I_k$ and $I_{k+1}$ overlap because we want to show
$$ (k+1)^2 + 2(k+1) \le 2k^2 - 4k + 1 $$
$$ k^2 + 2k + 1 + 2k + 2 \le 2k^2 - 4k + 1 $$
$$ k^2 - 8k - 2 \ge 0 $$
The roots of $k^2 - 8k - 2 = 0$ are $k = \frac{8 \pm \sqrt{64 + 8}}{2} = \frac{8 \pm \sqrt{72}}{2} = 4 \pm 3\sqrt{2}$.  Since $3\sqrt{2} \approx 4.2$, we have roots around $8.2$ and $-0.2$.  Thus, for $k \ge 9$, $k^2 - 8k - 2 \ge 0$, which means the intervals overlap.

$I_9 = [99, 127]$, $I_{10} = [120, 161]$, $I_{11} = [143, 200]$, etc.

Hence $I_9 \cup I_{10} \cup \dots = [99, \infty)$, which proves the statement for $n \ge 99$. Since the problem states $n \ge 100$, the condition is satisfied and the statement is proven.


\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N3.} Find all positive integers $n$ with the following property: the $k$ positive divisors of $n$ have a permutation $(d_1, d_2, \dots, d_k)$ such that for every $i=1, 2, \dots, k$, the number $d_1 + d_2 + \dots + d_i$ is a perfect square.

\textbf{Answer:} $n=1$ and $n=3$.

\textbf{Solution.} For $i=1, 2, \dots, k$ let $d_1 + \dots + d_i = s_i^2$, and define $s_0 = 0$ as well. Obviously $0 = s_0 < s_1 < s_2 < \dots < s_k$, so
$$ s_i \ge i \quad \text{and} \quad d_i = s_i^2 - s_{i-1}^2 = (s_i + s_{i-1})(s_i - s_{i-1}) \ge s_i + s_{i-1} \ge 2i-1. \quad (1) $$
The number 1 is one of the divisors $d_1, \dots, d_k$ but, due to $d_i \ge 2i-1$, the only possibility is $d_1 = 1$.

Now consider $d_2$ and $s_2 \ge 2$. By definition, $d_2 = s_2^2 - 1 = (s_2-1)(s_2+1)$, so the numbers $s_2-1$ and $s_2+1$ are divisors of $n$. In particular, there is some index $j$ such that $d_j = s_2+1$. Notice that
$$ s_2 + s_1 = s_2+1 = d_j \ge s_j + s_{j-1}; \quad (2) $$
since the sequence $s_0 < s_1 < \dots < s_k$ increases, the index $j$ cannot be greater than 2. Hence, the divisors $s_2-1$ and $s_2+1$ are listed among $d_1$ and $d_2$. That means $s_2-1 = d_1 = 1$ and $s_2+1 = d_2$; therefore $s_2 = 2$ and $d_2 = 3$.

We can repeat the above process in general.

\textbf{Claim.} $d_i = 2i-1$ and $s_i = i$ for $i = 1, 2, \dots, k$.

\textbf{Proof.} Apply induction on $i$. The Claim has been proved for $i=1, 2$. Suppose that we have already proved $d_1 = 1$, $d_2 = 3, \dots, d_i = 2i-1$, and consider the next divisor $d_{i+1}$:
$$ d_{i+1} = s_{i+1}^2 - s_i^2 = s_{i+1}^2 - i^2 = (s_{i+1} - i)(s_{i+1} + i). $$
The number $s_{i+1} + i$ is a divisor of $n$, so there is some index $j$ such that $d_j = s_{i+1} + i$.

Similarly to (2), by (1) we have
$$ s_{i+1} + s_i = s_{i+1} + i = d_j \ge s_j + s_{j-1}; \quad (3) $$
since the sequence $s_0 < s_1 < \dots < s_k$ increases, (3) forces $j \le i+1$. On the other hand, $d_j = s_{i+1} + i > 2i > d_i > d_{i-1} > \dots > d_1$, so $j \le i$ is not possible. The only possibility is $j = i+1$. Hence,
$$ s_{i+1} + i = d_{i+1} = s_{i+1}^2 - s_i^2 = s_{i+1}^2 - i^2; $$
$$ s_{i+1}^2 - s_{i+1} = i(i+1). $$
By solving this equation we get $s_{i+1} = i+1$ and $d_{i+1} = 2i+1$, that finishes the proof. $\square$

Now we know that the positive divisors of the number $n$ are $1, 3, 5, \dots, n-2, n$. The greatest divisor is $d_k = 2k-1 = n$ itself, so $n$ must be odd. The second greatest divisor is $d_{k-1} = n-2$; then $n-2$ divides $n = (n-2) + 2$, so $n-2$ divides 2. Therefore, $n$ must be 1 or 3.

The numbers $n=1$ and $n=3$ obviously satisfy the requirements: for $n=1$ we have $k=1$ and $d_1 = 1 = 1^2$; for $n=3$ we have $k=2$, $d_1=1$ and $d_2=3$ and $1+3 = 2^2$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N4.} Alice is given a rational number $r > 1$ and a line with two points $R \ne B$, where point $R$ contains a red bead and point $B$ contains a blue bead. Alice plays a solitaire game by performing a sequence of moves. In every move, she chooses a (not necessarily positive) integer $k$, and a bead to move. If that bead is placed at point $X$, and the other bead is placed at $Y$, then Alice moves the chosen bead to point $X'$ with $\overrightarrow{YX'} = r^k \overrightarrow{YX}$.

Alice's goal is to move the red bead to the point $B$. Find all rational numbers $r > 1$ such that Alice can reach her goal in at most 2021 moves.

\textbf{Answer:} All $r = (b+1)/b$ with $b=1, \dots, 1010$.

\textbf{Solution.} Denote the red and blue beads by $\mathcal{R}$ and $\mathcal{B}$, respectively. Introduce coordinates on the line and identify the points with their coordinates so that $\mathcal{R}=0$ and $\mathcal{B}=1$. Then, during the game, the coordinate of $\mathcal{R}$ is always smaller than the coordinate of $\mathcal{B}$. Moreover, the distance between the beads always has the form $r^\ell$ with $\ell \in \mathbb{Z}$, since it only multiplies by numbers of this form. Denote the value of the distance after the $m^{th}$ move by $d_m = r^{\ell_m}$, where $\ell_m \in \mathbb{Z}$ (after the $0^{th}$ move we have just the initial position, so $d_0 = 1$).

If some bead is moved in two consecutive moves, then Alice could instead perform a single move (and change the distance from $d$ directly to $d_{i+2}$) which has the same effect as these two moves. So, if Alice can achieve her goal, then she may as well achieve it in fewer (or the same) number of moves by alternating the moves of $\mathcal{B}$ and $\mathcal{R}$. In the sequel, we assume that Alice alternates the moves, and that $\mathcal{R}$ is shifted altogether $r$ times.

If $\mathcal{R}$ is shifted in the $m^{th}$ move, then its coordinate increases by $d_{m-1}$. Therefore, the total increment of $\mathcal{R}$'s coordinate, which should be 1, equals

either
$$ (d_0 - d_1) + (d_2 - d_3) + \dots + (d_{2i-2} - d_{2i-1}) = 1 + \sum_{k=1}^i r^{\alpha_{k-1}} - \sum_{k=1}^i r^{\alpha_k}, $$
or
$$ (d_1 - d_2) + (d_3 - d_4) + \dots + (d_{2i-1} - d_{2i}) = -1 + \sum_{k=1}^i r^{\alpha_{k-1}} - \sum_{k=1}^i r^{\alpha_k}, $$
depending on whether $\mathcal{R}$ or $\mathcal{B}$ is shifted in the first move. Moreover, in the former case we should have $i \le 1011$, while in the latter one we need $i \le 1010$. So both cases reduce to an equation

$$ \sum_{i=1}^n r^{\beta_i} - \sum_{i=1}^n r^{\gamma_i} = 1, \quad \beta_i, \gamma_i \in \mathbb{Z}, \quad (1) $$
for some $n \le 1011$. Thus, if Alice can reach her goal, then this equation has a solution for $n = 1011$ (we can add equal terms to both sums in order to increase $n$).

Conversely, if (1) has a solution for $n = 1011$, then Alice can compose a corresponding sequence of distances $d_0, d_1, \dots, d_{2021}$ and then realise it by a sequence of moves. So the problem reduces to the solvability of (1) for $n = 1011$.

Assume that, for some rational $r$, there is a solution of (1). Write $r$ in lowest terms as $r=a/b$. Substitute this into (1), multiply by the common denominator, and collect all terms on the left hand side to get
$$ \sum_{i=1}^{2n-1} (-1)^i a^{\mu_i} b^{N - \mu_i} = 0, \quad \mu_i \in \{0, 1, \dots, N\}, \quad (2) $$
for some $N > 0$. We assume that there exist indices $j_+$ and $j_-$ such that $\mu_{j_+} = 0$ and $\mu_{j_-} = N$.

\textbf{Shortlisted problems - solutions}

Reducing (2) modulo $a-b$ (so that $a=b$), we get
$$ 0 = \sum_{i=1}^{2n-1} (-1)^i a^{\mu_i} b^{N - \mu_i} = \sum_{i=1}^{2n-1} (-1)^i b^{N} = - b^N \text{ mod } (a-b). $$
Since $\text{gcd}(a-b, b)=1$, this is possible only if $a-b = 1$.

Reducing (2) modulo $a+b$ (so that $a = -b$), we get
$$ 0 = \sum_{i=1}^{2n-1} (-1)^i a^{\mu_i} b^{N - \mu_i} = \sum_{i=1}^{2n-1} (-1)^i (-1)^{\mu_i} b^{N - \mu_i} = - S b^N \text{ mod } (a+b) $$
for some odd (thus nonzero) $S$ with $|S| \le 2n - 1$. Since $\text{gcd}(a+b, b) = 1$, this is possible only if $a+b | S$. So $a+b \le 2n - 1$, and hence $b= a - 1 \le n - 1 \le 1010$.

Thus we have shown that any sought $r$ has the form indicated in the answer. It remains to show that for any $b=1, 2, \dots, 1010$ and $a=b+1$, Alice can reach the goal. For this purpose, in (1) we put $n=b$, $\beta_1 = -1$, $\beta_2 = \dots = \beta_b = 0$, and $\gamma_1 = \dots = \gamma_b = -1$.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N5.} Prove that there are only finitely many quadruples $(a,b,c,n)$ of positive integers such that
$$ n! = a^{n-1} + b^{n-1} + c^{n-1}. $$

\textbf{Solution.} For fixed $n$ there are clearly finitely many solutions; we will show that there is no solution with $n > 100$. So, assume $n > 100$. By the AM-GM inequality,
\begin{align*} n! &= 2n(n-1)(n-2)(n-3) \cdot (3 \cdot 4 \dots (n-4)) \\ &\le 2(n-1)^4 \left( \frac{3 + \dots + (n-4)}{n-6} \right)^{n-6} = 2(n-1)^4 \left( \frac{n-1}{2} \right)^{n-6} < \left( \frac{n-1}{2} \right)^{n-1}, \end{align*}
thus $a, b, c < (n-1)/2$.

For every prime $p$ and integer $m \ne 0$, let $\nu_p(m)$ denote the $p$-adic valuation of $m$; that is, the greatest non-negative integer $k$ for which $p^k$ divides $m$. Legendre's formula states that
$$ \nu_p(n!) = \sum_{s=1}^{\infty} \left\lfloor \frac{n}{p^s} \right\rfloor, $$
and a well-know corollary of this formula is that
$$ \nu_p(n!) < \sum_{s=1}^{\infty} \frac{n}{p^s} = \frac{n}{p-1}. \quad (\heartsuit) $$

If $n$ is odd then $a^{n-1}, b^{n-1}, c^{n-1}$ are squares, and by considering them modulo 4 we conclude that $a, b$ and $c$ must be even. Hence, $2^{n-1} \mid n!$ but that is impossible for odd $n$ because $\nu_2(n!) < n-1$ by $(\heartsuit)$.

From now on we assume that $n$ is even. If all three numbers $a+b, b+c, c+a$ are powers of 2 if they all are odd, then $n! = a^{n-1} + b^{n-1} + c^{n-1}$ is also odd which is absurd. If all $a, b, c$ are divisible by 4, this contradicts $\nu_2(n!) \le n-1$. If, say, $a$ is not divisible by 4, then $2a = (a+b) + (a+c) - (b+c)$ is not divisible by 8, and since all $a+b, b+c, c+a$ are powers of 2, we get that one of these sums equals 4, so two of the numbers of $a, b, c$ are equal to 2. Say, $a=b=2$, then $c=2^r-2$ and, since $c \mid n!$, we must have $c \mid a^{n-1} + b^{n-1} = 2^n$ implying $r=2$, and so $c=2$, which is impossible because $n! \equiv 0 \not\equiv 3 \cdot 2^{n-1}$ (mod 5).

So now we assume that the sum of two numbers among $a, b, c$, say $a+b$, is not a power of 2, so it is divisible by some odd prime $p$. Then $p \le a+b < n$ and so $c^{n-1} = n! - (a^{n-1} + b^{n-1})$ is divisible by $p$. If $p$ divides $a$ and $b$, we get $p^{n-1} \mid n!$, contradicting $(\heartsuit)$. Next, using $(\heartsuit)$ and the Lifting the Exponent Lemma we get
$$ \nu_p(1!) + \nu_p(2!) + \dots + \nu_p(n!) = \nu_p(n!) = \nu_p(n! - c^{n-1}) = \nu_p(a^{n-1} + b^{n-1}) = \nu_p(a+b) + \nu_p(n-1). \quad (\diamondsuit) $$

In view of $(\diamondsuit)$, no number of $1, 2, \dots, n$ can be divisible by $p$, except $a+b$ and $n-1>a+b$. On the other hand, $p \mid c$ implies that $p < n/2$ and so there must be at least two such numbers. Hence, there are two multiples of $p$ among $1, 2, \dots, n$, namely $a+b = p$ and $n-1 = 2p$. But this is another contradiction because $n-1$ is odd. This final contradiction shows that there is no solution of the equation for $n > 100$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N6.} Determine all integers $n \ge 2$ with the following property: every $n$ pairwise distinct integers whose sum is not divisible by $n$ can be arranged in some order $a_1, a_2, \dots, a_n$ so that $n$ divides $1 \cdot a_1 + 2 \cdot a_2 + \dots + n \cdot a_n$.

\textbf{Answer:} All odd integers and all powers of 2.

\textbf{Solution.} If $n = 2^\alpha a$, where $a \ge 3$ is odd and $k$ is a positive integer, we can consider a set containing the number $2^\alpha + 1$ and $n-1$ numbers congruent to 1 modulo $n$. The sum of these numbers is congruent to $2^\alpha + 1 + n - 1 = n + 2^\alpha$ modulo $n$ and therefore is not divisible by $n$; for any permutation $(a_1, a_2, \dots, a_n)$ of these numbers
$$ 1 \cdot a_1 + 2 \cdot a_2 + \dots + n \cdot a_n \equiv 1 + \dots + n = \frac{n(n+1)}{2} = 2^{\alpha-1}a(2^\alpha a + 1) \not\equiv 0 \pmod{2^\alpha} $$
and \textit{a fortiori} $1 \cdot a_1 + 2 \cdot a_2 + \dots + n \cdot a_n$ is not divisible by $n$.

From now on, we suppose that $n$ is either odd or a power of 2. Let $S$ be the given set of integers, and $s$ be the sum of elements of $S$.

\textbf{Lemma 1.} If there is a permutation $(a_i)$ of $S$ such that $(n, s)$ divides $\sum_{i=1}^n ia_i$, then there is a permutation $(b_i)$ of $S$ such that $n$ divides $\sum_{i=1}^n ib_i$.

\textbf{Proof.} Let $r = \sum_{i=1}^n ia_i$. Consider the permutation $(b_i)$ defined by $b_i = a_{i+x}$, where $a_{j+n} = a_j$. For this permutation, we have
$$ \sum_{i=1}^n ib_i - \sum_{i=1}^n ia_i = \sum_{i=1}^n i(a_{i+x} - a_i) = \sum_{i=1}^n i(-x)a_i = -sx \pmod n. $$
Since $(n, s)$ divides $r$, the congruence $r - sx \equiv 0 \pmod n$ admits a solution.

\textbf{Lemma 2.} Every set $T$ of $km$ integers, $m>1$, can be partitioned into $m$ sets of $k$ integers so that in every set either the sum of elements is not divisible by $k$ or all the elements leave the same remainder upon division by $k$.

\textbf{Proof.} The base case, $m=2$. If $T$ contains $k$ elements leaving the same remainder upon division by $k$, we form one subset $A$ of these elements; the remaining elements form a subset $B$. If $k$ does not divide the sum of all elements of $B$, we are done. Otherwise it is enough to exchange any element of $A$ with any element of $B$ not congruent to it modulo $k$, thus making sums of both $A$ and $B$ not divisible by $k$. This cannot be done only when all the elements of $T$ are congruent modulo $k$; in this case any partition will do.

If no $k$ elements of $T$ have the same residue modulo $k$, there are three elements $a,b,c \in T$ leaving pairwise distinct remainders upon division by $k$. Let $t$ be the sum of elements of $T$. It suffices to find $A \subset T$ such that $|A| = k$ and $\sum_{T \setminus A} a \equiv 0 \pmod k$; then neither the sum of elements of $A$ nor the sum of elements of $B = T \setminus A$ is divisible by $k$. Consider $U = T \setminus \{a, b, c\}$ with $|U| = k-1$. The sums of elements of three sets $U \cup \{a\}, U \cup \{b\}, U \cup \{c\}$ leave three different remainders upon division by $k$, and at least one of them is not congruent either to 0 or to $t$.

Now let $m>2$. If $T$ contains $k$ elements leaving the same remainder upon division by $k$, we form one subset $A$ of these elements and apply the inductive hypothesis to the remaining $k(m-1)$ elements. Otherwise, we choose any $U \subset T$, $|U|=k-1$. Since all the remaining elements cannot be congruent modulo $k$, there is a $a \in T \setminus U$ such that $a \not\equiv -\sum_{x \in U} x \pmod k$. Now we can take $A = U \cup \{a\}$ and apply the inductive hypothesis to $T \setminus A$.


\textbf{Shortlisted problems -- solutions}

Now we are ready to prove the statement of the problem for all odd $n$ and $n=2^k$. The proof is by induction.

If $n$ is prime, the statement follows immediately from Lemma 1, since in this case $(n,s)=1$. Turning to the general case, we can find prime $p$ and an integer $t$ such that $p^t \mid n$ and $p^t \nmid s$. By Lemma 2, we can partition $S$ into sets of $k=n/p^t$ elements so that in every set either the sum of members is not divisible by $k$ or all numbers have the same residue modulo $k$. For sets in the first category, by the inductive hypothesis there is a permutation such that $k | \sum ia_i$.

If $n=2^k$, we have $p=2$ and $k=2^{k-t}$. Then for each of the subsets there is a permutation.

Now the numbers of each permutation should be multiplied by all the odd or all the even numbers not exceeding $n$ in increasing order so that the resulting sums are divisible by $k$.


Combining these two sums, we again get a permutation $[c_i]$ of $S$ such that $k | \sum ic_i$, and finish the case by applying Lemma 1.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{N7.} Let $a_1, a_2, a_3, \dots$ be an infinite sequence of positive integers such that $a_{n+2m}$ divides $a_n + a_{n+m}$ for all positive integers $n$ and $m$. Prove that this sequence is eventually periodic, i.e. there exist positive integers $N$ and $d$ such that $a_n = a_{n+d}$ for all $n > N$.

\textbf{Solution.} We will make repeated use of the following simple observation:

\textbf{Lemma 1.} If a positive integer $d$ divides $a_n$ and $a_{n+m}$ for some $m$ and $n > 2m$, it also divides $a_{n-2m}$. If $d$ divides $a_n$ and $a_{n-2m}$ it also divides $a_{n-m}$.

\textbf{Proof.} Both parts are obvious since $a_n$ divides $a_{n-2m} + a_{n-m}$. $\square$

\textbf{Claim.} The sequence $(a_n)$ is bounded.

\textbf{Proof.} Suppose the contrary. Then there exist infinitely many indices $n$ such that $a_n$ is greater than each of the previous terms $a_1, a_2, \dots, a_{n-1}$. Let $a_n = k$ be such a term, $n > 10$. For each $s < \frac{n}{2}$ the number $a_n = k$ divides $a_{n-s} + a_{n-2s} < 2k$, therefore
$$ a_{n-s} + a_{n-2s} = k. $$
In particular,
$$ a_n = a_{n-1} + a_{n-2} = a_{n-2} + a_{n-4} = a_{n-4} + a_{n-8}, $$
that is, $a_{n-1} = a_{n-4}$ and $a_{n-2} = a_{n-8}$. It follows from Lemma 1 that $a_{n-1}$ divides $a_{n-1-3s}$ for $3s < n-1$ and $a_{n-2}$ divides $a_{n-2-6s}$ for $6s < n-2$. Since at least one of the numbers $a_{n-1}$ and $a_{n-2}$ is at least $a_n/2$, so is some $a_i$ with $i \le 6$. However, $a_n$ can be arbitrarily large. $\square$

Since $(a_n)$ is bounded, there exist only finitely many $i$ for which $a_i$ appears in the sequence for infinitely many times $j$. In other words, there exists $N$ such that if $a_i = t$ and $i > N$, then $a_j = t$ for infinitely many $j$.

Clearly the sequence $(a_n)_{n > 0}$ satisfies the divisibility condition, and it is enough to prove that this sequence is eventually periodic. Thus truncating the sequence if necessary, we can assume that each number appears infinitely many times in the sequence. Let $k$ be the maximum number appearing in the sequence.

\textbf{Lemma 2.} If a positive integer $d$ divides $a_n$ for some $n$, then the numbers $i$ such that $d$ divides $a_i$ form an arithmetical progression with an odd difference.

\textbf{Proof.} Let $i_1 < i_2 < i_3 < \dots$ be all the indices $i$ such that $d$ divides $a_i$. If $i_s + i_{s+1}$ is even, it follows from Lemma 1 that $d$ also divides $a_{\frac{i_s + i_{s+1}}{2}}$, impossible since $i_s < \frac{i_s + i_{s+1}}{2} < i_{s+1}$. Thus $i_s$ and $i_{s+1}$ are always of different parity, and therefore $i_s + i_{s+2}$ is even. Applying Lemma 1 again, we see that $d$ divides $a_{\frac{i_s + i_{s+2}}{2}}$, hence $\frac{i_s + i_{s+2}}{2} = i_{s+1}$. $\square$


We are ready now to solve the problem.

The number of positive divisors of all terms of the progression is finite. Let $d_s$ be the difference of the progression corresponding to $s$, that is, $s \mid a_i \iff i \equiv r \pmod{d_s}$ for any positive integer $r$. Let $D$ be the product of all $d_s$. Then each dividing a term of the progression divides $a_n$ if and only if it divides $a_{n+D}$. This means that the sets of divisors of $a_n$ and $a_{n+D}$ coincide, and $a_{n+D} = a_n$. Thus $D$ is a period of the sequence.


\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\section*{N8.}

For a polynomial $P(x)$ with integer coefficients let $P^1(x) = P(x)$ and $P^{k+1}(x) = P(P^k(x))$ for $k \geq 1$. Find all positive integers $n$ for which there exists a polynomial $P(x)$ with integer coefficients such that for every integer $m \geq 1$, the numbers $P^m(1), \dots, P^m(n)$ leave exactly $\lfloor n/2^m \rfloor$ distinct remainders when divided by $n$.

\section*{Answer:}

All powers of 2 and all primes.

\section*{Solution:}

Denote the set of residues modulo $\ell$ by $\mathbb{Z}_\ell$. Observe that $P$ can be regarded as a function $\mathbb{Z}_\ell \to \mathbb{Z}_\ell$ for any positive integer $\ell$. Denote the cardinality of the set $P^m(\mathbb{Z}_\ell)$ by $f_{m, \ell}$. Note that $f_{m, n} = \lfloor n/2^m \rfloor$ for all $m \geq 1$ if and only if $f_{m+1, n} = \lfloor f_{m, n}/2 \rfloor$ for all $m \geq 0$.

\textbf{Part 1. The required polynomial exists when $n$ is a power of 2 or a prime.}

If $n$ is a power of 2, set $P(x) = 2x$.

If $n = p$ is an odd prime, every function $f: \mathbb{Z}_p \to \mathbb{Z}_p$ coincides with some polynomial with integer coefficients. So we can pick the function that sends $x \in \{0, 1, \dots, p-1\}$ to $\lfloor x/2 \rfloor$.

\textbf{Part 2. The required polynomial does not exist when $n$ is not a prime power.}

Let $n = ab$ where $a, b > 1$ and $\gcd(a, b) = 1$. Note that, since $\gcd(a, b) = 1$,
\[ f_{m, ab} = f_{m, a} f_{m, b} \]
by the Chinese remainder theorem. Also, note that, if $f_{m, \ell} = f_{m+1, \ell}$, then $P$ permutes the image of $P^m$ on $\mathbb{Z}_\ell$, and therefore $f_{s, \ell} = f_{m, \ell}$ for all $s > m$. So, as $f_{m, ab} = 1$ for sufficiently large $m$, we have for each $m$
\[ f_{m, a} > f_{m+1, a} \quad \text{or} \quad f_{m, a} = 1, \quad f_{m, b} > f_{m+1, b} \quad \text{or} \quad f_{m, b} = 1. \]

Choose the smallest $m$ such that $f_{m+1, a} = 1$ or $f_{m+1, b} = 1$. Without loss of generality assume that $f_{m+1, a} = 1$. Then $f_{m+1, ab} = f_{m+1, b} < f_{m, b} \leq f_{m, ab}/2 \leq f_{m+1, ab}$, a contradiction.

\textbf{Part 3. The required polynomial does not exist when $n$ is an odd prime power that is not a prime.}

Let $n = p^k$, where $p \geq 3$ is prime and $k \geq 2$. For $r \in \mathbb{Z}_{p^k}$ let $S_r$ denote the subset of $\mathbb{Z}_{p^k}$ consisting of numbers congruent to $r$ modulo $p$. We denote the cardinality of a set $S$ by $|S|$.

\textbf{Claim.} For any residue $r$ modulo $p$, either $|P(S_r)| = p^{k-1}$ or $|P(S_r)| \leq p^{k-2}$.

\textbf{Proof.} Recall that $P(r+h) = P(r) + hP'(r) + h^2 Q(r, h)$, where $Q$ is an integer polynomial. If $p \nmid P'(r)$, then $P(r + ps) \equiv P(r) \pmod{p^2}$, hence all elements of $P(S_r)$ are congruent modulo $p^2$. So in this case $|P(S_r)| \leq p^{k-2}$.

Now we show that $p \mid P'(r)$ implies $|P(S_r)| = p^{k-1}$ for all $k$. Suppose the contrary: $|P(S_r)| < p^{k-1}$ for some $k > 1$. Let us choose the smallest $k$ for which this is so. To each residue in $P(S_r)$ we assign its residue modulo $p^{k-1}$; denote the resulting set by $\overline{P(S_r)}$. We have $|\overline{P(S_r)}| < p^{k-1}$ by virtue of minimality of $k$. Then $|P(S_r)| < p^{k-1} - p |\overline{P(S_r)}|$. That is, there is $u = P(x) \in P(S_r)$ ($x \equiv r \pmod{p}$) and $t \neq 0 \pmod{p}$ such that $u + p^{k-1} t \notin P(S_r)$.

Note that $P(x + p^{k-1} s) \equiv u + p^{k-1} s P'(x) \pmod{p^k}$. Since $P(x + p^{k-1} s) \neq u + p^{k-1} t \pmod{p^k}$, the congruence $p^{k-1} s P'(x) \equiv p^{k-1} t \pmod{p^k}$ has no solutions. So the congruence $s P'(x) \equiv t \pmod{p}$ has no solutions, which contradicts $p \mid P'(r)$. $\Box$

Since the image of $P^m$ consists of one element for sufficiently large $m$, we can take the smallest $m$ such that $|P^{m-1}(S_r)| = p^{k-1}$ for some $r \in \mathbb{Z}_p$, but $|P^m(S_q)| \leq p^{k-2}$ for all $q \in \mathbb{Z}_p$. From now on, we fix $m$ and $r$.

Since the image of $P^{m-1}(\mathbb{Z}_{p^k}) \setminus P^{m-1}(S_r)$ under $P$ contains $P^m(\mathbb{Z}_{p^k}) \setminus P^m(S_r)$, we have
\[ a := |P^m(\mathbb{Z}_{p^k}) \setminus P^m(S_r)| \leq |P^{m-1}(\mathbb{Z}_{p^k}) \setminus P^{m-1}(S_r)|, \]
thus
\[ a + p^{k-1} \leq f_{m-1, p^k} \leq 2f_{m, p^k} \leq 2p^{k-2} + 2a, \]
so
\[ (p-2)p^{k-2} \leq a. \]

Since $f_{i, p} = 1$ for sufficiently large $i$, there is exactly one $t \in \mathbb{Z}_p$ such that $P(t) \equiv t \pmod{p}$. Moreover, as $i$ increases, the cardinality of the set $\{s \in \mathbb{Z}_p \mid P^i(s) \equiv t \pmod{p} \}$ increases (strictly), until it reaches the value $p$. So either
\[ |\{s \in \mathbb{Z}_p \mid P^{m-1}(s) \equiv t \pmod{p} \}| = p \quad \text{or} \quad |\{s \in \mathbb{Z}_p \mid P^{m-1}(s) \equiv t \pmod{p} \}| \geq m. \]

Therefore, either $f_{m-1, p} = 1$ or there exists a subset $X \subset \mathbb{Z}_p$ of cardinality at least $m$ such that $P^{m-1}(x) \equiv t \pmod{p}$ for all $x \in X$. In the first case $|P^{m-1}(\mathbb{Z}_{p^k})| \leq p^{k-1} - |P^{m-1}(S_r)|$, so $a = 0$, a contradiction. In the second case let $Y$ be the set of all elements of $\mathbb{Z}_{p^k}$ congruent to some element of $X$ modulo $p$. Let $Z = \mathbb{Z}_{p^k} \setminus Y$. Then $P^{m-1}(Y) \subseteq S_t$, $P(S_t) \subseteq S_t$, and $\mathbb{Z}_{p^k} \setminus ( \cup_{x \in X} S_x)$, so
\[ |P^m(Y)| \leq |P(S_t)| \leq p^{k-2} \quad \text{and} \quad |P^m(Z)| \leq |\mathbb{Z}_{p^k} \setminus X| \cdot p^{k-2} \leq (p-m+1)p^{k-2}. \]

Hence,
\[ (p-2)p^{k-2} \leq a < |P^m(\mathbb{Z}_{p^k})| \leq |P^m(Y)| + |P^m(Z)| \leq (p-m+1)p^{k-2} \]
and $m < 3$. Then $|P^2(S_q)| \leq p^{k-2}$ for all $q \in \mathbb{Z}_p$, so
\[ p^{k}/4 \leq |P^2(\mathbb{Z}_{p^k})| \leq p^{k-1}, \]
which is impossible for $p \geq 5$. It remains to consider the case $p=3$.

As before, let $t$ be the only residue modulo 3 such that $P(t) \equiv t \pmod{3}$.

If $3 \nmid P'(t)$, then $P(S_t) = S_t$ by the proof of the Claim above, which is impossible. So $3 \mid P'(t)$. By substituting $h - 3s$'s into the formula $P(t + h) = P(t) + h P'(t) + h^2 Q(t, h)$, we obtain $P(t+3^s s) \equiv P(t) \pmod{3^{s+1}}$. Using induction on $i$ we see that all elements of $P^i(S_t)$ are congruent modulo $3^{i+1}$. Thus, $|P^{k-1}(S_t)| = 1$.

Note that $f_{1,3} \leq 2$ and $f_{2,3} \leq 1$, so $P^2(\mathbb{Z}_{3^k}) \subseteq S_t$. Therefore, $|P^{k+1}(\mathbb{Z}_{3^k})| \leq |P^{k-1}(S_t)| = 1$. It follows that $3^k \leq 2^{k-1}$, which is impossible for $k \geq 2$.
\end{document}












"""