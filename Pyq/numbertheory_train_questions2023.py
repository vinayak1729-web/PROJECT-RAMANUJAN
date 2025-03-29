def numbertheory():
    return r"""

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N1.} Determine all positive, composite integers $n$ that satisfy the following property: if the positive divisors of $n$ are $1 = d_1 < d_2 < \cdots < d_k = n$, then $d_i$ divides $d_{i+1} + d_{i+2}$ for every $1 \leq i \leq k-2$.

(Colombia)

\textbf{Answer:} $n = p^r$ is a prime power for some $r \geq 2$.

\textbf{Solution 1.} It is easy to see that such an $n = p^r$ with $r \geq 2$ satisfies the condition as $d_i = p^{i-1}$ with $1 \geq i \geq k = r+1$ and clearly
\[ p^{i-1} \mid p^i + p^{i+1}. \]

Now, let us suppose that there is a positive integer $n$ that satisfies the divisibility condition of the problem and that has two different prime divisors $p$ and $q$. Without loss of generality, we assume $p < q$ and that they are the two smallest prime divisors of $n$. Then there is a positive integer $j$ such that
\[ d_1 = 1, d_2 = p, \dots, d_j = p^{j-1}, d_{j+1} = p^j, d_{j+2} = q, \]
and it follows that
\[ d_{k-j-1} = \frac{n}{q}, d_{k-j} = \frac{n}{p^j}, d_{k-j+1} = \frac{n}{p^{j-1}}, \dots, d_{k-1} = \frac{n}{p}, d_k = n. \]

Thus
\[ d_{k-j-1} = \frac{n}{q} \mid d_{k-j} + d_{k-j+1} = \frac{n}{p^j} + \frac{n}{p^{j-1}} = \frac{n}{p^j} (p+1). \]

This gives $p^j \mid q(p+1)$, which is a contradiction since $\gcd(p, p+1) = 1$ and $p \neq q$.
\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N2.} Determine all pairs $(a,p)$ of positive integers with $p$ prime such that $p^a + a^4$ is a perfect square.

(Bangladesh)

\textbf{Answer:} $(a,p) = (1,3), (2,3), (6,3), (9,3)$ are all the possible solutions.

\textbf{Solution.} Let $p^a + a^4 = b^2$ for some positive integer $b$. Then we have
\[ p^a = b^2 - a^4 = (b+a^2)(b-a^2). \]

Hence both $b+a^2$ and $b-a^2$ are powers of $p$. Let $b-a^2 = p^x$ for some integer $x$. Then $b+a^2 = p^{a-x}$ and $a - x > x$. Therefore, we have
\[ 2a^2 = (b+a^2) - (b-a^2) = p^{a-x} - p^x = p^x (p^{a-2x} - 1). \tag{1} \]

We shall consider two cases according to whether $p=2$ or $p \neq 2$. We let $v_p(m)$ denote the $p$-adic valuation of $m$.
\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N3.} For positive integers $n$ and $k \geq 2$ define $E_k(n)$ as the greatest exponent $r$ such that $k^r$ divides $n!$. Prove that there are infinitely many $n$ such that $E_{10}(n) > E_9(n)$ and infinitely many $m$ such that $E_{10}(m) < E_9(m)$.

(Brazil)

\textbf{Solution 1.} We let $v_p(m)$ denote the $p$-adic valuation of $m$. By Legendre's Formula we know, for $p$ prime, that $v_p(n!) = \lfloor n/p \rfloor + \lfloor n/p^2 \rfloor + \cdots$. We can see that $E_9(n) = \lfloor \frac{v_3(n!)}{2} \rfloor$. Since $v_5(n!) \leq v_2(n!)$ and $E_{10}(n) = \min(v_5(n!), v_2(n!))$, we have $E_{10}(n) = v_5(n!)$.

Let $\ell$ be a positive integer. Set $n = 5^{2\ell - 1}$. Then we have
\[ E_{10}(n) = v_5(n!) = 5^{2\ell-2} + 5^{2\ell-3} + \cdots + 5 + 1 = \frac{5^{2\ell-1} - 1}{4} = \frac{n-1}{4}. \]

Since $n = 5^{2\ell - 1} \equiv 2 \pmod{3}$, we have $\lfloor \frac{n}{3} \rfloor = \frac{n-2}{3}$ and it implying
\[ v_3(n!) = \left\lfloor \frac{n}{3} \right\rfloor + \left\lfloor \frac{n}{3^2} \right\rfloor + \left\lfloor \frac{n}{3^3} \right\rfloor + \cdots < \frac{n-2}{3} + \frac{n}{3^2} + \frac{n}{3^3} + \cdots = \frac{n-2}{3} + \frac{n}{2} \frac{n}{3}. \]

From this we obtain
\[ E_9(n) = \left\lfloor \frac{v_3(n!)}{2} \right\rfloor \leq \frac{v_3(n!)}{2} \leq \frac{n}{4} - \frac{1}{3} < \frac{n-1}{4} = E_{10}(n). \]

In a similar way, we set now $m = 3^{4\ell - 2}$. Then we have
\[ v_3(m!) = 3^{4\ell - 3} + 3^{4\ell - 4} + \cdots + 3 + 1 = \frac{3^{4\ell - 2} - 1}{2} = \frac{m-1}{2}. \]

Note that $m = 3^{4\ell - 2} \equiv 1 \pmod{4}$ and hence $E_9(m) = \left\lfloor \frac{v_3(m!)}{2} \right\rfloor = \left\lfloor \frac{m-1}{4} \right\rfloor = \frac{m-1}{4}$. We also have $m = 3^{4\ell - 2} \equiv 4 \pmod{5}$ implying $\lfloor \frac{m}{5} \rfloor = \frac{m-4}{5}$. Therefore we obtain
\[ E_{10}(m) = v_5(m!) = \left\lfloor \frac{m}{5} \right\rfloor + \left\lfloor \frac{m}{5^2} \right\rfloor + \cdots < \frac{m-4}{5} + \frac{m}{5^2} + \cdots = \frac{m}{4} - \frac{4}{5} < \frac{m-1}{4} = E_9(m). \]

We can take infinitely many $n = 5^{2\ell - 1}$ and $m = 3^{4\ell - 2}$ completing the proof.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N4.} Let $a_1, a_2, \dots, a_n, b_1, b_2, \dots, b_n$ be $2n$ positive integers such that the $n+1$ products
\[
\begin{array}{c}
    a_1 a_2 a_3 \cdots a_n, \\
    b_1 a_2 a_3 \cdots a_n, \\
    b_1 b_2 a_3 \cdots a_n, \\
    \vdots \\
    b_1 b_2 b_3 \cdots b_n
\end{array}
\]
form a strictly increasing arithmetic progression in that order. Determine the smallest positive integer that could be the common difference of such an arithmetic progression.

(Canada)

\textbf{Answer:} The smallest common difference is $n!$.

\textbf{Solution 1.} The condition in the problem is equivalent to
\[ D = (b_1 - a_1)a_2 a_3 \cdots a_n = b_1(b_2 - a_2)a_3 \cdots a_n = \cdots = b_1 b_2 \cdots b_{n-1} (b_n - a_n), \]
where $D$ is the common difference. Since the progression is strictly increasing, $D > 0$, hence $b_i > a_i$ for every $1 \leq i \leq n$. Individually, these equalities simplify to
\[ (b_i - a_i)a_{i+1} = b_i (b_{i+1} - a_{i+1}) \text{ for every } 1 \leq i \leq n - 1. \tag{1} \]

If $g_i := \gcd(a_i, b_i) > 1$ for some $1 \leq i \leq n$, then we can replace $a_i$ with $\frac{a_i}{g_i}$ and $b_i$ with $\frac{b_i}{g_i}$ to get a smaller common difference. Hence we may assume $\gcd(a_i, b_i) = 1$ for every $1 \leq i \leq n$.

Then, we have $\gcd(b_i - a_i, b_i) = \gcd(a_i, b_i) = 1$ and $\gcd(a_{i+1}, b_{i+1}) = \gcd(a_{i+1}, b_{i+1} - a_{i+1}) = 1$ for every $1 \leq i \leq n - 1$. The equality (1) implies $a_{i+1} = b_i$ and $b_i - a_i = b_{i+1} - a_{i+1}$. Thus,
\[ a_1, b_1 = a_2, b_2 = a_3, \dots, b_{n-1} = a_n, b_n \]
is an arithmetic progression with positive common difference. Since $a_1 \geq 1$, we have $a_i \geq i$ for every $1 \leq i \leq n$, so
\[ D = (b_1 - a_1) a_2 a_3 \cdots a_n \geq 1 \cdot 2 \cdot 3 \cdots n = n!. \]

Equality is achieved when $b_i - a_i = 1$ for $1 \leq i \leq n$ and $a_1 = 1$, i.e. $a_i = i$ and $b_i = i+1$ for every $1 \leq i \leq n$. Indeed, it is straightforward to check that these integers produce an arithmetic progression with common difference $n!$.
\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N5.} Let $a_1 < a_2 < a_3 < \cdots$ be positive integers such that $a_{k+1}$ divides $2(a_1 + a_2 + \cdots + a_k)$ for every $k \geq 1$. Suppose that for infinitely many primes $p$, there exists $k$ such that $p$ divides $a_k$. Prove that for every positive integer $n$, there exists $k$ such that $n$ divides $a_k$.

(Netherlands)

\textbf{Solution.} For every $k \geq 2$ define the quotient $b_k = 2(a_1 + \cdots + a_{k-1})/a_k$, which must be a positive integer. We first prove the following properties of the sequence $(b_k)$:

Claim 1. We have $b_{k+1} \leq b_k + 1$ for all $k \geq 2$.

\textbf{Proof.} By subtracting $b_k a_k = 2(a_1 + \cdots + a_{k-1})$ from $b_{k+1}a_{k+1} = 2(a_1 + \cdots + a_k)$, we find that $b_{k+1}a_{k+1} = b_k a_k + 2 a_k = (b_k + 2) a_k$. From $a_k < a_{k+1}$ it follows that $b_k + 2 > b_{k+1}$. \qed

Claim 2. The sequence $(b_k)$ is unbounded.

\textbf{Proof.} We start by rewriting $b_{k+1}a_{k+1} = (b_k + 2) a_k$ as
\[ a_{k+1} = a_k \cdot \frac{b_k + 2}{b_{k+1}} \implies a_{k+1} \mid a_k (b_k + 2). \]

If the sequence $(b_k)$ were bounded, say by some positive integer $B$, then the prime factors of the terms of the sequence $(a_k)$ could only be primes less than or equal to $B+2$ or those dividing $a_1$ or $a_2$, which contradicts the property in the statement of the problem. \qed

Consider now an arbitrary positive integer $n$. We assume $n > b_2$, otherwise we replace $n$ by an arbitrary multiple of $n$ that is bigger than $b_2$. By Claim 2, there exists $k$ such that $b_{k+1} \geq n$. Consider the smallest such $k$. From Claim 1, it follows that we must have $b_k = n - 1$ and $b_{k+1} = n$ (we assumed $n > b_2$ to ensure that $k \geq 2$). We now find that
\[ a_{k+1} = a_k \cdot \frac{b_k + 2}{b_{k+1}} = a_k \cdot \frac{n+1}{n}. \]

Because $n$ and $n+1$ are coprime, this immediately implies that $a_k$ is divisible by $n$.
\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N6.} A sequence of integers $a_0, a_1, a_2, \dots$ is called \textit{kawaii} if $a_0 = 0$, $a_1 = 1$, and, for any positive integer $n$, we have
\[ (a_{n+1} - 3a_n + 2a_{n-1})(a_{n+1} - 4a_n + 3a_{n-1}) = 0. \]

An integer is called \textit{kawaii} if it belongs to a kawaii sequence.

Suppose that two consecutive positive integers $m$ and $m+1$ are both kawaii (not necessarily belonging to the same kawaii sequence). Prove that 3 divides $m$, and that $m/3$ is kawaii.

(China)

\textbf{Solution 1.} We start by rewriting the condition in the problem as:
\[ a_{n+1} = 3a_n - 2a_{n-1} \text{ or } a_{n+1} = 4a_n - 3a_{n-1}. \]

We have $a_{n+1} \equiv a_n \text{ or } a_{n-1} \pmod{2}$ and $a_{n+1} \equiv a_{n-1} \text{ or } a_n \pmod{3}$ for all $n \geq 1$. Now, since $a_0 = 0$ and $a_1 = 1$, we have that $a_n \equiv 0, 1 \pmod{3}$ for all $n \geq 0$. Since $m$ and $m+1$ are kawaii integers, then necessarily $m \equiv 0 \pmod{3}$.

We also observe that $a_2 = 3$ or $a_2 = 4$. Moreover,

(1) If $a_2 = 3$, then $a_n \equiv 1 \pmod{2}$ for all $n \geq 1$ since $a_1 \equiv a_2 \equiv 1 \pmod{2}$.

(2) If $a_2 = 4$, then $a_n \equiv 1 \pmod{3}$ for all $n \geq 1$ since $a_1 \equiv a_2 \equiv 1 \pmod{3}$.

Since $m \equiv 0 \pmod{3}$, any kawaii sequence containing $m$ does not satisfy (2), so it must satisfy (1). Hence, $m$ is odd and $m+1$ is even.

Take a kawaii sequence $(a_n)$ containing $m+1$. Let $t \geq 2$ be such that $a_t = m+1$. As $(a_n)$ does not satisfy (1), it must satisfy (2). Then $a_n \equiv 1 \pmod{3}$ for all $n \geq 1$. We define the sequence $a'_n = (a_{n+1} - 1)/3$. This is a kawaii sequence: $a'_0 = 0, a'_1 = 1$ and for all $n \geq 1$,
\[ (a'_{n+1} - 3a'_n + 2a'_{n-1})(a'_{n+1} - 4a'_n + 3a'_{n-1}) = (a_{n+2} - 3a_{n+1} + 2a_n)(a_{n+2} - 4a_{n+1} + 3a_n) / 9 = 0. \]

Finally, we notice that the term $a'_{t-1} = m/3$ which implies that $m/3$ is kawaii.
\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N7.} Let $a, b, c, d$ be positive integers satisfying
\[ \frac{ab}{a+b} + \frac{cd}{c+d} = \frac{(a+b)(c+d)}{a+b+c+d}. \]
Determine all possible values of $a+b+c+d$.

(Netherlands)

\textbf{Answer:} The possible values are the positive integers that are not square-free.

\textbf{Solution.}

First, note that if we take $a = \ell, b = k\ell, c = k\ell, d = k^2\ell$ for some positive integers $k$ and $\ell$, then we have
\[ \frac{ab}{a+b} + \frac{cd}{c+d} = \frac{k\ell^2}{\ell + k\ell} + \frac{k^3\ell^2}{k\ell + k^2\ell} = \frac{k\ell}{k+1} + \frac{k^2 \ell}{k+1} = k\ell \]
and
\[ \frac{(a+b)(c+d)}{a+b+c+d} = \frac{(\ell + k\ell)(k\ell + k^2\ell)}{\ell + k\ell + k\ell + k^2\ell} = \frac{k(k+1)^2\ell^2}{\ell (k+1)^2} = k\ell, \]
so that
\[ \frac{ab}{a+b} + \frac{cd}{c+d} = k\ell = \frac{(a+b)(c+d)}{a+b+c+d}. \]

This means that $a+b+c+d = \ell(1+2k+k^2) = \ell (k+1)^2$ can be attained. We conclude that all non-square-free positive integers can be attained.

Now, we will show that if
\[ \frac{ab}{a+b} + \frac{cd}{c+d} = \frac{(a+b)(c+d)}{a+b+c+d} \]
then $a+b+c+d$ is not square-free. We argue by contradiction. Suppose that $a+b+c+d$ is square-free, and note that after multiplying by $(a+b)(c+d)(a+b+c+d)$, we obtain
\[ (ab(c+d) + cd(a+b))(a+b+c+d) = (a+b)^2(c+d)^2. \tag{1} \]

A prime factor of $a+b+c+d$ must divide $a+b$ or $c+d$, and therefore divides both $a+b$ and $c+d$. Because $a+b+c+d$ is square-free, the fact that every prime factor $a+b+c+d$ divides $a+b$ implies that $a+b+c+d$ itself divides $a+b$. Because $a+b < a+b+c+d$, this is impossible. So $a+b+c+d$ cannot be square-free.
\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{N8.} Let $\mathbb{Z}_{>0}$ be the set of positive integers. Determine all functions $f: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ such that
\[ f^{f(b)}(a + 1) = (a+1)f(b) \]
holds for all $a, b \in \mathbb{Z}_{>0}$, where $f^k(n) = f(f(\dots f(n) \dots ))$ denotes the composition of $f$ with itself $k$ times.

(Taiwan)


\textbf{Solution 2.}  In the same way as Steps 1-2 of Solution 1, we have that $f$ is injective and $f(\mathbb{Z}_{\geq 0}) = \mathbb{Z}_{\geq 2}$.

\noindent We first note that Claim 2 in Solution 1 is also true for $a = 1$.

\bigskip

\noindent Claim 2'. For any $a, n \in \mathbb{Z}_{\geq 0}$, we have $f^n(a) \neq a$.

\bigskip

\noindent \textit{Proof}. If $a \geq 2$, the assertion was proved in Claim 2 in Solution 1. If $a = 1$, we have that 1 is not in the range of $f$ by Claim 3 in Solution 1. So, $f^n(1) \neq 1$ for every $n \in \mathbb{Z}_{\geq 0}$. \hfill $\square$

\bigskip

\noindent For any $a, b \in \mathbb{Z}_{\geq 0}$, we have

$$f^{bf(f(a)-1)+1}(a) = f^{bf(f(a)-1)}(f(a))^{p(f(a)-1,b)} f(a)f(b).$$

\bigskip

\noindent Since the right-hand side is symmetric in $a, b$, we have

$$f^{bf(f(a)-1)+1}(a) = f(a)f(b) = f^{af(f(b)-1)+1}(b).$$

\bigskip

\noindent Since $f$ is injective, we have $f^{bf(f(a)-1)}(a) = f^{af(f(b)-1)}(b)$. We set $g(n) = f(f(n)-1)$. Then we have $f^{bg(a)}(a) = f^{ag(b)}(b)$ for any $a, b \in \mathbb{Z}_{\geq 0}$. We set $n_{a,b} = bg(a) - ag(b)$. Then, for sufficiently large $n$, we have $f^{n+n_{a,b}}(a) = f^{n}(b)$. For any $a, b, c \in \mathbb{Z}_{\geq 0}$ and sufficiently large $n$, we have

$$f^{n+n_{a,b}+n_{b,c}+n_{c,a}}(a) = f^{n}(a).$$

\bigskip

\noindent By Claim 2' above, we have $n_{a,b} + n_{b,c} + n_{c,a} = 0$, so

$$(a - b)g(c) + (b - c)g(a) + (c - a)g(b) = 0.$$

\bigskip

\noindent Taking $(a, b, c) = (n, n+1, n+2)$, we have $g(n+1) - g(n) = g(n+2) - g(n+1)$. So, $\{g(n)\}_{n \geq 1}$ is an arithmetic progression.

\bigskip

\noindent There exist $C, D \in \mathbb{Z}$ such that $g(n) = f(f(n)-1) = Cn + D$ for all $n \in \mathbb{Z}_{\geq 0}$. By Step 2 of Solution 1, we have $f(\mathbb{Z}_{\geq 0}) = \mathbb{Z}_{\geq 2}$, so $C = 1$. Since $2 = \min_{n \in \mathbb{Z}_{\geq 0}} \{f(f(n)-1)\}$, we have $D = 1$. Thus, $g(n) = f(f(n) - 1) = n + 1$ for all $n \geq 1$. For any $a, b \in \mathbb{Z}_{\geq 0}$, we have $f^{b(a+1)}(a) = f^{a(b+1)}(b)$. By the injectivity of $f$, we have $f^{a}(a) = f^{a}(b)$. For any $n \in \mathbb{Z}_{\geq 0}$, taking $(a, b) = (1, n)$, we have $f^{n}(1) = f^{n}(n)$, so $f^{n-1}(1) = n$ again by the injectivity of $f$. For any $n \geq 1$, we have $f(n) = f(f^{n-1}(1)) = f^n(1) = n + 1$.

\end{document}





"""