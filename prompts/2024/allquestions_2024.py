def allquestions_2024():
    return r"""

\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{Problem 1}

Three airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?

\textbf{Answer:} 79

\textbf{Solution:} The airlines are called A100, A120 and A150, labelled by the frequency of their departures. We first prove that there is a period of 99 days after an A100 departure during which no A150 plane takes off.

Consider a period of 301 days which starts with an A150 departure on Day 0, followed by a departure on Day 150 and on Day 300. Let the first A100 departure in this period be on Day $x$.

There are two possibilities: (i) $0 \le x \le 50$ or (ii) $51 \le x \le 99$. In case (i), there is a quiet period of 99 days after the first A100 departure. In case (ii), the second A100 departure will be on Day $100+x$ where $151 \le 100+x \le 199$ so there will be a period of 99 consecutive days after the second A100 departure with no A150 departure.

We will now prove that there are 79 consecutive days on which no departure of any airline happens, including the A120 planes. We restart time and define Day 0 to be when an A100 flight departs and there is no A150 flight before Day 100. This situation will repeat later because $300 = 3 \times 100 = 2 \times 150$. The fourth A100 flight will take off on Day 300 and there will be no subsequent departure of an A150 plane before Day 400.

Suppose the first departure of an A120 plane is on Day $y$. If $y \le 20$ or $y \ge 80$, we have found the 79 consecutive days by looking after or before this A120 departure.

If $20 \le y \le 60$, then there will be an A120 departure on day $240 + y$ where $260 \le 240 + y \le 300$ so there will be no A120 departure strictly between Day 300 and Day 380 and so we will find the required 79 consecutive quiet days between those dates.

Finally, if $61 \le y \le 80$, there will be an A120 departure on Day $y+240$ where $301 \le y+240 \le 320$ and there will be no subsequent departures before Day 400 and again we find the required 79 consecutive quiet days.

We now show that this bound can be attained. Suppose that an A100 departs on Day 0, an A120 departs on Day 80 and an A150 departs on Day 120. The departure days are then:

0, 80, 100, 120, 200\&200, 270, 300, 320, 400, 420, 440, 500, 560, 570

modulo 600 (i.e. it repeats every 600 days).

The longest run of consecutive days without flights is 79 days (and this is obtained three times in this 600 day cycle).

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 2}

Let $ABC$ be a triangle with $BC=108$, $CA=126$, and $AB=39$. Point $X$ lies on segment $AC$ such that $BX$ bisects $\angle CBA$. Let $\omega$ be the circumcircle of triangle $ABX$. Let $Y$ be a point on $\omega$ different from $X$ such that $CX = CY$. Line $XY$ meets $BC$ at $E$. The length of the segment $BE$ can be written as $\frac{m}{n}$, where $m$ and $n$ are coprime positive integers. Find $m+n$.

\textbf{Answer:} 751

\textbf{Solution:} We have the key claim: $\omega$ is tangent to $BC$.

\textbf{Proof of Claim:} The angle bisector theorem gives $\frac{CX}{CA} = \frac{CB}{CB+BA}$ which rearranges to
\[
CX = \frac{AC \cdot BC}{AB+BC} = \frac{126 \times 108}{147} = \frac{6 \times 108}{7} = \frac{648}{7}.
\]
Now calculate: $CB^2 = 108^2 = \frac{648}{7} \times 126 = CX \cdot CA$ and we establish the required tangency by the converse of power of point (the tangent-secant theorem) applied to $C$ and $\omega$. $\Box$


\vspace{1em}

Having established this tangency, we now perform a short calculation.

Let $\Gamma$ denote the circle with centre $C$ and radius $CX$ which passes through $Y$. The point $E$ is on the radical axis $XY$ of $\omega$ and $\Gamma$. It follows that $E$ has equal powers with respect to both circles $\omega$ and $\Gamma$.

Let $x = BE$ so $EC = 108-x$. The power of $E$ with respect to $\omega$ is $x^2$ (because of the tangency at $B$) and the power of $E$ with respect to $\Gamma$ is $EC^2 - XC^2$ because $C$ is the centre of $\Gamma$ and $XC$ is its radius.

We have
\[
x^2 = (108-x)^2 - \left(\frac{648}{7}\right)^2.
\]
The quadratic terms cancel so $216x = 108^2 - \frac{648^2}{49} = \frac{49 \times 108^2 - 648^2}{49}$ and this gives the solution $x = \frac{702}{49}$.

Now, 702 and 49 are coprime so $m+n = 751$ is the required answer.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{tikz}

\begin{document}

\textbf{Problem 3}

Triangle $ABC$ has side length $AB = 120$ and circumradius $R = 100$. Let $D$ be the foot of the perpendicular from $C$ to the line $AB$. What is the greatest possible length of segment $CD$?

\textbf{Answer:} 180

\textbf{Solution:} Let $O$ be the circumcentre of triangle $ABC$. Then
\[
\text{dist}(O, AB) = \sqrt{R^2 - (AB/2)^2} = \sqrt{100^2 - 60^2} = \sqrt{10000 - 3600} = \sqrt{6400} = 80
\]
by Pythagoras.

\begin{center}
\begin{tikzpicture}[scale=0.6]
  \coordinate (O) at (0,0);
  \draw (O) circle (5);
  \node at (0.2,0.2) {$O$};
  \coordinate (A) at (-3,4);
  \coordinate (B) at (-3,-4);
  \coordinate (C) at (5,0);
  \coordinate (D) at (-3,0);
  \draw (A)--(B)--(C)--cycle;
  \draw (C)--(D);
  \node at (-3.3,4.2) {$A$};
  \node at (-3.3,-4.2) {$B$};
  \node at (5.2,0.2) {$C$};
  \node at (-3.3,0.2) {$D$};
    \draw[dashed] (A)--(O)--(C);
     \node at (2.5,1.2) {$100$};
    \draw[dashed] (O)--(B);
     \node at (-1.5,2.2) {$80$};

  \draw[dashed] (O)--(A);

  \node at (-2.7,3.7) {$90^\circ$};
  \draw (-3.1, -0.2) rectangle (-2.9, 0.2);
\end{tikzpicture}
\end{center}

Since $C$ must be on the circle with centre $O$ and radius $OA$, the largest possible altitude $h_c$ is attained when $C$ is the mid-point of the larger arc $AB$ of the circumcircle (i.e. on the perpendicular bisector of $AB$) in which case we have $h_c = \text{dist}(O, AB) + R = 80 + 100 = 180$.

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 4}

Find the three-digit number $n$ such that writing any other three-digit number $10^{1024}$ times in a row and $10^{2024} + 2$ times in a row results in two numbers divisible by $n$.

\textbf{Answer:} 143

\textbf{Solution:} Let $M = 10^{1024}$. Let $a$ be any three-digit number. Writing $M$ copies of $a$ in a row results in a number $X$ where
\[
X = a \times 100100100\dots1001001
\]
and there are $M$ copies of the digit one in the long number. If instead we wrote $M+2$ copies of $a$ in a row, the resulting number would be $10^6 X + 1001a$. We use the notation $(u,v)$ to denote the greatest common divisor of two integers $u$ and $v$ which are not both 0.

We apply Euclid's algorithm so
\[
((10^6 X + 1001a), X) = (1001a, X).
\]
It is therefore a necessary condition that our three-digit number $n$ should divide $(1001a, X)$ for all three-digit numbers $a$. By considering $a = 100$ and $a=101$, we see that any candidate for $n$ must divide $1001 \times 101 - 1001 \times 100 = 1001$. Moreover, if $n$ is a divisor of 1001, then $n$ will divide $X$ because 1001 divides $10010010010\dots01001001$ which is
\[
1001 \times 1000001000010\dots01000001.
\]
The second factor involves $M/2$ copies of the digit one. Such an $n$ will also divide $10^6 X + 1001a$.

Thus it is a necessary and sufficient condition for $n$ to satisfy the conditions of the problem that $n$ be a three-digit divisor of 1001 ($= 7 \times 11 \times 13$). There is a unique such number: 143.

\end{document}








\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 5}

Alice writes all positive integers from 1 to $n$ on the board for some positive integer $n \ge 11$. Bob then erases ten of them. The mean of the remaining numbers is $3000/37$. The sum of the numbers Bob erased is $S$. What is the remainder when $n \times S$ is divided by 997?

\textbf{Answer:} 902

\textbf{Solution:} Let $T$ be the sum of the numbers, after Bob has erased 10 of them. We can bound $T$ by considering what happens if Bob happens to erase the smallest ten numbers, or the largest ten numbers.

The average of the set $\{1, 2, \dots, n-10\}$ is $\frac{n-9}{2}$ (the average of the first and last terms of a finite arithmetic progression). Similarly, average of the set $\{11, 12, \dots, n\}$ is $\frac{n+11}{2}$. The average of the remaining numbers, $\frac{3000}{37} = \frac{T}{n-10}$, must be bounded by these quantities, so
\[
\frac{n-9}{2} \le \frac{T}{n-10} = \frac{3000}{37} \le \frac{n+11}{2}.
\]
It follows that $n-10$ must be a multiple of 37 so that it can cancel down to 37. Another way to say that is $n \equiv 10 \pmod{37}$. Multiplying the inequalities by 2 we obtain
\[
n-9 \le \frac{6000}{37} \le n+11
\]
or rather
\[
\frac{6000}{37} - 11 \le n \le \frac{6000}{37} + 9.
\]
Now $6000/37 = 162 + \frac{6}{37}$ so
\[
152 \le n \le 171.
\]
The only integer in this range which is 10 modulo 37 is 158, so $n=158$ and
\[
T = (n-10) \times \frac{3000}{37} = \frac{148 \times 3000}{37} = 4 \times 3000 = 12000.
\]
Let the sum of the numbers erased by Bob be $S$, so
\[
S = \left(\sum_{i=1}^{158} i\right) - 12000 = \frac{158 \times 159}{2} - 12000 = 12561 - 12000 = 561.
\]
Bob can achieve this by erasing $\{51, 52, \dots, 59, 66\}$.

The number that we must report is $n \times S$ modulo 997, which is $158 \times 561$ modulo 997, which is 902.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 6}

For positive integers $x_1, \dots, x_n$ define $G(x_1, \dots, x_n)$ to be the sum of their $\binom{n}{2}$ pairwise greatest common divisors. We say that an integer $n \ge 2$ is \textit{artificial} if there exist $n$ different positive integers $a_1, \dots, a_n$ such that
\[
a_1 + \dots + a_n = G(a_1, \dots, a_n) + 1.
\]
Find the sum of all artificial integers $m$ in the range $2 \le m \le 40$.

\textbf{Answer:} 810

\textbf{Solution:} We will show that the smallest artificial number is 5, and that if $a$ is an artificial number, then so too is $a+1$. This will solve the problem.

First, we eliminate small cases. If $n=2$ and the different positive integers are $a, b$ with $a < b$. Then, $\gcd(a, b) \le a$ so $\gcd(a, b) + 1 \le a+1 \le b < a+b$.

Now suppose that $n=3$ and the different positive integers are $a < b < c$. Using round brackets to denote gcds, we have
\[
(a,b) + (b,c) + (c,a) \le 2a + b \le a + b + c - 2
\]
because $a \le c-2$. Therefore $G(a, b, c) + 1 < a+b+c$.

Next we tackle the case $n=4$, and let the positive integers be $a < b < c < d$. Now
\begin{align*}
G(a, b, c, d) + 1 &= [(a,b) + (b,c) + (c,d)] + [(a,c) + (a,d)] + [(b,d) + 1 \\
&= [(a,b) - a) + (b,c) - b) + (c,d) - c)] + [(a,c) + (a,d)] + (b,d) + 1 \\
&\le (b - a + c - b + d - c) + 2a + b + 1 \\
&= a + b + d + 1.
\end{align*}
Now $c \ge 3$ so
\[
G(a,b,c,d) + 1 \le a+b+c+d + (1-c) \le a+b+c+d - 2.
\]
Having eliminated small cases, we show that 5 is artificial. Consider the numbers 1, 2, 3, 4 and 6. Now
\[
G(1, 2, 3, 4, 6) = 1+1+1+1+1+2+2+1+3+2+1 = 16 = (1+2+3+4+6).
\]
Therefore 5 is artificial.

Now suppose that $m$ is an artificial positive integer witnessed by different positive integers $a_1, a_2, \dots, a_m$. For $1 \le i \le m$, let $b_i = ma_i$ and let $b_{m+1} = 1$. We will show that these $m+1$ different positive integers $b_i$ are witnesses to $m+1$ being artificial.

If $i,j \le m$, then $\gcd(b_i, b_j) = m \cdot \gcd(a_i, a_j)$ and $(b_i, b_{m+1}) = 1$ for $1 \le i \le m$. Therefore
\begin{align*}
G(b_1, b_2, \dots, b_{m+1}) &= G(b_1, b_2, \dots, b_m) + m \\
&= m \cdot G(a_1, a_2, \dots, a_m) + m \\
&= m(a_1 + a_2 + \dots + a_m - 1) + m \\
&= b_1 + b_2 + \dots + b_m \\
&= (b_1 + b_2 + \dots + b_{m+1}) - 1.
\end{align*}

Therefore $m$ is artificial for all $m \ge 5$ by induction. We must report
\[
5 + 6 + \dots + 40 = \frac{45 \times 36}{2} = 810.
\]

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 7}

We call a sequence $a_1, a_2, \dots$ of non-negative integers \textit{delightful} if there exists a positive integer $N$ such that for all $n > N$, $a_n = 0$, and for all $i \ge 1$, $a_i$ counts the number of multiples of $i$ in $a_1, a_2, \dots, a_N$. How many delightful sequences of non-negative integers are there?

\textbf{Answer:} 3

\textbf{Solution:} We claim the only such sequences are $(1, 0, 0, \dots)$, $(2, 1, 0, 0, \dots)$ and $(2, 2, 0, 0, \dots)$. Note that $a_1 = N$ because 1 divides each of the first $N$ terms. Hence if $N=1$, we necessarily have the sequence $(1, 0, 0, \dots)$, and that obeys the conditions.

Observe that if $1 \le i \le N$, then $a_i$ is at most $N$ because $a_i$ counts the size of a subset of $\{1, 2, \dots, N\}$. For each $1 \le i \le N$, if (for contradiction) $a_i = 0$, then $i$ divides $a_i$ and so $a_i \neq 0$, which is absurd. Therefore the first $N$ terms of the sequence are non-zero (including $a_N$), and all subsequent terms are 0 because if $i > N$, then $i$ cannot divide any of the first $N$ terms which are all non-zero and at most $N$. This means that a sequence satisfying the condition for some $N$ will only satisfy the condition for that particular $N$.

Next assume that $N > 1$. The term $a_{N-1}$ is positive and so there is an index $j$ in the range $1 \le j \le N$ such that $N-1$ divides $a_j$. However, for $1 \le i \le N$ each $a_i$ is at most $N$, so $N-1 \le a_j \le N$. In the case that $N=2$ this yields the second and third delightful sequences mentioned above, and proves that there are no others.

It remains to study the case $N > 2$. In that case, $N-1$ does not divide $N$ so, taking $j$ as above, we must have $a_j = N-1 (\neq 1)$. If (for contradiction) $a_N \ge 2$ there is an index $k$ with $1<k<N$ such that $a_k = N$, so $k$ divides all non-zero terms of the sequence, and in particular $k$ divides both $N-1$ and $N$ and so must be 1, which is absurd. Finally suppose (for contradiction) that $a_N=1$. In that case, $j$ (recall that $a_j = N-1 > 1$ so $2 \le j \le N-1$) does not divide $a_N$ but $j$ does divide all previous terms of the sequence. Therefore $j$ divides $a_1$ which is $N$ and $a_j$ which is $N-1$ so $j=1$. Therefore, $a_1$ is both $N-1$ and $N$, which is absurd.

Thus, there are no delightful sequences with $N > 2$. There are exactly the 3 delightful sequences mentioned above so we report the answer 3.

\end{document}  








\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 8}

Fred and George take part in a tennis tournament with 4046 other players. In each round, the players are paired into 2024 matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \textit{different} if there is a player with a different opponent in the two arrangements.)

\textbf{Answer:} 250

\textbf{Solution:} Consider an tournament with $2m$ players. The number of possible first round pairings can be calculated by labelling the matches $1$ to $m$. Label the players in order 1 to $2m$ (this can be done in $(2m)!$ ways), and assign players $(2i-1)$ and $2i$ to match number $i$.

How many times does any given particular first round pairing arise from the method specified above? Swapping the labels of any pair $2i-1, 2i$ does not change the pairings, nor does permuting the order of the labels of the matches. Doing anything else will result in a different first round pairing, so $(2m)!$ is overcounting the number of first round pairings is by a factor of $2^m(m!)$.

Therefore the number of first round pairings is
\[
\frac{(2m)!}{2^m m!}
\]
Now consider the odd and even factors in the product defining $(2m)!$ separately. We see that
\[
(2m)! = [(2m) \cdot (2m-2) \cdots 2] \times [(2m-1) \cdot (2m-3) \cdots 3 \cdot 1].
\]
The product of the odd numbers $(2m-1) \cdot (2m-3) \cdots 3 \cdot 1$ is often written as $(2m-1)!!$. Pulling factors of 2 out of the even factors we obtain
\[
(2m)! = 2^m \cdot m! \cdot (2m-1)!!.
\]
Therefore the number of different first round pairings is
\[
\frac{(2m)!}{2^m \cdot m!} = (2m-1)!!.
\]
The number of first round pairings of the $4048 = 2n+2$ players where Fred and George do not play each other is the total number of pairings minus the number of pairings in which they play each other. This is $(2n+1)!! - (2n-1)!! = 2n(2n-1)!! = 4046 \cdot 4045!!$. This number is clearly divisible by 125 because of the large number of factors of 5 in $4045!!$. We would like to know the remainder when $4046 \cdot 4045!!$ is divided by 8, because then we could apply the Chinese Remainder Theorem and deduce the remainder on division by 1000. Note that $4045 \times 4043 \times 4041 \equiv 5 \times 3 \times 1 \equiv -1 \pmod 8$. The sequence of odd positive integers has period 4 modulo 8, and $4039 \equiv 7 \pmod 8$. Notice that $1 \times 3 \times 5 \times 7 \equiv 1 \pmod 8$. Running the sequence of odd numbers from 1 to 4039 cycles through a whole number of periods modulo 8 and so $4039!! \equiv 1 \pmod 8$. Now $4046 \cdot 4045!! \equiv 6 \times (-1) \times 1 \equiv 2 \pmod 8$.

By the Chinese remainder theorem there is a unique integer $x$ in the range $0 \le x \le 999$ which satisfies our conditions modulo 8 and modulo 125, and by inspection that is 250 and so
\[
4046 \cdot 4045!! \equiv 250 \pmod{1000}
\]
and we report 250.

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 9}

For a positive integer $n$, let $S(n)$ denote the sum of the digits of $n$ in base 10. Compute $S(S(1) + S(2) + \dots + S(N))$ with $N = 10^{100} - 2$.

\textbf{Answer:} 891

\textbf{Solution:} For each integer $k$ in the range $0 \le k \le 10^{100} - 1$ we have
\[
k + (10^{100} - k - 1) = 10^{100} - 1,
\]
which in decimal notation is a string of 100 nines. Deeming all numbers $k$ in the range to be decimal strings of 100 digits (including initial padding zeros when necessary), we see that for each $j$ in the range $1 \le j \le 100$, the $j$-th digit of $k$ and $j$-th digit of $10^{100} - 1 - k$ add up to 9.

Therefore for each integer $k$ in the range $0 \le k \le 10^{100} - 1$ we have $S(k) + S(10^{100} - 1 - k) = 900$.

Recall that $N = 10^{100} - 2$ and observe that $S(0) = 0$. Then
\[
2(S(0) + S(1) + S(2) + \dots + S(10^{100} - 1)) = 900 \times 10^{100}
\]
so
\[
S(1) + S(2) + \dots + S(N) = 450 \times (10^{100} - 1) - S(10^{100} - 1) = 450 \times 10^{100} - 900.
\]
In decimal notation, $450 \times 10^{100}$ is the string 45 followed by 101 zeros. Subtracting 900 gives the string 44 followed by 98 nines and then the digits 100.

The digit sum of this number is $4 + 4 + 98 \times 9 + 1 + 0 + 0 = 8 + 882 = 890 + 1= 891$. We report 891.

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{Problem 10}

The Fibonacci numbers are defined as follows: $F_0 = 0$, $F_1 = 1$, and $F_{n+1} = F_n + F_{n-1}$ for $n \ge 1$.
There are $N$ positive integers $n$ strictly less than $10^{101}$ such that $n^2 + (n+1)^2$ is a multiple of 5 but $F_{n-1}^2 + F_n^2$ is not. How many prime factors does $N$ have, counted with multiplicity?

\textbf{Answer:} 201

\textbf{Solution:} Checking modulo 5, we find that $n^2 + (n+1)^2 \equiv 0 \pmod 5$ if, and only if, $n$ is 1 or 3 modulo 5. On the other hand, the Fibonacci numbers modulo 5 form a sequence of period 20 and their squares form a sequence of period 10. By inspection $F_{n-1}^2 + F_n^2 \equiv 0 \pmod 5$ if, and only if, $n$ is 3 mod 5. Therefore we are being asked to find the number of positive integers $m$ in the range $1 \le m \le 10^{101}$ such that $m$ is 1 modulo 5. This is one fifth of the numbers in the range since $10^{101}$ is divisible by 5, so
\[
N = 10^{101} / 5 = 2 \times 10^{100} = 2^{101} \cdot 5^{100}.
\]
We therefore report $101 + 100 = 201$.

\end{document}






"""