def geometry2022():
    return r"""




\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{Geometry}

\textbf{G1.} Let $ABCDE$ be a convex pentagon such that $BC = DE$. Assume there is a point $T$ inside $ABCDE$ with $TB = TD$, $TC = TE$ and $\angle TBA = \angle AET$. Let lines $CD$ and $CT$ intersect line $AB$ at points $P$ and $Q$, respectively, and let lines $CD$ and $DT$ intersect line $AE$ at points $R$ and $S$, respectively. Assume that points $P, B, A, Q$ and $R, E, A, S$ respectively, are collinear and occur on their lines in this order. Prove that the points $P, Q, R, S$ are concyclic.

\textit{(Slovakia)}

\textbf{Solution 1.} By the conditions we have $BC = DE$, $CT = ET$ and $TB = TD$, so the triangles $TBC$ and $TDE$ are congruent, in particular $\angle BTC = \angle DTE$.

In triangles $TBQ$ and $TES$ we have $\angle TBQ = \angle SET$ and $\angle QTB = 180^\circ - \angle BTC = 180^\circ - \angle DTE = \angle ETS$, so these triangles are similar to each other. It follows that $\angle TSE = \angle BQT$ and
$$ \frac{TD}{TQ} = \frac{TB}{TQ} = \frac{TE}{TS} = \frac{TC}{TS}. $$

By rearranging this relation we get $TD \cdot TS = TC \cdot TQ$, so $C, D, Q$ and $S$ are concyclic. (Alternatively, we can get $\angle CQD = \angle CSD$ from the similar triangles $TCS$ and $TDQ$.) Hence $\angle DCQ = \angle DSQ$.

Finally, from the angles of triangle $CQP$ we get
$$ \angle RPQ = \angle RCQ - \angle PQC = \angle DSQ - \angle DSR = \angle RSQ, $$
which proves that $P, Q, R$ and $S$ are concyclic.



\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G2.} In the acute-angled triangle $ABC$, the point $F$ is the foot of the altitude from $A$, and $P$ is a point on the segment $AF$. The lines through $P$ parallel to $AC$ and $AB$ meet $BC$ at $D$ and $E$, respectively. Points $X \neq A$ and $Y \neq A$ lie on the circles $ABD$ and $ACE$, respectively, such that $DA = DX$ and $EA = EY$.

Prove that $B, C, X$ and $Y$ are concyclic.

\textit{(Netherlands)}

\textbf{Solution 1.} Let $A'$ be the intersection of lines $BX$ and $CY$. By power of a point, it suffices to prove that $\overline{A'B} \cdot \overline{A'X} = \overline{A'C} \cdot \overline{A'Y}$, or, equivalently, that $A'$ lies on the radical axis of the circles $ABDX$ and $ACEY$.

From $DA = DX$ it follows that in circle $ABDX$, point $D$ bisects of one of the arcs $AX$. Therefore, depending on the order of points, the line $BC$ is either the internal or external bisector of $\angle ABX$. In both cases, line $BX$ is the reflection of $BA$ in line $BDC$. Analogously, line $CY$ is the reflection of $CA$ in line $BC$; we can see that $A'$ is the reflection of $A$ in line $BC$, so $A, F$ and $A'$ are collinear.

By $PD \parallel AC$ and $PE \parallel AB$ we have $\frac{FD}{FC} = \frac{FP}{FA} = \frac{FE}{FB}$, hence $FD \cdot FB = FE \cdot FC$. So, point $F$ has equal powers with respect to circles $ABDX$ and $ACEY$.

Point $A$, being a common point of the two circles, is another point with equal powers, so the radical axis of circles $ABDX$ and $ACEY$ is the altitude $AF$ that passes through $A'$.

\end{document}





\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G3.} Let $ABCD$ be a cyclic quadrilateral. Assume that the points $Q, A, B, P$ are collinear in this order, in such a way that the line $AC$ is tangent to the circle $ADQ$, and the line $BD$ is tangent to the circle $BCP$. Let $M$ and $N$ be the midpoints of $BC$ and $AD$, respectively. Prove that the following three lines are concurrent: line $CD$, the tangent of circle $ANQ$ at point $A$, and the tangent to circle $BMP$ at point $B$.

\textit{(Slovakia)}

\textbf{Solution 1.} We first prove that triangles $ADQ$ and $CDB$ are similar. Since $ABCD$ is cyclic, we have $\angle DAQ = \angle DCB$. By the tangency of $AC$ to the circle $AQD$ we also have $\angle CBD = \angle CAD = \angle AQD$. The claimed similarity is proven.

Let $R$ be the midpoint of $CD$. Points $N$ and $R$ correspond in the proven similarity, and so $\angle QNA = \angle BRC$.

Let $K$ be the second common point of line $CD$ with circle $ABR$ (i.e., if $CD$ intersects circle $ABR$, then $K \neq R$ is the other intersection; otherwise, if $CD$ is tangent to $CD$, then $K = R$). In both cases, we have $\angle BAK = \angle BRC = \angle QNA$; that indicates that $AK$ is tangent to circle $ANQ$. It can be showed analogously that $BK$ is tangent to circle $BMP$.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G4.} Let $ABC$ be an acute-angled triangle with $AC > AB$, let $O$ be its circumcentre, and let $D$ be a point on the segment $BC$. The line through $D$ perpendicular to $BC$ intersects the lines $AO$, $AC$ and $AB$ at $W$, $X$ and $Y$, respectively. The circumcircles of triangles $AXY$ and $ABC$ intersect again at $Z \neq A$.

Prove that if $OW = OD$, then $DZ$ is tangent to the circle $AXY$.

\textit{(United Kingdom)}

\textbf{Solution 1.} Let $AO$ intersect $BC$ at $E$. As $EDW$ is a right-angled triangle and $O$ is on $WE$, the condition $OW = OD$ means $O$ is the circumcentre of this triangle. So $OD = OE$ which establishes that $D, E$ are reflections in the perpendicular bisector of $BC$.

Now observe:
$$ 180^\circ - \angle DXZ = \angle ZXY = \angle ZAY = \angle ZCD, $$
which shows $CDXZ$ is cyclic.

We next show that $AZ \parallel BC$. To do this, introduce point $Z'$ on circle $ABC$ such that $AZ' \parallel BC$. By the previous result, it suffices to prove that $CDXZ'$ is cyclic. Notice that triangles $BAE$ and $CZ'D$ are reflections in the perpendicular bisector of $BC$. Using this and that $A, O, E$ are collinear:
$$ \angle DZ'C = \angle BAE = \angle BAO = 90^\circ - \frac{1}{2} \angle AOB = 90^\circ - \angle C = \angle DXC, $$
so $DXZ'C$ is cyclic, giving $Z = Z'$ as desired.

Using $AZ \parallel BC$ and $CDXZ$ cyclic we get:
$$ \angle AZD = \angle CDZ = \angle CXZ = \angle AYZ, $$
which by the converse of alternate segment theorem shows $DZ$ is tangent to circle $AXY$.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G5.} Let $ABC$ be a triangle, and let $\ell_1$ and $\ell_2$ be two parallel lines. For $i = 1, 2$, let $\ell_i$ meet the lines $BC, CA, AB$ at $X_i, Y_i, Z_i$, respectively. Suppose that the line through $X_i$ perpendicular to $BC$, the line through $Y_i$ perpendicular to $CA$, and finally the line through $Z_i$ perpendicular to $AB$, determine a non-degenerate triangle $\Delta_i$.

Show that the circumcircles of $\Delta_1$ and $\Delta_2$ are tangent to each other.

\textit{(Vietnam)}

\textbf{Solution 1.} Throughout the solutions, $\measuredangle (p, q)$ will denote the directed angle between lines $p$ and $q$, taken modulo $180^\circ$.

Let the vertices of $\Delta_i$ be $D_i, E_i, F_i$, such that lines $E_i F_i, F_i D_i$ and $D_i E_i$ are the perpendiculars through $X_i, Y_i$ and $Z_i$, respectively, and denote the circumcircle of $\Delta_i$ by $\omega_i$.

In triangles $D_1 Y_1 Z_1$ and $D_2 Y_2 Z_2$ we have $Y_1 Z_1 \parallel Y_2 Z_2$ because they are parts of $\ell_1$ and $\ell_2$. Moreover, $D_1 Y_1 \parallel D_2 Y_2$ are perpendicular to $AC$ and $D_1 Z_1 \parallel D_2 Z_2$ are perpendicular to $AB$, so the two triangles are homothetic and their homothetic centre is $Y_1 Y_2 \cap Z_1 Z_2 = A$. Hence line $D_1 D_2$ passes through $A$. Analogously, line $E_1 E_2$ passes through $B$ and $F_1 F_2$ passes through $C$.

The corresponding sides of $\Delta_1$ and $\Delta_2$ are parallel, because they are perpendicular to the respective sides of triangle $ABC$. Hence, $\Delta_1$ and $\Delta_2$ are either homothetic, or they can be translated to each other. Using that $B, X_2, Z_2$ and $E_2$ are concyclic, $C, X_2, Y_2$ and $F_2$ are concyclic, $Z_2 E_2 \perp AB$ and $Y_2 F_2 \perp AC$ we can calculate
\begin{align*}
    \measuredangle (E_1 E_2, F_1 F_2) &= \measuredangle (E_1 E_2, X_1 X_2) + \measuredangle (X_1 X_2, F_1 F_2) = \measuredangle (B E_2, B X_2) + \measuredangle (C X_2, C F_2) \\
    &= \measuredangle (Z_2 E_2, Z_2 X_2) + \measuredangle (Y_2 X_2, Y_2 F_2) = \measuredangle (Z_2 E_2, \ell_2) + \measuredangle (\ell_2, Y_2 F_2) \\
    &= \measuredangle (Z_2 E_2, Y_2 F_2) = \measuredangle (AB, AC) \neq 0,
\end{align*}
and conclude that lines $E_1 E_2$ and $F_1 F_2$ are not parallel. Hence, $\Delta_1$ and $\Delta_2$ are homothetic; the lines $D_1 D_2, E_1 E_2$, and $F_1 F_2$ are concurrent at the homothetic centre of the two triangles. Denote this homothetic centre by $H$.

For $i = 1, 2$, using (1), and that $A, Y_i, Z_i$ and $D_i$ are concyclic,
\begin{align*}
    \measuredangle (HE_i, HF_i) &= \measuredangle (E_1 E_2, F_1 F_2) = \measuredangle (AB, AC) \\
    &= \measuredangle (AZ_i, AY_i) = \measuredangle (D_i Z_i, D_i Y_i) = \measuredangle (D_i E_i, D_i F_i),
\end{align*}
so $H$ lies on circle $\omega_i$.

The same homothety that maps $\Delta_1$ to $\Delta_2$ sends $\omega_1$ to $\omega_2$ as well. Point $H$, that is the centre of the homothety, is a common point of the two circles. That finishes proving that $\omega_1$ and $\omega_2$ are tangent to each other.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G6.} In an acute-angled triangle $ABC$, point $H$ is the foot of the altitude from $A$. Let $P$ be a moving point such that the bisectors $k$ and $\ell$ of angles $PBC$ and $PCB$, respectively, intersect each other on the line segment $AH$. Let $k$ and $AC$ meet at $E$, $\ell$ and $AB$ meet at $F$, and let $EF$ and $AH$ meet at $Q$. Prove that, as $P$ varies, the line $PQ$ passes through a fixed point.

\textit{(Iran)}

\textbf{Solution 1.} Let the reflections of the line $BC$ with respect to the lines $AB$ and $AC$ intersect at point $K$. We will prove that $P, Q$ and $K$ are collinear, so $K$ is the common point of the varying line $PQ$.

Let lines $BE$ and $CF$ intersect at $I$. For every point $O$ and $d > 0$, denote by $(O, d)$ the circle centred at $O$ with radius $d$, and define $\omega_I = (I, IH)$ and $\omega_A = (A, AH)$. Let $\omega_K$ and $\omega_P$ be the incircle of triangle $KBC$ and the $P$-excircle of triangle $PBC$, respectively.

Since $IH \perp BC$ and $AH \perp BC$, the circles $\omega_A$ and $\omega_I$ are tangent to each other at $H$. So, $H$ is the external homothetic centre of $\omega_A$ and $\omega_I$. From the complete quadrangle $BCEF$ we have $(A, I; Q, H) = -1$, therefore $Q$ is the internal homothetic centre of $\omega_A$ and $\omega_I$. Since $BA$ and $CA$ are the external bisectors of angles $\angle KBC$ and $\angle KCB$, circle $\omega_K$ is the $K$-excircle in triangle $BKC$. Hence, $K$ is the external homothetic centre of $\omega_I$ and $\omega_K$. Also it is clear that $P$ is the external homothetic centre of $\omega_I$ and $\omega_P$. Let point $T$ be the tangency point of $\omega_P$ and $BC$, and let $T'$ be the tangency point of $\omega_K$ and $BC$. Since $\omega_K$ is the incircle and $\omega_P$ is the $P$-excircle of $PBC$, $TC = BH$ and since $\omega_K$ is the incircle and $\omega_A$ is the $K$-excircle of $KBC$, $T'C = BH$. Therefore $TC = T'C$ and $T = T'$. It yields that $\omega_K$ and $\omega_P$ are tangent to each other at $T$.

Let point $S$ be the internal homothetic centre of $\omega_A$ and $\omega_P$, and let $S'$ be the internal homothetic centre of $\omega_I$ and $\omega_K$. It's obvious that $S$ and $S'$ lie on $BC$. We claim that $S = S'$.

To prove our claim, let $r_A, r_I, r_P$, and $r_K$ be the radii of $\omega_A$, $\omega_I$, $\omega_P$ and $\omega_K$, respectively. It is well known that if the sides of a triangle are $a, b, c$, its semiperimeter is $s = (a + b + c) / 2$, and the radii of the incircle and the $a$-excircle are $r$ and $r_a$, respectively, then $r \cdot r_a = (s-b)(s-c)$. Applying this fact to triangle $PBC$ we get $r_I \cdot r_P = BH \cdot CH$. The same fact in triangle $KCB$ yields $r_K \cdot r_A = CT \cdot BT$. Since $BH = CT$ and $BT = CH$, from these two we get
$$ \frac{HS}{ST} = \frac{r_A}{r_P} = \frac{r_I}{r_K} = \frac{HS'}{S'T}, $$
so $S = S'$ indeed.

Finally, by applying the generalised Monge's theorem to the circles $\omega_A, \omega_I$, and $\omega_K$ (with two pairs of internal and one pair of external common tangents), we can see that points $Q, S$ and $K$ are collinear. Similarly one can show that $Q, S$ and $P$ are collinear, and the result follows.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G7.} Let $ABC$ and $A'B'C'$ be two triangles having the same circumcircle $\omega$, and the same orthocentre $H$. Let $\Omega$ be the circumcircle of the triangle determined by the lines $AA', BB'$ and $CC'$. Prove that $H$, the centre of $\omega$, and the centre of $\Omega$ are collinear.

\textit{(Denmark)}

\textbf{Solution.} In what follows, $\measuredangle (p, q)$ will denote the directed angle between lines $p$ and $q$, taken modulo $180^\circ$. Denote by $O$ the centre of $\omega$. In any triangle, the homothety with ratio $-\frac{1}{2}$ centred at the centroid of the triangle takes the vertices to the midpoints of the opposite sides and it takes the orthocentre to the circumcentre. Therefore the triangles $ABC$ and $A'B'C'$ share the same centroid $G$ and the midpoints of their sides lie on a circle $\rho$ with centre on $OH$. We will prove that $\omega, \Omega$, and $\rho$ are coaxial, so in particular it follows that their centres are collinear on $OH$.

Let $D = BB' \cap CC'$, $E = CC' \cap AA'$, $F = AA' \cap BB'$, $S = BC \cap B'C'$, and $T = BC' \cap B'C$. Since $D, S$, and $T$ are the intersections of opposite sides and of the diagonals in the quadrilateral $BB'CC'$ inscribed in $\omega$, by Brocard's theorem triangle $DST$ is self-polar with respect to $\omega$, i.e. each vertex is the pole of the opposite side. We apply this in two ways.

First, from $D$ being the pole of $ST$ it follows that the inverse $D*$ of $D$ with respect to $\omega$ is the projection of $D$ onto $ST$. In particular, $D*$ lies on the circle with diameter $SD$. If $N$ denotes the midpoint of $SD$ and $R$ the radius of $\omega$, then the power of $O$ with respect to this circle is $ON^2 - ND^2 = OD \cdot OD* = R^2$. By rearranging, we see that $ND^2$ is the power of $N$ with respect to $\omega$.

Second, from $T$ being the pole of $SD$ it follows that $OT$ is perpendicular to $SD$. Let $M$ and $M'$ denote the midpoints of $BC$ and $B'C'$. Then since $OM \perp BC$ and $OM' \perp B'C'$ it follows that $OMMT'$ is cyclic and
$$ \measuredangle (SD, BC) = \measuredangle (OT, OM) = \measuredangle (B'C', MM'). $$
From $BB'CC'$ being cyclic we also have $\measuredangle (BC, BB') = \measuredangle (CC', B'C')$, hence we obtain
\begin{align*}
    \measuredangle (SD, BB') &= \measuredangle (SD, BC) + \measuredangle (BC, BB') \\
    &= \measuredangle (B'C', MM') + \measuredangle (CC', B'C') = \measuredangle (CC', MM').
\end{align*}

Now from the homothety mentioned in the beginning, we know that $MM'$ is parallel to $AA'$, hence the above implies that $\measuredangle (SD, BB') = \measuredangle (CC', AA')$, which shows that $\Omega$ is tangent to $SD$ at $D$. In particular, $ND^2$ is also the power of $N$ with respect to $\Omega$.

Additionally, from $BB'CC'$ being cyclic it follows that triangles $DBC$ and $DC'B'$ are inversely similar, so $\measuredangle (BB', DM') = \measuredangle (DM, CC')$. This yields
\begin{align*}
    \measuredangle (SD, DM') &= \measuredangle (SD, BB') + \measuredangle (BB', DM') \\
    &= \measuredangle (CC', MM') + \measuredangle (DM, CC') = \measuredangle (DM, MM'),
\end{align*}
which shows that the circle $DMM'$ is also tangent to $SD$. Since $N, M$, and $M'$ are collinear on the Newton-Gauss line of the complete quadrilateral determined by the lines $BB', CC', BC,$ and $B'C'$, it follows that $ND^2 = NM \cdot NM'$. Hence $N$ has the same power with respect to $\omega, \Omega$, and $\rho$.

By the same arguments there exist points on the tangents to $\omega, \Omega$ at $E$ and $F$ which have the same power with respect to $\omega, \Omega$, and $\rho$. The tangents to a given circle at three distinct points cannot be concurrent, hence we obtain at least two distinct points with the same power with respect to $\omega, \Omega$, and $\rho$. Hence the three circles are coaxial, as desired.

\end{document}






\documentclass{article}
\usepackage{amsmath}

\begin{document}

\textbf{G8.} Let $AA'BCC'B'$ be a convex cyclic hexagon such that $AC$ is tangent to the incircle of the triangle $A'B'C'$, and $A'C'$ is tangent to the incircle of the triangle $ABC$. Let the lines $AB$ and $A'B'$ meet at $X$ and let the lines $BC$ and $B'C'$ meet at $Y$.

Prove that if $XBYB'$ is a convex quadrilateral, then it has an incircle.

\textit{(Australia)}

\textbf{Solution.} Denote by $\omega$ and $\omega'$ the incircles of $\triangle ABC$ and $\triangle A'B'C'$ and let $I$ and $I'$ be the centres of these circles. Let $N$ and $N'$ be the second intersections of $BI$ and $B'I'$ with $\Omega$, the circumcircle of $A'BCC'B'A$, and let $O$ be the centre of $\Omega$. Note that $ON \perp AC$, $ON' \perp A'C'$ and $ON = ON'$ so $NN'$ is parallel to the angle bisector $II'$ of $AC$ and $A'C'$. Thus $II' \parallel NN'$ which is antiparallel to $BB'$ with respect to $BI$ and $B'I'$. Therefore $B, I, I', B'$ are concyclic.

Further define $P$ as the intersection of $AC$ and $A'C'$ and $M$ as the antipode of $N'$ in $\Omega$. Consider the circle $\Gamma_1$ with centre $N$ and radius $NA = NC$ and the circle $\Gamma_2$ with centre $M$ and radius $MA' = MC'$. Their radical axis passes through $P$ and is perpendicular to $MN \perp NN' \parallel II' \perp IP$, so $I$ lies on their radical axis. Therefore, since $I$ lies on $\Gamma_1$, it must also lie on $\Gamma_2$. Thus, if we define $Z$ as the second intersection of $MI$ with $\Omega$, we have that $I$ is the incentre of triangle $ZA'C'$. (Note that the point $Z$ can also be constructed directly via Poncelet's porism.)

Consider the incircle $\omega_c$ with centre $I_c$ of triangle $C'B'Z$. Note that $\angle ZIC' = 90^\circ + \frac{1}{2} \angle ZA'C' = 90^\circ + \frac{1}{2} \angle ZB'C' = \angle ZI_cC'$ so $Z, I, I_c, C'$ are concyclic. Similarly $B', I', I_c', C'$ are concyclic.

The external centre of dilation from $\omega$ to $\omega_c$ is the intersection of $II_c$ and $C'Z$ ($D$ in the picture), that is the radical centre of circles $\Omega, C'I_cIZ$ and $II'I_c$. Similarly, the external centre of dilation from $\omega'$ to $\omega_c$ is the intersection of $I'I_c$ and $B'C'$ ($D'$ in the picture), that is the radical centre of circles $\Omega, B'I'I_c'$ and $II'I_c$. Therefore the Monge line of $\omega, \omega'$ and $\omega_c$ is line $DD'$, and the radical axis of $\Omega$ and circle $II'I_c$ coincide. Hence the external centre $T$ of dilation from $\omega$ to $\omega'$ is also on the radical axis of $\Omega$ and circle $II'I_c$.

Now since $B, I, I', B'$ are concyclic, the intersection $T'$ of $BB'$ and $II'$ is on the radical axis of $\Omega$ and circle $II'I_c$. Thus $T' = T$ and $T$ lies on line $BB'$. Finally, construct a circle $\Omega_0$ tangent to $A'B', B'C', AB$ on the same side of these lines as $\omega'$. The centre of dilation from $\omega'$ to $\Omega_0$ is $B'$, so by Monge's theorem the external centre of dilation from $\Omega$ to $\omega$ must be on the line $TBB'$. However, it is on line $AB$, so it must be $B$ and $BC$ must be tangent to $\Omega_0$ as desired.

\end{document}








"""