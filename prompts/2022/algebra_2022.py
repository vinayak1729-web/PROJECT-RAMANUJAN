def algebra_2022():
    return r"""

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A1.} Let $(a_n)_{n \ge 1}$ be a sequence of positive real numbers with the property that
\[
(a_{n+1})^2 + a_n a_{n+2} \le a_n + a_{n+2}
\]
for all positive integers $n$. Show that $a_{2022} \le 1$. \hfill (Nigeria)

\textbf{Solution.} We begin by observing that $(a_{n+1})^2 - 1 \le a_n + a_{n+2} - a_n a_{n+2} - 1$, which is equivalent to
\[
(a_{n+1})^2 - 1 \le (1 - a_n)(a_{n+2} - 1).
\]
Suppose now that there exists a positive integer $n$ such that $a_{n+1} > 1$ and $a_{n+2} > 1$.
Since $(a_{n+1})^2 - 1 \le (1 - a_n)(a_{n+2} - 1)$, we deduce that $0 < 1 - a_n < 1 < 1 + a_{n+2}$, thus $(a_{n+1})^2 - 1 < (a_{n+2} + 1)(a_{n+2} - 1) = (a_{n+2})^2 - 1$.
On the other hand, $(a_{n+2})^2 - 1 \le (1 - a_{n+3})(a_{n+1} - 1) < (1 + a_{n+1})(a_{n+1} - 1) = (a_{n+1})^2 - 1$, a contradiction. We have shown that we cannot have two consecutive terms, except maybe $a_1$ and $a_2$, strictly greater than 1.

Finally, suppose $a_{2022} > 1$. This implies that $a_{2021} \le 1$ and $a_{2023} \le 1$. Therefore $0 < (a_{2022})^2 - 1 \le (1 - a_{2021})(a_{2023} - 1) \le 0$, a contradiction. We conclude that $a_{2022} \le 1$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A2.} Let $k \ge 2$ be an integer. Find the smallest integer $n \ge k+1$ with the property that there exists a set of $n$ distinct real numbers such that each of its elements can be written as a sum of $k$ other distinct elements of the set. \hfill (Slovakia)

\textbf{Answer:} $n = k+4$.

\textbf{Solution.} First we show that $n \ge k+4$. Suppose that there exists such a set with $n$ numbers and denote them by $a_1 < a_2 < \dots < a_n$.

Note that in order to express $a_1$ as a sum of $k$ distinct elements of the set, we must have $a_1 \ge a_2 + \dots + a_{k+1}$ and, similarly for $a_n$, we must have $a_{n-k} + \dots + a_{n-1} \ge a_n$. We also know that $n \ge k+1$.

If $n = k+1$ then we have $a_1 \ge a_2 + \dots + a_{k+1} > a_1 + \dots + a_k > a_{k+1}$, which gives a contradiction.

If $n = k+2$ then we have $a_1 \ge a_2 + \dots + a_{k+1} \ge a_{k+2}$, that again gives a contradiction.

If $n = k+3$ then we have $a_1 \ge a_2 + \dots + a_{k+1}$ and $a_3 + \dots + a_{k+2} \ge a_{k+3}$. Adding the two inequalities we get $a_1 + a_{k+2} \ge a_2 + a_{k+3}$, again a contradiction.

It remains to give an example of a set with $k+4$ elements satisfying the condition of the problem. We start with the case when $k = 2l$ and $l \ge 1$. In that case, denote by $A_i = \{-i, i\}$ and take the set $A_1 \cup \dots \cup A_{l+2}$, which has exactly $k+4 = 2l+4$ elements. We are left to show that this set satisfies the required condition.

Note that if a number $i$ can be expressed in the desired way, then so can $-i$ by negating the expression. Therefore, we consider only $1 \le i \le l+2$.

If $i < l+2$, we sum the numbers from some $l-1$ sets $A_j$ with $j \neq i, l+1$, and the numbers $i + 1$ and $-1$.

For $i = l+2$, we sum the numbers from some $l-1$ sets $A_j$ with $j \neq i, l+1$, and the numbers $l+1$ and 1.

It remains to a give a construction for odd $k = 2l+1$ with $l \ge 1$ (since $k \ge 2$). To that end, we modify the construction for $k = 2l$ by adding 0 to the previous set.

This is a valid set as 0 can be added to each constructed expression, and 0 can be expressed as follows: take the numbers 1, 2, -3 and all the numbers from the remaining $l-1$ sets $A_4, A_5, \dots, A_{l+2}$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A3.} Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Find all functions $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ such that, for every $x \in \mathbb{R}_{>0}$, there exists a unique $y \in \mathbb{R}_{>0}$ satisfying
\[
xf(y) + yf(x) < 2.
\] \hfill (Netherlands)

\textbf{Answer:} The function $f(x) = 1/x$ is the only solution.

\textbf{Solution 1.} First we prove that the function $f(x) = 1/x$ satisfies the condition of the problem statement. The AM-GM inequality gives
\[
\frac{x}{y} + \frac{y}{x} \ge 2
\]
for every $x, y > 0$, with equality if and only if $x=y$. This means that, for every $x>0$, there exists a unique $y>0$ such that
\[
\frac{x}{y} + \frac{y}{x} < 2,
\]
namely $y=x$.

Let now $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ be a function that satisfies the condition of the problem statement.
We say that a pair of positive real numbers $(x, y)$ is good if $xf(y) + yf(x) < 2$. Observe that if $(x, y)$ is good then so is $(y, x)$.

\textbf{Lemma 1.0.} If $(x, y)$ is good, then $x=y$.

\textbf{Proof.} Assume that there exist positive real numbers $x \neq y$ such that $(x, y)$ is good. The uniqueness assumption says that $y$ is the unique positive real number such that $(x, y)$ is good. In particular, $(x, x)$ is not a good pair. This means that
\[
xf(x) + xf(x) \ge 2
\]
and thus $xf(x) \ge 1$. Similarly, $(y, x)$ is a good pair, so $(y, y)$ is not a good pair, which implies $yf(y) \ge 1$. We apply the AM-GM inequality to obtain
\[
xf(y) + yf(x) \ge 2\sqrt{xf(y) \cdot yf(x)} = 2\sqrt{xy \cdot f(x)f(y)} \ge 2.
\]
This is a contradiction, since $(x, y)$ is a good pair.

By assumption, for any $x > 0$, there always exists a good pair containing $x$, however Lemma 1 implies that the only good pair that can contain $x$ is $(x, x)$, so
\[
xf(x) < 1 \iff f(x) < \frac{1}{x}
\]
for every $x>0$.

In particular, with $x = 1/f(t)$ for $t>0$, we obtain
\[
\frac{1}{f(t)} \cdot f(f(t)) < 1.
\]
Hence
\[
t - f\left(\frac{1}{f(t)}\right) < tf(t) < 1.
\]
We claim that $(t, 1/f(t))$ is a good pair for every $t > 0$. Indeed,
\[
t \cdot f\left(\frac{1}{f(t)}\right) + \frac{1}{f(t)} f(t) = t \cdot f\left(\frac{1}{f(t)}\right) + 1 < 2.
\]
Lemma 1 implies that $t = 1/f(t) \iff f(t) = 1/t$ for every $t > 0$.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A4.} Let $n \ge 3$ be an integer, and let $x_1, x_2, \dots, x_n$ be real numbers in the interval $[0, 1]$. Let $s = x_1 + x_2 + \dots + x_n$, and assume that $s \ge 3$. Prove that there exist integers $i$ and $j$ with $1 \le i < j \le n$ such that
\[
2^{j-i} x_i x_j > 2^{s-3}.
\] \hfill (Trinidad and Tobago)

\textbf{Solution.}

Let $1 \le a < b \le n$ be such that $2^{b-a} x_a x_b$ is maximal. This choice of $a$ and $b$ implies that $x_{a+t} \le 2^t x_a$ for all $1-a \le t \le b-a-1$, and similarly $x_{b-t} \le 2^t x_b$ for all $b-n \le t \le b-a+1$.
Now, suppose that $x_a \in \left(\frac{1}{2^{u+1}}, \frac{1}{2^u}\right]$ and $x_b \in \left(\frac{1}{2^{v+1}}, \frac{1}{2^v}\right]$, and write $x_a = 2^{-\alpha}, x_b = 2^{-\beta}$. Then
\[
\sum_{i=1}^{a+u-1} x_i \le 2^u x_a \left(\frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2^{a+u-1}}\right) < 2^u x_a \le 1,
\]
and similarly,
\[
\sum_{i=b-v+1}^{n} x_i \le 2^v x_b \left(\frac{1}{2} + \frac{1}{4} + \dots + \frac{1}{2^{n-b+v}}\right) < 2^v x_b \le 1.
\]
In other words, the sum of the $x_i$'s for $i$ outside of the interval $[a+u, b-v]$ is strictly less than 2. Since the total sum is at least 3, and each term is at most 1, it follows that this interval must have at least two integers, i.e., $a+u < b-v$. Thus, by bounding the sum of the $x_i$ for $i \in [1, a+u] \cup [b-v, n]$ like above, and trivially bounding each $x_i \in (a+u, b-v)$ by 1, we obtain
\[
s < 2^{u+1} x_a + 2^{v+1} x_b + ((b-v) - (a+u) - 1) = b-a + (2^{u+1-\alpha} + 2^{v+1-\beta} - (u+v+1)).
\]
Now recall $\alpha \in (u, u+1]$ and $\beta \in (v, v+1]$, so applying Bernoulli's inequality yields
\[
2^{u+1-\alpha} + 2^{v+1-\beta} - u - v - 1 \le (1 + (u+1-\alpha)) + (1 + (v+1-\beta)) - u - v - 1 = 3 - \alpha - \beta.
\]
It follows that $s - 3 < b-a - \alpha - \beta$, and so
\[
2^{s-3} < 2^{b-a - \alpha - \beta} = 2^{b-a} x_a x_b.
\]

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A5.} Find all positive integers $n \ge 2$ for which there exist n real numbers $a_1 < \dots < a_n$ and a real number $r > 0$ such that that the $\frac{1}{2}n(n-1)$ differences $a_j - a_i$ for $1 \le i < j \le n$ are equal, in some order, to the numbers $r^1, r^2, \dots, r^{\frac{1}{2}n(n-1)}$. \hfill (Czech Republic)

\textbf{Answer:} $n \in \{2, 3, 4\}$.

\textbf{Solution.} We first show a solution for each $n \in \{2, 3, 4\}$. We will later show the impossibility of finding such a solution for $n \ge 5$.
For $n = 2$, take for example $\{a_1, a_2\} = (1, 3)$ and $r = 2$.
For $n = 3$, take the root $r > 1$ of $x^2 - x - 1 = 0$ (the golden ratio) and set $\{a_1, a_2, a_3\} = (0, r, r + r^2)$. Then
\[
(a_2 - a_1, a_3 - a_2, a_3 - a_1) = (r, r^2, r + r^2 = r^3).
\]
For $n = 4$, take the root $r \in (1, 2)$ of $x^3 - x - 1 = 0$ (such a root exists because $1^3 - 1 - 1 < 0$ and $2^3 - 2 - 1 > 0$) and set $(a_1, a_2, a_3, a_4) = (0, r, r + r^2, r + r^2 + r^3)$. Then
\[
(a_2 - a_1, a_3 - a_2, a_3 - a_1, a_4 - a_1, a_4 - a_2, a_4 - a_1) = (r, r^2, r^3, r^4, r^5, r^6).
\]
For $n \ge 5$, we will proceed by contradiction. Suppose there exist numbers $a_1 < \dots < a_n$ and $r > 1$ satisfying the conditions of the problem. We start with a lemma:

\textbf{Lemma.} We have $r^{n - 1} > 2$.

\textbf{Proof.} There are only $n - 1$ differences $a_j - a_i$, with $j = i + 1$, so there exists an exponent $e \le n$ and a difference $a_j - a_i$ with $j \ge i + 2$ such that $a_j - a_i = r^e$. This implies
\[
r^n > r^e = a_j - a_i = (a_j - a_{j-1}) + (a_{j-1} - a_i) > r + r = 2r,
\]
thus $r^{n - 1} > 2$ as desired.

To illustrate the general approach, we first briefly sketch the idea behind the argument in the special case $n = 5$. In this case, we clearly have $a_5 - a_1 = r^{10}$. Note that there are 3 ways to rewrite $a_5 - a_1$ as a sum of two differences, namely
\[
(a_5 - a_4) + (a_4 - a_1), (a_5 - a_3) + (a_3 - a_1), (a_5 - a_2) + (a_2 - a_1).
\]
Using the lemma above and convexity of the function $f(n) = r^n$, we argue that those three ways must be $r^{10} = r^9 + r^1 = r^8 + r^4 = r^7 + r^6$. That is, the "large" exponents keep dropping by 1, while the "small" exponents keep increasing by $n - 2, n - 3, ..., 2$. Comparing any two such equations, we then get a contradiction unless $n < 4$.
Now we go back to the full proof for any $n \ge 5$. Denote $b = \frac{1}{2}n(n - 1)$. Clearly, we have $a_n - a_1 = r^b$. Consider the $n - 2$ equations of the form:
\[
a_n - a_1 = (a_n - a_i) + (a_i - a_1) \text{ for } i \in \{2, ..., n-1\}.
\]

In each equation, one of the two terms on the right-hand side must be at least $\frac{1}{2} (a_n - a_1)$.
But from the lemma we have $r^{b - (n-1)} = r^b / r^{n-1} < \frac{1}{2} (a_n - a_1)$, so there are at most $n-2$ sufficiently large elements in $\{r^k | 1 < k < b\}$, namely $r^{b-1}, ..., r^{b - (n-2)}$ (note that $r^b$ is already used for $a_n - a_1$). Thus, the "large" terms must be, in some order, precisely equal to elements in
\[
L = \{r^{b-1}, ..., r^{b - (n-2)}\}.
\]

Next we claim that the "small" terms in the $n - 2$ equations must be equal to the elements in
\[
S = \{r^{b - (n-2) - \frac{1}{2}i(i+1)} | 1 \le i < n - 2\},
\]
in the corresponding order (the largest "large" term with the smallest "small" term, etc.). Indeed, suppose that
\[
r^{b} = a_n - a_1 = r^{b-i} + r^{\alpha_i} \text{ for } i \in \{1, ..., n-2\},
\]
where $1 < \alpha_1 < \dots < \alpha_{n-2} \le b - (n-1)$. Since $r > 1$ and $f(r) = r^b$ is convex, we have
\[
r^{b-1} - r > r^{b-2} - r^3 > \dots > r^{b-(n-3)} - r^{n-2},
\]
implying that
\[
r^{\alpha_2} - r^{\alpha_1} > r^{\alpha_3} - r^{\alpha_2} > \dots > r^{\alpha_{n-2}} - r^{\alpha_{n-3}}.
\]
Convexity of $f(r) = r^n$ further implies
\[
\alpha_2 - \alpha_1 > \alpha_3 - \alpha_2 > \dots > \alpha_{n-2} - \alpha_{n-3}.
\]
Note that $a_{n-2} - a_{n-3} \ge 2$: Otherwise we would have $a_{n-2} - a_{n-3} = 1$ and thus
\[
r^{\alpha_{n-3}} \cdot (r-1) = r^{a_{n-2}} - r^{\alpha_{n-3}} = r^{b-(n-3)} - r^{b-(n-2)},
\]
implying that $a_{n-3} = b - (n-2)$, a contradiction. Therefore, we have
\begin{align*}
    a_{n-2} - a_1 &= (a_{n-2} - a_{n-3}) + \dots + (a_2 - a_1) \\
    &\ge 2 + 3 + \dots + (n-2) \\
    &= \frac{1}{2}(n-2)(n-1) - 1 = \frac{1}{2}n(n-3).
\end{align*}
On the other hand, from $a_{n-2} < b - (n-1)$ and $a_1 > 1$ we get
\[
\alpha_{n-2} - \alpha_1 \le b - n = \frac{1}{2}n (n-1) - n = \frac{1}{2}n(n-3),
\]
implying that equalities must occur everywhere and the claim about the small terms follows.
Now, assuming $n - 2 > 2$, we have the two different equations:
\[
r^{b} = r^{b - (n-2)} + r^{b-(n-2)-1} \text{ and } r^{b} = r^{b - (n-3)} + r^{b-(n-2)-2},
\]
which can be rewritten as
\[
r^{n-1} = r + 1 \text{ and } r^{n+1} = r^4 + 1.
\]
Simple algebra now gives
\[
r^4 + 1 = r^{n+1} = r^{n-1} \cdot r^2 = r^3 + r^2 \implies (r-1)(r^3 - r - 1) = 0.
\]
Since $r \neq 1$, using Equation (1) we conclude $r^3 = r + 1 = r^{n-1}$, thus $n = 4$, which gives a contradiction.

\end{document}









\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A6.} Let $\mathbb{R}$ be the set of real numbers. We denote by $\mathcal{F}$ the set of all functions $f: \mathbb{R} \to \mathbb{R}$ such that
\[
f(x + f(y)) = f(x) + f(y)
\]
for every $x, y \in \mathbb{R}$. Find all rational numbers $q$ such that for every function $f \in \mathcal{F}$, there exists some $z \in \mathbb{R}$ satisfying $f(z) = qz$. \hfill (Indonesia)

\textbf{Answer:} The desired set of rational numbers is $\left\{ \frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0 \right\}$.

\textbf{Solution.} Let $\mathbb{Z}$ be the set of all rational numbers $q$ such that for every function $f \in \mathcal{F}$, there exists some $z \in \mathbb{R}$ satisfying $f(z) = qz$. Let further
\[
S = \left\{ \frac{n+1}{n}: n \in \mathbb{Z}, n \neq 0 \right\}.
\]
We prove that $Z = S$ by showing the two inclusions: $S \subseteq Z$ and $Z \subseteq S$.
We first prove that $S \subseteq Z$. Let $f \in \mathcal{F}$ and let $P(x, y)$ be the relation $f(x + f(y)) = f(x) + f(y)$. First note that $P(0, 0)$ gives $f(f(0)) = 2f(0)$. Then, $P(0, f(0))$ gives $f(2f(0)) = 3f(0)$.

We claim that
\[
f(kf(0)) = (k+1)f(0)
\]
for every integer $k \ge 1$. The claim can be proved by induction. The cases $k = 1$ and $k = 2$ have already been established. Assume that $f(kf(0)) = (k+1)f(0)$ and consider $P(0, kf(0))$ which gives
\[
f((k+1)f(0)) = f(0) + f(kf(0)) = (k+2)f(0).
\]
This proves the claim. We conclude that $\frac{k+1}{k} \in Z$ for every integer $k \ge 1$. Note that $P(-f(0), 0)$ gives $f(-f(0)) = 0$. We now claim that
\[
f(-kf(0)) = (-k+1)f(0)
\]
for every integer $k \ge 1$. The proof by induction is similar to the one above. We conclude that $\frac{-k+1}{-k} \in Z$ for every integer $k \ge 1$. This shows that $S \subseteq Z$.

We now prove that $Z \subseteq S$. Let $p$ be a rational number outside the set $S$. We want to prove that $p$ does not belong to $Z$. To that end, we construct a function $f \in \mathcal{F}$ such that $f(z) \neq pz$ for every $z \in \mathbb{R}$. The strategy is to first construct a function
\[
g: [0, 1) \to \mathbb{Z}
\]
and then define $f$ as $f(x) = g(\{x\}) + [x]$. This function $f$ belongs to $\mathcal{F}$. Indeed,
\begin{align*}
f(x + f(y)) &= g(\{x + f(y)\}) + [x + f(y)] \\
&= g(\{x + g(\{y\}) + [y] \}) + [x + g(\{y\}) + [y]] \\
&= g(\{x\}) + [x] + g(\{y\}) + [y] \\
&= f(x) + f(y).
\end{align*}
where we used that $g$ only takes integer values.

Lemma 1. For every $\alpha \in [0, 1)$, there exists $m \in \mathbb{Z}$ such that
\[
m + n \neq p(\alpha + n)
\]
for every $n \in \mathbb{Z}$.

\end{document}

 \documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\begin{document}
Shortlisted problems - solutions

19

Proof. Note that if $p = 1$ the claim is trivial. If $p \neq 1$, then the claim is equivalent to the existence of an integer $m$ such that
\[
\frac{m - pa}{p - 1}
\]
is never an integer. Assume the contrary. That would mean that both
\[
\frac{m - pa}{p - 1} \text{ and } \frac{(m+1) - pa}{p - 1}
\]
are integers, and so is their difference. The latter is equal to
\[
\frac{1}{p - 1}.
\]

Since we assumed $p \notin S$, $1 / (p - 1)$ is never an integer. This is a contradiction.

Define $g: [0, 1) \to Z$ by $g(\alpha) = m$ for any integer m that satisfies the conclusion of Lemma 1. Note that $f(z) = pz if and and only if
\[
g(\{z\}) + [z] \neq p(\{z\} + [z])
\]
The latter is guaranteed by the construction of the function $g$. We conclude that $p \notin Z$ as desired. This shows that $Z \subset S$.
\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A7.} For a positive integer $n$ we denote by $s(n)$ the sum of the digits of $n$. Let $P(x) = x^n + a_{n-1}x^{n-1} + \dots + a_1x + a_0$ be a polynomial, where $n \ge 2$ and $a_i$ is a positive integer for all $0 \le i \le n-1$. Could it be the case that, for all positive integers $k$, $s(k)$ and $s(P(k))$ have the same parity? \hfill (Belarus)

\textbf{Answer:} No. For any such polynomial there exists a positive integer $k$ such that $s(k)$ and $s(P(k))$ have different parities.

\textbf{Solution.} With the notation above, we begin by choosing a positive integer $t$ such that
\[
10^t > \max \left\{ \frac{100^{n-1} a_{n-1}}{(10^{n-1} - 9^{\frac{a_{n-1}}{9^{n-1} - 1}})}, \frac{a_{n-1}}{9} 10^{n-1}, \frac{a_{n-1}}{9}, \dots, \frac{a_{n-1}}{9} (10 a_0)^{n-1} \right\}
\]
As a direct consequence of $10^t$ being bigger than the first quantity listed in the above set, we get that the interval
\[
I = \left[ \left( \frac{9}{a_{n-1}} 10^t \right)^{\frac{1}{n-1}}, \left( \frac{1}{a_{n-1}} 10^{t+1} \right)^{\frac{1}{n-1}} \right]
\]
contains at least 100 consecutive positive integers.

Let $X$ be a positive integer in $I$ such that $X$ is congruent to 1 mod 100. Since $X \in I$ we have
\[
9 \cdot 10^t \le a_{n-1}X^{n-1} < 10^{t+1},
\]
thus the first digit (from the left) of $a_{n-1} X^{n-1}$ must be 9.

Next, we observe that $a_{n-1} (10 a_i)^{n-1} < 9 \cdot 10^t \le a_{n-1} X^{n-1}$, thus $10 a_i < X$ for all $i$, which immediately implies that $a_0 < a_1 X < \dots < a_{n} X^{n}$, and the number of digits of this strictly increasing sequence forms a strictly increasing sequence too. In other words, if $i < j$, the number of digits of $a_i X^{i}$ is less than the number of digits of $a_j X^{j}$.

Let $\alpha$ be the number of digits of $a_{n-1} X^{n-1}$, thus $10^{a-1} \le a_{n-1} X^{n-1} < 10^{\alpha}$. We are now going to look at $P(10^{\alpha} X)$ and $P(10^{\alpha-1} X)$ and prove that the sum of their digits has different parities. This will finish the proof since $s(10^{\alpha} X) = s(X)$.

We have $P(10^{\alpha} X) = 10^{\alpha n} X^n + a_{n-1}10^{\alpha (n-1)} X^{n-1} + \dots + a_0$, and since $10^{\alpha(i+1)} > 10^{\alpha i} a_{n-1} X^{n-1} > 10^{\alpha i} + 1 a_i X^{i}$, thus all terms

\[
\frac{}{} \ge 10^(\alpha-1)a_{i-1}X^{i-1}
\]

come in 'blocks', exactly as in the previous case.

Finally, $10^{(\alpha-1)n+1} > 10^{(\alpha-1)n}a_{n-1}X^{n-1} \ge 10^{\alpha-1(n-1)} \ge 10^{(\alpha-1)n}a_{n-1}X^{n-1}$, thus $10^{(\alpha-1)n}$ has exactly $(\alpha - 1)n+1$ digits, and its first digit is 9, as established above. On the other hand, $10^{(\alpha - 1)n}X^{n}$ has exactly $(\alpha - 1)n$ zeros, followed by 01 (as X is 1 mod 100). Therefore, when we add the terms, the 9 and 1 turn into 0, the 0 turns into 1, and nothing else is affected. Putting everything together, we obtain
\[
\frac{}{}\geq 10^{\alpha}_{(\alpha-1)+1} \geq 10 ^{(\alpha -1)-N}
\]

\[
s(P(10^{\alpha-1} X)) = s(X^n) + s(a_{n-1} X^{n-1}) + \dots + s(a_0) - 9 = s(P(10^{\alpha} X)) - 9
\]
thus $s(P(10^{\alpha} X))$ and $s(P(10^{\alpha-1} X))$ have different parities, as claimed.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{A8.} For a positive integer $n$, an n-sequence is a sequence $(a_0, \dots, a_n)$ of non-negative integers satisfying the following condition: if $i$ and $j$ are non-negative integers with $i + j \le n$, then $a_i + a_j \le n$ and $a_{a_i+a_j} = a_{i+j}$.
Let $f(n)$ be the number of n-sequences. Prove that there exist positive real numbers $c_1, c_2$ and $\lambda$ such that
\[
c_1 \lambda^n < f(n) < c_2 \lambda^n
\]
for all positive integers $n$. \hfill (Canada)

\textbf{Answer:} Such constants exist with $\lambda = 3^{\frac{1}{6}}$; we will discuss appropriate values of $c_1$ and $c_2$ in the solution below.

\textbf{Solution.} In order to solve this, we will give a complete classification of n-sequences.
Let $k = \lfloor n/2 \rfloor$. We will say that an n-sequence is large if $a_i > k$ for some $i$, and small if no such i exists. For now we will assume that $(a_i)$ is not the identity sequence (in other words, that $a_i \neq i$ for some $i$).

\textbf{Lemma 1.} If $a_r = a_s$ and $r, s < n$, then $a_{r+1} = a_{s+1}$.
\textbf{Proof.} We have $a_{r+1} = a_{r+a_1} = a_{a_r+a_1} = a_{a_s+a_1} = a_{s+1}$.

\textbf{Lemma 2.} If $i \le k$, then $a_i \le k$.
\textbf{Proof.} We have $i + i \le n$, so $a_i + a_i \le n$, so $a_i + a_i \le n$ whence $a_i \le k$.

\textbf{Lemma 3.} There exist $r, s$ such that $a_r = a_s$ and $r \neq s$.
\textbf{Proof.} If $a_0 \neq 0$ then $a_{2a_0} = a_0$. Otherwise, $a_i = a_i$ for all $i$, so take $i$ such that $a_i \neq i$ (which we can do by our earlier assumption).

\textbf{Lemma 4.} Let $r$ be the smallest index such that $a_s = a_r$ for some $s > r$, and let $d$ be the minimum positive integer such that $a_{r+d} = a_r$. Then

1. The subsequence $(a_r, a_{r+1}, \dots, a_n)$ is periodic with minimal period $d$. That is, for $u < v$, we have $a_u = a_v$ if and only if $u, v \ge r$ and $d \mid u-v$.

2. $a_i = i$ for $i < r$ and $a_i \ge r$ for $i \ge r$.

In this case we say $(a_i)$ has period $d$ and offset $r$.

\textbf{Proof.} We prove each in turn:

1. The "if" implication is clear from Lemma 1. For the reverse direction, suppose $a_u = a_v$. Then there are integers $r \le u_0, v_0 < r + d$ such that $d \mid u - u_0, v - v_0$, so $a_{u_0} = a_u = a_v = a_{v_0}$. If $u_0 < v_0$ then $a_{r+d + u_0 - v_0} = a_{r+d} = a_r$, contradicting the minimality of $d$. There is a similar contradiction when $u_0 > v_0$. Thus $u_0 = v_0$, so $d \mid u - v$.

2. If $r = 0$ there is nothing to prove. Otherwise $a_0 = a_{2a_0}$ so $2a_0 = 0$. Then we have $a_i = a_i$ for all i, so $a_i = i$ for i < r.

\textbf{Lemma 5.} Either

1. $d \mid a_i - i$ for all i, or

2. $r = 0$ and $d \mid a_i - i - d/2$ for all i.

\end{document}



"""