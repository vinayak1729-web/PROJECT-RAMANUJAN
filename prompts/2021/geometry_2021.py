def gemoetry_2021():
    return r"""


\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\textbf{G1.} Let $ABCD$ be a parallelogram such that $AC=BC$. A point $P$ is chosen on the extension of the segment $AB$ beyond $B$. The circumcircle of the triangle $ACD$ meets the segment $PD$ again at $Q$, and the circumcircle of the triangle $APQ$ meets the segment $PC$ again at $R$. Prove that the lines $CD$, $AQ$, and $BR$ are concurrent.


\textbf{Common remarks.} The introductory steps presented here are used in all solutions below.

Since $AC = BC = AD$, we have $\angle ABC = \angle BAC = \angle ACD = \angle ADC$. Since the quadrilaterals $APRQ$ and $AQCD$ are cyclic, we obtain
$$ \angle CRA = 180^\circ - \angle ARP = 180^\circ - \angle AQP = \angle DQA = \angle DCA = \angle CBA, $$
so the points $A$, $B$, $C$, and $R$ lie on some circle $\gamma$.


\textbf{Solution 1.} Introduce the point $X = AQ \cap CD$; we need to prove that $B$, $R$ and $X$ are collinear.

By means of the circle $(APRQ)$ we have
$$ \angle RQX = 180^\circ - \angle AQR = \angle RPA = \angle RCX $$
(the last equality holds in view of $AB \parallel CD$), which means that the points $C$, $Q$, $R$, and $X$ also lie on some circle $\delta$.


Using the circles $\delta$ and $\gamma$ we finally obtain
$$ \angle XRC = \angle XQC = 180^\circ - \angle CQA = \angle ADC = \angle BAC = 180^\circ - \angle CRB, $$
that proves the desired collinearity.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\textbf{G2.} Let $ABCD$ be a convex quadrilateral circumscribed around a circle with centre $I$. Let $\omega$ be the circumcircle of the triangle $ACI$. The extensions of $BA$ and $BC$ beyond $A$ and $C$ meet $\omega$ at $X$ and $Z$, respectively. The extensions of $AD$ and $CD$ beyond $D$ meet $\omega$ at $Y$ and $T$, respectively. Prove that the perimeters of the (possibly self-intersecting) quadrilaterals $ADTX$ and $CDYZ$ are equal.

\textbf{Solution.} The point $I$ is the intersection of the external bisector of the angle $TCZ$ with the circumcircle $\omega$ of the triangle $TCZ$, so $I$ is the midpoint of the arc $TCZ$ and $IT = IZ$. Similarly, $I$ is the midpoint of the arc $YAX$ and $IX = IY$. Let $O$ be the centre of $\omega$. Then $X$ and $T$ are the reflections of $Y$ and $Z$ in $IO$, respectively. So $XT = YZ$.

Let the incircle of $ABCD$ touch $AB$, $BC$, $CD$, and $DA$ at points $P$, $Q$, $R$, and $S$, respectively. The right triangles $IXP$ and $IYS$ are congruent, since $IP = IS$ and $IX = IY$. Similarly, the right triangles $IRT$ and $IQZ$ are congruent. Therefore, $XP = YS$ and $RT = QZ$. Since $AS = AP$, $CQ = RC$, and $SD = DR$, we obtain
\begin{align*} P_{ADTX} &= XT + XA + AS + SD + DT = XT + XP + RT \\ &= YZ + YS + QZ = YZ + YD + DR + RC + CZ = P_{CDYZ} \end{align*} as required.

\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{G3.}
\textbf{Version 1.} Let $n$ be a fixed positive integer, and let $S$ be the set of points $(x,y)$ on the Cartesian plane such that both coordinates $x$ and $y$ are nonnegative integers smaller than $2n$ (thus $|S| = 4n^2$). Assume that $\mathcal{F}$ is a set consisting of $n^2$ quadrilaterals such that all their vertices lie in $S$, and each point in $S$ is a vertex of exactly one of the quadrilaterals in $\mathcal{F}$. Determine the largest possible sum of areas of all $n^2$ quadrilaterals in $\mathcal{F}$.

\textbf{Version 2.} Let $n$ be a fixed positive integer, and let $S$ be the set of points $(x,y)$ on the Cartesian plane such that both coordinates $x$ and $y$ are nonnegative integers smaller than $2n$ (thus $|S| = 4n^2$). Assume that $\mathcal{F}$ is a set of polygons such that all vertices of polygons in $\mathcal{F}$ lie in $S$, and each point in $S$ is a vertex of exactly one of the polygons in $\mathcal{F}$. Determine the largest possible sum of areas of all polygons in $\mathcal{F}$.

\textbf{Answer for both Versions:} The largest possible sum of areas is $\Sigma(n) = \frac{1}{3}n^2(2n+1)(2n-1)$.

\textbf{Common remarks.} Throughout all solutions, the area of a polygon $P$ will be denoted by $[P]$. We say that a polygon is \textit{legal} if all its vertices belong to $S$. Let $O = (\frac{n-1}{2}, \frac{n-1}{2})$ be the centre of $S$. We say that a legal square is \textit{central} if its centre is situated at $O$. Finally, say that a set $\mathcal{F}$ of polygons is \textit{acceptable} if it satisfies the problem requirements, i.e. if all polygons in $\mathcal{F}$ are legal, and each point in $S$ is a vertex of exactly one polygon in $\mathcal{F}$. For an acceptable set $\mathcal{F}$, we denote by $\Sigma(\mathcal{F})$ the sum of areas of polygons in $\mathcal{F}$.

\textbf{Solution 1, for both Versions.} Each point in $S$ is a vertex of a unique central square. Thus the set $\mathcal{G}$ of central squares is acceptable. We will show that
$$ \Sigma(\mathcal{F}) \le \Sigma(\mathcal{G}) - \Sigma(n), \quad (1) $$
thus establishing the answer.

We will use the following key lemma.

\textbf{Lemma 1.} Let $P = A_1 A_2 \dots A_m$ be a polygon, and let $O$ be an arbitrary point in the plane. Then
$$ [P] \le \frac{1}{2} \sum_{i=1}^m OA_i^2. \quad (2) $$
Moreover, if $P$ is a square centred at $O$, then the inequality (2) turns into as equality.

\textbf{Proof.} Put $A_{m+1} = A_1$. For each $i = 1, 2, \dots, m$, we have
$$ [OA_i A_{i+1}] \le \frac{OA_i \cdot OA_{i+1}}{2} \le \frac{OA_i^2 + OA_{i+1}^2}{4} $$
Therefore,
$$ [P] \le \sum_{i=1}^m [OA_i A_{i+1}] \le \frac{1}{4} \sum_{i=1}^m (OA_i^2 + OA_{i+1}^2) = \frac{1}{2} \sum_{i=1}^m OA_i^2, $$
which proves (2). Finally, all the above inequalities turn into equalities when $P$ is a square centred at $O$. $\square$

Back to the problem, consider an arbitrary acceptable set $\mathcal{F}$. Applying Lemma 1 to each element in $\mathcal{F}$ and to each element in $\mathcal{G}$ (achieving equality in the latter case), we obtain
$$ \Sigma(\mathcal{F}) \le \frac{1}{2} \sum_{A \in S} OA^2 = \Sigma(\mathcal{G}), $$
which establishes the left inequality in (1).

\textbf{Shortlisted problems --- solutions}

It remains to compute $\Sigma(\mathcal{G})$. We have
\begin{align*} \Sigma(\mathcal{G}) &= \frac{1}{2} \sum_{A \in S} OA^2 = \frac{1}{2} \sum_{i=0}^{2n-1} \sum_{j=0}^{2n-1} \left( \left( i - \frac{n-1}{2} \right)^2 + \left( j - \frac{n-1}{2} \right)^2 \right) \\ &= \frac{1}{8} \cdot 4n \cdot 2 \sum_{i=0}^{2n-1} (2n-2i-1)^2 = n \sum_{j=0}^{n} (2j+1)^2 = n \frac{(2n)^2(2n-1) - \sum_{j=1}^{n} (2j)^2}{3} - \sum(n). \end{align*} 

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{G4.} Let $ABCD$ be a quadrilateral inscribed in a circle $\Omega$. Let the tangent to $\Omega$ at $D$ intersect the rays $BA$ and $BC$ at points $E$ and $F$, respectively. A point $T$ is chosen inside the triangle $ABC$ so that $TE \parallel CD$ and $TF \parallel AD$. Let $K \ast D$ be a point on the segment $DF$ such that $TD=TK$. Prove that the lines $AC$, $DT$ and $BK$ intersect at one point.

\textbf{Solution 1.} Let the segments $TE$ and $TF$ cross $AC$ at $P$ and $Q$, respectively. Since $PE \parallel CD$ and $ED$ is tangent to the circumcircle of $ABCD$, we have
$$ \angle EPA = \angle DCA = \angle EDA, $$
and so the points $A$, $P$, $D$, and $E$ lie on some circle $\alpha$. Similarly, the points $C$, $Q$, $D$, and $F$ lie on some circle $\gamma$.

We now want to prove that the line $DT$ is tangent to both $\alpha$ and $\gamma$ at $D$. Indeed, since $\angle FCD + \angle EAD = 180^\circ$, the circles $\alpha$ and $\gamma$ are tangent to each other at $D$. To prove that $T$ lies on their common tangent line at $D$ (i.e., on their radical axis), it suffices to check that $TP \cdot TE = TQ \cdot TF$, or that the quadrilateral $PEFQ$ is cyclic. This fact follows from
$$ \angle QFE = \angle ADE = \angle APE. $$

Since $TD=TK$, we have $\angle TKD = \angle TDK$. Next, as $TD$ and $DE$ are tangent to $\alpha$ and $\Omega$, respectively, we obtain
$$ \angle TKD = \angle TDK = \angle EAD = \angle BDE, $$
which implies $TK \parallel BD$.

Next we prove that the five points $T$, $P$, $Q$, $D$, and $K$ lie on some circle $\tau$. Indeed, since $TD$ is tangent to the circle $\alpha$ we have
$$ \angle EPD = \angle TDF = \angle TKD, $$
which means that the point $P$ lies on the circle $(TDK)$. Similarly, we have $Q \in (TDK)$.

Finally, we prove that $PK \parallel BC$. Indeed, using the circles $\tau$ and $\gamma$ we conclude that
$$ \angle PKD = \angle PQD = \angle FDC, $$
which means that $PK \parallel BC$.

Triangles $TPK$ and $DCB$ have pairwise parallel sides, which implies the fact that $TD$, $PC$ and $KB$ are concurrent, as desired.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\textbf{G5.} Let $ABCD$ be a cyclic quadrilateral whose sides have pairwise different lengths. Let $O$ be the circumcentre of $ABCD$. The internal angle bisectors of $\angle ABC$ and $\angle ADC$ meet $AC$ at $B_1$ and $D_1$, respectively. Let $O_B$ be the centre of the circle which passes through $B$ and is tangent to $AC$ at $B_1$. Similarly, let $O_D$ be the centre of the circle which passes through $D$ and is tangent to $AC$ at $D_1$. Assume that $BD_1 \parallel DB_1$. Prove that $O$ lies on the line $O_B O_D$.

\textbf{Common remarks.} We introduce some objects and establish some preliminary facts common for all solutions below. Let $\Omega$ denote the circle $(ABCD)$, and let $\gamma_B$ and $\gamma_D$ denote the two circles from the problem statement (their centres are $O_B$ and $O_D$, respectively). Clearly, all three centres $O$, $O_B$, and $O_D$ are distinct.

Assume, without loss of generality, that $AB > BC$. Suppose that $AD > DC$, and let $H = AC \cap BD$. Then the rays $BB_1$ and $DD_1$ lie on one side of $BD$, as they contain the midpoints of the arcs $ADC$ and $ABC$, respectively. However, if $BD_1 \parallel DB_1$, then $B_1$ and $D_1$ should be separated by $H$. This contradiction shows that $AD < CD$.

Let $\gamma_B$ and $\gamma_D$ meet $\Omega$ again at $T_B$ and $T_D$, respectively. The common chord $BT_B$ of $\Omega$ and $\gamma_B$ is perpendicular to their line of centres $OO_B$; likewise, $DT_D \perp OO_D$. Therefore, $O \in O_B O_D \iff O_B O \parallel O_D O \iff BT_B \parallel DT_D$, and the problem reduces to showing that
$$ BT_B \parallel DT_D. \quad (1) $$

\textbf{Comment 1.} It seems that the discussion of the positions of points is necessary for both Solutions below. However, this part automatically follows from the angle chasing in Comment 2.

\textbf{Solution 1.} Let the diagonals $AC$ and $BD$ cross at $H$. Consider the homothety $h$ centred at $H$ and mapping $B$ to $D$. Since $BD_1 \parallel DB_1$, we have $h(D_1) = B_1$. Let the tangents to $\Omega$ at $B$ and $D$ meet $AC$ at $L_B$ and $L_D$, respectively. We have
$$ \angle L_B B B_1 = \angle L_B BC + \angle CBB_1 = \angle BAL_B + \angle B_1 BA = \angle B B_1 L_B, $$
which means that the triangle $L_B B B_1$ is isosceles, $L_B B = L_B B_1$. The powers of $L_B$ with respect to $\Omega$ and $\gamma_B$ are $L_B B^2$ and $L_B B_1^2$, respectively; so they are equal, whence $L_B$ lies on the radical axis $T_B D$ of those two circles. Similarly, $L_D$ lies on the radical axis $T_D B$ of $\Omega$ and $\gamma_B$.

By the sine rule in the triangle $BHL_B$, we obtain
$$ \frac{HL_B}{\sin \angle HBL_B} = \frac{BL_B}{\sin \angle BHL_B} = \frac{B_1 L_B}{\sin \angle BHL_B}; \quad (2) $$
similarly,
$$ \frac{HL_D}{\sin \angle HDL_D} = \frac{DL_D}{\sin \angle DHL_D} = \frac{D_1 L_D}{\sin \angle DHL_D}. \quad (3) $$
Clearly, $\angle BHL_B = \angle DHL_D$. In the circle $\Omega$, tangent lines $BL_B$ and $DL_D$ form equal angles with the chord $BD$, so $\sin \angle HBL_B = \sin \angle HDL_D$ (this equality does not depend on the picture). Thus, dividing (2) by (3) we get
$$ \frac{HL_B}{HL_D} = \frac{B_1 L_B}{D_1 L_D}, \quad \text{and hence} \quad \frac{HL_B}{HL_D} = \frac{HL_B - B_1 L_B}{HL_D - D_1 L_D} = \frac{HB_1}{HD_1}. $$
Since $h(D_1) = B_1$, the obtained relation yields $h(L_D) = L_B$, so $h$ maps the line $L_D B$ to $L_B D$, and these lines are parallel, as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{graphicx}

\begin{document}

\textbf{G6.} Determine all integers $n \ge 3$ satisfying the following property: every convex $n$-gon whose sides all have length 1 contains an equilateral triangle of side length 1. (Every polygon is assumed to contain its boundary.)

\textbf{Answer:} All odd $n \ge 3$.

\textbf{Solution.} First we show that for every even $n \ge 4$ there exists a polygon violating the required statement. Consider a regular $k$-gon $A_0 A_1 \dots A_{k-1}$ with side length 1. Let $B_1, B_2, \dots, B_{k-1}$ be the points symmetric to $A_1, A_2, \dots, A_{k-1}$ with respect to the line $A_0 A_{k/2}$. Then $P = A_0 A_1 A_2 \dots A_{k/2-1} B_{k/2-1} B_{k/2-2} \dots B_2 B_1$ is a convex $n$-gon whose sides all have length 1. If $k$ is big enough, $P$ is contained in a strip of width $1/2$, which clearly does not contain any equilateral triangle of side length 1.

Assume now that $n = 2k+1$. As the case $k=1$ is trivially true, we assume $k \ge 2$ henceforth. Consider a convex $(2k+1)$-gon $P$ whose sides all have length 1. Let $d$ be its longest diagonal. The endpoints of $d$ split the perimeter of $P$ into two polylines, one of which has length at least $k+1$. Hence we can label the vertices of $P$ so that $P = A_0 A_1 \dots A_t$ and $d=A_0 A_t$ with $t \le k+1$. We will show that, in fact, the polygon $A_0 A_1 \dots A_t$ contains an equilateral triangle of side length 1.

Suppose that $\angle A_0 A_t A_1 > 60^\circ$. Since $d$ is the longest diagonal, we have $A_1 A_t \le A_0 A_t$, so $\angle A_0 A_1 A_t > \angle A_0 A_t A_1 > 60^\circ$. It follows that there exists a point $X$ inside the triangle $A_0 A_1 A_t$ such that the triangle $A_0 A_1 X$ is equilateral, and this triangle is contained in $P$. Similar arguments apply if $\angle A_{t-1} A_0 A_t > 60^\circ$.

From now on, assume $\angle A_0 A_1 A_t < 60^\circ$ and $\angle A_{t-1} A_t A_0 < 60^\circ$. Consider an isosceles trapezoid $A_0 Y Z A_t$ such that $A_0 A_t \parallel YZ$, $A_0 Y=ZA_t=1$, and $\angle ZA_t Y = \angle YZA_t A_0 = 60^\circ$. Suppose that $A_0 A_1 \dots A_t$ is contained in $A_0 Y Z A_t$. Note that the perimeter of $A_0 A_1 \dots A_t$ equals $\ell + A_0 A_t$ and the perimeter of $A_0 Y Z A_t$ equals $2A_0 A_t + 1$.

Recall a well-known fact stating that if a convex polygon $P_1$ is contained in a convex polygon $P_2$, then the perimeter of $P_1$ is at most the perimeter of $P_2$. Hence we obtain
$$ \ell + A_0 A_t \le 2A_0 A_t + 1, \quad \text{i.e.} \quad \ell - 1 \le A_0 A_t. $$
On the other hand, the triangle inequality yields
$$ A_0 A_t < A_t A_1 + A_1 A_2 + \dots + A_{2k} A_0 = 2k+1 = \ell \le \ell-1, $$
which gives a contradiction. Therefore, there exists a vertex $A_m$ of $A_0 A_1 \dots A_t$ which lies outside $A_0 Y Z A_t$. Since $\angle A_0 A_1 A_t < 60^\circ = \angle A_0 Y$ and $\angle A_{t-1} A_t A_0 < 60^\circ = \angle ZA_t A_0 \quad (1)$ the distance between $A_m$ and $A_0 A_t$ is at least $\sqrt{3}/2$. Let $P$ be the projection of $A_m$ to $A_0 A_t$. Then $PA_m \ge \sqrt{3}/2$, and by (1) we have $A_0 P > 1/2$ and $PA_t > 1/2$. Choose points $Q \in A_0 P$, $R \in PA_t$, and $S \in PA_m$ such that $PQ=PR=1/2$ and $PS=\sqrt{3}/2$. Then $QRS$ is an equilateral triangle of side length 1 contained in $A_0 A_1 \dots A_t$.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{G7.} A point $D$ is chosen inside an acute-angled triangle $ABC$ with $AB > AC$ so that $\angle BAD = \angle DAC$. A point $E$ is constructed on the segment $AC$ so that $\angle ADE = \angle DCB$. Similarly, a point $F$ is constructed on the segment $AB$ so that $\angle ADF = \angle DBC$. A point $X$ is chosen on the line $AC$ so that $CX = BX$. Let $O_1$ and $O_2$ be the circumcentres of the triangles $ADC$ and $DXE$. Prove that the lines $BC$, $EF$, and $O_1 O_2$ are concurrent.

\textbf{Common remarks.} Let $Q$ be the isogonal conjugate of $D$ with respect to the triangle $ABC$. Since $\angle BAD = \angle DAC$, the point $Q$ lies on $AD$. Then $\angle QBA = \angle DBC = \angle FDA$, so the points $Q$, $D$, $F$, and $B$ are concyclic. Analogously, the points $Q$, $D$, $E$, and $C$ are concyclic. Thus $AF \cdot AB = AD \cdot AQ = AE \cdot AC$ and so the points $B$, $F$, $E$, and $C$ are also concyclic.

Let $T$ be the intersection of $BC$ and $FE$.

\textbf{Claim.} $TD^2 = TB \cdot TC = TF \cdot TE$.

\textbf{Proof.} We will prove that the circles $(DEF)$ and $(BDC)$ are tangent to each other. Indeed, using the above arguments, we get
\begin{align*} \angle BDF &= \angle AFD = \angle ABD = 180^\circ - \angle FAD - \angle FDA) - (\angle ABC - \angle DBC) \\ &= 180^\circ - \angle FAD - \angle ABC - 180^\circ - \angle DAE - \angle FEA - \angle FED + \angle ADE - \angle FED + \angle DCB, \end{align*} which implies the desired tangency.
Since the points $B$, $C$, $E$, and $F$ are concyclic, the powers of the point $T$ with respect to the circles $(BDC)$ and $(EDF)$ are equal. So their radical axis, which coincides with the common tangent at $D$, passes through $T$, and hence $TD^2 = TE \cdot TF = TB \cdot TC$. $\square$

\textbf{Solution 1.} Let $TA$ intersect the circle $(ABC)$ again at $M$. Due to the circles $(BCEF)$ and $(AMCB)$, and using the above Claim, we get $TM \cdot TA = TF \cdot TE = TB \cdot TC = TD^2$; in particular, the points $A$, $M$, $E$, and $F$ are concyclic.
Under the inversion with centre $T$ and radius $TD$, the point $M$ maps to $A$, and $B$ maps to $C$, which implies that the circle $(MBD)$ maps to the circle $(ADC)$. Their common point $D$ lies on the circle of the inversion, so the second intersection point $K$ also lies on that circle, which means $TK = TD$. It follows that the point $T$ and the centres of the circles $(KDE)$ and $(ADC)$ lie on the perpendicular bisector of $KD$.
Since the center of $(ADC)$ is $O_1$, it suffices to show now that the points $D$, $K$, $E$, and $X$ are concyclic (the center of the corresponding circle will be $O_2$). The lines $BM$, $DK$, and $AC$ are the pairwise radical axes of the circles $(ABCM)$, $(ACDCK)$ and $(BMDK)$, so they are concurrent at some point $P$. Also, $M$ lies on the circle $(AEF)$, thus
\begin{align*} \ast(EX,XB) &= \ast(CX,XB) = \ast(XC,BC) + \ast(BC,BX) - 2\ast(AC,CB) \\ &= \ast(AC,CB) + \ast(EF,FA) - \ast(AM,BM) + 2\ast(EM,MA) - \ast(EM,BM), \end{align*} so the points $M$, $E$, $X$, and $B$ are concyclic. Therefore, $PE \cdot PX = PM \cdot PB = PK \cdot PD$, so the points $E$, $K$, $D$, and $X$ are concyclic, as desired.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}

\begin{document}

\textbf{G8.} Let $\omega$ be the circumcircle of a triangle $ABC$, and let $\Omega_A$ be its excircle which is tangent to the segment $BC$. Let $X$ and $Y$ be the intersection points of $\omega$ and $\Omega_A$. Let $P$ and $Q$ be the projections of $A$ onto the tangent lines to $\Omega_A$ at $X$ and $Y$, respectively. The tangent line at $P$ to the circumcircle of the triangle $APX$ intersects the tangent line at $Q$ to the circumcircle of the triangle $AQY$ at a point $R$. Prove that $AR \perp BC$.

\textbf{Solution 1.} Let $D$ be the point of tangency of $BC$ and $\Omega_A$. Let $D'$ be the point such that $DD'$ is a diameter of $\Omega_A$. Let $R'$ be (the unique) point such that $AR' \perp BC$ and $R' D' \parallel BC$. We shall prove that $R$ coincides with $R$.

Let $PX$ intersect $AB$ and $D'R$ at $S$ and $T$, respectively. Let $U$ be the ideal common point of the parallel lines $BC$ and $D'R$. Note that the (degenerate) hexagon $ASXTUC$ is circumscribed around $\Omega_A$, hence by the Brianchon theorem $AT$, $SU$, and $XC$ concur at a point which we denote by $V$. Then $VS \parallel BC$. It follows that $\ast(SV,VX) = \ast(BC,CX) = \ast(BA,AX)$, hence $AXSV$ is cyclic. Therefore, $\ast(PX,XA) = \ast(SV,VA) = \ast(RT,TA)$. Since $\angle APT = \angle ART = 90^\circ$, the quadrilateral $APRT$ is cyclic. Hence,
$$ \ast(XA,AP) = 90^\circ - \ast(PX,XA) = 90^\circ - \ast(RT,TA) = \ast(TA,AR) = \ast(TP,PR). $$
It follows that $PR$ is tangent to the circle $(APX)$.

Analogous argument shows that $QR'$ is tangent to the circle $(AQY)$. Therefore, $R=R'$ and $AR \perp BC$.

\end{document}







"""