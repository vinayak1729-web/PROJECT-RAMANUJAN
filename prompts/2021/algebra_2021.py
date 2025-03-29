def algebra_2021():
    return r"""


\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A1.} Let $n$ be an integer, and let $A$ be a subset of $\{0, 1, 2, 3, \dots, 5^n\}$ consisting of $4n + 2$ numbers. Prove that there exist $a, b, c \in A$ such that $a < b < c$ and $c + 2a > 3b$.

\textbf{Solution 1.} (By contradiction) Suppose that there exist $4n + 2$ non-negative integers $x_0 < x_1 < \dots < x_{4n+1}$ that violate the problem statement. Then in particular $x_{4n+1} + 2x_i \leq 3x_{i+1}$ for all $i = 0, \dots, 4n-1$, which gives
$$ x_{4n+1} - x_i \geq \frac{3}{2} (x_{4n+1} - x_{i+1}). $$

By a trivial induction we then get
$$ x_{4n+1} - x_i \geq \left( \frac{3}{2} \right)^{4n-i} (x_{4n+1} - x_{4n}), $$
which for $i = 0$ yields the contradiction
$$ x_{4n+1} - x_0 \geq \left( \frac{3}{2} \right)^{4n} (x_{4n+1} - x_{4n}) = \left( \frac{81}{16} \right)^n (x_{4n+1} - x_{4n}) > 5^n \cdot 1. $$

\textbf{Solution 2.} Denote the maximum element of $A$ by $c$. For $k = 0, \dots, 4n-1$ let
$$ A_k = \left\{ x \in A : \left( 1 - \left( \frac{2}{3} \right)^k \right) c \leq x < \left( 1 - \left( \frac{2}{3} \right)^{k+1} \right) c \right\}. $$

Note that
$$ \left( 1 - \left( \frac{2}{3} \right)^{4n} \right) c = c - \left( \frac{16}{81} \right)^n c > c - \left( \frac{1}{5} \right)^n c \geq c - 1, $$
which shows that the sets $A_0, A_1, \dots, A_{4n-1}$ form a partition of $A \setminus \{c\}$. Since $A \setminus \{c\}$ has $4n + 1$ elements, by the pigeonhole principle some set $A_k$ does contain at least two elements of $A \setminus \{c\}$. Denote these two elements $a$ and $b$ and assume $a < b$, so that $a < b < c$. Then
$$ c + 2a \geq c + 2 \left( 1 - \left( \frac{2}{3} \right)^k \right) c = \left( 3 - 2 \left( \frac{2}{3} \right)^k \right) c = 3 \left( 1 - \frac{2}{3} \left( \frac{2}{3} \right)^k \right) c > 3b, $$
as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A2.} For every integer $n \geq 1$ consider the $n \times n$ table with entry $\left\lfloor \frac{ij}{n+1} \right\rfloor$ at the intersection of row $i$ and column $j$, for every $i = 1, \dots, n$ and $j = 1, \dots, n$. Determine all integers $n \geq 1$ for which the sum of the $n^2$ entries in the table is equal to $\frac{n^2(n-1)}{4}$.

\textbf{Answer:} All integers $n$ for which $n + 1$ is a prime.

\textbf{Solution 1.} First, observe that every pair $x, y$ of real numbers for which the sum $x + y$ is integer satisfies
$$ \lfloor x \rfloor + \lfloor y \rfloor \geq x + y - 1. \qquad (1) $$

The inequality is strict if $x$ and $y$ are integers, and it holds with equality otherwise. We estimate the sum $S$ as follows.
\begin{align*}
    2S &- \sum_{i, j \leq n} \left( \left\lfloor \frac{ij}{n+1} \right\rfloor + \left\lfloor \frac{(n+1-i)j}{n+1} \right\rfloor \right) - \sum_{i \leq n} \left( \left\lfloor \frac{ij}{n+1} \right\rfloor + \left\lfloor \frac{i(n+1-j)}{n+1} \right\rfloor \right) \\
    &\geq \sum_{i \leq n} (j - 1) - \frac{(n-1)n^2}{2}
\end{align*}

The inequality in the last line follows from (1) by setting $x = ij/(n+1)$ and $y = (n+1-i)j/(n+1)$, so that $x + y - j$ is integral.

Now $S = \frac{n^2(n-1)}{4}$ if and only if the inequality in the last line holds with equality, which means that none of the values $ij/(n+1)$ with $1 < i, j < n$ may be integral.

Hence, if $n+1$ is composite with factorisation $n+1 = ab$ for $2 \leq a, b < n$, one gets a strict inequality for $i = a$ and $j = b$. If $n+1$ is a prime, then $ij/(n+1)$ is never integral and $S = \frac{n^2(n-1)}{4}$.



\end{document}







\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A3.} Given a positive integer $n$, find the smallest value of $\left\lfloor \frac{a_1}{1} \right\rfloor + \left\lfloor \frac{a_2}{2} \right\rfloor + \dots + \left\lfloor \frac{a_n}{n} \right\rfloor$ over all permutations $(a_1, a_2, \dots, a_n)$ of $\{1, 2, \dots, n\}$.

\textbf{Answer:} The minimum of such sums is $\lfloor \log_2 n \rfloor + 1$; so if $2^k \leq n < 2^{k+1}$, the minimum is $k+1$.

\textbf{Solution 1.} Suppose that $2^k \leq n < 2^{k+1}$ with some nonnegative integer $k$. First we show a permutation $(a_1, a_2, \dots, a_n)$ such that $\left\lfloor \frac{a_1}{1} \right\rfloor + \left\lfloor \frac{a_2}{2} \right\rfloor + \dots + \left\lfloor \frac{a_n}{n} \right\rfloor = k + 1$; then we will prove that $\left\lfloor \frac{a_1}{1} \right\rfloor + \left\lfloor \frac{a_2}{2} \right\rfloor + \dots + \left\lfloor \frac{a_n}{n} \right\rfloor \geq k + 1$ for every permutation. Hence, the minimal possible value will be $k+1$.

\textbf{I.} Consider the permutation
\begin{align*}
    (a_1) &= (1), \quad (a_2, a_3) = (3, 2), \quad (a_4, a_5, a_6, a_7) = (7, 4, 5, 6), \dots \\
    (a_{2^{k-1}}, \dots, a_{2^{k-1} - 1}) &= (2^k - 1, 2^{k-1}, 2^{k-1} + 1, \dots, 2^k - 2), \\
    (a_{2^{k}}, \dots, a_{n}) &= (n, 2^k, 2^k + 1, \dots, n - 1)
\end{align*}

This permutation consists of $k + 1$ cycles. In every cycle $(a_p, \dots, a_q) = (q, p, p+1, \dots, q - 1)$ we have $q < 2p$, so
$$ \sum_{i=p}^{q} \left\lfloor \frac{a_i}{i} \right\rfloor - \left\lfloor \frac{q}{p} \right\rfloor + \sum_{i=p+1}^{q} \left\lfloor \frac{i-1}{i} \right\rfloor - 1; $$

The total sum over all cycles is precisely $k + 1$.

\textbf{II.} In order to establish the lower bound, we prove a more general statement.

\textbf{Claim.} If $b_1, \dots, b_{2^k}$ are distinct positive integers then
$$ \sum_{i=1}^{2^k} \left\lfloor \frac{b_i}{i} \right\rfloor \geq k + 1. $$

From the Claim it follows immediately that $\sum_{i=1}^{n} \left\lfloor \frac{a_i}{i} \right\rfloor \geq \sum_{i=1}^{2^k} \left\lfloor \frac{a_i}{i} \right\rfloor \geq k + 1$.

\textbf{Proof of the Claim.} Apply induction on $k$. For $k - 1$ the claim is trivial, $\left\lfloor \frac{1}{1} \right\rfloor \geq 1$. Suppose the Claim holds true for some positive integer $k$, and consider $k + 1$.

If there exists an index $j$ such that $2^k < j \leq 2^{k+1}$ and $b_j \geq j$ then
$$ \sum_{i=1}^{2^{k+1}} \left\lfloor \frac{b_i}{i} \right\rfloor \geq \sum_{i=1}^{2^{k}} \left\lfloor \frac{b_i}{i} \right\rfloor + \left\lfloor \frac{b_j}{j} \right\rfloor \geq (k + 1) + 1 $$
by the induction hypothesis, so the Claim is satisfied.

Otherwise we have $b_j < j \leq 2^{k+1}$ for every $2^k < j \leq 2^{k+1}$. Among the $2^{k+1}$ distinct numbers $b_1, \dots, b_{2^{k+1}}$ there is some $b_m$ which is at least $2^{k+1}$; that number must be among $b_1, \dots, b_{2^k}$. Hence, $1 \leq m \leq 2^k$ and $b_m \geq 2^{k+1}$.

We will apply the induction hypothesis to the numbers
$$ c_1 - b_1, \dots, c_{m-1} - b_{m-1}, \quad c_m - b_{2^k + 1}, \dots, c_{2^k} - b_{2^{k}}, $$
so take the first $2^k$ numbers but replace $b_m$ with $b_{2^k + 1}$. Notice that
$$ \left\lfloor \frac{b_m}{m} \right\rfloor - \left\lfloor \frac{2^{k+1}}{m} \right\rfloor \geq \left\lfloor \frac{2^{k+2}}{m} \right\rfloor > \left\lfloor \frac{b_{2^k + 1} + m}{m} \right\rfloor - \left\lfloor \frac{c_m}{m} \right\rfloor + 1. $$

For the other indices $i$ with $1 \leq i \leq 2^k, i \neq m$ we have $\left\lfloor \frac{b_i}{i} \right\rfloor = \left\lfloor \frac{c_i}{i} \right\rfloor$, so
$$ \sum_{i=1}^{2^{k+1}} \left\lfloor \frac{b_i}{i} \right\rfloor - \sum_{i=1}^{2^{k}} \left\lfloor \frac{b_i}{i} \right\rfloor \geq \sum_{i=1}^{2^{k}} \left\lfloor \frac{c_i}{i} \right\rfloor + 1 > (k + 1) + 1. $$

That proves the Claim and hence completes the solution.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A4.} Show that for all real numbers $x_1, \dots, x_n$ the following inequality holds:
$$ \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{|x_i - x_j|} \leq \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{|x_i + x_j|}. $$

\textbf{Solution 1.} If we add $t$ to all the variables then the left-hand side remains constant and the right-hand side becomes
$$ H(t) := \sum_{i=1}^{n} \sum_{j=1}^{n} \sqrt{|x_i + x_j + 2t|}. $$

Let $T$ be large enough such that both $H(-T)$ and $H(T)$ are larger than the value $L$ of the left-hand side of the inequality we want to prove. Not necessarily distinct points $p_{i,j} := -(x_i + x_j)/2$ together with $T$ and $-T$ split the real line into segments and two rays such that on each of these segments and rays the function $H(t)$ is concave since $f(t) := \sqrt{|\ell + 2t|}$ is concave on both intervals $(-\infty, -\ell/2]$ and $[-\ell/2, +\infty)$. Let $[a, b]$ be the segment containing zero. Then concavity implies $H(0) \geq \min\{H(a), H(b)\}$ and, since $H(\pm T) > L$, it suffices to prove the inequalities $H(-(x_i + x_j)/2) \geq L$, that is to prove the original inequality in the case when all numbers are shifted in such a way that two variables $x_i$ and $x_j$ add up to zero. In the following we denote the shifted variables still by $x_i$.

If $i = j$, i.e. $x_i = 0$ for some index $i$, then we can remove $x_i$ which will decrease both sides by $2 \sum_{k} \sqrt{|x_k|}$. Similarly, if $x_i + x_j = 0$ for distinct $i$ and $j$ we can remove both $x_i$ and $x_j$ which decreases both sides by
$$ 2 \sqrt{2|x_i|} + 2 \cdot \sum_{k \neq i, j} \left( \sqrt{|x_k + x_i|} + \sqrt{|x_k + x_j|} \right). $$

In either case we reduced our inequality to the case of smaller $n$. It remains to note that for $n = 0$ and $n = 1$ the inequality is trivial.

\end{document}





\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A5.} Let $n \geq 2$ be an integer, and let $a_1, a_2, \dots, a_n$ be positive real numbers such that $a_1 + a_2 + \dots + a_n = 1$. Prove that
$$ \sum_{k=1}^{n} \frac{a_k}{1 - a_k} (a_1 + a_2 + \dots + a_{k-1})^2 < \frac{1}{3}. $$

\textbf{Solution 1.} For all $k \leq n$, let
$$ s_k = a_1 + a_2 + \dots + a_k \quad \text{and} \quad b_k = \frac{a_k s_{k-1}^2}{1 - a_k}, $$
with the convention that $s_0 = 0$. Note that $b_k$ is exactly a summand in the sum we need to estimate. We shall prove the inequality
$$ b_k < \frac{s_k^3 - s_{k-1}^3}{3}. \qquad (1) $$

Indeed, it suffices to check that
\begin{align*}
    (1) &\iff 0 < (1 - a_k) \left( (s_{k-1} + a_k)^3 - s_{k-1}^3 \right) - 3a_k s_{k-1}^2 \\
    &\iff 0 < (1 - a_k) \left( 3s_{k-1}^2 a_k + 3s_{k-1} a_k^2 + a_k^3 \right) - 3a_k s_{k-1}^2 \\
    &\iff 0 < -3a_k s_{k-1}^2 a_k + 3(1 - a_k) s_{k-1} a_k^2 + (1 - a_k) a_k^3 \\
    &\iff 0 < 3(1 - a_k - s_{k-1}) s_{k-1} a_k + (1 - a_k) a_k^2
\end{align*}
which holds since $a_k + s_{k-1} = s_k \leq 1$ and $a_k \in (0, 1)$.

Thus, adding inequalities (1) for $k = 1, \dots, n$, we conclude that
$$ b_1 + b_2 + \dots + b_n < \frac{s_n^3 - s_0^3}{3} = \frac{1}{3}, $$
as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A6.} Let $A$ be a finite set of (not necessarily positive) integers, and let $m \geq 2$ be an integer. Assume that there exist non-empty subsets $B_1, B_2, B_3, \dots, B_m$ of $A$ whose elements add up to the sums $m^1, m^2, m^3, \dots, m^m$, respectively. Prove that $A$ contains at least $m/2$ elements.

\textbf{Solution.} Let $A = \{a_1, \dots, a_k\}$. Assume that, on the contrary, $k = |A| < m/2$. Let
$$ s_i := \sum_{j : a_j \in B_i} a_j $$
be the sum of elements of $B_i$. We are given that $s_i = m^i$ for $i = 1, \dots, m$.

Now consider all $m^m$ expressions of the form
$$ f(c_1, \dots, c_m) := c_1 s_1 + c_2 s_2 + \dots + c_m s_m, \quad c_i \in \{0, 1, \dots, m-1\} \text{ for all } i = 1, 2, \dots, m. $$

Note that every number $f(c_1, \dots, c_m)$ has the form
$$ \alpha_1 a_1 + \dots + \alpha_k a_k, \quad \alpha_i \in \{0, 1, \dots, m(m-1)\}. $$

Hence, there are at most $[m(m-1) + 1]^k < m^{2k} < m^{m}$ distinct values of our expressions; therefore, at least two of them coincide.

Since $s_i = m^i$, this contradicts the uniqueness of representation of positive integers in the base-$m$ system.

\end{document}








\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A7.} Let $n \geq 1$ be an integer, and let $x_0, x_1, \dots, x_{n+1}$ be $n + 2$ non-negative real numbers that satisfy $x_i x_{i+1} - x_{i-1}^2 \geq 1$ for all $i = 1, 2, \dots, n$. Show that
$$ x_0 + x_1 + \dots + x_n + x_{n+1} > \left( \frac{2n}{3} \right)^{3/2}. $$

\textbf{Solution 1.}

\textbf{Lemma 1.1.} If $a, b, c$ are non-negative numbers such that $ab - c^2 \geq 1$, then
$$ (a + 2b)^2 \geq (b + 2c)^2 + 6. $$

\textbf{Proof.} $(a + 2b)^2 - (b + 2c)^2 - (a - b)^2 + 2(b - c)^2 + 6(ab - c^2) \geq 6$. $\square$

\textbf{Lemma 1.2.} $\sqrt{1} + \dots + \sqrt{n} > \frac{2}{3} n^{3/2}$.

\textbf{Proof.} Bernoulli's inequality $(1 + t)^{3/2} > 1 + \frac{3}{2} t$ for $0 > t \geq -1$ (or, alternatively, a straightforward check) gives
$$ (k - 1)^{3/2} - k^{3/2} \left( 1 - \frac{1}{k} \right)^{3/2} > k^{3/2} \left( 1 - \frac{3}{2k} \right) - k^{3/2} - \frac{3}{2} \sqrt{k}. \qquad (*) $$

Summing up $(*)$ over $k = 1, 2, \dots, n$ yields
$$ 0 > n^{3/2} - \frac{3}{2} \left( \sqrt{1} + \dots + \sqrt{n} \right). $$

Now put $y_i := 2x_i + x_{i+1}$ for $i = 0, 1, \dots, n$. We get $y_0 \geq 0$ and $y_i^2 \geq y_{i-1}^2 + 6$ for $i = 1, 2, \dots, n$ by Lemma 1.1. Thus, an easy induction on $i$ gives $y_i \geq \sqrt{6i}$. Using this estimate and Lemma 1.2 we get
$$ 3(x_0 + \dots + x_{n+1}) \geq y_1 + \dots + y_n > \sqrt{6} \left( \sqrt{1} + \sqrt{2} + \dots + \sqrt{n} \right) > \sqrt{6} \cdot \frac{2}{3} n^{3/2} - 3 \left( \frac{2n}{3} \right)^{3/2}. $$

\end{document}







\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{A8.} Determine all functions $f : \mathbb{R} \to \mathbb{R}$ that satisfy
$$ (f(a) - f(b)) (f(b) - f(c)) (f(c) - f(a)) = f(ab^2 + bc^2 + ca^2) - f(a^2b + b^2c + c^2a) $$
for all real numbers $a, b, c$.

\textbf{Answer:} $f(x) = \alpha x + \beta$ or $f(x) = \alpha x^3 + \beta$ where $\alpha \in \{-1, 0, 1\}$ and $\beta \in \mathbb{R}$.

\textbf{Solution.} It is straightforward to check that above functions satisfy the equation. Now let $f(x)$ satisfy the equation, which we denote $E(a, b, c)$. Then clearly $f(x) + C$ also does; therefore, we may suppose without loss of generality that $f(0) = 0$. We start with proving

\textbf{Lemma.} Either $f(x) = 0$ or $f$ is injective.

\textbf{Proof.} Denote by $\Theta \subset \mathbb{R}^2$ the set of points $(a, b)$ for which $f(a) = f(b)$. Let $\Theta^* = \{(x, y) \in \Theta : x \neq y\}$. The idea is that if $(a, b) \in \Theta$, then by $E(a, b, x)$ we get
$$ H_{a,b}(x) := (ab^2 + bx^2 + xa^2, a^2b + b^2x + x^2a) \in \Theta $$
for all real $x$. Reproducing this argument starting with $(a, b) \in \Theta^*$, we get more and more points in $\Theta$. There are many ways to fill in the details, we give below only one of them. Assume that $(a, b) \in \Theta^*$. Note that
$$ g_-(x) := (ab^2 + bx^2 + xa^2) - (a^2b + b^2x + x^2a) - (a - b)(b - x)(x - a) $$
and
$$ g_+(x) := (ab^2 + bx^2 + xa^2) + (a^2b + b^2x + x^2a) - (x^2 + ab)(a + b) + x(a^2 + b^2). $$
Hence, there exists $x$ for which both $g_-(x) \neq 0$ and $g_+(x) \neq 0$. This gives a point $(\alpha, \beta) = H_{a,b}(x) \in \Theta^*$ for which $\alpha \neq - \beta$. Now compare $E(\alpha, 1, 0)$ and $E(\beta, 1, 0)$. The left-hand side expressions coincide, on right-hand side we get $f(a) - f(\alpha^2)$ and $f(\beta) - f(\beta^2)$, respectively. Hence, $f(\alpha^2) - f(\beta^2)$ and we get a point $(\alpha_1, \beta_1) := (\alpha^2, \beta^2) \in \Theta^*$ with both coordinates $\alpha_1, \beta_1$ non-negative. Continuing squaring the coordinates, we get a point $(\gamma, \delta) \in \Theta^*$ for which $\delta > 5 \gamma \geq 0$. Our nearest goal is to get a point $(0, r) \in \Theta^*$. If $\gamma > 0$, denote by $x$ a real root of the quadratic equation $\delta \gamma x^2 + \gamma x + x \delta^2 = 0$, which exists since the discriminant $\delta^4 - 4 \delta \gamma^3$ is positive. Also $x < 0$ since this equation cannot have non-negative root. For the point $H_{\delta, \gamma}(x) := (0, r) \in \Theta$ the first coordinate is 0. The difference of coordinates equals $-r - (\delta - \gamma) (\gamma - x) (x - \delta) < 0$, so $r \neq 0$ as desired.

Now let $(0, r) \in \Theta^*$. We get $H_{0,r}(x) = (rx^2, r^2x) \in \Theta$. Thus $f(rx^2) - f(r^2x)$ for all $x \in \mathbb{R}$. Replacing $x$ to $-x$ we get $H_{a, -a}(x) = (a^3 - ar^2 + ra^2, -a^3 + a^2r + r^2a) \in \Theta$ for all real $a, x$. Putting $x = \frac{1-\sqrt{5}}{2}a$ we obtain $(0, (1 + \sqrt{5}) a^3) \in \Theta$ which means that $f(y) - f(0) = 0$ for every real $y$. $\square$

Hereafter we assume that $f$ is injective and $f(0) = 0$. By $E(a, b, 0)$ we get
$$ f(a) f(b) (f(a) - f(b)) = f(a^2b) - f(ab^2). \qquad (\spadesuit) $$

Let $\kappa := f(1)$ and note that $\kappa = f(1) \neq f(0) = 0$ by injectivity. Putting $b = 1$ in $(\spadesuit)$ we get
$$ \kappa f(a) (f(a) - \kappa) = f(a^2) - f(a). \qquad (\clubsuit) $$

Subtracting the same equality for $-a$ we get
$$ \kappa (f(a) - f(-a)) (f(a) + f(-a) - \kappa) - f(-a) - f(a). $$

Now, if $a \neq 0$, by injectivity we get $f(a) - f(-a) \neq 0$ and thus
$$ f(a) + f(-a) - \kappa - \kappa^{-1} := \lambda. \qquad (\spadesuit) $$

It follows that
$$ f(a) - f(b) - f(-b) - f(-a) $$
for all non-zero $a, b$. Replace non-zero numbers $a, b$ in $(\spadesuit)$ with $-a, -b$, respectively, and add the two equalities. Due to $(\spadesuit)$ we get
$$ (f(a) - f(b)) (f(a) f(b) - f(-a) f(-b)) = 0, $$
thus $f(a) f(b) - f(-a) f(-b) - (\lambda - f(a)) (\lambda - f(b))$ for all non-zero $a \neq b$. If $\lambda \neq 0$, this implies $f(a) + f(b) - \lambda$ that contradicts injectivity when we vary $b$ with fixed $a$. Therefore, $\lambda = 0$ and $\kappa = \pm 1$. Thus $f$ is odd. Replacing $f$ with $-f$ if necessary (this preserves the original equation) we may suppose that $f(1) = 1$.

Now, $(\clubsuit)$ yields $f(a^2) = f(a)^2$. Summing relations $(\spadesuit)$ for pairs $(a, b)$ and $(a, -b)$, we get $-2f(a) f^2(b) = -2f(ab^2)$, i.e. $f(a) f(b^2) = f(ab^2)$. Putting $b = \sqrt{x}$ for each non-negative $x$ we get $f(ax) = f(a) f(x)$ for all real $a$ and non-negative $x$. Since $f$ is odd, this multiplicativity relation is true for all $a, x$. Also, from $f(a^2) = f(a)^2$ we see that $f(x) \geq 0$ for $x \geq 0$. Next, assume that $f(x)$ for $x > 0$ does not have the form $f(x) = x^{\tau}$ for a constant $\tau$. The known property of multiplicative functions yields that the graph of $f$ is dense on $(0, \infty)^2$. In particular, we may find positive $b < 1/10$ for which $f(b) > 1$. Also, such $b$ can be found if $f(x) = x^{\tau}$ for some $\tau < 0$. Then for all $x$ we have $x^2 + xb + b \geq 0$ and so $E(1, b, x)$ implies that
$$ f(b^2 + bx^2 + x) - f(x^2 + xb^2 + b) + (f(b) - 1) (f(x) - f(b)) (f(x) - 1) \geq 0 - \left( (f(b) - 1)^3/4 $$
is bounded from below (the quadratic trinomial bound $(t - f(1)) (t - f(b)) \geq -(f(b) - 1)^2/4$ for $t - f(x)$ is used). Hence, $f$ is bounded from below on $(b^2 - \frac{1}{4b}, +\infty)$, and since $f$ is odd it is bounded from above on $(0, \frac{1}{4b} - b^2)$. This is absurd if $f(x) = x^{\tau}$ for $\tau < 0$, and contradicts to the above dense graph condition otherwise.

Therefore, $f(x) = x^{\tau}$ for $x > 0$ and some constant $\tau > 0$. Dividing $E(a, b, c)$ by $(a-b)(b - c)(c - a)$ and taking a limit when $a, b, c$ all go to 1 (the divided ratios tend to the corresponding derivatives, say, $\frac{\overline{ab}}{b-a} \to |xz'|_{x=1} = \tau$), we get $3^{\tau/2} 1/2 - \tau = 0$. Since function $F(\tau)$ is strictly convex, it has at most two roots, and we get $\tau \in \{1, 3\}$.

\end{document}
    """