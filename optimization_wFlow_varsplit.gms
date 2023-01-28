OPTION limrow = 10 ;
OPTION limcol = 10;

SET  VNFs        "Set of VNFs"
     Apps        "Set of IoT Apps"
     Servers     "Set of Servers"
     Users       "Set of Users";

ALIAS (Servers,Servers2);
ALIAS (VNFs,VNFs2);

***************************************************************************************************************************************************************************************************

PARAMETERS
         Topology(Servers,Servers2)     "Table to define our network topology with bidirectional links"
         LinkDelay(Servers,Servers2)    "Table to define our network topology with bidirectional links"
         App_Definition(VNFs,Apps)      "Matrix to define VNFs -> Apps relation and order of deployement"
         CPU_Req(VNFs)                  "Parameter to define each VNFs's CPU requirement"
         BW_Req(Apps)                   "Parameter to define each VNFs's CPU requirement"
         Users_AP(Users,Servers)                "Parameter to define User -> AP Association"
         Users_App(Users,Apps)
         HostUtilizationCap(Servers)    "Parameter to define Server Utilization Capacity"
         LinkCap(Servers,Servers2)      "Parameter to define max link capacity";

PARAMETER M
M /1000000/;

***************************************************************************************************************************************************************************************************

$if not set gdxin $set gdxin Optimization_input
$GDXIN %gdxin%
$LOAD VNFs Apps Servers HostUtilizationCap Users Users_AP Users_App Topology LinkDelay App_Definition BW_Req CPU_Req LinkCap
$GDXIN


***************************************************************************************************************************************************************************************************

VARIABLES
*SERVERs LEVEL
U(Servers)               "Binary decision variable: Which server on?",
BWu(Servers,Servers2)    "Positive variable: bandwidth on a physical link between servers",

*VNFs LEVEL
V(Servers,VNFs)          "Binary decision variable: Which server on? Which VNFs installed?",
BWv(Servers,Servers2,VNFs,VNFs2)   "Positive variable: link bandwidth on virtual link between VNFs",

*APPs LEVEL
W(Servers,VNFs,Apps)    "Binary decision variable: Which server on? Which VNFs installed? Serving which app?",
BWw(Servers,Servers2,VNFs,VNFs2,Apps)   "Positive variable: link bandwidth on virtual link between VNFs",

*USERs LEVEL
X(Servers,VNFs,Apps,Users)      "Binary decision variable: Which server on? Which VNFs installed? Serving which app? Serving which users?",
BWx(Servers,Servers2,VNFs,VNFs2,Apps,Users)   "Positive variable: link bandwidth on virtual link between VNFs",

*OTHER VARIABLES
CPU(Servers)     "Positive variable: CPU resource utilization on a server",
Delay(Apps)      "Positive variable: total delay experienced by each app",
z                "Variable: Objective Value"  ,
G(Servers,Servers2,Apps);


BINARY VARIABLES
U(Servers),
V(Servers,VNFs),
W(Servers,VNFs,Apps),
X(Servers,VNFs,Apps,Users),
G(Servers,Servers2,Apps);

POSITIVE VARIABLES
BWu(Servers,Servers2),
BWh(Servers,Servers2,Users),
BWv(Servers,Servers2,VNFs,VNFs2),
BWw(Servers,Servers2,VNFs,VNFs2,Apps),
BWx(Servers,Servers2,VNFs,VNFs2,Apps,Users),
CPU(Servers),
Delay(Apps);



EQUATIONS
Obj                                      "Objective to minimize cost by using least number of servers and by sharing common VNFs among Apps's"
ActivateServer(Servers)                  "Constraint to ensure server status = ON"
AppsSatisfied(VNFs)
ServerLoad(Servers)                      "Constraint to ensure server load is updated when VNFs are deployed"
ActivateSingleServer(VNFs)
ActivateSingleVNF(Servers,VNFs)          "For each VNF activate a single server only (Later change threshold for replication)"
ServerLoadCap(Servers)                   "Constraint to ensure server load does not exceed the maximum load (<threshold%)"
*vLinkBandwidth(Servers,Servers2,VNFs,VNFs2,Apps)
*pLinkBandwidth(Servers,Servers2)
LinkFlow(Servers,Servers2)
SCFlow(Servers,Servers2,VNFs,VNFs2)
AppFlow(Servers,Servers2,VNFs,VNFs2,Apps)
*Forcing(Servers,Servers2,VNFs,VNFs2,Apps)
*ConnectAP(Servers,Users)
*APFlow(Servers,Servers2)

;

Obj..
         z =e=  SUM(Servers,U(Servers)*1000)+ SUM((Servers,VNFs), V(Servers,VNFs)*100) + SUM((Servers,Servers2),BWu(Servers,Servers2)*10) ;


*Switch on only one server for a VNF
ActivateSingleServer(VNFs)..
         SUM(Servers,  V(Servers,VNFs)) =l= 1;

*Switch on only one VNF for all apps
ActivateSingleVNF(Servers,VNFs)..
        SUM(Apps, W(Servers,VNFs,Apps)) =e= V(Servers,VNFs) ;

*Switch on a server, due to VNF
ActivateServer(Servers)..
         SUM(VNFs, V(Servers,VNFs)) =l= U(Servers)*M ;



ServerLoad(Servers)..
         CPU(Servers) =e= SUM(VNFs,V(Servers,VNFs)*CPU_Req(VNFs));

ServerLoadCap(Servers)..
         CPU(Servers)  =l= 60;

AppsSatisfied(VNFs)..
         SUM(Servers,  V(Servers,VNFs))  =e= 1$SUM(Apps,App_Definition(VNFs,Apps)>=1);

*AND


*v1
*AppFlow(Servers,Servers2,VNFs,VNFs2,Apps)$(App_Definition(VNFs,Apps) AND App_Definition(VNFs2,Apps) AND Topology(Servers,Servers2)  AND ORD(VNFs) ne ORD(VNFs2) AND ORD(VNFs) < ORD(VNFs2))..
*BWw(Servers,Servers2,VNFs,VNFs2,Apps) - BWw(Servers2,Servers,VNFs2,VNFs,Apps) =g= BW_Req(Apps)*(W(Servers,VNFs,Apps) + W(Servers2,VNFs2,Apps));


*v2
AppFlow(Servers,Servers2,VNFs,VNFs2,Apps)$(App_Definition(VNFs,Apps) AND App_Definition(VNFs2,Apps) AND Topology(Servers,Servers2)  AND ORD(VNFs) ne ORD(VNFs2) AND ORD(VNFs) < ORD(VNFs2))..
BWw(Servers,Servers2,VNFs,VNFs2,Apps) =g= BW_Req(Apps)*(G(Servers,Servers2,Apps) );



*-SUM(Servers2$Topology(Servers,Servers2),BWw(Servers,Servers2,VNFs,VNFs2,Apps)*BW_Req(Apps))
* +BWw(Servers2,Servers,VNFs,VNFs2,Apps)
*=g= BW_Req(Apps)*(W(Servers,VNFs,Apps) + W(Servers2,VNFs2,Apps));



$ontext
vLinkBandwidth(Servers,VNFs,VNFs2,Apps)$(ORD(VNFs) ne ORD(VNFs2)  AND App_Definition(VNFs,Apps) AND App_Definition(VNFs2,Apps))..
          SUM(Servers2$Topology(Servers,Servers2),BWw(Servers,Servers2,VNFs,VNFs2,Apps)
         - BWw(Servers2,Servers,VNFs,VNFs2,Apps))
         =e= SUM(Users, Users_App(Users,Apps))* BW_Req(Apps)*(W(Servers,VNFs,Apps) - W(Servers,VNFs2,Apps)) ;
$offtext

SCFlow(Servers,Servers2,VNFs,VNFs2)$(Topology(Servers,Servers2) AND ORD(VNFs) ne ORD(VNFs2) AND ORD(VNFs) < ORD(VNFs2))..
BWv(Servers,Servers2,VNFs,VNFs2) =e= SUM(Apps,BWw(Servers,Servers2,VNFs,VNFs2,Apps)) ;

LinkFlow(Servers,Servers2)$Topology(Servers,Servers2)..
BWu(Servers,Servers2) =e= SUM((VNFs,VNFs2)$(ORD(VNFs) ne ORD(VNFs2) AND ORD(VNFs) < ORD(VNFs2)),BWv(Servers,Servers2,VNFs,VNFs2)) ;


*Forcing(Servers,Servers2,VNFs,VNFs2,Apps)$(App_Definition(VNFs,Apps) AND App_Definition(VNFs2,Apps) AND Topology(Servers,Servers2)  AND ORD(VNFs) ne ORD(VNFs2) AND ORD(VNFs) < ORD(VNFs2))..
*           G(Servers,Servers2,Apps)*(M) + 1 =g=W(Servers,VNFs,Apps)+W(Servers2,VNFs2,Apps);


$ontext
ConnectAP(Servers,Users)..
SUM(Servers2$Topology(Servers,Servers2),BWh(Servers,Servers2,Users)) =e= SUM((Apps),Users_App(Users,Apps)*  BW_Req(Apps)* Users_AP(Users,Servers))  ;

APFlow(Servers,Servers2)$(Topology(Servers,Servers2) AND ord(Servers2)>ord(Servers))..
               BWu(Servers,Servers2) =e=  SUM(Users,BWh(Servers,Servers2,Users));
$offtext

MODEL VNFs_Placement /all/;

SOLVE VNFs_Placement using MIP minimizing z;

DISPLAY Users, Users_App, Users_AP, App_Definition, CPU_Req, BW_Req,V.l, U.l,W.l,CPU.l, BWu.l,BWw.l;
