def numbertheory2022():

    return r"""

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N1.} A number is called \textit{Norwegian} if it has three distinct positive divisors whose sum is equal to 2022. Determine the smallest Norwegian number.

(Note: The total number of positive divisors of a Norwegian number is allowed to be larger than 3.)

\textit{(Cyprus)}

\textbf{Answer:} 1344

\textbf{Solution.} Observe that 1344 is a Norwegian number as 6, 672 and 1344 are three distinct divisors of 1344 and $6 + 672 + 1344 = 2022$. It remains to show that this is the smallest such number.

Assume for contradiction that $N < 1344$ is Norwegian and let $N/a, N/b$ and $N/c$ be the three distinct divisors of $N$, with $a < b < c$. Then
$$ 2022 = N \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \right) < 1344 \left( \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \right) $$
and so
$$ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} > \frac{2022}{1344} = \frac{337}{224} = \frac{3}{2} + \frac{1}{224}. $$

If $a > 1$ then
$$ \frac{1}{a} + \frac{1}{b} + \frac{1}{c} \leq \frac{1}{2} + \frac{1}{3} + \frac{1}{4} = \frac{13}{12} < \frac{3}{2}, $$
so it must be the case that $a = 1$. Similarly, it must hold that $b < 4$ since otherwise
$$ 1 + \frac{1}{b} + \frac{1}{c} \leq 1 + \frac{1}{4} + \frac{1}{5} < \frac{3}{2}. $$

This leaves two cases to check, $b = 2$ and $b = 3$.

\textbf{Case} $b = 3$. Then
$$ \frac{1}{c} > \frac{3}{2} + \frac{1}{224} - 1 - \frac{1}{3} > \frac{1}{6}, $$
so $c = 4$ or $c = 5$. If $c = 4$ then
$$ 2022 = N \left( 1 + \frac{1}{3} + \frac{1}{4} \right) = \frac{19}{12} N, $$
but this is impossible as $19 \nmid 2022$. If $c = 5$ then
$$ 2022 = N \left( 1 + \frac{1}{3} + \frac{1}{5} \right) = \frac{23}{15} N, $$
which again is impossible, as $23 \nmid 2022$.

\textbf{Case} $b = 2$. Note that $c < 224$ since
$$ \frac{1}{c} > \frac{3}{2} + \frac{1}{224} - 1 - \frac{1}{2} = \frac{1}{224}. $$

It holds that
$$ 2022 = N \left( 1 + \frac{1}{2} + \frac{1}{c} \right) = \frac{3c + 2}{2c} N \implies (3c + 2) N = 4044 c. $$
Since $(c, 3c - 2) = (c, 2) \in \{1, 2\}$, then $3c + 2 \mid 8088 = 2^3 \cdot 3 \cdot 337$ which implies that $3c + 2 \mid 2^3 \cdot 337$. But since $3c + 2 \geq 3 \cdot 3 + 2 = 8 = 2^3$ and $3c + 2 \neq 337$, then it must hold that $3c + 2 > 2 \cdot 337$, contradicting $c < 224$.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N2.} Find all positive integers $n > 2$ such that
$$ n! \mid \prod_{\substack{p < q \leq n \\ p, q \text{ primes}}} (p + q). $$

\textit{(Nigeria)}

\textbf{Answer:} This only holds for $n = 7$.

\textbf{Solution.} Assume that $n$ satisfies $n! \mid \prod_{p < q \leq n} (p + q)$ and let $2 = p_1 < p_2 < \dots < p_m \leq n$ be the primes in $\{1, 2, \dots, n\}$. Each such prime divides $n!$. In particular, $p_m \mid p_i + p_j$ for some $p_i < p_j \leq n$. But
$$ 0 < \frac{p_i + p_j}{p_m} \leq \frac{p_{m-1} + p_m}{p_m} < 2, $$
so $p_m = p_i + p_j$ which implies $m \geq 3$, $p_i = 2$ and $p_m = 2 + p_j = 2 + p_{m-1}$.

Similarly, $p_{m-1} \mid p_k + p_l$ for some $p_k < p_l \leq n$. But
$$ 0 < \frac{p_l + p_k}{p_{m-1}} \leq \frac{p_m + p_{m-1}}{p_{m-1}} = \frac{2p_{m-1} + 2}{p_{m-1}} < 3, $$
so either $p_{m-1} = p_l + p_k$ or $2p_{m-1} = p_l + p_k$. As above, the former case gives $p_{m-1} = 2 + p_{m-2}$. If $2p_{m-1} = p_l + p_k$, then $p_{m-1} < p_k$, so $k = m$ and
$$ 2p_{m-1} = p_l + p_{m-1} + 2 \implies p_{m-1} = p_l + 2 = p_{m-2} + 2. $$

Either way, $p_{m-2} > 2$ and 3 divides one of $p_{m-2}, p_{m-1} = p_{m-2} + 2$ and $p_m = p_{m-2} + 4$. This implies $p_{m-2} = 3$ and thus $p_m = 7$, giving $7 \leq n < 11$.

Finally, a quick computation shows that $7 \mid \prod_{p < q \leq 7} (p + q)$ but $8 \nmid \prod_{p < q \leq 7} (p + q)$, so neither does $9!$ and $10!$.

\end{document}





\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N3.} Let $a > 1$ be a positive integer, and let $d > 1$ be a positive integer coprime to $a$. Let $x_1 = 1$ and, for $k \geq 1$, define
$$ x_{k+1} = \begin{cases}
x_k + d & \text{if $a$ doesn't divide $x_k$,} \\
x_k/a & \text{if $a$ divides $x_k$.}
\end{cases} $$

Find the greatest positive integer $n$ for which there exists an index $k$ such that $x_k$ is divisible by $a^n$.

\textit{(Croatia)}

\textbf{Answer:} $n$ is the exponent with $d < a^n < ad$.

\textbf{Solution 1.} By trivial induction, $x_k$ is coprime to $d$.

By induction and the fact that there can be at most $a - 1$ consecutive increasing terms in the sequence, it also holds that $x_k < da$ if $x_k = x_{k-1} + d$ and that $x_k < d$ if $x_k = \frac{x_{k-1}}{a}$ or $k = 1$. This gives the upper bound on the exponent.

This implies that the sequence is (eventually) periodic, and that both increasing and decreasing steps happen infinitely many times. Let $a^{-k}$ be the multiplicative inverse of $a^k$ modulo $d$. The sequence contains elements congruent to $1, a^{-1}, a^{-2}, \dots$ modulo $d$.

Let $x_{k_0}$ the first element such that $x_{k_0} \equiv a^{-n} \pmod{d}$. We have either $k_0 = 1$ or $x_{k_0} = x_{k_0-1}/a$; in both cases $x_{k_0} < d < a^n < da$ and therefore
$$ x_{k_0} \in \{a^n - d, a^n - 2d, \dots, a^n - (a - 1)d\}. $$

In this set no element is divisible by $a$, so therefore the sequence will visit the value $a^n$ in the next $a - 1$ steps.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N4.} Find all triples of positive integers $(a, b, p)$ with $p$ prime and
$$ a^p = b! + p. $$

\textit{(Belgium)}

\textbf{Answer:} $(2, 2, 2)$ and $(3, 4, 3)$.

\textbf{Solution 1.} Clearly, $a > 1$. We consider three cases.

\textbf{Case 1:} We have $a < p$. Then we either have $a \leq b$ which implies $a \mid a^p - b! = p$ leading to a contradiction, or $a > b$ which is also impossible since in this case we have $b! \leq a! < a^p - p$, where the last inequality is true for any $p > a > 1$.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N5.} For each $1 \leq i \leq 9$ and $T \in \mathbb{N}$, define $d_i(T)$ to be the total number of times the digit $i$ appears when all the multiples of 1829 between 1 and $T$ inclusive are written out in base 10.

Show that there are infinitely many $T \in \mathbb{N}$ such that there are precisely two distinct values among $d_1(T), d_2(T), \dots, d_9(T)$.

\textit{(United Kingdom)}

\textbf{Solution.} Let $n := 1829$. First, we choose some $k$ such that $n \mid 10^k - 1$. For instance, any multiple of $\varphi(n)$ would work since $n$ is coprime to 10. We will show that either $T = 10^k - 1$ or $T = 10^k - 2$ has the desired property, which completes the proof since $k$ can be taken to be arbitrary large.

For this it suffices to show that $\#\{d_i(10^k - 1) : 1 \leq i \leq 9 \} \leq 2$. Indeed, if
$$ \#\{d_i(10^k - 1) : 1 \leq i \leq 9 \} = 1 $$
then, since $10^k - 1$ which consists of all nines is a multiple of $n$, we have
$$ d_i(10^k - 2) = d_i(10^k - 1) \text{ for } i \in \{1, \dots, 8\}, \text{ and } d_9(10^k - 2) < d_9(10^k - 1). $$

This means that $\#\{d_i(10^k - 2) : 1 \leq i \leq 9 \} = 2$.

To prove that $\#\{d_i(10^k - 1) \} \leq 2$ we need an observation. Let $\overline{a_{k-1} a_{k-2} \dots a_0} \in \{1, \dots, 10^k - 1 \}$ be the decimal expansion of an arbitrary number, possibly with leading zeroes. Then $\overline{a_{k-1} a_{k-2} \dots a_0}$ is divisible by $n$ if and only if $\overline{a_{k-2} \dots a_0 a_{k-1}}$ is divisible by $n$. Indeed, this follows from the fact that
$$ 10 \cdot \overline{a_{k-1} a_{k-2} \dots a_0} - \overline{a_{k-2} \dots a_0 a_{k-1}} = (10^k - 1) \cdot a_{k-1} $$
is divisible by $n$.

This observation shows that the set of multiples of $n$ between 1 and $10^k - 1$ is invariant under simultaneous cyclic permutation of digits when numbers are written with leading zeroes. Hence, for each $i \in \{1, \dots, 9\}$ the number $d_i(10^k - 1)$ is $k$ times larger than the number of $k$ digit numbers which start from the digit $i$ and are divisible by $n$. Since the latter number is either $\lfloor 10^{k-1}/n \rfloor$ or $1 + \lfloor 10^{k-1}/n \rfloor$, we conclude that $\#\{d_i(10^k - 1) \} \leq 2$.

\end{document}







\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N6.} Let $Q$ be a set of prime numbers, not necessarily finite. For a positive integer $n$ consider its prime factorisation; define $p(n)$ to be the sum of all the exponents and $q(n)$ to be the sum of the exponents corresponding only to primes in $Q$. A positive integer $n$ is called \textit{special} if $p(n) + p(n+1)$ and $q(n) + q(n+1)$ are both even integers. Prove that there is a constant $c > 0$ independent of the set $Q$ such that for any positive integer $N > 100$, the number of special integers in $[1, N]$ is at least $cN$.

(For example, if $Q = \{3, 7\}$, then $p(42) = 3, q(42) = 2, p(63) = 3, q(63) = 3, p(2022) = 3, q(2022) = 1$.)

\textit{(Costa Rica)}

\textbf{Solution.} Let us call two positive integers $m, n$ \textit{friends} if $p(m) + p(n)$ and $q(m) + q(n)$ are both even integers. We start by noting that the pairs $(p(k), q(k))$ modulo 2 can take at most 4 different values; thus, among any five different positive integers there are two which are friends.

In addition, both functions $p$ and $q$ satisfy $f(ab) = f(a) + f(b)$ for any $a, b$. Therefore, if $m$ and $n$ are divisible by $d$, then both $p$ and $q$ satisfy the equality $f(m) + f(n) = f(m/d) + f(n/d) + 2f(d)$. This implies that $m, n$ are friends if and only if $m/d, n/d$ are friends.

Let us call a set of integers $\{n_1, n_2, \dots, n_5\}$ an \textit{interesting} set if for any indexes $i, j$, the difference $d_{ij} = |n_i - n_j|$ divides both $n_i$ and $n_j$. We claim that if elements of an interesting set are all positive, then we can obtain a special integer. Indeed, if we were able to construct such a set, then there would be a pair of integers $\{n_i, n_j\}$ which are friends, according to the first observation. Additionally, the second observation yields that the quotients $n_i/d_{ij}, n_j/d_{ij}$ form a pair of friends, which happen to be consecutive integers, thus giving a special integer as desired.

In order to construct a family of interesting sets, we can start by observing that the set $\{0, 6, 8, 9, 12\}$ is an interesting set. Using that $72 = 2^3 \cdot 3^2$ is the least common multiple of all pairwise differences in this set, we obtain a family of interesting sets by considering
$$ \{72k, 72k + 6, 72k + 8, 72k + 9, 72k + 12\}, $$
for any $k \geq 1$. If we consider the quotients (of these numbers by the appropriate differences), then we obtain that the set
$$ S_k = \{6k, 8k, 9k, 12k, 12k + 1, 18k + 2, 24k + 2, 24k + 3, 36k + 3, 72k + 8\}, $$
has at least one special integer. In particular, the interval $[1, 100k]$ contains the sets $S_1, S_2, \dots, S_k$, each of which has a special number. Any special number can be contained in at most ten sets $S_k$, from where we conclude that the number of special integers in $[1, 100k]$ is at least $k/10$.

Finally, let $N = 100k + r$, with $k \geq 1$ and $0 \leq r < 100$, so that we have $N < 100(k+1) \leq 200k$. Then the number of special integers in $[1, N]$ is at least $k/10 > N/2000$, as we wanted to prove.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N7.} Let $k$ be a positive integer and let $S$ be a finite set of odd prime numbers. Prove that there is at most one way (modulo rotation and reflection) to place the elements of $S$ around a circle such that the product of any two neighbors is of the form $x^2 + x + k$ for some positive integer $x$.

\textit{(U.S.A.)}

\textbf{Solution.} Let us allow the value $x = 0$ as well; we prove the same statement under this more general constraint. Obviously that implies the statement with the original conditions.

Call a pair $\{p, q\}$ of primes with $p \neq q$ \textit{special} if $pq = x^2 + x + k$ for some nonnegative integer $x$. The following claim is the key mechanism of the problem:

\textbf{Claim.}
\begin{itemize}
    \item[(a)] For every prime $r$, there are at most two primes less than $r$ forming a special pair with $r$.
    \item[(b)] If such $p$ and $q$ exist, then $\{p, q\}$ is itself special.
\end{itemize}

We present two proofs of the claim.

\textbf{Proof 1.} We are interested in integers $1 \leq x < r$ satisfying
$$ x^2 + x + k \equiv 0 \pmod{r}. \qquad (1) $$

Since there are at most two residues modulo $r$ that can satisfy that quadratic congruence, there are at most two possible values of $x$. That proves (a).

Now suppose there are primes $p, q$ with $p < q < r$ and nonnegative integers $x, y$ such that
\begin{align*}
    x^2 + x + k &= pr, \\
    y^2 + y + k &= qr.
\end{align*}

From $p < q < r$ we can see that $0 \leq x < y \leq r - 1$. The numbers $x, y$ are the two solutions of (1); by Vieta's formulas, we should have $x + y \equiv -1 \pmod{r}$, so $x + y = r - 1$.

Letting $K = 4k - 1, X = 2x + 1$, and $Y = 2y + 1$, we obtain
\begin{align*}
    4pr &= X^2 + K, \\
    4qr &= Y^2 + K
\end{align*}

with $X + Y = 2r$. Multiplying the two above equations,
\begin{align*}
    16 p q r^2 &= (X^2 + K) (Y^2 + K) \\
    &= (XY - K)^2 + K(X + Y)^2 \\
    &= (XY - K)^2 + 4K r^2,
\end{align*}
$$ 4pq = \left( \frac{XY - K}{2r} \right)^2 + K. $$

In particular, the number $Z = \frac{XY - K}{2r}$ should be an integer, and so $4pq = Z^2 + K$. By parity, $Z$ is odd, and thus
$$ pq = z^2 + z + k \text{ where } z = \frac{Z - 1}{2}, $$
so $\{p, q\}$ is special.

\end{document}





\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N8.} Prove that $5^n - 3^n$ is not divisible by $2^n + 65$ for any positive integer $n$.

\textit{(Belgium)}

\textbf{Solution 1.} Let $n$ be a positive integer, and let $m = 2^n + 65$. For the sake of contradiction, suppose that $m \mid 5^n - 3^n$, so $5^n \equiv 3^n \pmod{m}$.

Notice that if $n$ is even, then $3 \mid m$, but $3 \nmid 5^n - 3^n$, contradiction. So, from now on we assume that $n$ is odd, $n = 2k + 1$. Obviously $n = 1$ is not possible, so $n \geq 3$. Notice that $m$ is coprime to 2, 3 and 5.

Let $m_1$ be the smallest positive multiple of $m$ that can be written in the form of either $|5a^2 - 3b^2|$ or $|a^2 - 15b^2|$ with some integers $a$ and $b$.

Note that $5^n - 3^n = 5(5^k)^2 - 3(3^k)^2$ is a multiple of $m$, so the set of such multiples is non-empty, and therefore $m_1$ is well-defined.

\textbf{I.} First we show that $m_1 \leq 5m$. Consider the numbers
$$ 5^{k+1} x + 3^{k+1} y, \quad 0 \leq x, y \leq \sqrt{m}. $$
There are $\lfloor \sqrt{m} \rfloor + 1 > \sqrt{m}$ choices for $x$ and $y$, so there are more than $m$ possible pairs $(x, y)$. Hence, two of these sums are congruent modulo $m$: $5^{k+1} x_1 + 3^{k+1} y_1 \equiv 5^{k+1} x_2 + 3^{k+1} y_2 \pmod{m}$. Now choose $a = x_1 - x_2$ and $b = y_1 - y_2$; at least one of $a, b$ is nonzero, and
$$ 5^{k+1} a + 3^{k+1} b \equiv 0 \pmod{m}, \quad |a|, |b| \leq \sqrt{m}. $$
From
$$ 0 \equiv (5^{k+1} a)^2 - (3^{k+1} b)^2 = 5 \cdot 3^n a^2 - 3 \cdot 5^n b^2 = 5 \cdot 3^n a^2 - 3^{n+1} b^2 = 3^n (5a^2 - 3b^2) \pmod{m} $$
we can see that $|5a^2 - 3b^2|$ is a multiple of $m$. Since at least one of $a$ and $b$ is nonzero, $5a^2 \neq 3b^2$. Hence, by the choice of $a, b$, we have $0 < |5a^2 - 3b^2| \leq \max(5a^2, 3b^2) \leq 5m$. That shows that $m_1 \leq 5m$.

\textbf{II.} Next, we show that $m_1$ cannot be divisible by 2, 3 and 5. Since $m_1$ equals either $|5a^2 - 3b^2|$ or $|a^2 - 15b^2|$ with some integers $a, b$, we have six cases to check. In all six cases, we will get a contradiction by presenting another multiple of $m$, smaller than $m_1$.

\begin{itemize}
    \item If $5 \mid m_1$ and $m_1 = |5a^2 - 3b^2|$, then $5 \mid b$ and $|a^2 - 15 (\frac{b}{5})^2| = \frac{m_1}{5} < m_1$.
    \item If $5 \mid m_1$ and $m_1 = |a^2 - 15b^2|$, then $5 \mid a$ and $|5(\frac{a}{5})^2 - 3b^2| = \frac{m_1}{5} < m_1$.
    \item If $3 \mid m_1$ and $m_1 = |5a^2 - 3b^2|$, then $3 \mid a$ and $|b^2 - 15 (\frac{a}{3})^2| = \frac{m_1}{3} < m_1$.
    \item If $3 \mid m_1$ and $m_1 = |a^2 - 15b^2|$, then $3 \mid a$ and $|5b^2 - 3 (\frac{a}{3})^2| = \frac{m_1}{3} < m_1$.
    \item If $2 \mid m_1$ and $m_1 = |5a^2 - 3b^2|$, then $|5 (\frac{a-b}{2})^2 - 3(\frac{a+b}{2})^2| = \frac{m_1}{2} < m_1$.
    \item If $2 \mid m_1$ and $m_1 = |a^2 - 15b^2|$, then $|5 (\frac{a-3b}{2})^2 - 3(\frac{a+5b}{2})^2| = \frac{m_1}{2} < m_1$.
\end{itemize}

(The last two expressions can be obtained from $(\sqrt{5a} + \sqrt{3b})(\sqrt{5a} - \sqrt{3b}) = (5a - 3b) + \sqrt{15(b - a)}$ and $(a + \sqrt{15}b)(\sqrt{5} - \sqrt{3}) = \sqrt{5}(a - 3b) + \sqrt{3(5b - a)}$.)

In all six cases, we found that either $\frac{m_1}{3}$ or $\frac{m_1}{5}$ is of the form $|5x^2 - 3y^2|$ or $|x^2 - 15y^2|$. Since $m$ is coprime to 2, 3 and 5, the presented number is a multiple of $m$, but this contradicts the minimality of $m_1$.

\textbf{III.} The last remaining case is $m_1 = m$, so either $m = |5a^2 - 3b^2|$ or $m = |a^2 - 15b^2|$. We will get a contradiction by considering the two sides modulo 3, 4 and 5.
\begin{itemize}
    \item $2^n + 65 = 5a^2 - 3b^2$ is not possible, because $2^n + 65 \equiv 1 \pmod{3}$, but $5a^2 - 3b^2 \not\equiv 1 \pmod{3}$.
    \item $2^n + 65 = 3b^2 - 5a^2$ is not possible, because $2^n + 65 \equiv 1 \pmod{4}$, but $3b^2 - 5a^2 \not\equiv 1 \pmod{4}$.
    \item $2^n + 65 = a^2 - 15b^2$ is not possible, because $2^n + 65 \equiv \pm 2 \pmod{5}$, but $a^2 - 15b^2 \not\equiv \pm 2 \pmod{5}$.
    \item $2^n + 65 = 15b^2 - a^2$ is not possible, because $2^n + 65 \equiv 1 \pmod{4}$, but $15b^2 - a^2 \not\equiv 1 \pmod{4}$.
\end{itemize}

We found a contradiction in all cases, that completes the solution.

\end{document}









"""