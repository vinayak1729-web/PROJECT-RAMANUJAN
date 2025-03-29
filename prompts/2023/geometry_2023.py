def geometry_2023():
    return r"""

\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G1.} Let $ABCDE$ be a convex pentagon such that $\angle ABC = \angle AED = 90^{\circ}$. Suppose that the midpoint of $CD$ is the circumcentre of triangle $ABE$. Let $O$ be the circumcentre of triangle $ACD$.

Prove that line $AO$ passes through the midpoint of segment $BE$.

(Slovakia)

\textbf{Solution 1 (Area Ratio).}

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

Let $M$ be the midpoint of $CD$ and $X = BC \cap ED$. Since $\angle ABX = \angle AEX = 90^{\circ}$, $AX$ is a diameter of the circumcircle of $\triangle ABE$, so the midpoint of $AX$ is the circumcentre of $\triangle ABE$. Therefore, the midpoint of $AX$ coincides with $M$. This means $ACXD$ is a parallelogram and in particular, $AD \parallel BC$ and $AC \parallel ED$.

We denote the area of $\triangle P_1 P_2 P_3$ by $[P_1 P_2 P_3]$. To prove that line $AO$ bisects $BE$, it suffices to show $[OAB] = [OAE]$.

Let $C', D'$ be the midpoints of $AC, AD$ respectively. Since $OD' \perp AD$, $AD \parallel BC$, and $BC \perp AB$, we have $AB \parallel OD'$, so $[OAB] = [D'AB]$. Using $AD \parallel BC$ again, we have $[D'AB] = [D'AC]$. Therefore
\[ [OAB] = [D'AB] = [D'AC] = \frac{1}{2} [ACD]. \]

Similarly,
\[ [OAE] = [C'AE] = [C'AD] = \frac{1}{2} [ACD]. \]

Combining these gives $[OAB] = [OAE]$.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G2.} Let $ABC$ be a triangle with $AC > BC$. Let $\omega$ be the circumcircle of triangle $ABC$ and let $r$ be the radius of $\omega$. Point $P$ lies on segment $AC$ such that $BC = CP$ and point $S$ is the foot of the perpendicular from $P$ to line $AB$. Let ray $BP$ intersect $\omega$ again at $D$ and let $Q$ lie on line $SP$ such that $PQ = r$ and $S,P,Q$ lie on the line in that order. Finally, let the line perpendicular to $CQ$ from $A$ intersect the line perpendicular to $DQ$ from $B$ at $E$.

Prove that $E$ lies on $\omega$.

(Iran)

\textbf{Solution 1 (Similar Triangles).}

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

First observe that
\[ \angle DPA = \angle BPC \overset{CP=CB}{=} \angle CBP = \angle CBD = \angle CAD = \angle PAD \]
so $DP = DA$. Thus there is a symmetry in the problem statement swapping $(A,D) \leftrightarrow (B,C)$.

Let $O$ be the centre of $\omega$ and let $E$ be the reflection of $P$ in $CD$ which, by
\[ \angle CED = \angle DPC = 180^{\circ} - \angle CPB \overset{CP=CB}{=} 180^{\circ} - \angle PBC = 180^{\circ} - \angle DBC \]
lies on $\omega$. We claim the two lines concur at $E$. By the symmetry noted above, it suffices to prove that $BE \perp DQ$ and then $AE \perp CQ$ will follow by symmetry.

We have $AO = PQ$, $AD = DP$ and
\[ \angle DAO = 90^{\circ} - \angle ABD \overset{PQ \parallel AB}{=} \angle DPQ. \]

Hence $\triangle AOD \cong \triangle PQD$. Thus
\[ \angle QDB + \angle DBE = \angle ODA + \angle DAE \overset{DE=DA}{=} \angle ODA + \angle AED = (90^{\circ} - \angle AED ) + \angle AED = 90^{\circ} \]
giving $BE \perp DQ$ as required.

\end{document}





\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G3.} Let $ABCD$ be a cyclic quadrilateral with $\angle BAD < \angle ADC$. Let $M$ be the midpoint of the arc $CD$ not containing $A$. Suppose there is a point $P$ inside $ABCD$ such that $\angle ADB = \angle CPD$ and $\angle ADP = \angle PCB$.

Prove that lines $AD, PM, BC$ are concurrent.

(Slovakia)

\textbf{Solution 1.} Let $X$ and $Y$ be the intersection points of $AM$ and $BM$ with $PD$ and $PC$ respectively. Since $ABCMD$ is cyclic and $CM = MD$, we have
\[ \angle XAD = \angle MAD = \angle CBM = \angle CBY. \]
Combining this with $\angle ADX = \angle YCB$, we get $\angle DXA = \angle BYC$, and so $\angle PXM = \angle MYP$. Moreover, $\angle YPX = \angle CPD = \angle ADB = \angle AMB$. The quadrilateral $MXPY$ therefore has equal opposite angles and so is a parallelogram.

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

Let $R$ and $S$ be the intersection points of $AM$ and $BM$ with $BC$ and $AD$ respectively. Due to $AM \parallel PC$ and $BM \parallel PD$, we have $\angle ASB = \angle ADB = \angle PCB = \angle ARB$ and so the quadrilateral $ABRS$ is cyclic. We then have $\angle SRB = 180^{\circ} - \angle BAS = \angle DCB$ and so $SR \parallel CD$. In triangles $PCD$ and $MRS$, the corresponding sides are parallel so they are homothetic meaning lines $DS, PM, CR$ concur at the centre of this homothety.
\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G4.} Let $ABC$ be an acute-angled triangle with $AB < AC$. Denote its circumcircle by $\Omega$ and denote the midpoint of arc $CAB$ by $S$. Let the perpendicular from $A$ to $BC$ meet $BS$ at $D$ and $E \neq A$ respectively. Let the line through $D$ parallel to $BC$ meet line $BE$ at $L$ and denote the circumcircle of triangle $BDL$ by $\omega$. Let $\omega$ meet $\Omega$ again at $P \neq B$.

Prove that the line tangent to $\omega$ at $P$, and line $BS$ intersect on the internal bisector of $\angle BAC$.

(Portugal)

\textbf{Solution 1 (Triangles in Perspective).} Let $S'$ be the midpoint of arc $BC$ of $\Omega$, diametrically opposite to $S$ so $SS'$ is a diameter in $\Omega$ and $AS'$ is the angle bisector of $\angle BAC$. Let the tangent of $\omega$ at $P$ meet $\Omega$ again at $Q \neq P$, then we have $\angle SQS' = 90^{\circ}$.

We will show that triangles $APD$ and $S'QS$ are similar and their corresponding sides are parallel. Then it will follow that the lines connecting the corresponding vertices, namely line $AS'$, that is the angle bisector of $\angle BAC$, line $PQ$, that is the tangent to $\omega$ at $P$, and line $DS$ are concurrent. Note that the sides $AD$ and $SS'$ have opposite directions, so the three lines cannot be parallel.

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

First we show that $AP \perp DP$. Indeed, from cyclic quadrilaterals $APBE$ and $DPLB$ we can see that
\[ \angle PAD = \angle PAE = 180^{\circ} - \angle EBP = \angle PBL = \angle PDL = 90^{\circ} - \angle ADP. \]

Then, in triangle $APD$ we have $\angle DPA = 180^{\circ} - \angle PAD - \angle ADP = 90^{\circ}$.

Now we can see that:

*   Both lines $ADE$ and $SS'$ are perpendicular to $BC$, so $AD \parallel S'S$.
*   Line $PQ$ is tangent to circle $\omega$ at $P$ so $\angle DPQ = \angle DBP = \angle SBP = \angle S'QP$; it follows that $PD \parallel QS$.
*   Finally, since $AP \perp PD \parallel QS \perp S'Q$, we have $AP \parallel S'Q$ as well.

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G5.} Let $ABC$ be an acute-angled triangle with circumcircle $\omega$ and circumcentre $O$. Points $D \neq B$ and $E \neq C$ lie on $\omega$ such that $BD \perp AC$ and $CE \perp AB$. Let $CO$ meet $AB$ at $X$, and $BO$ meet $AC$ at $Y$.

Prove that the circumcircles of triangles $BXD$ and $CYE$ have an intersection on line $AO$.

(Malaysia)

\textbf{Solution 1 (Reflections).}

Note that $AO = OC$ implies the lines $AO$, $XO$ are reflections of each other about the line parallel to $AC$ through $O$, which is the perpendicular bisector of $BD$. Call this line $\ell$.

Let $P \neq X$ be the second intersection of circle $\odot BXD$ with line $XO$, and let $Z$ be the intersection of circle $\odot BXD$ with line $AO$ furthest from $A$.

Consider a reflection across $\ell$. This maps $B$ to $D$, $AO$ to $XO$, and circle $\odot BXD$ to itself so the transformation must map $P$, the intersection of $XO$ and circle $\odot BXD$, to the intersection of $AO$ and $\odot BXD$ furthest from $A$ i.e. $Z$. Thus we have

\[ \angle OZB = \angle DPO = \angle DPX = \angle DBX = 90^{\circ} - \angle BAC = \angle OCB \]

which implies $BOCZ$ is cyclic.

Therefore the second intersection of circle $\odot BOC$ with line $AO$ lies on circle $\odot BXD$. Similarly, $Z$ lies on circle $\odot CYE$ so the two circles have common point $Z$ on $AO$.

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G6.} Let $ABC$ be an acute-angled triangle with circumcircle $\omega$. A circle $\Gamma$ is internally tangent to $\omega$ at $A$ and also tangent to $BC$ at $D$. Let $AB$ and $AC$ intersect $\Gamma$ at $P$ and $Q$ respectively. Let $M$ and $N$ be points on line $BC$ such that $B$ is the midpoint of $DM$ and $C$ is the midpoint of $DN$. Lines $MP$ and $NQ$ meet at $K$ and intersect $\Gamma$ again at $I$ and $J$ respectively. The ray $KA$ meets the circumcircle of triangle $IJK$ at $X \neq K$.

Prove that $\angle BXP = \angle CXQ$.

(United Kingdom)

\textbf{Solution 1 (Similar Triangles).}

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

Let $MP$ and $NQ$ intersect $AD$ at $K_1$ and $K_2$ respectively. By applying Menelaus' theorem to triangle $ABD$ and line $MPK_1$, we have
\[ \frac{AK_1}{K_1 D} \cdot \frac{AP}{PB} \cdot \frac{BM}{MD} = 1 \implies \frac{AK_1}{K_1 D} = \frac{AP}{2PB} \]
and similarly
\[ \frac{AK_2}{K_2 D} = \frac{AQ}{2QC}. \]
A homothety at $A$ takes $\Gamma \to \omega$ and $D$ to the midpoint of arc $BC$ not containing $A$, so $PQ \parallel BC$ and $AD$ bisects $\angle BAC$. Thus
\[ \frac{AK_1}{K_1 D} = \frac{AP}{2PB} = \frac{AQ}{2QC} = \frac{AK_2}{K_2 D} \]
which implies $K_1 = K_2$, and $K$ lies on $AD$.

Then we obtain
\[ \angle JXD = \angle JXK = \angle JIK = \angle JIP = \angle JQP = \angle JND \]

where the last equality follows from $PQ \parallel BC$. This shows $JXND$ is cyclic and hence
\[ \angle DXN = \angle DJN = \angle DJQ = \angle DAQ = \angle DAC \]

\end{document}






\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G7.} Let $ABC$ be an acute, scalene triangle with orthocentre $H$. Let $\ell_a$ be the line through the reflection of $B$ with respect to $CH$ and the reflection of $C$ with respect to $BH$. Lines $\ell_b$ and $\ell_c$ are defined similarly. Suppose lines $\ell_a, \ell_b$ and $\ell_c$ determine a triangle $T$.

Prove that the orthocentre of $T$, the circumcentre of $T$ and $H$ are collinear.

(Ukraine)

\textbf{Solution 1.}

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

We write $\triangle P_1 P_2 P_3 \overset{\sim}{\longrightarrow} \triangle Q_1 Q_2 Q_3$ (resp. $\triangle P_1 P_2 P_3 \overset{\approx}{\longrightarrow} \triangle Q_1 Q_2 Q_3$) to indicate that two triangles are directly (resp. oppositely) similar. We use directed angles throughout denoted with $\angle$.

Denote by $A_b, A_c$ the reflections of $A$ in $BH$ and $CH$ respectively. $B_i, B_c$ and $C_b, C_a$ are defined similarly. By definition, $\ell_a = B_cC_b, \ell_b = C_aA_c, \ell_c = A_bB_c$. Let $A_1 = \ell_b \cap \ell_c, B_1 = \ell_c \cap \ell_a, C_1 = \ell_a \cap \ell_b$ and let $O_1, H_1$ be the orthocentre and circumcentre of $T = \triangle A_1 B_1 C_1$ respectively.

Claim 1. $\triangle AA_bA_c \overset{\sim}{\longrightarrow} \triangle ABC$.

\textbf{Proof.} Let $P = BH \cap AC, Q = CH \cap AB$, then it is well known that $\triangle APQ \overset{\sim}{\longrightarrow} \triangle ABC$. By the dilation with factor 2 centred at $A$, $\triangle APQ$ is sent to $\triangle AA_bA_c$, so we have $\triangle AA_bA_c \overset{\sim}{\longrightarrow} \triangle ABC$. \qed

Claim 2. $\triangle AA_bA_c \overset{\approx}{\longrightarrow} \triangle A B_cC_b$, and $A_1$ lies on the circumcircle of $\triangle AA_bA_c$ which is centred at $H$.

\textbf{Proof.} Since $B_c, C_b$ are reflections of $B, C$ in $AH$, we have $\triangle AB_cC_b \overset{\approx}{\longrightarrow} \triangle ABC$. Combining this with Claim 1, we have $\triangle AA_bA_c \overset{\approx}{\longrightarrow} \triangle AB_cC_b$, where $A$ is the centre of this similarity. Therefore, $\angle A_1A_bA_c = \angle A_aA_bA$ meaning $A_1$ lies on $\odot AA_bA_c$. By symmetry, $HA_b = HA_c = HA$, so $H$ is the centre of this circle. \qed

Claim 3. $\triangle A_1B_1C_1 \overset{\sim}{\longrightarrow} \triangle ABC$.

\textbf{Proof.} From Claim 2 we have

\[ \angle C_1 A_1 B_1 = \angle A_b A_1 A_c \overset{Claim 2}{=} \angle A_b A A_c = -\angle CAB \]

and similarly $\angle A_1 B_1 C_1 = -\angle ABC, \angle B_1 C_1 A_1 = -\angle BCA$, which imply $\triangle A_1 B_1 C_1 \overset{\sim}{\longrightarrow} \triangle ABC$. \qed

Denote the ratio of similitude of $\triangle A_1 B_1 C_1$ and $\triangle ABC$ by $\lambda (=-\frac{R}{2R})$, then

\[ \lambda = \frac{H_1 A_1}{HA} = \frac{H_1 B_1}{HB} = \frac{H_1 C_1}{HC}. \]

Since $HA \cdot HA_1$ and similarly $HB\cdot HB_1 = HC \cdot HC_1$ from Claim 2, we get

\[ \lambda = \frac{H_1 A_1}{HA} = \frac{H_1 B_1}{HB} = \frac{H_1 C_1}{HC} .\]

Therefore, the circle $A_1B_1C_1$ is the Apollonian circle of the segment $HH_1$ with ratio $\lambda$ so the line $HH_1$ passes through $O_1$. \qed
\end{document}







\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}

\begin{document}

\textbf{G8.} Let $ABC$ be an equilateral triangle. Points $A_1, B_1, C_1$ lie inside triangle $ABC$ such that triangle $A_1 B_1 C_1$ is scalene. $\angle BA_1C = \angle ACB_1A = \angle BCA_1B = 40^\circ$.

Prove that the circumcircles of triangles $AA_1A_2$, $BB_1B_2$, $CC_1C_2$ have two common points.
Lines $BC_1$ and $CB_1$ intersect at $A_2$, lines $CA_1$ and $AC_1$ intersect at $B_2$ and lines $AB_1$ and $BA_1$ intersect at $C_2$.
Prove that the circumcircles of triangles $AA_1A_2, BB_1B_2, CC_1C_2$ have two common points.

(U.S.A.)

\textbf{Solution.} Let $\kappa_a, \kappa_b, \kappa_c$ be the circumcircles of $\triangle AA_1A_2, \triangle BB_1B_2, \triangle CC_1C_2$. The general strategy of the solution is to find two different points having equal power with respect to $\kappa_a, \kappa_b, \kappa_c.$

Claim 1. $A$ is the circumcentre of $A_1B_1C_1$ and cyclic variations.

\textbf{Proof.} Since $AA_1$ lies on the perpendicular bisector of $BC$ and inside $\angle BA_1C$, it suffices to prove $\angle BA_1C = 2\angle BAC$. This follows from
\begin{align*}
    \angle BA_1C &= \frac{1}{2}(\angle B_1 A_1 A + \angle ABA_1) \\
    &= \frac{1}{2}(180^{\circ} - \angle A C_1 B) + (180^{\circ} - \angle CA B_1) + 60 \\
    &= \frac{1}{2}(180^{\circ} - \frac{1}{2}(180^{\circ} - \angle ACB_1A)) + \frac{1}{2}(180^{\circ} - \angle BA C_1 A) \\
    &= \frac{1}{2} \angle BA_1C.
\end{align*}
\qed

\begin{center}
    \begin{picture}(200,150)
        \put(100,75){\line(1,0){0}} % Placeholder for diagram
        % Add your tikz or other code to draw the diagram here
    \end{picture}
\end{center}

The circumcircles therefore give:

\[ \angle B_1 B B_2 = \angle B_1 B_1 B_2 = \angle C B_1 A = \angle CBC_1=\angle ACB_1 = \angle BAC, \]
Libertas $\odot AB_cC_a$ and $\odot BC_aA_b$ and $\odot CA_bB_c$ and Aubel's are cyclic. Note that hexagon $A_b B_1 C_a A_b C_1 B_c$ is not cyclic since
\[ \angle C_a A_b B_1 + \angle B_1 C_a A_b + \angle A_b B_1 C_a = 480^{\circ} \neq 360^{\circ}. \]

Thus we can apply radical axis theorem to the three circles to show that $AA_1, BB_1, CC_1$ concur at a point $X$ and this point has equal power with respect to $\kappa_a,\kappa_b,\kappa_c$.

Let the circumcircle of $\triangle AA_bB_c$ meet $\kappa_a$ at $A_3 \neq A$. Define $B_3$ and $C_3$ similarly.
Claim 2. $BCB_cC_b$ cyclic.

Proof. Using directed angles

\[ \angle B C_b C = \angle AB_cC = \angle A C_bC, \]
\[ \angle B A_b B_c = \angle CB_cC = 90^{\circ} + 4 ( \angle C B_bC, \angle C B_bC = (CC_1 \perp AB) \]
and
\[ \angle AB_bC = 90^{\circ} + 4 \angle CBC_b. \]

(Claim 1 \perp AB) \qed

Similarly $\angle C B_bB = 90^{\circ} + 4 \angle A B_bC$. Hence, using $B_cC_bB_a$ cyclic,
\[ \angle A B_bC = 90^{\circ} + 4 \angle CBC_b = 90^{\circ} + 4 \angle B C_bC = \angle AB_bC \]

\[\frac{AK_1}{K_1 D} = \frac{AP}{PB} \cdot \frac{BM}{MD} = 1 \implies \frac{AK_1}{K_1 D} = \frac{AP}{2PB} \label{eq:Menelaus1}\]

A homothety at $A$ takes $\Gamma \to \omega$ and $D$ to the midpoint of arc $BC$ not containing $A$, so $PQ \parallel BC$ and $AD$ bisects $\angle BAC$.

Moreover, $A_b_A B_cC_a$ and $ABA_bB_c$ are cyclic. $A_c B_aC_b$ is not cyclic because then $AB_cC_b$ would meet $B_1$ lies on $\odot ABC$ which is impossible since $B_1$ lies inside $\triangle ABC$. Thus we can apply radical axis theorem to the three circles to get $AA_3, BB_3, CC_3$ concur at a point $Y$ which has equal power with respect to $\kappa_a, \kappa_b$.

We now make some isolated observations before finishing.

*   Let $O$ be the centre of $\triangle ABC$. We have that

\[ \angle B A_3 C = 40^{\circ} - \angle C B_a B = 40^{\circ} -(180^{\circ} - 180^{\circ} - 120^{\circ}) = 120^{\circ} \]

so $A_3$ lies inside $\triangle BOC$. We have similar results for $B_3, C_3$ and thus $\triangle A B_3C, \triangle CB_3 A, \triangle BCA_3, \triangle AAC_3,\triangle ABC$ have disjoint interiors. It follows that $A_3 B_3 C_3A_1 B_1 C_1$ is a convex hexagon that $X$ lies on segment $A_1A_3$ and therefore is inside $B_1$.

 \textbf{72} Chiba, Japan, 2nd-13th July \textbf{2023}

*   Since $A_1$ is to the centre of $A_b A_1C_1$ we have that $AA_1 = AA_b = AA_c$, so these cyclic quadrilaterals $AA_1A_3B_1A_1A_3C_1$ get that lines $AA_3$ and $AA_b and $AA_3 and $AY are reflections in line $AA_1$. As $X$ lies on segment $A_1A_3$, the only way $X and Y$ if $A_1 and $A_b both lie on the perpendicular bisector of $BC$. But this forces $(BC)$ to also be reflections in this line meaning $AA_3 = ABC_1$, contradicting the scalene condition.

Summarising, we have distinct points $X, Y$ with equal power with respect to $\kappa_a,\kappa_b,\kappa_c$ thus these circles have a common radical axis. As $X$ lies inside A4 (and similarly $K_a B_aC_b$, this radical axis intersects the circle at two points and so $\kappa_a, \kappa_b, \kappa_c $ have two points in common.
\end{document}


    
    
    
    
    
    
    
    """