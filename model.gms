$ontext
A simple LP model demonstrating reading from an input GDX file and exporting results to an output GDX file.
$offtext

$gdxin input.gdx

Sets
    i /all/;  $* Assuming CNFNameSet is a set identifier in input.gdx
$load i=CNFNameSet

Parameters
    cost(i);  $* Assume cost is a parameter associated with elements in CNFNameSet
$load cost

Variables
    x(i)  $* Decision variables for each item in the set
    z;  $* Objective variable representing total cost

Positive Variables
    x;

Equations
    CostObjective;  $* Objective function to minimize cost

CostObjective.. 
    z =e= sum(i, cost(i)*x(i));  $* Minimize total cost

Model simpleLPModel /all/;
Solve simpleLPModel using lp minimizing z;

$gdxout output.gdx
$unload z x
$gdxout off
