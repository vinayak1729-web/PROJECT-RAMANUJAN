def combinators_prompt():
    return r"""
    \documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{Combinatorics}

\medskip
\noindent \textbf{C1.} The infinite sequence $a_0, a_1, a_2, \dots$ of (not necessarily different) integers has the following properties: $0 \le a_i \le i$ for all integers $i \ge 0$, and
\[
\binom{k}{a_0} + \binom{k}{a_1} + \cdots + \binom{k}{a_k} = 2^k
\]
for all integers $k \ge 0$.

\medskip
\noindent Prove that all integers $N \ge 0$ occur in the sequence (that is, for all $N \ge 0$, there exists $i \ge 0$ with $a_i = N$).

\medskip
\noindent \textit{(Netherlands)}

\medskip
\noindent \textbf{Solution.} We prove by induction on $k$ that every initial segment of the sequence, $a_0, a_1, \dots, a_k$, consists of the following elements (counted with multiplicity, and not necessarily in order), for some $\ell \ge 0$ with $2\ell \le k + 1$:
\[
0, 1, \dots, \ell-1, \quad 0, 1, \dots, k-\ell.
\]

\medskip
For $k = 0$ we have $a_0 = 0$, which is of this form. Now suppose that for $k = m$ the elements $a_0, a_1, \dots, a_m$ are $0, 0, 1, 1, 2, 2, \dots, \ell - 1, \ell - 1, \ell, \dots, m-\ell, m-\ell$ for some $\ell$ with $0 \le 2\ell \le m + 1$. It is given that
\[
\binom{m+1}{a_0} + \binom{m+1}{a_1} + \cdots + \binom{m+1}{a_m} + \binom{m+1}{a_{m+1}} = 2^{m+1},
\]
which becomes
\begin{align*}
\left( \binom{m+1}{0} + \binom{m+1}{1} + \cdots + \binom{m+1}{\ell-1} \right)
+ \left( \binom{m+1}{0} + \binom{m+1}{1} + \cdots + \binom{m+1}{m-\ell} \right)
+ \binom{m+1}{a_{m+1}} = 2^{m+1},
\end{align*}
or, using $\binom{m+1}{i} = \binom{m+1}{m+1-i}$, that
\begin{align*}
\left( \binom{m+1}{0} + \binom{m+1}{1} + \cdots + \binom{m+1}{\ell-1} \right)
+ \left( \binom{m+1}{0} + \binom{m+1}{1} + \cdots + \binom{m+1}{m-\ell} \right)
+ \binom{m+1}{a_{m+1}} = 2^{m+1}.
\end{align*}

\medskip
On the other hand, it is well known that
\[
\binom{m+1}{0} + \binom{m+1}{1} + \cdots + \binom{m+1}{m+1} = 2^{m+1},
\]
and so, by subtracting, we get
\[
\binom{m+1}{a_{m+1}} = \binom{m+1}{\ell} - \binom{m+1}{m-\ell+1} = \binom{m+1}{\ell} - \binom{m+1}{\ell} = 0.
\]

\medskip
From this, using the fact that the binomial coefficients $\binom{m+1}{i}$ are increasing for $i \le \frac{m+1}{2}$ and decreasing for $i \ge \frac{m+1}{2}$, we conclude that either $a_{m+1} = \ell$ or $a_{m+1} = m + 1 - \ell$. In either case, $a_0, a_1, \dots, a_{m+1}$ is again of the claimed form, which concludes the induction.
As a result of this description, any integer $N \ge 0$ appears as a term of the sequence $a_i$ for some $0 \le i \le 2N$.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\newtheorem{claim}{Claim}

\begin{document}

\noindent \textbf{Combinatorics}

\medskip
\noindent \textbf{C2.} You are given a set of $n$ blocks, each weighing at least 1; their total weight is $2n$.
Prove that for every real number $r$ with $0 \le r \le 2n - 2$ you can choose a subset of the blocks whose total weight is at least $r$ but at most $r + 2$.

\medskip
\noindent \textit{(Thailand)}

\medskip
\noindent \textbf{Solution 1.} We prove the following more general statement by induction on $n$.
\medskip
\noindent \textbf{Claim.} Suppose that you have $n$ blocks, each of weight at least 1, and of total weight $s \le 2n$. Then for every $r$ with $-2 \le r \le s$, you can choose some of the blocks whose total weight is at least $r$ but at most $r + 2$.

\medskip
\noindent \textit{Proof.} The base case $n = 1$ is trivial. To prove the inductive step, let $x$ be the largest block weight. Clearly, $x \ge s/n$, so $s - x \le \frac{n-1}{n}s \le 2(n - 1)$. Hence, if we exclude a block of weight $x$, we can apply the inductive hypothesis to show the claim holds (for this smaller set) for any $-2 \le r \le s - x$. Adding the excluded block to each of those combinations, we see that the claim also holds when $x - 2 \le r \le s$. So if $x - 2 \le s - x$, then we have covered the whole interval $[-2, s]$. But each block weight is at least 1, so we have $x \ge 1$. We need to show $x - 2 \le s - x$, i.e. $2x - 2 \le s$. But $s - 2x \le s - 2(s/n) = s (1 - 2/n) \le 0$ since $s \le 2n$. Indeed, $s - 2x \le 2n - 2(2n/n) = 2n - 4 = 2(n-2)$. We must have $n \ge 2$. Then $s-2x \le s - 2(s/n) = s(1 - 2/n) \le s - s = 0$ if $n \ge 2$. Actually $s - 2x \le 2n - 2(2n/n) = 2n - 4 = 2(n-2)$. We must have $n \ge 2$. Then $x - 2 \le (s - (n - 1)) - 2 = s - n - 1 \le s - x$, as desired. $\Box$

\medskip
\noindent \textbf{Comment.} Instead of inducting on sets of blocks with total weight $s \le 2n$, we could instead prove the result only for $s = 2n$. We would then need to modify the inductive step to scale up the block weights before applying the induction hypothesis.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{Combinatorics}

\medskip
\noindent \textbf{C3.} Let $n$ be a positive integer. Harry has $n$ coins lined up on his desk, each showing heads or tails. He repeatedly does the following operation: if there are $k$ coins showing heads and $k>0$, then he flips the $k^{\text{th}}$ coin over; otherwise he stops the process. (For example, the process starting with $THT$ would be $THT \to HHT \to HTT \to TTT$, which takes three steps.)

\medskip
Letting $C$ denote the initial configuration (a sequence of $n$ $H$'s and $T$'s), write $\ell(C)$ for the number of steps needed before all coins show $T$. Show that this number $\ell(C)$ is finite, and determine its average value over all $2^n$ possible initial configurations $C$.

\medskip
\noindent \textit{(USA)}

\medskip
\noindent \textbf{Answer:} The average is $\frac{1}{4} n(n + 1)$.

\medskip
\noindent \textbf{Common remarks.} Throughout all these solutions, we let $E(n)$ denote the desired average value.

\medskip
\noindent \textbf{Solution 1.} We represent the problem using a directed graph $G_n$ whose vertices are the length-$n$ strings of $H$'s and $T$'s. The graph features an edge from each string to its successor (except for $TT \cdots TT$, which has no successor). We will also write $H = T$ and $T = H$.
The graph $G_n$ consists of a single vertex: the empty string. The main claim is that $G_n$ can be described explicitly in terms of $G_{n-1}$:
\begin{itemize}
    \item We take two copies, $X$ and $Y$, of $G_{n-1}$.
    \item In $X$, we take each string of $n-1$ coins and just append a $T$ to it. In symbols, we replace $s_1 \cdots s_{n-1}$ with $s_1 \cdots s_{n-1} T$.
    \item In $Y$, we take each string of $n-1$ coins, flip every coin, reverse the order, and append an $H$ to it. In symbols, we replace $s_1 \cdots s_{n-1}$ with $\overline{s_{n-1}} \cdots \overline{s_1} H$.
    \item Finally, we add one new edge from $Y$ to $X$, namely $HH \cdots HHH \to HH \cdots HHT$.
\end{itemize}

\medskip
We depict $G_4$ below, in a way which indicates this recursive construction:

\medskip
\noindent \begin{center}
    \includegraphics[width=0.8\textwidth]{example-image-a}
\end{center}


\medskip
We prove the claim inductively. Firstly, $X$ is correct as a subgraph of $G_n$, as the operation on coins is unchanged by an extra $T$ at the end: if $s_1 \cdots s_{n-1}$ is sent to $t_1 \cdots t_{n-1}$, then $s_1 \cdots s_{n-1} T$ is sent to $t_1 \cdots t_{n-1} T$.

\medskip
Next, $Y$ is also correct as a subgraph of $G_n$, as if $s_1 \cdots s_{n-1}$ has $k$ occurrences of $H$, then $\overline{s_{n-1}} \cdots \overline{s_1} H$ has $(n-1 - k) + 1 = n-k$ occurrences of $H$, and thus (provided that $k > 0$), if $s_1 \cdots s_{n-1}$ is sent to $t_1 \cdots t_{n-1}$, then $\overline{s_{n-1}} \cdots \overline{s_1} H$ is sent to $\overline{t_{n-1}} \cdots \overline{t_1} H$.

\medskip
Finally, the one edge from $Y$ to $X$ is correct, as the operation does send $HH \cdots HHH$ to $HH \cdots HHT$.

\vspace{2cm}
\hrulefill \textit{Shortlisted problems - solutions} \hrulefill 33

\medskip
To finish, note that the sequences in $X$ take an average of $E(n-1)$ steps to terminate, whereas the sequences in $Y$ take an average of $E(n-1) + n$ steps to reach $HH \cdots H$ and then an additional $n$ steps to terminate. Therefore, we have
\[
E(n) = \frac{1}{2} (E(n - 1) + (E(n - 1) + n)) = E(n - 1) + \frac{n}{2}.
\]

\medskip
We have $E(0) = 0$ from our description of $G_0$. Thus, by induction, we have $E(n) = \frac{1}{2} (1 + \cdots + n) = \frac{1}{4} n(n+1)$, which in particular is finite.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\newtheorem{claim}{Claim}

\begin{document}

\noindent \textbf{Combinatorics}

\medskip
\noindent \textbf{C4.} On a flat plane in Camelot, King Arthur builds a labyrinth $\mathcal{L}$ consisting of $n$ walls, each of which is an infinite straight line. No two walls are parallel, and no three walls have a common point. Merlin then paints one side of each wall entirely red and the other side entirely blue.

\medskip
At the intersection of two walls there are four corners: two diagonally opposite corners where a red side and a blue side meet, one corner where two red sides meet, and one corner where two blue sides meet. At each such intersection, there is a two-way door connecting the two diagonally opposite corners at which sides of different colours meet.

\medskip
After Merlin paints the walls, Morgana then places some knights in the labyrinth $\mathcal{L}$. The knights can walk through doors, but cannot walk through walls.

\medskip
Let $k(\mathcal{L})$ be the largest number $k$ such that, no matter how Merlin paints the labyrinth $\mathcal{L}$, Morgana can always place at least $k$ knights such that no two of them can ever meet. For each $n$, what are all possible values for $k(\mathcal{L})$, where $\mathcal{L}$ is a labyrinth with $n$ walls?

\medskip
\noindent \textit{(Canada)}

\medskip
\noindent \textbf{Answer:} The only possible value of $k$ is $k = n + 1$, no matter what shape the labyrinth is.

\medskip
\noindent \textbf{Solution 1.} First we show by induction that the $n$ walls divide the plane into $\binom{n}{2} + 1$ regions. The claim is true for $n = 0$ as, when there are no walls, the plane forms a single region. When placing the $n^{\text{th}}$ wall, it intersects each of the $n-1$ other walls exactly once and hence splits each of $n$ of the regions formed by those other walls into two regions. By the induction hypothesis, this yields $(\binom{n-1}{2} + 1) + n = (\binom{n}{2} + 1)$ regions, proving the claim.

\medskip
Now let $G$ be the graph with vertices given by the $(\binom{n}{2} + 1)$ regions, and with two regions connected by an edge if there is a door between them.

\medskip
We now show that no matter how Merlin paints the $n$ walls, Morgana can place at least $n+1$ knights. No matter how the walls are painted, there are exactly $\binom{n}{2}$ intersection points, each of which corresponds to a single edge in $G$. Consider adding the edges of $G$ sequentially and note that each edge reduces the number of connected components by at most one. Therefore the number of connected components of $G$ is at least $(\binom{n}{2} + 1) + 1 - \binom{n}{2} = n + 1$. If Morgana places a knight in regions corresponding to different connected components of $G$, then no two knights can ever meet.

\medskip
Now we give a construction showing that, no matter what shape the labyrinth is, Merlin can colour it such that that there are exactly $n + 1$ connected components, allowing Morgana to place at most $n + 1$ knights.

\medskip
First, we choose a coordinate system on the labyrinth so that none of the walls run due north-south, or due east-west. We then have Merlin paint the west face of each wall red, and the east face of each wall blue. We label the regions according to how many walls the region is on the east side of: the labels are integers between $0$ and $n$.

\medskip
We claim that, for each $i$, the regions labelled $i$ are connected by doors. First, we note that for each $i$ with $0 \le i \le n$ there is a unique region labelled $i$ which is unbounded to the north.

\medskip
Now, consider a knight placed in some region with label $i$, and ask them to walk north (moving east or west by following the walls on the northern sides of regions, as needed). This knight will never get stuck: each region is convex, and so, if it is bounded to the north, it has a single northernmost vertex with a door northwards to another region with label $i$.

\medskip
Eventually it will reach a region which is unbounded to the north, which will be the unique such region with label $i$. Hence every region with label $i$ is connected to this particular region, and so all regions with label $i$ are connected to each other.

\medskip
As a result, there are exactly $n + 1$ connected components, and Morgana can place at most $n + 1$ knights.

\vspace{1cm}
\hrulefill \textit{Shortlisted problems - solutions} \hrulefill 37

\medskip
\noindent \textbf{Comment.} Variations on this argument exist: some of them capture more information, and some of them capture less information, about the connected components according to this system of numbering.
For example, it can be shown that the unbounded regions are numbered $0, 1, \dots, n-1, n, n, -1, \dots, 1$ as one cycles around them, that the regions labelled 0 and $n$ are the only regions in their connected components, and that each other connected component forms a single chain running between the two unbounded ones. It is also possible to argue that the regions are acyclic without revealing much about their structure.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{C5.} On a certain social network, there are 2019 users, some pairs of which are friends, where friendship is a symmetric relation. Initially, there are 1010 people with 1009 friends each and 1009 people with 1010 friends each. However, the friendships are rather unstable, so events of the following kind may happen repeatedly, one at a time:

\medskip
Let $A, B$, and $C$ be people such that $A$ is friends with both $B$ and $C$, but $B$ and $C$ are not friends; then $B$ and $C$ become friends, but $A$ is no longer friends with them.

\medskip
Prove that, regardless of the initial friendships, there exists a sequence of such events after which each user is friends with at most one other user.

\medskip
\noindent \textit{(Croatia)}

\medskip
\noindent \textbf{Common remarks.} The problem has an obvious rephrasing in terms of graph theory. One is given a graph $G$ with 2019 vertices, 1010 of which have degree 1009 and 1009 of which have degree 1010. One is allowed to perform operations on $G$ of the following kind:

\medskip
Suppose that vertex $A$ is adjacent to two distinct vertices $B$ and $C$ which are not adjacent to each other. Then one may remove the edges $AB$ and $AC$ from $G$ and add the edge $BC$ into $G$.

\medskip
Call such an operation a \textit{refriending}. One wants to prove that, via a sequence of such refriendings, one can reach a graph which is a disjoint union of single edges and vertices.
All of the solutions presented below will use this reformulation.

\medskip
\noindent \textbf{Solution 1.} Note that the given graph is connected, since the total degree of any two vertices is at least 2018 and hence they are either adjacent or have at least one neighbour in common. Hence the given graph satisfies the following condition:
\begin{enumerate}
    \item[(1)] Every connected component of $G$ with at least three vertices is not complete and has a vertex of odd degree.
\end{enumerate}

\medskip
We will show that if a graph $G$ satisfies condition (1) and has a vertex of degree at least 2, then there is a refriending on $G$ that preserves condition (1). Since refriendings decrease the total number of edges of $G$, by using a sequence of such refriendings, we must reach a graph $G$ with maximal degree at most 1, so we are done.

\medskip
\noindent \begin{center}
   \documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}

\begin{document}

Pick a vertex $A$ of degree at least 2 in a connected component $G'$ of $G$. Since no component of $G$ with at least three vertices is complete we may assume that not all of the neighbours of $A$ are adjacent to one another. (For example, pick a maximal complete subgraph $K$ of $G'$. Some vertex $A$ of $K$ has a neighbour outside $K$, and this neighbour is not adjacent to every vertex of $K$ by maximality.) Removing $A$ from $G$ splits $G'$ into smaller connected components $G_1,\dots, G_k$ (possibly with $k=1$), to each of which $A$ is connected by at least one edge. We divide into several cases.

Case 1: $k\geq 2$ and $A$ is connected to some $G_i$ by at least two edges.

Choose a vertex $B$ of $G_i$ adjacent to $A$, and a vertex $C$ in another component $G_j$ adjacent to $A$. The vertices $B$ and $C$ are not adjacent, and hence removing edges $AB$ and $AC$ and adding in edge $BC$ does not disconnect $G'$. It is easy to see that this preserves the condition, since the refriending does not change the parity of the degrees of vertices.

Case 2: $k\geq 2$ and $A$ is connected to each $G_i$ by exactly one edge.

Consider the induced subgraph on any $G_i$ and the vertex $A$. The vertex $A$ has degree 1 in this subgraph; since the number of odd-degree vertices of a graph is always even, we see that $G_i$ has a vertex of odd degree (in $G$). Thus if we let $B$ and $C$ be any distinct neighbours of $A$, then removing edges $AB$ and $AC$ and adding in edge $BC$ preserves the above condition: the refriending creates two new components, and if either of these components has at least three vertices, then it cannot be complete and must contain a vertex of odd degree (since each $G_i$ does).

Case 3: $k=1$ and $A$ is connected to $G_1$ by at least three edges.

By assumption, $A$ has two neighbours $B$ and $C$ which are not adjacent to one another. Removing edges $AB$ and $AC$ and adding in edge $BC$ does not disconnect $G'$. We are then done as in Case 1.

Case 4: $k=1$ and $A$ is connected to $G_1$ by exactly two edges.

Let $B$ and $C$ be the two neighbours of $A$, which are not adjacent. Removing edges $AB$ and $AC$ and adding in edge $BC$ results in two new components: one consisting of a single vertex; and the other containing a vertex of odd degree. We are done unless this second component would be a complete graph on at least 3 vertices. But in this case, $G_1$ would be a complete graph minus the single edge $BC$, and hence has at least 4 vertices since $G'$ is not a 4-cycle. If we let $D$ be a third vertex of $G_1$, then removing edges $BA$ and $BD$ and adding in edge $AD$ does not disconnect $G'$. We are then done as in Case 1.

\end{document}
\end{center}

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{C6.} Let $n > 1$ be an integer. Suppose we are given $2n$ points in a plane such that no three of them are collinear. The points are to be labelled $A_1, A_2, \dots, A_{2n}$ in some order. We then consider the $2n$ angles $\angle A_1 A_2 A_3, \angle A_2 A_3 A_4, \dots, \angle A_{2n-2} A_{2n-1} A_{2n}, \angle A_{2n-1} A_{2n} A_1, \angle A_{2n} A_1 A_2$. We measure each angle in the way that gives the smallest positive value (i.e. between $0^\circ$ and $180^\circ$). Prove that there exists an ordering of the given points such that the resulting $2n$ angles can be separated into two groups with the sum of one group of angles equal to the sum of the other group.

\medskip
\noindent \textit{(USA)}

\medskip
\noindent \textbf{Comment.} The first three solutions all use the same construction involving a line separating the points into groups of $n$ points each, but give different proofs that this construction works. Although Solution 1 is very short, the Problem Selection Committee does not believe any of the solutions is easy to find and thus rates this as a problem of medium difficulty.

\medskip
\noindent \textbf{Solution 1.} Let $\ell$ be a line separating the points into two groups ($L$ and $R$) with $n$ points in each. Label the points $A_1, A_2, \dots, A_{2n}$ so that $L = \{A_1, A_3, \dots, A_{2n-1}\}$. We claim that this labelling works.

\medskip
Take a line $s = A_{2n} A_1$.

\begin{enumerate}
    \item[(a)] Rotate $s$ around $A_1$ until it passes through $A_2$; the rotation is performed in a direction such that $s$ is never parallel to $\ell$.
    \item[(b)] Then rotate the new $s$ around $A_2$ until it passes through $A_3$ in a similar manner.
    \item[(c)] Perform $2n-2$ more such steps, after which $s$ returns to its initial position.
\end{enumerate}

\medskip
The total (directed) rotation angle $\Theta$ of $s$ is clearly a multiple of $180^\circ$. On the other hand, $s$ was never parallel to $\ell$, which is possible only if $\Theta = 0$. Now it remains to partition all the $2n$ angles into those where $s$ is rotated anticlockwise, and the others.

\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\newtheorem{obs}{Observation}
\newtheorem{claim}{Claim}

\begin{document}

\noindent \textbf{C7.} There are 60 empty boxes $B_1, \dots, B_{60}$ in a row on a table and an unlimited supply of pebbles. Given a positive integer $n$, Alice and Bob play the following game.

\medskip
In the first round, Alice takes $n$ pebbles and distributes them into the 60 boxes as she wishes. Each subsequent round consists of two steps:
\begin{enumerate}
    \item[(a)] Bob chooses an integer $k$ with $1 \le k \le 59$ and splits the boxes into the two groups $B_1, \dots, B_k$ and $B_{k+1}, \dots, B_{60}$.
    \item[(b)] Alice picks one of these two groups, adds one pebble to each box in that group, and removes one pebble from each box in the other group.
\end{enumerate}

\medskip
Bob wins if, at the end of any round, some box contains no pebbles. Find the smallest $n$ such that Alice can prevent Bob from winning.

\medskip
\noindent \textit{(Czech Republic)}

\medskip
\noindent \textbf{Answer:} $n = 960$. In general, if there are $N > 1$ boxes, the answer is $n = \lfloor \frac{N}{2} + 1 \rfloor \lceil \frac{N}{2} + 1 \rceil - 1$.

\medskip
\noindent \textbf{Common remarks.} We present solutions for the general case of $N > 1$ boxes, and write $M = \lfloor \frac{N}{2} + 1 \rfloor \lceil \frac{N}{2} + 1 \rceil - 1$ for the claimed answer. For $1 \le k < N$, say that Bob makes a $k$-\textit{move} if he splits the boxes into a left group $\{B_1, \dots, B_k\}$ and a right group $\{B_{k+1}, \dots, B_N \}$. Say that one configuration \textit{dominates} another if it has at least as many pebbles in each box, and say that it \textit{strictly dominates} the other configuration if it also has more pebbles in at least one box. (Thus, if Bob wins in some configuration, he also wins in every configuration that it dominates.)

\medskip
It is often convenient to consider ``V-shaped'' configurations; for $1 \le i \le N$, let $V_i$ be the configuration where $B_j$ contains $1 + |j - i|$ pebbles (i.e. where the $i^{\text{th}}$ box has a single pebble and the numbers increase by one in both directions, so the first box has $i$ pebbles and the last box has $N + 1 - i$ pebbles). Note that $V_i$ contains $\frac{1}{2} i(i + 1) + \frac{1}{2} (N + 1 - i)(N + 2 - i) - 1$ pebbles. If $i = \lfloor \frac{N}{2} \rfloor$, this number equals $M$.

\medskip
Solutions split naturally into a strategy for Alice (starting with $M$ pebbles and showing she can prevent Bob from winning) and a strategy for Bob (showing he can win for any starting configuration with at most $M - 1$ pebbles). The following observation is also useful to simplify the analysis of strategies for Bob.

\medskip
\noindent \textbf{Observation A.} Consider two consecutive rounds. Suppose that in the first round Bob made a $k$-move and Alice picked the left group, and then in the second round Bob makes an $\ell$-move, with $\ell > k$. We may then assume, without loss of generality, that Alice again picks the left group.

\medskip
\noindent \textit{Proof.} Suppose Alice picks the right group in the second round. Then the combined effect of the two rounds is that each of the boxes $B_{k+1}, \dots, B_{\ell}$ lost two pebbles (and the other boxes are unchanged). Hence this configuration is strictly dominated by that before the first round, and it suffices to consider only Alice's other response. $\Box$

\medskip
\noindent \textbf{Solution 1 (Alice).} Alice initially distributes pebbles according to $V_{\lfloor \frac{N}{2} \rfloor}$. Suppose the current configuration of pebbles dominates $V_i$. If Bob makes a $k$-move with $k \ge i$ then Alice picks the left group, which results in a configuration that dominates $V_{i+1}$. Likewise, if Bob makes a $k$-move with $k < i$ then Alice picks the right group, which results in a configuration that dominates $V_{i-1}$. Since none of $V_1, \dots, V_N$ contains an empty box, Alice can prevent Bob from ever winning.

\vspace{2cm}
\noindent 48 \hfill Bath --- UK, 11th-22nd July 2019

\medskip
\noindent \textbf{Solution 1 (Bob).} The key idea in this solution is the following claim.
\medskip
\noindent \textbf{Claim.} If there exist a positive integer $k$ such that there are at least $2k$ boxes that have at most $k$ pebbles each then Bob can force a win.
\medskip
\noindent \textit{Proof.} We ignore the other boxes. First, Bob makes a $k$-move (splits the $2k$ boxes into two groups of $k$ boxes each). Without loss of generality, Alice picks the left group. Then Bob makes a $(k+1)$-move, $\dots$, a $(2k-1)$-move. By Observation A, we may suppose Alice always picks the left group. After Bob's $(2k-1)$-move, the rightmost box becomes empty and Bob wins. $\Box$

\medskip
Now, we claim that if $n < M$ then either there already exists an empty box, or there exist a positive integer $k$ and $2k$ boxes with at most $k$ pebbles each (and thus Bob can force a win). Otherwise, assume each box contains at least $1$ pebble, and for each $1 \le k \le \lfloor \frac{N}{2} \rfloor$, at least $N - (2k - 1) = N + 1 - 2k$ boxes contain at least $k + 1$ pebbles. Summing, there are at least as many pebbles in total as in $V_{\lfloor \frac{N}{2} \rfloor}$; that is, at least $M$ pebbles, as desired.

\end{document}

\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}

\begin{document}

\textbf{C8.} Alice has a map of Wonderland, a country consisting of $n \geq 2$ towns. For every pair of towns, there is a narrow road going from one town to the other. One day, all the roads are declared to be "one way" only. Help her. She is allowed to ask him a number of questions, but the King of Hearts has offered to help. She is allowed to ask the direction of the roads.

For each question in turn, Alice chooses a pair of towns and the King of Hearts tells her the direction of the road connecting those two towns.

Alice wants to know whether there is at least one town in Wonderland with at most one outgoing road. Prove that she can always find out by asking at most $4n$ questions.

(Thailand)

\textbf{Comment.} This problem could be posed with an explicit statement about points being awarded for weaker bounds on $cn$ for some $c < 4$, in the style of IMO 2014 Problem 6.


\textbf{Solution.} We will show Alice needs to ask at most $4n - 7$ questions. Her strategy has the following phases. In what follows, $S$ is the set of towns $ \{1, 2, \dots, n\}$ that, so far, does not know to have more than one outgoing road (so initially $S = \{1, \dots, n\}$).


\textbf{Phase 1.} Alice chooses any two towns, say $A$ and $B$. Without loss of generality, suppose that the King of Hearts answer is that the road goes from $A$ to $B$.


At the end of this phase, Alice has asked 1 question.


\textbf{Phase 2.} During this phase there is a single (variable) town $T$ that is known to have at least one incoming road but not yet known to have any outgoing roads. Initially, $T$ is $B$. Alice does the following $n-2$ times: she picks a town $X$ if she has not asked about before, and asks the direction of the road between $T$ and $X$. If $X$ is from $X$ to $T$, it is unchanged; if it is from $T$ to $X$, $X$ becomes the new choice of town $T$, as the previous $T$ is now known to have an outgoing road.

At the end of this phase, Alice has asked a total of $n - 1$ questions. The final town $T$ is not yet known to have any outgoing roads, while every other town has exactly one outgoing road known. The undirected graph of roads whose directions are known is a tree.


\textbf{Phase 3.} During this phase, Alice asks about the directions of all roads between $T$ and another town she has not previously asked about, stopping if she finds two outgoing roads from $T$. This phase involves at most $n - 2$ questions. If she does not find two outgoing roads from $T$, she has supposed that she does find two outgoing roads, asking a total of $k$ questions, so in this phase, where $k < n - 2$ (and thus $n \geq 4$), while the last question resulted in $T$ being from $S$ (as it already had one outgoing road known) for what follows at the other end is removed from $S$. Furthermore, the undirected graph of roads of known direction is a tree.


\textbf{Phase 4.} During this phase, Alice repeatedly picks any pair of towns in $S$ for which she does not know the direction of the road between them. Because every town in $S$ has exactly one outgoing road known, this always results in the removal of one of those two towns from $S$. Because there are at most 2 towns left in $S$. Until there are no cycles in the graph of roads of known direction within $S$, this can continue.


If it ends with $t$ towns left, $n - k + 1 - t$ questions were asked in this phase, so a total of $2n - 7$ questions have been asked.

\textbf{Phase 5.} During this phase, Alice asks about all the roads from the remaining towns in $S$ that she has not previously asked about. She has definitely already asked about any road between those towns (if $t = 2$). She must also have asked in one of the first two phases about at least one other road involving one of those towns (as those phases resulted in a tree with $n \geq 2$ vertices). So she asks at most $n(n - t) - 1$ questions in this phase.



If $t = 1$, at most $3n - 3 < 4n - 7$ questions were needed in total, while if $t = 2$, at most $4n - 7$ questions were needed in total.

\end{document}


"""