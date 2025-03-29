def NumberTheory():
    return r"""

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N1.} Find all pairs $(m, n)$ of positive integers satisfying the equation
$$(2^0 - 1)(2^1 - 1)(2^2 - 1) \dots (2^{n-1} - 1) = m!$$

\textbf{Answer:} The only such pairs are (1, 1) and (3, 2).


\textbf{Solution 1.} We will get an upper bound on $n$ from the speed at which $L_n = (2^0 - 1)(2^1 - 1)(2^2 - 1) \dots (2^{n-1} - 1)$ grows.

From
$$L_n = (2^0 - 1)(2^1 - 1)\dots (2^{n-1} - 1) = 2^{1+2+ \dots + (n-1)} - 2^{0+1+\dots + (n-2)} - \dots - 1$$
we read
$$L_n = 2^{\frac{n(n-1)}{2}} - \left( 2^{\frac{(n-1)(n-2)}{2}} + \dots + 1 \right)$$
On the other hand, $v_2(m!)$ is expressed by the Legendre formula as
$$v_2(m!) = \sum_{i=1}^\infty \left\lfloor \frac{m}{2^i} \right\rfloor.$$

Thus, $L_n = m!$ implies the inequality
$$n\frac{n-1}{2} < m.$$

In order to obtain an opposite estimate, observe that
$$(2^0 - 1)(2^1 - 1)\dots (2^{n-1} - 1) < (2^0 + 1)(2^1 + 1)\dots (2^{n-1} + 1) = (2^{n-1} + 1) < 2^n.$$
We claim that for $n \ge 6$:
$$2^{\frac{n(n-1)}{2}} < \frac{n(n-1)}{2}!$$

For $n = 6$, the estimate (3) is true because $2^{15} < 6 \cdot 5 \cdot 4 = 120$.  $2^{15} = 32768$ and $120! \approx 6.4 \times 10^{22}$.
For $n > 7$, we prove (3) by the following inequalities:
$$ \frac{n(n-1)}{2} \ge 2^{n-1} \cdot 2^{n-2} \dots 2^{15}.$$

Putting together (2) and (3), for $n \ge 6$ we get a contradiction, since $L_n < 2^n < \left( \frac{n(n-1)}{2} \right)! < m!$,
Hence $n \ge 6$ is not possible.

Checking manually the cases $n < 5$ we find
$L_1 = 1 = 1!$, $L_2 = 6-3 = 3$, $5 < L_4 = 168$, $L_5 = 9990$, $7! < L_4$, $20 \cdot 160 < 8!$.

So, there are two solutions: $(m, n) \in \{(1, 1), (3, 2)\}$.

\end{document}

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N2.} Find all triples $(a, b, c)$ of positive integers such that $a^3 + b^3 + c^3 = (abc)^2$.

\textbf{Answer:} The solutions are (1, 2, 3) and its permutations.

\textbf{Common remarks.} Note that the equation is symmetric. In all solutions, we will assume without loss of generality that $a \ge b \ge c$, and prove that $c = 1$ is the only solution is $(a, b, c) = (3, 2, 1)$.

\textbf{Solution 1.} We will start by proving that $c = 1$. Note that
$$3a^3 \ge a^3 + b^3 + c^3 \ge a^3,$$
so $3a^3 \ge (abc)^2 \ge a^3$, and hence $3a^3 \ge b^2c^2 \ge a^3$. Now $b^3 + c^3 = (bc^2 - a^2) \ge a^3$, and so
$$18a^3 \ge 9(b^3 + c^3) \ge 9a^2 \ge 2b^3c^3 \ge b^3c^3.$$
so $18 \ge c^3$, which yields $c = 1$.
Now, note that we must have $a \ge b$, as otherwise we would have $2b^3 + 1 = b^6$, which has no positive integer solutions. So $a^3 + b^3 - (b + 1)^3 \ge 1$
and 
$$2a^3 \ge a^3 + b^3 + 1 \ge a^3 \quad \text{and} \quad 2a \ge b^2 + a + 1.$$
Therefore, 
$$4(1 + b^3) = 4(a^3(b^2-a)) \ge 4a^4 - 6a^3.$$

Now, for each possible value of $b$ with $2 \le b \le 4$, we obtain a cubic equation for $a$ with constant coefficients. These are as follows:

$b = 2$: $a^3 - 4a^2 + 9 = 0$
$b = 3$: $a^3 - 9a^2 + 28 = 0$
$b = 4$: $a^3 - 16a^2 + 65 = 0$
The only case with an integer solution for $a$ with $b \le a$ is $b = 2$, leading to $(a, b, c) = (3, 2, 1)$.

\end{document}

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N3.} We say that a set $S$ of integers is rootifull if, for any positive integer $n$ and any $a_0, a_1, \dots, a_n \in S$, all integer roots of the polynomial $a_0 + a_1x + \dots + a_n x^n$ are also in $S$. Find all rootifull sets of integers that contain all numbers of the form $2^a - 2^b$ for positive integers $a$ and $b$.

\textbf{Answer:} The set $\mathbb{Z}$ of all integers is the only such rootifull set.

\textbf{Solution 1.} The set $\mathbb{Z}$ of all integers is clearly rootifull. We shall prove that any rootifull set $S$ containing all the numbers of the form $2^a - 2^b$ for $a, b \in \mathbb{Z}_{\ge 0}$ must be all of $\mathbb{Z}$.
First, note that $0 = 2^1 - 2^1 \in S$. Now $-1 \in S$, since it is a root of $2x + 2$, and $1 \in S$, since it is a root of $2x^2 - x - 1$. Also, if $n \in S$, then $-n \in S$, since it is a root of $x + n$, so it suffices to prove that all positive integers must be in $S$.

Now, we claim that any positive integer $n$ has a multiple in $S$. Indeed, suppose that $n = 2^{a_1} t$ for $\alpha \in \mathbb{Z}_{\ge 0}$ and $t$ odd. Then $t | 2^{a_1}t-1$, so $n | 2^{a_1+t} - 2^{a_1+1}$. Moreover, $2^{a_1 + t} - 2^{a_1+1} \in S$.
We will now prove by induction that all positive integers are in $S$. Suppose that $0, 1, \dots, n-1 \in S$; furthermore, let $N$ be a multiple of $n$ in $S$. Consider the base-$n$ expansion of $N$, say $N = a_k n^k + a_{k-1} n^{k-1} + \dots + a_1 n + a_0$. Since $0 \le a_i < n$ for each $a_i$, we have that all the $a_i$ are in $S$. Furthermore, $a_k n^k + a_{k-1} n^{k-1} + \dots + a_1 n + a_0 = 0$ since $N$ is a multiple of $n$. Therefore, $a_k n^k + a_{k-1} n^{k-1} + \dots + a_1 n + a_0 = 0$ so $n$ is a root of a polynomial with coefficients in $S$. This tells us that $n \in S$, completing the induction.


\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{N4.} Let $\mathbb{Z}_{>0}$ be the set of positive integers. A positive integer constant $C$ is given. Find all functions $f: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ such that, for all positive integers $a$ and $b$ satisfying $a + b > C$,
\[
a + f(b) \mid a^2 + b f(a). \tag{*}
\]

\medskip
\noindent \textit{(Croatia)}

\medskip
\noindent \textbf{Answer:} The functions satisfying $(*)$ are exactly the functions $f(a) = ka$ for some constant $k \in \mathbb{Z}_{>0}$ (irrespective of the value of $C$).

\medskip
\noindent \textbf{Common remarks.} It is easy to verify that the functions $f(a) = ka$ satisfy $(*)$. Thus, in the proofs below, we will only focus on the converse implication: that condition $(*)$ implies that $f = ka$.

\medskip
A common minor part of these solutions is the derivation of some relatively easy bounds on the function $f$. An upper bound is easily obtained by setting $a = 1$ in $(*)$, giving the inequality
\[
f(b) \le b \cdot f(1)
\]
for all sufficiently large $b$. The corresponding lower bound is only marginally more difficult to obtain: substituting $b = 1$ in the original equation shows that
\[
a + f(1) \mid (a^2 + f(a)) - (a - f(1)) \cdot (a + f(1)) = f(1)^2 + f(a)
\]
for all sufficiently large $a$. It follows from this that one has the lower bound
\[
f(a) \ge a + f(1) \cdot (1 - f(1)),
\]
again for all sufficiently large $a$.
Each of the following proofs makes use of at least one of these bounds.

\medskip
\noindent \textbf{Solution 1.} First, we show that $b \mid f(b)^2$ for all $b$. To do this, we choose a large positive integer $n$ so that $nb - f(b) \ge C$. Setting $a = nb - f(b)$ in $(*)$ then shows that
\[
nb \mid (nb - f(b))^2 + bf(nb - f(b))
\]
so that $b \mid f(b)^2$ as claimed.

\medskip
Now in particular we have that $p \mid f(p)^2$ for every prime $p$. If we write $f(p) = k(p) \cdot p$, then the bound $f(p) \le f(1) \cdot p$ (valid for $p$ sufficiently large) shows that some value $k$ of $k(p)$ must be attained for infinitely many $p$. We will show that $f(a) = ka$ for all positive integers $a$. To do this, we substitute $b = p$ in $(*)$, where $p$ is any sufficiently large prime for which $k(p) = k$, obtaining
\[
a + kp \mid (a^2 + p f(a)) - a(a + kp) = p f(a) - pka.
\]
For suitably large $p$ we have $\text{gcd}(a + kp, p) = 1$, and hence we have
\[
a + kp \mid f(a) - ka.
\]
But the only way this can hold for arbitrarily large $p$ is if $f(a) - ka = 0$. This concludes the proof.

\medskip
\noindent \textbf{Comment.} There are other ways to obtain the divisibility $p \mid f(p)$ for primes $p$, which is all that is needed in this proof. For instance, if $f(p)$ were not divisible by $p$ then the arithmetic progression $p^2 + bf(p)$ would attain prime values for infinitely many $b$ by Dirichlet's Theorem: hence, for these pairs $p, b$, we would have $p + f(b) = p^2 + bf(p)$. Substituting $a \leftrightarrow b$ and $b \leftrightarrow p$ in $(*)$ then shows that $(f(p)^2 - p^2)(p - 1)$ is divisible by $b + f(p)$ and hence vanishes, which is impossible since $p \nmid f(p)$ by assumption.

\end{document}

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N5.} Let $a$ be a positive integer. We say that a positive integer $b$ is a $a$-good if $(an-1) \dots (an-b+1) = b! \pmod{an+1}$.  Suppose $b$ is a positive integer such that $b$ is $a$-good, but $b+2$ is not a-good. Prove that $b+1$ is prime. (Netherlands)

\textbf{Solution 1.} For a prime $p$ and a nonzero integer, we write $v_p(n)$ for the $p$-adic valuation of $n$. The first show that $b$ is a-good if and only if $b$ is even, and $p|a$ for all primes $p < b$.

To start with, the condition that $an(an-1) \dots (an-b+1) = b! \pmod{an+1}$ can be rewritten as saying that
$$an(an-1) \dots (an-b+1) = b! \pmod{an+1}.$$ (1)


Suppose, on the one hand, there is a prime $p \le b$ with $p | a$. Take $t = v_p(b!)$. Then there exist positive integers $c$ such that $ac = 1 \pmod{p^t}$. If we take $n = (p-1)c$, then $an = a(p-1)c = p-1 \pmod{p^t}$.
And $an \ge b$. Since $p < b$, one of the terms of the numerator of $an(an-1)\dots (an-b+1)$ is at least $an+1$, but that of the denominator by $p$ is exactly $t$. This means that $p | (an), so \phi(an-1) \dots (an-b+1) - b! = 1$. As $p | an+1$, so $b$ is not a-good.

On the other hand, if for all primes $p < b$ we have $p | a$, then every factor of $b!$ is coprime to $an+1$, and hence $b!$ is also invertible modulo $an+1$. Then equation (1) reduces to
$$an(an-1) \dots (an-b+1) = b! \pmod{an+1}.$$
However, we can rewrite the left-hand side as follows:
$$an(an-1)\dots (an-b+1) = (-1)^{b}b! \pmod{an+1}.$$

Provided that $an > 1$, if $b$ is even we deduce $(-1)^b b! = b!$ as needed. On the other hand, if $b$ is odd, and we take $an+1 > 2b!$, then we will not have $(-1)^b b! = b!$, so $b$ is not a-good. This completes the claim.

To conclude from here, suppose that $b$ is a $a$-good, but $b+2$ is not. Then $b$ is even, and $p | a$ for all primes $p \le b$. We cannot have $q \le b$, but $b+2$ is not a-good. Then $b+1$ is even, so we have $q = b+1$. In other words, $b+1$ is prime.


\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{N6.} Let $H = \{\lfloor i\sqrt{2} \rfloor : i \in \mathbb{Z}_{>0} \} = \{1, 2, 4, 5, 7, \dots \}$, and let $n$ be a positive integer. Prove that there exists a constant $C$ such that, if $A \subseteq \{1, 2, \dots, n\}$ satisfies $|A| \ge C\sqrt{n}$, then there exist $a, b \in A$ such that $a - b \in H$. (Here $\mathbb{Z}_{>0}$ is the set of positive integers, and $\lfloor z \rfloor$ denotes the greatest integer less than or equal to $z$.)

\medskip
\noindent \textit{(Brazil)}

\medskip
\noindent \textbf{Common remarks.} In all solutions, we will assume that $A$ is a set such that $\{a - b : a, b \in A \}$ is disjoint from $H$, and prove that $|A| < C\sqrt{n}$.

\medskip
\noindent \textbf{Solution 1.} First, observe that if $n$ is a positive integer, then $n \in H$ exactly when
\[
\left\{ \frac{n}{\sqrt{2}} \right\} > 1 - \frac{1}{\sqrt{2}}. \tag{1}
\]

\medskip
To see why, observe that $n \in H$ if and only if $0 < i\sqrt{2} - n < 1$ for some $i \in \mathbb{Z}_{>0}$. In other words, $0 < i - n/\sqrt{2} < 1/\sqrt{2}$, which is equivalent to (1).

\medskip
Now, write $A = \{a_1 < a_2 < \cdots < a_k \}$, where $k = |A|$. Observe that the set of differences is not altered by shifting $A$, so we may assume that $A \subseteq \{0, 1, \dots, n-1\}$ with $a_1 = 0$.

\medskip
From (1), we learn that $\{ a_i / \sqrt{2} \} < 1 - 1/\sqrt{2}$ for each $i \ge 1$ since $a_i - a_1 \notin H$. Furthermore, we must have $\{ a_i / \sqrt{2} \} < \{ a_j / \sqrt{2} \}$ whenever $i < j$; otherwise, we would have
\[
-\left( 1 - \frac{1}{\sqrt{2}} \right) < \left\{ \frac{a_j}{\sqrt{2}} \right\} - \left\{ \frac{a_i}{\sqrt{2}} \right\} < 0.
\]
Since $\{ (a_j - a_i) / \sqrt{2} \} = \{ a_j / \sqrt{2} \} - \{ a_i / \sqrt{2} \} + 1$, this implies that $\{ (a_j - a_i) / \sqrt{2} \} > 1/\sqrt{2} > 1 - 1/\sqrt{2}$, contradicting (1).

\medskip
Now, we have a sequence $0 = a_1 < a_2 < \cdots < a_k < n$, with
\[
0 = \left\{ \frac{a_1}{\sqrt{2}} \right\} < \left\{ \frac{a_2}{\sqrt{2}} \right\} < \cdots < \left\{ \frac{a_k}{\sqrt{2}} \right\} < 1 - \frac{1}{\sqrt{2}}.
\]
We use the following fact: for any $d \in \mathbb{Z}$, we have
\[
\left\{ \frac{d}{\sqrt{2}} \right\} \ge \frac{d}{2\sqrt{2}}. \tag{2}
\]

\medskip
To see why this is the case, let $h = \lfloor d/\sqrt{2} \rfloor$, so $\{ d/\sqrt{2} \} = d/\sqrt{2} - h$. Then
\[
\left\{ \frac{d}{\sqrt{2}} \right\} \left( \frac{d}{\sqrt{2}} + h \right) = \frac{d^2 - 2h^2}{2} \ge \frac{1}{2},
\]
since the numerator is a positive integer. Because $d/\sqrt{2} + h < 2d/\sqrt{2}$, inequality (2) follows.

\medskip
Let $d_i = a_{i+1} - a_i$, for $1 \le i < k$. Then $\{ a_{i+1} / \sqrt{2} \} - \{ a_i / \sqrt{2} \} = \{ d_i / \sqrt{2} \}$. Then
\begin{align*}
1 - \frac{1}{\sqrt{2}} &> \sum_{i=1}^{k-1} \left( \left\{ \frac{a_{i+1}}{\sqrt{2}} \right\} - \left\{ \frac{a_i}{\sqrt{2}} \right\} \right) = \sum_{i=1}^{k-1} \left\{ \frac{d_i}{\sqrt{2}} \right\} > \sum_{i=1}^{k-1} \frac{d_i}{2\sqrt{2}} \\
&\ge \frac{1}{2\sqrt{2}} \sum_{i=1}^{k-1} d_i \ge \frac{(k-1)^2}{2\sqrt{2} \sum_i d_i} > \frac{(k-1)^2}{2\sqrt{2}} \cdot \frac{1}{n}. \tag{3}
\end{align*}
Here, the first inequality holds because $\{ a_k / \sqrt{2} \} < 1 - 1/\sqrt{2}$, the second follows from (2), the third follows from an easy application of the AM-HM inequality (or Cauchy-Schwarz), and the fourth follows from the fact that $\sum_i d_i = a_k < n$.
Rearranging this, we obtain
\[
\sqrt{2\sqrt{2} - 2} \cdot \sqrt{n} > k - 1,
\]
which provides the required bound on $k$.

\end{document}

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N7.} Prove that there is a constant $c > 0$ and infinitely many positive integers $n$ with the following property: there are infinitely many positive integers that cannot be expressed as the sum of fewer than $cn \log(n)$ pairwise coprime $n^{th}$ powers. (Canada)

\textbf{Solution 1.} Suppose, for an integer $n$, that we can find another integer $N$ satisfying the following property:
$n$ is divisible by $p^r$ for every prime power $p^r$ exactly dividing $N$.

This property ensures that all $n^{th}$ powers are congruent to 0 or 1 modulo each such prime power $p^r$, since at most one of the $m$ powers is divisible by $p$. Thus, if $k$ denotes the number of distinct prime factors of $N$, we find by the Chinese Remainder Theorem at most $2^m$ residue classes modulo $N$ which are sums of at most $m$ pairwise coprime $n^{th}$ powers. In particular, if $N > 2^m n$, then there are infinitely many positive integers not expressible as a sum of at most $m$ pairwise coprime $n^{th}$ powers. It thus suffices to prove that there are arbitrarily large pairs $(n, N)$ of integers satisfying $(*)$.

We construct such pairs as follows. Fix a positive integer $t$ and choose (distinct) prime numbers $p = 2^{2^t} + 1$ and $q = 2^{2^{t+1}} + 1$. We set $N = pq$. It is well-known that $p^r | p-1$ and $q^r | q-1$, hence
$$n = \frac{(p-1)(q-1)}{2^{t+1}}.$$
Estimating the size of $N$ and $n$ is now straightforward. We have
$$\log(n) < 2^{t+1} - 2^t - t + 2^{t+1} < \frac{N}{n}.$$
which rearranges to
$$N > 2^{t+1} \cdot 2^{t}\log(n)$$
and so we are done if we choose $c < \frac{8}{s\log(2)} = 0.18$.


\end{document}

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{N8.} Let $a$ and $b$ be two positive integers. Prove that the integer $\frac{a^2 + 4a^2}{b}$ is not a square. (Here $[z]$ denotes the least integer greater than or equal to $z$). (Russia)

\textbf{Solution 1.} Arguing indirectly, assume that
$$\left\lfloor \frac{a^2 + 4a^2}{b} \right\rfloor = (a+k)^2, \quad \text{or} \quad \left\lfloor \frac{(2a)^2}{b} \right\rfloor = (2a+k)^2.$$
Clearly, $k \ge 1$. In other words, the equation
$$\left\lfloor \frac{c^2}{b} \right\rfloor = (c+k)^2$$ (1)
has a positive integer solution $(c, k)$, with an even value of $c$, without regard to the parity of $c$. From
$$\frac{c^2}{b} - \left\lfloor \frac{c^2}{b} \right\rfloor = 1 = c k + k^2 - 1 > ck.$$
and 
$$(c - k)(c + k) < b \le \frac{c^2}{b} < (c + k)(c + k + 1)$$
it can be seen that $c > b > c - k$, so $c = kb + r$ with some $0 < r < k$.
By substituting this in (1) we get
$$\left\lfloor \frac{(kb+r)^2}{b} \right\rfloor = k^2 + 2kr + \left\lfloor \frac{r^2}{b} \right\rfloor = k^2 + 2kr + \left[ \frac{r^2}{b} \right] = (k+b+r)^2.$$ (2)
So
$$k = (kb + r + k)(k + b + r - r) = k(b + r + k) = k b + 2k r + k^2 - r.$$
Notice that relation (2) provides another positive integer solution of (1), namely $c' = c - k$, with $c' > 0$ and $0 < k < k$. That contradicts the minimality of $k$, and hence finishes the solution.

\end{document}


"""