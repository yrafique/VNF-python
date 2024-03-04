$ontext
This GAMS file reads the input GDX file, solves the model, and creates the output GDX file.
$offtext

set nodes / Node1, Node2 /;
parameter capacity(nodes);

$ontext
Read input GDX file
$offtext

$gdxin input.gdx
$load nodes capacity
$gdxin

display capacity;

$ontext
Define parameters for the LP model
$offtext

parameter a / 2 /;
parameter b / 3 /;

$ontext
Define LP model
$offtext

* Define variables
variables
    x(nodes);

* Define equations
equations
    objective;

* Define objective function
objective..
    z =e= a * b * sum(nodes, x(nodes));

* Define constraints (if any)
*constraints
*    constraint1..
*        sum(nodes, x(nodes)) =l= 10;

* Solve LP model
* Model type: LP (Linear Programming)
model lp_model /all/;
solve lp_model using lp maximizing z;

$ontext
Create output GDX file
$offtext

set nodes / Node1, Node2 /;
parameter solution(nodes);

* Read solved model results
solution(nodes) = x.l;

* Export results to output GDX file
$gdxout output.gdx
$unload solution
$gdxout
