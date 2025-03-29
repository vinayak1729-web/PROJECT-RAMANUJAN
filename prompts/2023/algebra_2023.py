def algebra_2023():
    return r"""
imo-2023
Q1.  Professor Oak is feeding his 100 Pokémon. Each Pokémon has a bowl whose capacity
 is a positive real number of kilograms. These capacities are known to Professor Oak. The total
 capacity of all the bowls is 100 kilograms. Professor Oak distributes 100 kilograms of food in
 such a way that each Pokémon receives a non-negative integer number of kilograms of food
 (which may be larger than the capacity of their bowl). The dissatisfaction level of a Pokémon
 who received N kilograms of food and whose bowl has a capacity of C kilograms is equal to
 |N C|.
 Find the smallest real number D such that, regardless of the capacities of the bowls, Pro
fessor Oak can distribute the food in a way that the sum of the dissatisfaction levels over all
 the 100 Pokémon is at most D.

Ans : 50
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{Answer:} The answer is $D = 50$.

\noindent \textbf{Solution 1.} First, consider the situation where 99 bowls have a capacity of 0.5 kilograms and the last bowl has a capacity of 50.5 kilograms. No matter how Professor Oak distributes the food, the dissatisfaction level of every Pokémon will be at least 0.5. This amounts to a total dissatisfaction level of at least 50, proving that $D \ge 50$.

\medskip
Now we prove that no matter what the capacities of the bowls are, Professor Oak can always distribute food in a way that the total dissatisfaction level is at most 50. We start by fixing some notation. We number the Pokémon from 1 to 100. Let $C_i > 0$ be the capacity of the bowl of the $i^{\text{th}}$ Pokémon. By assumption, we have $C_1 + C_2 + \cdots + C_{100} = 100$. We write $F_i := C_i - \lfloor C_i \rfloor$ for the fractional part of $C_i$. Without loss of generality, we may assume that $F_1 \le F_2 \le \cdots \le F_{100}$.

\medskip
Here is a strategy: Professor Oak starts by giving $\lfloor C_i \rfloor$ kilograms of food to the $i^{\text{th}}$ Pokémon. Let
\begin{align*}
R &:= 100 - \lfloor C_1 \rfloor - \lfloor C_2 \rfloor - \cdots - \lfloor C_{100} \rfloor = F_1 + F_2 + \cdots + F_{100} \ge 0
\end{align*}
be the amount of food left. He continues by giving an extra kilogram of food to the $R$ Pokémon numbered $100-R+1, 100-R+2, \dots, 100$, i.e., the Pokémon with the $R$ largest values of $F_i$. By doing so, Professor Oak distributed 100 kilograms of food. The total dissatisfaction level with this strategy is
\begin{align*}
d := F_1 + \cdots + F_{100-R} + (1 - F_{100-R+1}) + \cdots + (1 - F_{100}).
\end{align*}

\medskip
We can rewrite
\begin{align*}
d &= 2(F_1 + \cdots + F_{100-R}) + R - (F_1 + \cdots + F_{100}) \\
  &= 2(F_1 + \cdots + F_{100-R}).
\end{align*}

\medskip
Now, observe that the arithmetic mean of $F_1, F_2, \dots, F_{100-R}$ is not greater than the arithmetic mean of $F_1, F_2, \dots, F_{100}$, because we assumed $F_1 \le F_2 \le \cdots \le F_{100}$. Therefore
\begin{align*}
d &\le 2(100 - R) \cdot \frac{\frac{F_1 + \cdots + F_{100}}{100} \cdot 100}{100} \\
  &= 2 \cdot \frac{R(100 - R)}{100}.
\end{align*}

\medskip
Finally, we use the AM-GM inequality to see that $R(100 - R) \le \frac{100^2}{2^2}$ which implies $d \le 50$. We conclude that there is always a distribution for which the total dissatisfaction level is at most 50, proving that $D \le 50$.

\end{document}

Q2 :
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A2.} Let $\mathbb{R}$ be the set of real numbers. Let $f: \mathbb{R} \to \mathbb{R}$ be a function such that
\[
f(x + y) f(x - y) \ge f(x)^2 - f(y)^2
\]
for every $x, y \in \mathbb{R}$. Assume that the inequality is strict for some $x_0, y_0 \in \mathbb{R}$.
Prove that $f(x) \ge 0$ for every $x \in \mathbb{R}$ or $f(x) \le 0$ for every $x \in \mathbb{R}$.

\medskip
\noindent \textbf{Common remarks.} We will say that $f$ has constant sign, if $f$ satisfies the conclusion of the problem.

\medskip
\noindent \textbf{Solution 1.} We introduce the new variables $s := x + y$ and $t := x - y$. Equivalently, $x = \frac{s+t}{2}$ and $y = \frac{s-t}{2}$. The inequality becomes
\[
f(s) f(t) \ge f \left( \frac{s+t}{2} \right)^2 - f \left( \frac{s-t}{2} \right)^2
\]
for every $s, t \in \mathbb{R}$. We replace $t$ by $-t$ to obtain
\[
f(s) f(-t) \ge f \left( \frac{s-t}{2} \right)^2 - f \left( \frac{s+t}{2} \right)^2.
\]
Summing the previous two inequalities gives
\[
f(s) (f(t) + f(-t)) \ge 0
\]
for every $s, t \in \mathbb{R}$. This inequality is strict for $s = x_0 + y_0$ and $t = x_0 - y_0$ by assumption. In particular, there exists some $t_0 = x_0 - y_0$ for which $f(t_0) + f(-t_0) \ne 0$. Since $f(s) (f(t_0) + f(-t_0)) \ge 0$ for every $s \in \mathbb{R}$, we conclude that $f(s)$ must have constant sign.

\medskip
\noindent \textbf{Solution 2.} We do the same change of variables as in Solution 1 to obtain
\[
f(s) f(t) \ge f \left( \frac{s+t}{2} \right)^2 - f \left( \frac{s-t}{2} \right)^2. \tag{1}
\]
In this solution, we replace $s$ by $-s$ (instead of $t$ by $-t$). This gives
\[
f(-s) f(t) \ge f \left( \frac{-s+t}{2} \right)^2 - f \left( \frac{-s-t}{2} \right)^2. \tag{2}
\]

We now go back to the original inequality. Substituting $x = y$ gives $f(2x) f(0) \ge 0$ for every $x \in \mathbb{R}$. If $f(0) \ne 0$, then we conclude that $f$ indeed has constant sign. From now on, we will assume that
\[
f(0) = 0.
\]
Substituting $x = -y$ gives $f(-x)^2 \ge f(x)^2$. By permuting $x$ and $-x$, we conclude that
\[
f(-x)^2 = f(x)^2
\]
for every $x \in \mathbb{R}$.
Using the relation $f(x)^2 = f(-x)^2$, we can rewrite (2) as
\[
f(-s) f(t) \ge f \left( \frac{s-t}{2} \right)^2 - f \left( \frac{s+t}{2} \right)^2.
\]
Summing this inequality with (1), we obtain
\[
(f(s) + f(-s)) f(t) \ge 0
\]
for every $s, t \in \mathbb{R}$ and we can conclude as in Solution 1.

\end{document}

Q3 
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A3.} Let $x_1, x_2, \dots, x_{2023}$ be \textit{distinct} real positive numbers such that
\[
a_n = \sqrt{(x_1 + x_2 + \cdots + x_n) \left( \frac{1}{x_1} + \frac{1}{x_2} + \cdots + \frac{1}{x_n} \right)}
\]
is an integer for every $n = 1, 2, \dots, 2023$. Prove that $a_{2023} \ge 3034$.

\medskip
\noindent \textit{(Netherlands)}

\medskip
\noindent \textbf{Solution 1.} We start with some basic observations. First note that the sequence $a_1, a_2, \dots, a_{2023}$ is increasing and thus, since all elements are integers, $a_{n+1} - a_n \ge 1$. We also observe that $a_1 = 1$ and
\[
a_2 = \sqrt{(x_1 + x_2) \left( \frac{1}{x_1} + \frac{1}{x_2} \right)} > \sqrt{2 \sqrt{x_1 x_2} \cdot 2 \sqrt{\frac{1}{x_1 x_2}}} = 2
\]
by Cauchy-Schwarz inequality and using $x_1 \neq x_2$. So, $a_2 \ge 3$.

\medskip
Now, we proceed to the main part of the argument. We observe that 3034 is about three halves of 2023. Motivated by this observation, we will prove the following.
\medskip
\textbf{Claim.} \textit{If $a_{n+1} - a_n = 1$, then $a_{n+2} - a_{n+1} \ge 2$.}

\medskip
In other words, the sequence has to increase by at least 2 at least half of the times. Assuming the claim is true, since $a_1 = 1$, we would be done since
\begin{align*}
a_{2023} &= (a_{2023} - a_{2022}) + (a_{2022} - a_{2021}) + \cdots + (a_2 - a_1) + a_1 \\
&\ge (\underbrace{2 + 1 + 2 + 1 + \cdots + 2 + 1}_{2022 \text{ terms}}) + 1 \\
&= (2 + 1) \cdot 1011 + 1 \\
&= 3034.
\end{align*}

\medskip
We now prove the claim. We start by observing that
\begin{align*}
a_{n+1}^2 &= (x_1 + \cdots + x_{n+1}) \left( \frac{1}{x_1} + \cdots + \frac{1}{x_{n+1}} \right) \\
&= (x_1 + \cdots + x_n + x_{n+1}) \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} + \frac{1}{x_{n+1}} \right) \\
&= (x_1 + \cdots + x_n) \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right) + 1 + 1 + \frac{x_{n+1}}{x_1 + \cdots + x_n} + x_{n+1} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right) \\
&= a_n^2 + 2 + \frac{x_{n+1}}{x_1 + \cdots + x_n} + \frac{x_1 + \cdots + x_n}{x_1 \cdots x_n} \cdot x_{n+1} \left( \frac{x_2 \cdots x_n + x_1 x_3 \cdots x_n + \cdots + x_1 \cdots x_{n-1}}{x_1 \cdots x_n} \right) \\
&\ge a_n^2 + 2 + 2 \sqrt{\frac{x_{n+1}}{x_1 + \cdots + x_n} \cdot (x_1 + \cdots + x_n) \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right) \frac{1}{x_{n+1}}} \\
&= a_n^2 + 2 + 2 \sqrt{a_n^2} \\
&= a_n^2 + 2 + 2a_n \\
&= (a_n + 1)^2,
\end{align*}
where we used AM-GM to obtain the inequality. In particular, if $a_{n+1} = a_n + 1$, then
\[
\frac{x_{n+1}}{x_1 + \cdots + x_n} = \frac{1}{x_{n+1} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right)}. \tag{1}
\]

\medskip
Now, assume for the sake of contradiction that both $a_{n+1} = a_n + 1$ and $a_{n+2} = a_{n+1} + 1$ hold.
In this case, (1) gives
\[
\frac{x_{n+1}}{x_1 + \cdots + x_n} = \frac{1}{x_{n+1} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right)} = \frac{x_{n+2}}{x_1 + \cdots + x_{n+1}} = \frac{1}{x_{n+2} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_{n+1}} \right)}.
\]
We can rewrite this relation as
\[
\frac{\frac{1}{x_{n+1}}}{\frac{1}{x_{n+2}}} = \frac{x_{n+2}}{x_{n+1}} = \frac{x_1 + \cdots + x_n}{x_1 + \cdots + x_{n+1}} = \frac{x_{n+1} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_n} \right)}{x_{n+2} \left( \frac{1}{x_1} + \cdots + \frac{1}{x_{n+1}} \right)}.
\]
From (1) again, we conclude that $x_{n+1} = x_{n+2}$ which is a contradiction.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A4.} Let $\mathbb{R}_{>0}$ be the set of positive real numbers. Determine all functions $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ such that
\[
x(f(x) + f(y)) \ge (f(f(x)) + y) f(y)
\]
for every $x, y \in \mathbb{R}_{>0}$.

\medskip
\noindent \textit{(Belgium)}

\medskip
\noindent \textbf{Answer:} All functions $f(x) = \frac{c}{x}$ for some $c > 0$.

\medskip
\noindent \textbf{Solution 1.} Let $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ be a function that satisfies the inequality of the problem statement. We will write $f^k(x) = f(f(\cdots f(x)\cdots))$ for the composition of $f$ with itself $k$ times, with the convention that $f^0(x) = x$. Substituting $y = x$ gives
\[
x \ge f^2(x).
\]
Substituting $x = f(y)$ instead leads to $f(y) (f(f(y)) + f(y)) \ge (f(f(f(y))) + y) f(y)$, or equivalently
\[
f(y) + f^2(y) \ge f^3(y) + y,
\]
\[
f(y) - f^3(y) \ge y - f^2(y).
\]
We can generalise this inequality. If we replace $y$ by $f^{n-1}(y)$ in the above inequality, we get
\[
f^n(y) - f^{n+2}(y) \ge f^{n-1}(y) - f^{n+1}(y),
\]
for every $y \in \mathbb{R}_{>0}$ and for every integer $n \ge 1$. In particular, $f^n(y) - f^{n+2}(y) \ge y - f^2(y) \ge 0$ for every $n \ge 1$. Hereafter consider even integers $n = 2m$. Observe that
\[
y - f^{2m}(y) = \sum_{i=0}^{m-1} (f^{2i}(y) - f^{2i+2}(y)) \ge m(y - f^2(y)).
\]

\medskip
Since $f$ takes positive values, it holds that $y - f^{2m}(y) < y$ for every $m \ge 1$. So, we have proved that $y > m(y - f^2(y))$ for every $y \in \mathbb{R}_{>0}$ and every $m \ge 1$. Since $y>0$, this holds if only if
\[
y - f^2(y) \le 0.
\]
Combining this with $y \ge f^2(y)$, we conclude that
\[
f^2(y) = y
\]
for every $y \in \mathbb{R}_{>0}$. The original inequality becomes
\[
x f(x) \ge y f(y)
\]
for every $x, y \in \mathbb{R}_{>0}$. Hence, $x f(x)$ is constant. We conclude that $f(x) = \frac{c}{x}$ for some $c > 0$.
We now check that all the functions of the form $f(x) = \frac{c}{x}$ are indeed solutions of the original problem. First, note that all these functions satisfy $f(f(x)) = c/(c/x) = x$. So it's sufficient to check that $x f(x) \ge y f(y)$, which is true since $c \ge c$.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A5.} Let $a_1, a_2, \dots, a_{2023}$ be positive integers such that
\begin{itemize}
    \item $a_1, a_2, \dots, a_{2023}$ is a permutation of $1, 2, \dots, 2023$, and
    \item $|a_1 - a_2|, |a_2 - a_3|, \dots, |a_{2022} - a_{2023}|$ is a permutation of $1, 2, \dots, 2022$.
\end{itemize}
Prove that $\max(a_1, a_{2023}) \ge 507$.

\medskip
\noindent \textit{(Australia)}

\medskip
\noindent \textbf{Solution.} For the sake of clarity, we consider and prove the following generalisation of the original problem (which is the case $N = 1012$):

\medskip
\noindent \textbf{Let} $N$ be a positive integer and $a_1, a_2, \dots, a_{2N-1}$ be positive integers such that
\begin{itemize}
    \item $a_1, a_2, \dots, a_{2N-1}$ is a permutation of $1, 2, \dots, 2N-1$, and
    \item $|a_1 - a_2|, |a_2 - a_3|, \dots, |a_{2N-2} - a_{2N-1}|$ is a permutation of $1, 2, \dots, 2N-2$.
\end{itemize}
Then $a_1 + a_{2N-1} \ge N + 1$ and hence $\max(a_1, a_{2N-1}) \ge \left\lceil \frac{N+1}{2} \right\rceil$.

\medskip
Now we proceed to the proof of the generalised statement. We introduce the notion of \textit{score} of a number $a \in \{1, 2, \dots, 2N-1\}$. The score of $a$ is defined to be
\[
s(a) := |a - N|.
\]

\medskip
Note that, by the triangle inequality,
\[
|a - b| = |a - N + N - b| \le |a - N| + |N - b| = s(a) + s(b).
\]

\medskip
Considering the sum $|a_1 - a_2| + |a_2 - a_3| + \cdots + |a_{2N-2} - a_{2N-1}|$, we find that
\begin{align*}
(N-1)(2N-1) &= |a_1 - a_2| + |a_2 - a_3| + \cdots + |a_{2N-2} - a_{2N-1}| \\
&\le (s(a_1) + s(a_2)) + (s(a_2) + s(a_3)) + \cdots + (s(a_{2N-2}) + s(a_{2N-1})) \\
&= 2(s(a_1) + s(a_2) + \cdots + s(a_{2N-1})) - (s(a_1) + s(a_{2N-1})) \\
&= 2 \sum_{i=1}^{2N-1} s(a_i) - (s(a_1) + s(a_{2N-1})).
\end{align*}

\medskip
For the last equality we used that the numbers $s(a_1), s(a_2), \dots, s(a_{2N-1})$ are a permutation of $0, 1, 1, 2, 2, \dots, N-1, N-1$.
Hence, $\sum_{i=1}^{2N-1} s(a_i) = 2 \sum_{j=0}^{N-1} j = N(N-1)$. We conclude that
\[
(N-1)(2N-1) \le 2N(N-1) - (s(a_1) + s(a_{2N-1})) = 2N(N-1) - (|a_1 - N| + |a_{2N-1} - N|).
\]
\[
(|a_1 - N| + |a_{2N-1} - N|) \le 2N(N-1) - (N-1)(2N-1) = (N-1)(2N - (2N-1)) = N-1,
\]
\[
(N - a_1) + (N - a_{2N-1}) \le |N - a_1| + |N - a_{2N-1}| = |a_1 - N| + |a_{2N-1} - N| \le N - 1,
\]
\[
2N - (a_1 + a_{2N-1}) \le N - 1,
\]
which implies $a_1 + a_{2N-1} \ge N + 1$.

\medskip
\noindent \textbf{Comment 1.} In the case $N = 1012$, such a sequence with $\max(a_1, a_{2023}) = 507$ indeed exists:
\[
507, 1517, 508, 1516, \dots, 1011, 1013, 1012, 2023, 1, 2022, 2, \dots, 1518, 506.
\]

\medskip
For a general even number $N$, a sequence with $\max(a_1, a_{2N-1}) = \left\lceil \frac{N+1}{2} \right\rceil = \frac{N+2}{2}$ can be obtained similarly. If $N \ge 3$ is odd, the inequality is not sharp, because $\max(a_1, a_{2N-1}) = \frac{N+1}{2}$ and $a_1 + a_{2N-1} \ge N+1$ together imply $a_1 = a_{2N-1} = \frac{N+1}{2}$, a contradiction.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{A6.} Let $k \ge 2$ be an integer. Determine all sequences of positive integers $a_1, a_2, \dots$ for which there exists a monic polynomial $P$ of degree $k$ with non-negative integer coefficients such that
\[
P(a_n) = a_{n+1} + a_{n+2} + \cdots + a_{n+k}
\]
for every integer $n \ge 1$.

\medskip
\noindent \textit{(Malaysia)}

\medskip
\noindent \textbf{Answer:} The sequence $(a_n)$ must be an arithmetic progression consisting of positive integers with common difference $d \ge 0$, and $P(x) = (x + d) \cdots (x + kd)$.

\medskip
\noindent \textbf{Common remarks.} The following arguments and observations are implicit in the solutions given below.

\medskip
Suppose the sequence $(a_n)$ is an arithmetic progression with common difference $d \ge 0$. Then it satisfies the condition with
\[
P(x) = (x + d) \cdots (x + kd).
\]

\medskip
This settles one direction. Now suppose $(a_n)$ is a sequence satisfying the condition. We will show that it is a non-decreasing arithmetic progression.
Since $P(x)$ has non-negative integer coefficients, it is strictly increasing on the positive real line. In particular, it holds that, for any positive integers $x, y$,
\[
P(x) < P(y) \iff x < y.
\]

\medskip
Furthermore, if the sequence $(a_n)$ is eventually constant, then $P(x) = x^k$ and the sequence $(a_n)$ is actually constant. Indeed, if $P(x)$ were not the polynomial $x^k$, then $P(a_n) = a_{n+1} + \cdots + a_{n+k}$ cannot be satisfied for $n$ such that $a_n = \cdots = a_{n+k}$. By a descending induction, we conclude that $(a_n)$ is constant. Thus we can restrict to the case $(a_n)$ is not eventually constant.

\medskip
\noindent \textbf{Solution 1.} We assume that $(a_n)$ is not eventually constant.

\medskip
\noindent \textbf{Step 1.} The first goal is to show that the sequence must be increasing, i.e. $a_n < a_{n+1}$ for all $n \ge 1$.

\medskip
First, by comparing the two equalities
\begin{align*}
P(a_n) &= a_{n+1} + a_{n+2} + \cdots + a_{n+k}, \\
P(a_{n+1}) &= a_{n+2} + a_{n+3} + \cdots + a_{n+k+1},
\end{align*}
we observe that
\begin{align*}
a_n < a_{n+1} &\implies P(a_n) < P(a_{n+1}) \implies a_{n+1} + \cdots + a_{n+k} < a_{n+2} + \cdots + a_{n+k+1} \implies a_{n+1} < a_{n+k+1}; \tag{1}\\
a_n > a_{n+1} &\implies P(a_n) > P(a_{n+1}) \implies a_{n+1} + \cdots + a_{n+k} > a_{n+2} + \cdots + a_{n+k+1} \implies a_{n+1} > a_{n+k+1}; \tag{2}\\
a_n = a_{n+1} &\implies P(a_n) = P(a_{n+1}) \implies a_{n+1} + \cdots + a_{n+k} = a_{n+2} + \cdots + a_{n+k+1} \implies a_{n+1} = a_{n+k+1}. \tag{3}
\end{align*}

\medskip
\noindent \textbf{Claim 1.} $a_n \le a_{n+1}$ for all $n \ge 1$.

\medskip
\noindent \textit{Proof.} Suppose, to the contrary, that $a_{n(0)} > a_{n(0)+1}$ for some $n(0) \ge 2$. We will give an infinite descending sequence of positive integers $a_{n(0)} > a_{n(1)} > a_{n(2)} > \cdots$ (absurd).

\medskip
Then $a_{n(0)} > a_{n(0)+1}$ implies by (2) that $a_{n(0)+1} > a_{n(0)+k+1}$. We construct such a sequence inductively. If we have chosen $n(i)$, then we let $n(i+1) = n(i) + k$. Note that such an index always exists since if $n(i+1)$ were not the smallest index larger than $n(i)$ such that $a_{n(i+1)} > a_{n(i+1)+1}$, then we always need to check that $n(i+1) \le n(i)+k$.  Because $a_{n(i)} > a_{n(i)+1}$, by (2), $a_{n(i)+1} > a_{n(i)+k+1}$. This is immediate if $n(i+1) = n(i)+k+1 = n(i) + k + 1$ by construction. If $n(i+1) \ge n(i) + 2$, then $a_{n(i)+1} \ge a_{n(i)+2} \ge \cdots \ge a_{n(i)+k}$. By minimality of $n(i+1)$, and so $a_{n(i)+1} > a_{n(i+1)}$.
Hence $a_{n(i)} > a_{n(i+1)}$. $\Box$

\vspace{1cm}
\hrulefill \textit{Chiba, Japan, 2nd-13th July 2023} \hrulefill
\vspace{1cm}

\noindent 24

\noindent We are now ready to prove that the sequence $a_n$ is increasing. Suppose $a_n = a_{n+1}$ for some $n \ge 1$. Then we also have $a_n = a_{n+1} = \cdots = a_{n+k+1}$ by (3), and since the sequence is non-decreasing we have $a_{n} = a_{n+1} = a_{n+2} = \cdots $. But that contradicts our assumption. Hence $a_n < a_{n+1}$ for all $n \ge 1$.

\medskip
\noindent \textbf{Step 2.} The next and final goal is to prove that the sequence $a_n$ is an arithmetic progression.
Observe that we can make differences of terms appear as follows:
\begin{align*}
P(x) &= a_{n+1} + a_{n+2} + \cdots + a_{n+k} \\
&= (a_{n+1} - a_n) + (a_{n+2} - a_n) + \cdots + (a_{n+k} - a_n) + k a_n \\
&= (a_{n+1} - a_n) + (a_{n+2} - a_{n+1} + a_{n+1} - a_n) + \cdots + (a_{n+k} - a_{n+k-1} + \cdots + a_{n+1} - a_n) + k a_n.
\end{align*}
We will prove that, for $n$ large enough, the sum
\[
(a_{n+1} - a_n) + (a_{n+2} - a_n) + \cdots + (a_{n+k} - a_n)
\]
is equal to the coefficient $b$ of the term $x^{k-1}$ in $P$. The argument is based on the following claim.

\medskip
\noindent \textbf{Claim 2.} There exists a bound $A$ with the following properties:
\begin{enumerate}
    \item If $(c_1, \dots, c_k)$ is a $k$-tuple of positive integers with $c_1 + \cdots + c_k > b$, then for every $x > A$ we have $P(x) < (x + c_1) (x + c_2) \cdots (x + c_k)$.
    \item If $(c_1, \dots, c_k)$ is a $k$-tuple of positive integers with $c_1 + \cdots + c_k < b$, then for every $x > A$ we have $P(x) > (x + c_1) (x + c_2) \cdots (x + c_k)$.
\end{enumerate}

\medskip
\noindent \textit{Proof.} It suffices to show parts 1 and 2 separately, because then we can take the maximum of two bounds.

\medskip
We first show part 1. For each single $(c_1, \dots, c_k)$ such a bound $A$ exists since
\[
P(x) - (x + c_1) (x + c_2) \cdots (x + c_k) = (b - (c_1 + \cdots + c_k)) x^{k-1} + (\text{terms of degree} \le k-2)
\]
has negative leading coefficient and hence takes negative values for $x$ large enough.

Suppose $A$ is a common bound for all tuples $c = (c_1, \dots, c_k)$ satisfying $c_1 + \cdots + c_k = b+1$ (note that there are only finitely many such tuples). Then, for any tuple $c' = (c'_1, \dots, c'_k)$ with $c'_1 + \cdots + c'_k > b$, there exists a tuple $c = (c_1, \dots, c_k)$ with $c_1 + \cdots + c_k = b+1$ and $c'_i \ge c_i$, and then the inequality for $c'$ follows from the inequality for $c$.

We can show part 2 either in a similar way, or by using that there are only finitely many such tuples. $\Box$

\medskip
Take $A$ satisfying the assertion of Claim 2, and take $N$ such that $n \ge N$ implies $a_n > A$. Then for every $n \ge N$, we have
\[
P(a_n) = (a_{n+1} - a_n) + (a_{n+2} - a_n) + \cdots + (a_{n+k} - a_n) = b.
\]
By taking the difference of this equality and the equality for $n+1$, we obtain
\[
a_{n+k+1} - a_{n+1} = k(a_{n+1} - a_n)
\]
for every $n \ge N$.

\medskip
We conclude using an extremal principle. Let $d = \min\{a_{n+1} - a_n \mid n \ge N\}$, and suppose it is attained at some index $n \ge N$. Since
\[
kd = k(a_{n+1} - a_n) = a_{n+k+1} - a_{n+1} = \sum_{i=n+2}^{n+k+1} (a_i - a_{i-1}) \ge kd,
\]
and each summand is at least $d$, we conclude that $d$ is also attained at $n+1, \dots, n+k$. And inductively at all $n' \ge n$. We see that the equation $P(x) = (x + d)(x + 2d) \cdots (x + kd)$ is true for infinitely many values of $x$ (all $a_{n'}$ for $n' \ge n$), hence this is an equality of polynomials. Finally we use (backward) induction to show that $a_{n+1} - a_n = d$ for every $n \ge 1$.

\end{document}
\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\newtheorem{claim}{Claim}
\usepackage{lipsum}

\begin{document}

\noindent \textbf{A7.} Let $N$ be a positive integer. Prove that there exist three permutations $a_1, a_2, \dots, a_N$; $b_1, b_2, \dots, b_n$; and $c_1, c_2, \dots, c_N$ of $1, 2, \dots, N$ such that
\[
|\sqrt{a_k} + \sqrt{b_k} + \sqrt{c_k} - 2\sqrt{N}| < 2023
\]
for every $k = 1, 2, \dots, N$.

\medskip
\noindent \textit{(China)}

\medskip
\noindent \textbf{Solution 1.} The idea is to approximate the numbers $\sqrt{1}, \sqrt{2}, \dots, \sqrt{N}$ by the nearest integer with errors $< 0.5$. This gives the following sequence
\[
1, 1, 2, 2, 2, 3, 3, 3, 3, 4, \dots
\]
More precisely, for each $k \ge 1$, we round $\sqrt{k^2 - k + 1}, \dots, \sqrt{k^2 + k}$ to $k$, so that there are $2k$ copies of $k$.

\medskip
\noindent \textbf{Step 1.} We first consider the easier case when $N$ has the form
\[
N = m(m+1).
\]
In this case, the numbers $\sqrt{1}, \sqrt{2}, \dots, \sqrt{N}$ are approximated by the elements of the multiset $\{ \underbrace{1, 1}_{2 \cdot 1}, \underbrace{2, 2, 2, 2}_{2 \cdot 2}, \dots, \underbrace{m, \dots, m}_{2 \cdot m} \}$. Let $T_m$ denote ``half'' of the multiset, i.e.
\[
T_m := \{ \underbrace{1, 1}_{2}, \underbrace{2, 2}_{2}, \underbrace{3, 3}_{2}, \dots, \underbrace{m, m}_{2} \}.
\]

\medskip
We will prove by induction that there exists three permutations $(u_k)$, $(v_k)$, and $(w_k)$ of the elements in the multiset $T_m$ such that $u_k + v_k + w_k = 2m + 1$ is constant for $k = 1, 2, \dots, \frac{m(m+1)}{2}$.
When $m = 1$, take $T_1 = \{1, 1\}$. Then take permutations $(u_k) = (1, 1)$, $(v_k) = (1, 1)$ and $(w_k) = (1, 1)$. Suppose that we have constructed three permutations $(u_k), (v_k)$, and $(w_k)$ of $T_{m-1}$ satisfying $u_k + v_k + w_k = 2(m-1) + 1 = 2m - 1$ for every $k = 1, 2, \dots, \frac{(m-1)m}{2}$. For $T_m$, we note that
\[
T_m = T_{m-1} \sqcup \{m\} \sqcup \{m\}.
\]
and also
\begin{equation}
T_m = (T_{m-1} + 1) \sqcup \{1, 2, \dots, m\}. \tag{1}
\end{equation}
Here $T_{m-1} + 1$ means to add 1 to all elements in $T_{m-1}$. We construct the permutations $(u'_k), (v'_k)$, and $(w'_k)$ of $T_m$ as follows:
\begin{itemize}
    \item For $k = 1, 2, \dots, \frac{m(m-1)}{2}$, we set $u'_k = u_k + 1$, $v'_k = v_k + 1$, $w'_k = w_k + 1$.
    \item For $k = \frac{m(m-1)}{2} + r$ with $r = 1, 2, \dots, m$, we set $u'_k = m$, $v'_k = r$, $w'_k = m + 1 - r$.
\end{itemize}
It is clear from (1) that $(u'_k), (v'_k)$, and $(w'_k)$ give three permutations of $T_m$, and that they satisfy $u'_k + v'_k + w'_k = 2m + 1$ for every $k = 1, 2, \dots, \frac{m(m+1)}{2}$.
The inductive construction can be visualised by the $3 \times \frac{m(m+1)}{2}$ matrix
\[
\begin{bmatrix}
    u'_1 & \cdots & u'_{\frac{m(m-1)}{2}} & u'_{\frac{m(m-1)}{2} + 1} & \cdots & u'_{\frac{m(m+1)}{2}} \\
    v'_1 & \cdots & v'_{\frac{m(m-1)}{2}} & v'_{\frac{m(m-1)}{2} + 1} & \cdots & v'_{\frac{m(m+1)}{2}} \\
    w'_1 & \cdots & w'_{\frac{m(m-1)}{2}} & w'_{\frac{m(m-1)}{2} + 1} & \cdots & w'_{\frac{m(m+1)}{2}}
\end{bmatrix} =
\begin{bmatrix}
    u_1+1 & \cdots & u_{\frac{(m-1)m}{2}}+1 & m & \cdots & m \\
    v_1+1 & \cdots & v_{\frac{(m-1)m}{2}}+1 & 1 & \cdots & m \\
    w_1+1 & \cdots & w_{\frac{(m-1)m}{2}}+1 & m & \cdots & 1
\end{bmatrix}
\]
in which the three rows represent the permutations $(u'_k), (v'_k), (w'_k)$, and the sum of the three entries of each column is $2m + 1$.

\vspace{1cm}
\hrulefill \textit{Chiba, Japan, 2nd-13th July 2023} \hrulefill
\vspace{1cm}

\noindent 28

\noindent Thus, when $N = m^2 + m$, we can construct permutations $(u_k)$, $(v_k)$, and $(c_k)$ of $1, 2, \dots, N$ such that
\begin{equation}
2m + 1 - 1.5 < \sqrt{u_k} + \sqrt{v_k} + \sqrt{c_k} < 2m + 1 + 1.5. \tag{2}
\end{equation}
This gives
\[
\sqrt{u_k} + \sqrt{v_k} + \sqrt{c_k} - 2\sqrt{N} < 2m + 1 + 1.5 - 2 \sqrt{m^2 + m} = 2m + 1.5 - 2m \sqrt{1 + \frac{1}{m}}
\]
Using $\sqrt{1 + x} \ge 1 + \frac{x}{2} - \frac{x^2}{8}$ for $x \ge 0$ for $x = \frac{1}{m}$ we have
\begin{align*}
\sqrt{u_k} + \sqrt{v_k} + \sqrt{c_k} - 2\sqrt{N} &< 2m + 1.5 - 2m \left( 1 + \frac{1}{2m} - \frac{1}{8m^2} \right) \\
&= 2m + 1.5 - 2m - 1 + \frac{1}{4m} = 0.5 + \frac{1}{4m} < 2.5 < 2023.
\end{align*}
where we used that $-1 < 2m - 2m \sqrt{1 + \frac{1}{m}} < 0$ for positive $m$.

\medskip
\noindent \textbf{Step 2.} We now proceed to the general case. Let $m$ be such that
\[
m(m+1) \le N < (m+1)(m+2).
\]
Write $N = m(m+1) + t$ for some $t \in \{0, 1, \dots, 2m + 1\}$ and let
\[
L := \left\lfloor \frac{4N}{9} \right\rfloor.
\]
We will make use of the following inequalities below:
\[
N > m^2, \quad N < (m+2)^2, \quad t \le 2m+1, \quad L + 1 > 4N/9, \quad L \le 4N/9.
\]
As above, we construct three permutations $(u_k), (v_k), (w_k)$ of $\{1, 2, \dots, m(m+1)\}$ satisfying (2). Now we construct the three required permutations $(A_k), (B_k)$, and $(C_k)$ of $\{1, 2, \dots, N\}$ as follows:

\medskip
For $k = 1, 2, \dots, m(m+1)$, if $a_k \le L$, take $A_k = a_k$, and if $a_k > L$, take $A_k = a_k + t$. For $k = m(m+1) + r$ with $r = 1, 2, \dots, t$, set $A_k = L + r$. Define the permutations $(B_k)$ and $(C_k)$ similarly. Now for $k = 1, 2, \dots, m(m+1)$, we show $0 \le \sqrt{A_k} - \sqrt{u_k} \le 2$. The lower bound is obvious. If $u_k \le L$, then $N \le 5$ and hence $\sqrt{A_k} - \sqrt{u_k} = \sqrt{u_k} - \sqrt{u_k} = 0 < 2$. If $u_k \ge 2$, then
\[
\sqrt{A_k} - \sqrt{u_k} = \sqrt{u_k + t} - \sqrt{u_k} = \frac{t}{\sqrt{u_k + t} + \sqrt{u_k}} \le \frac{t}{2\sqrt{L}} \le \frac{2m+1}{2\sqrt{4N/9}} \le \frac{3(2m+1)}{4\sqrt{N}} \le \frac{3}{2\sqrt{m}} \le 2.
\]
We have similar inequalities for $(B_k)$ and $(C_k)$. Thus
\begin{align*}
2\sqrt{N} - 4.5 &< 2m + 1 - 1.5 \le \sqrt{A_k} + \sqrt{B_k} + \sqrt{C_k} \le 2m + 1 + 1.5 + 6 \le 2\sqrt{N} + 8.5.
\end{align*}
For $k = m^2 + m + 1, \dots, m^2 + m + t$, we have
\[
2\sqrt{N} < 3\sqrt{L} + t < \sqrt{A_k} + \sqrt{B_k} + \sqrt{C_k} \le 3\sqrt{L+t} \le \sqrt{4N+9} < 2\sqrt{N} + 8.5.
\]

\medskip
To sum up, we have defined three permutations $(A_k), (B_k)$, and $(C_k)$ of $1, 2, \dots, N$, such that
\[
|\sqrt{A_k} + \sqrt{B_k} + \sqrt{C_k} - 2\sqrt{N}| < 8.5 < 2023.
\]
holds for every $k = 1, 2, \dots, N$.

\end{document}

"""
