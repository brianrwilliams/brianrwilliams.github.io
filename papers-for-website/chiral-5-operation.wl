(* ::Title:: *)
(* Verification of the chiral 5-operation *)
(* Authors: Z.Gui, M.Wang, B.R.Williams)
(* ::Text:: *)
(* As an supplement to arXiv:2510.26608, this Wolfram Language script verifies the equality between an integral
   formula for the chiral 5-operation and the expression appearing in
   Budzik--Gaiotto--Kulp--Wu--Yu, Section 4.8, Equation (4.67).

   It is intended to be readable as a plain text file, suitable for hosting
   on a webpage and running from Mathematica or wolframscript.
*)

ClearAll["Global`*"];

(* ::Section:: *)
(* Basic definitions *)

wedge[a_, b_] := a[[1]] b[[2]] - a[[2]] b[[1]];

lambda[1] = {lambda11, lambda12};
lambda[2] = {lambda21, lambda22};
lambda[3] = {lambda31, lambda32};
lambda[4] = {lambda41, lambda42};

(* Shorthand for the six basic wedge pairings. *)
w12 = wedge[lambda[1], lambda[2]];
w13 = wedge[lambda[1], lambda[3]];
w14 = wedge[lambda[1], lambda[4]];
w23 = wedge[lambda[2], lambda[3]];
w24 = wedge[lambda[2], lambda[4]];
w34 = wedge[lambda[3], lambda[4]];

(* ::Section:: *)
(* Integral formula *)

factor1 =
  wedge[
    (1 - r2) lambda[1] + (1 - r2 (1 - s2)) lambda[3],
    lambda[4] + (1 - s4) lambda[2]
  ];

factor2 =
  wedge[
    lambda[1],
    lambda[3] + (1 - s3) lambda[4] + (1 - s3) (1 - s4) lambda[2]
  ];

factor3 =
  wedge[
    -(1 - r3) (1 - r2) lambda[1]
      + (1 - r3) (r2 (1 - s2) - 1) lambda[3]
      + (-s3 - (1 - s3) (1 - r3) (1 - r2 (1 - s2))) lambda[4],
    lambda[2]
  ];

result =
  Integrate[
    factor1 factor2 factor3 r2 r3 r4,
    {s4, 0, 1}, {s3, 0, 1}, {s2, 0, 1},
    {r4, 0, 1}, {r3, 0, 1}, {r2, 0, 1}
  ];

(* ::Section:: *)
(* Reference expression *)

(* This is the expression from Budzik--Gaiotto--Kulp--Wu--Yu,
   Section 4.8, Equation (4.67), rewritten using the abbreviations
   wij = wedge[lambda[i], lambda[j]]. *)

F =
    1/864 w12^3
  + 1/96 w13 w23^2
  - 1/96 w14^2 w23
  + 1/96 w14 w23^2
  - 1/96 w13 w24^2
  - 1/96 w14^2 w24
  + 1/96 w13^2 w24
  - 1/8 w13 w24 w34
  + 1/48 w14 w23 w24
  - 1/48 w14 w24 w34
  - 1/96 w13 w24 w12
  - 1/48 w13 w23 w34
  + 1/16 w14 w23 w34
  - 1/48 w13 w14 w24
  + 1/48 w13 w23 w24
  + 1/144 w13 w14 w12
  - 1/48 w13 w14 w23
  - 1/96 w13 w23 w12
  - 1/96 w14 w23 w12
  - 1/96 w14 w24 w12
  + 1/144 w23 w24 w12
  - 1/288 w24 w12^2
  + 7/96 w34^2 w12
  - 1/288 w23 w12^2
  + 1/288 w14^2 w12
  + 1/288 w12^2 w14
  + 1/288 w12^2 w13
  + 1/288 w23^2 w12;

(* ::Section:: *)
(* Verification *)

verification = FullSimplify[Expand[result - F] == 0];

Print["Verification result: ", verification];

(* When run successfully, this script should print:

   Verification result: True
*)
