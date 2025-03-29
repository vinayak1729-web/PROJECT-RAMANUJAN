def geometry_prompt():
    return r"""
    \documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{graphicx} % Allows including images

\begin{document}

\textbf{G1.} Let $ABC$ be a triangle. Circle $\Gamma$ passes through $A$, meets segments $AB$ and $AC$ again at points $D$ and $E$ respectively, and intersects segment $BC$ at $F$ and $G$ such that $F$ lies between $B$ and $G$. The tangent to circle $BDF$ at $F$ and circle $CEG$ at $G$ meet at point $T$. Suppose that points $A$ and $T$ are distinct. Prove that line $AT$ is parallel to $BC$. (Nigeria)


\textbf{Solution.} Notice that $\angle TFB = \angle FDA$ because $FT$ is tangent to circle $BDF$, and moreover $\angle FDA = \angle CGA$ because quadrilateral $ADFG$ is cyclic. Similarly, $\angle TGB = \angle GEC$ because $GT$ is tangent to circle $CEG$, and $\angle GEC = \angle CFA$. Hence,
$$\angle TFB = \angle CGA \quad \text{and} \quad \angle TGB = \angle CFA.$$ (1)

Triangles $FGA$ and $GFT$ have a common side $FG$, and by (1) their angles at $F, G$ are the same. So, these triangles are congruent. So, their altitudes starting from $A$ and $T$, respectively, are equal and hence $AT$ is parallel to line $BFGC$.

\textbf{Comment.} Alternatively, we can prove first that $T$ lies on $\Gamma$. For example, this can be done by showing that $\angle AFT = \angle AGT$ using (1). Then the statement follows as $\angle TAF = \angle TGF = \angle GFA$.

\end{document}


\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb} % for symbols like \phi

\begin{document}

\textbf{G2.} Let $ABC$ be an acute-angled triangle and let $D$, $E$, and $F$ be the feet of altitudes from $A$, $B$, and $C$ to sides $BC$, $CA$, and $AB$, respectively. Denote by $\omega_b$ and $\omega_c$ the incircles of triangles $BDF$ and $CDE$, and let these circles be tangent to segments $DF$ and $DE$ at $M$ and $N$, respectively. Prove that line $MN$ meet circles $\omega_b$ and $\omega_c$ again at $P \ne M$ and $Q \ne N$, respectively.  Prove that $MP = NQ$.

\textbf{Solution.} Denote the centers of $\omega_b$ and $\omega_c$ by $O_b$ and $O_c$, let their radii be $r_b$ and $r_c$, and let $BC$ be tangent to the two circles at $T$ and $U$, respectively.

From the cyclic quadrilaterals $AFDC$ and $ABDE$ we have
$$\angle DMO_b = \frac{1}{2} \angle FDB = \frac{1}{2} \angle BAC = \frac{1}{2} \angle CDE = \angle O_cDN,$$
so the right-angled triangles $DMO_b$ and $DNO_c$ are similar. The ratio of similarity between the two triangles is
$$\frac{DN}{DM} = \frac{O_cN}{O_bM} = \frac{r_c}{r_b}.$$
Let $\varphi = \angle DMN$ and $\psi = \angle MND$. The lines $FM$ and $EN$ are tangent to $\omega_b$ and $\omega_c$, respectively.  $ \angle MTP = \angle FMP = \angle DMN = \varphi$ and $\angle QUN = \angle QNE = \angle MND = \psi$.
(It is possible that $P$ or $Q$ coincides with $T$ or $U$, or lie inside triangles $DMT$ or $DUN$, respectively. To reduce case-sensitivity, we may use directed angles or simply ignore angles MTP and QUN.)

In the circles $\omega_b$ and $\omega_c$, the lengths of chords $MP$ and $NQ$ are
$$MP = 2r_b \sin \varphi \quad \text{and} \quad NQ = 2r_c \sin \psi.$$

By applying the sine rule to triangle $DNM$ we get
$$\frac{DN}{\sin \angle DMN} = \frac{DM}{\sin \angle DMN} = \frac{NM}{\sin \varphi},$$
Finally, putting the above observations together, we get
$$\frac{MP}{NQ} = \frac{2r_b \sin \varphi}{2r_c \sin \psi} = \frac{r_b}{r_c} \frac{\sin \varphi}{\sin \psi} = \frac{DN}{DM} \frac{\sin \varphi}{\sin \psi} = \frac{r_c}{r_b} \frac{\sin \varphi}{\sin \psi}.$$
so $MP = NQ$ as required.


\end{document}

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{G3.} In triangle $ABC$, let $A_1$ and $B_1$ be two points on sides $BC$ and $AC$, and let $P$ and $Q$ be two points on segments $AA_1$ and $BB_1$, respectively, so that line $PQ$ is parallel to $AB$. On ray $PB_1$, beyond $B_1$, let $P_1$ be a point so that $\angle LPP_1 C = \angle BAC$. Similarly, on ray $QA_1$, beyond $A_1$, let $Q_1$ be a point so that $\angle LCQ_1 = \angle CBA$. Show that points $P$, $Q$, $P_1$, and $Q_1$ are concyclic.

\textbf{Solution 1.} Throughout the solution we use oriented angles.
Let rays $AA_1$ and $BB_1$ intersect the circumcircle of $\triangle ABC$ at $A_2$ and $B_2$, respectively. By
$$\angle QPA_2 = \angle BAA_2, \quad \angle B_2B_1 A_2 = \angle Q B_1 A_2,$$
points $P$, $Q$, $A_2$, $B_2$ are concyclic; denote the circle passing through these points by $\omega$. We shall prove that $P_1$ and $Q_1$ also lie on $\omega$.

By $\angle CA_1 A_2 = \angle CBA = \angle CQ_1 Q$, points $C, Q_1, A_1, A_2$ are also concyclic. From that we get
$$\angle CQ_1 A_2 = \angle CA_1 A_2 = \angle CBA = \angle CQ_1 Q,$$
so $Q_1$ lies on $\omega$.  It follows similarly that $P_1$ lies on $\omega$.



\end{document}

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{G4.} Let $P$ be a point inside triangle $ABC$. Let $AP$ meet $BC$ at $A_1$, let $BP$ meet $CA$ at $B_1$, and let $CP$ meet $AB$ at $C_1$. Let $A_2$ be the point such that $A_1$ is the midpoint of $PA_2$, let $B_2$ be the point such that $B_1$ is the midpoint of $PB_2$, and let $C_2$ be the point such that $C_1$ is the midpoint of $PC_2$. Prove that points $A_2$, $B_2$, and $C_2$ cannot all lie strictly inside the circumcircle of triangle $ABC$. (Australia)

\textbf{Solution 1.} Since
$$ \angle APB + \angle BPC + \angle CPA = 2\pi = (\pi - \angle ACB) + (\pi - \angle BAC) + (\pi - \angle CBA), $$
at least one of the following inequalities holds:
$$ \angle APB > \pi - \angle ACB, \quad \angle BPC > \pi - \angle BAC, \quad \angle CPA > \pi - \angle CBA. $$
Without loss of generality, we assume that $\angle BPC > \pi - \angle BAC$. We have $\angle BPC > \angle BAC$. So $\sin\angle BPC \ge \max \{\sin\angle BAC, \pi - \angle BAC\}$ and hence  $\sin\angle BPC > \sin\angle BAC$ (4)


Let the rays $AP$, $BP$, and $CP$ cross the circumcircle $\mathcal{Q}$ again at $A_3$, $B_3$, and $C_3$, respectively.
We will prove that at least one of the ratios $\frac{PB_1}{PB_3}$ and $\frac{PC_1}{PC_3}$ is at least 1, which yields that one of the points $A, B, C, B_3, and B_1, A_1$ are similar, so
$$\frac{CB_1}{CB_3} = \frac{BB_1}{BB_3} = \frac{B_1 A}{B_3 A}.$$

Applying the sine rule we obtain
$$\frac{PB_1}{CB_1} = \frac{\sin \angle LACP}{\sin \angle BAC}, \quad \frac{PB_1}{CB_1} = \frac{\sin \angle LBPB}{\sin \angle LBPB}.$$
$$\frac{PC_1}{CB_1} = \frac{\sin \angle LPB A}{\sin \angle L BAC}, \quad \frac{PC_1}{CB_1} = \frac{\sin \angle LBPB}{\sin \angle LACP}.$$
Multiplying these two equations we get
$$ \frac{PB_1}{CB_1} \cdot \frac{PC_1}{CB_1} = \frac{\sin^2\angle BAC}{\sin \angle BPC} \ge 1$$
using (4), which yields the desired conclusion.

\end{document}



\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{G5.} Let $ABCDE$ be a convex pentagon with $CD = DE$ and $\angle EDC = \frac{\pi}{2}$.  Suppose that a point $P$ is located in the interior of the pentagon such that $AP = AE$ and $BP = BC$. Prove that $P$ lies on the diagonal $CE$ if and only if area$(BCD) +$ area$(ADE) =$ area$(ABD) +$ area$(ABP)$. (Hungary)

\textbf{Solution 1.} Let $P'$ be the reflection of $P$ across line $AB$, and let $M$ and $N$ be the midpoints of $BC$ and $CD$, respectively.  We claim that the area condition is equivalent to the collinearity condition hinted in the problem statement.  To show that, we note the areas $(\text{condition})$ imply that $AP'$, $AE$, and $AD$ are directly similar ($\angle AP'M = \angle BPN$).

For the equivalence with the collinearity condition, let $F$ denote the foot of the perpendicular from $P$ to $AB$, so that $F$ is the midpoint of $PP'$.  We have that $P$ lies on $CE$ if and only if $F$ lies on $CE$.  By concyclicity of $AP'M$ and $BFN$, this is equivalent to $\angle ZAP'M = \angle ZBP'N$, which occurs if and only if $AP'M$ and $BP'N$ are directly similar.

For the other equivalence with the area condition, we have the equality of signed areas
$\text{area}(ABD) +$ area$(ABP) = \text{area}(AP'D) =$ area$(AP'D) +$ area$(B'DP)$. Using the identity $\text{area}(ADE) - \text{area}(AP'D) =$ 2 area$(ADM)$, and similarly for $B$, we find that the area condition is equivalent to $\text{area}(DAM) = \text{area}(DBN)$.

Now note that $A$ and $B$ lie on the perpendicular bisectors of $PE$ and $PC$, respectively.  If we write $G$ and $H$ for the feet of the perpendiculars from $D$ to these perpendicular bisectors respectively, then this area condition can be rewritten as
$MA \cdot GD = NB \cdot HD$.

(In this condition, we interpret all lengths as signed lengths according to suitable conventions for instance, we orient $P'E$ from $P$ to $E$, orient the parallel line $DH$ in the same direction, and orient the perpendicular bisector of $P'E$ at an angle $\pi/2$ clockwise from the oriented segment $PE$ -- we adopt the analogous conventions at $B$).


\end{document}

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

To relate the signed lengths $GD$ and $HD$ to the triangles $AP'M$ and $BP'N$, we use the following calculation.

\textbf{Claim.} Let $\Gamma$ denote the circle centered on $D$ with both $E$ and $C$ on the circumference, and $h$ the power of $P$ with respect to $\Gamma$. Then we have the equality
$$GD \cdot PM = HD \cdot PN = \frac{1}{h} \ne 0.$$

\textbf{Proof.} Firstly, we have $h \ne 0$, since otherwise $P'$ would lie on $\Gamma$, and hence the internal angle bisectors of $\angle LEDP$ and $\angle PDC$ would pass through $A$ and $B$ respectively. This would violate the angle inequality $\angle EDC \ge 2 \cdot \angle ADB$ given in the question.

Next, let $E'$ denote the point on $\Gamma$ diametrically opposite $E$, so that $E'E$ is perpendicular to $PE$. The point $G$ lies on the perpendicular bisectors of the sides $PE$. Since $D$ is the midpoint of $EE'$, we have $GD = \frac{1}{2}PE$. Since $PM = \frac{1}{2}PE$, we have $GD \cdot PM = \frac{1}{4} PE^2$.  The other equality $HD \cdot PN$ follows by exactly the same argument.

From this claim, we see that the area condition is equivalent to the equality
$$(MA \cdot P'M) = (NB \cdot P'N)$$
of ratios of signed lengths, which is equivalent to direct similarity of $AP'M$ and $BP'N$, as desired.



\end{document}


\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\begin{document}

\textbf{G6.} Let $I$ be the incenter of acute-angled triangle $ABC$. Let the incircle meet $BC$, $CA$, and $AB$ at $D$, $E$, and $F$, respectively. Let line $EF$ intersect the circumcircle of the triangle at $P$ and $Q$, such that $F$ lies between $E$ and $P$. Prove that $\angle DPA + \angle DQD = \angle QIP$. (Slovakia)

\textbf{Solution 1.} Let $N$ and $M$ be the midpoints of the arcs $BC$ of the circumcircle (containing opposite vertex $A$, respectively. By $\angle LFAE = \angle ZBAC = \angle LBNC$, the right-angled kites $AFIE$ and $BNMC$ are similar.  Consider the spiral similarity $\varphi$ (dilation in case of $|AB| = |AC|$).

The same as $(\angle APF) \approx (\angle NQ_2)$ so lines $AP$ and $AQ$ are mapped to lines $NP$ and $NQ$, respectively.  Line $EF$ is mapped to $BC$; we can see that the intersection points $P$ and $Q$ by $EF$ and $BC$ $\cap$ $NP$ and $BC$ $\cap$ $NQ$, respectively.

Let $L$ be the midpoint of $BC$.  We claim that points $P$, $Q$, $D$, $L$ are concyclic (if $D = L$ then line $BC$ is tangent to circle $PQD$). Let $PQ$ and $BC$ meet at $Z$. By applying Menelaus' theorem to triangle $ABC$ and line $EF$, we have
$$\frac{BD}{DC} \cdot \frac{FA}{AF} \cdot \frac{AE}{EC} = \frac{BZ}{ZC}.$$

so the pairs $B, C$ and $D, Z$ are harmonic. It is well-known that this implies $ZB \cdot ZC = ZD \cdot ZL$. (The inversion with pole $Z$ that swaps $B$ and $C$ sends $Z$ to infinity and $D$ to the midpoint of $BC$, because the cross-ratio is preserved.) Hence, $ZD \cdot ZL = ZB \cdot ZC = ZP \cdot ZQ$ by the power of $Z$ with respect to the circumcircle. This proves our claim.

By $\angle ZMP' = \angle ZMQ' = 90^\circ$, the quadrilaterals $MLPP'$ and $MLQQ'$ are cyclic. Then the problem statement follows by
$$\angle DPA + \angle DQP = 360^\circ - \angle ZPAQ - \angle ZQDP = 360^\circ - \angle ZLPN - \angle ZNQL = ZPML + \angle ZLMQ = ZP'MQ' = \angle ZPIQ.$$


\end{document}

\documentclass{article}
\usepackage{amsmath, amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\begin{document}

\noindent \textbf{G7.} The incircle $\omega$ of acute-angled scalene triangle $ABC$ has centre $I$ and meets sides $BC$, $CA$, and $AB$ at $D$, $E$, and $F$, respectively. The line through $D$ perpendicular to $EF$ meets $\omega$ again at $R$. Line $AR$ meets $\omega$ again at $P$. The circumcircles of triangles $PCE$ and $PBF$ meet again at $Q \neq P$. Prove that lines $DI$ and $PQ$ meet on the external bisector of angle $BAC$.

\medskip
\noindent \textit{(India)}

\medskip
\noindent \textbf{Common remarks.} Throughout the solution, $\angle(a, b)$ denotes the directed angle between lines $a$ and $b$, measured modulo $\pi$.

\medskip
\noindent \textbf{Solution 1.}

\medskip
\noindent \textbf{Step 1.} The external bisector of $\angle BAC$ is the line through $A$ perpendicular to $IA$. Let $DI$ meet this line at $L$ and let $DI$ meet $\omega$ at $K$. Let $N$ be the midpoint of $EF$, which lies on $IA$ and is the pole of line $AL$ with respect to $\omega$. Since $AN \cdot AI = AE^2 = AR \cdot AP$, the points $R$, $N, I$, and $P$ are concyclic. As $IR = IP$, the line $NI$ is the external bisector of $\angle PNR$, so $PN$ meets $\omega$ again at the point symmetric to $R$ with respect to $AN$ - i.e. at $K$.

\medskip
Let $DN$ cross $\omega$ again at $S$. Opposite sides of any quadrilateral inscribed in the circle $\omega$ meet on the polar line of the intersection of the diagonals with respect to $\omega$. Since $L$ lies on the polar line $AL$ of $N$ with respect to $\omega$, the line $PS$ must pass through $L$. Thus it suffices to prove that the points $S, Q$, and $P$ are collinear.

\medskip
\noindent \textbf{Step 2.} Let $\Gamma$ be the circumcircle of $\triangle BIC$. Notice that
\begin{align*}
\angle(BQ, QC) &= \angle(BQ, QP) + \angle(PQ, QC) = \angle(BF, FP) + \angle(PE, EC) \\
&= \angle(EF, EP) + \angle(FP, FE) = \angle(FP, EP) = \angle(DF, DE) = \angle(BI, IC),
\end{align*}
so $Q$ lies on $\Gamma$. Let $QP$ meet $\Gamma$ again at $T$. It will now suffice to prove that $S, P$, and $T$ are collinear. Notice that $\angle(BI, IT) = \angle(BQ, QT) = \angle(BF, FK) = \angle(FK, KP)$. Note $FD \perp FK$ and $FD \perp BI$ so $FK \parallel BI$ and hence $IT$ is parallel to the line $KNP$. Since $DI = IK$, the line $IT$ crosses $DN$ at its midpoint $M$.

\medskip
\noindent \textbf{Step 3.} Let $F'$ and $E'$ be the midpoints of $DE$ and $DF$, respectively. Since $DE' \cdot EF' = DE'^2 = BE' \cdot E'I$, the point $E'$ lies on the radical axis of $\omega$ and $\Gamma$; the same holds for $F'$. Therefore, this radical axis is $E'F'$, and it passes through $M$. Thus $IM \cdot MT = DM \cdot MS$, so $S, I, D$, and $T$ are concyclic. This shows $\angle(DS, ST) = \angle(DI, IT) = \angle(DK, KP) = \angle(DS, SP)$, whence the points $S, P$, and $T$ are collinear, as desired.

\end{document}
"""