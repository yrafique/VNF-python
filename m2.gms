OPTION limrow = 100 ;
OPTION limcol = 100;

SET  VNFs        "Set of VNFs"
     Apps        "Set of IoT Apps"
     Servers     "Set of Servers"
     Users       "Set of Users";

ALIAS (Servers,Servers2);
ALIAS (VNFs,VNFs2,VNFs3);

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
         LinkCap(Servers,Servers2)      "Parameter to define max link capacity"
         UserBW(Users)                  "new"
         UserSC(VNFs,Users)            "new"
         SCs(Users,VNFs,VNFs2)           "new";

PARAMETER M
M /1000000/;


***************************************************************************************************************************************************************************************************

$if not set gdxin $set gdxin data
$GDXIN %gdxin%
$LOAD VNFs Apps Servers HostUtilizationCap Users Users_AP Users_App Topology LinkDelay App_Definition BW_Req CPU_Req LinkCap UserBW UserSC SCs
$GDXIN


***************************************************************************************************************************************************************************************************

VARIABLES
z,
*SERVER-VNF
V(Servers,VNFs)                          "BinaryVariable: Which Server? Which VNF?",

*SERVER-SFC-VNF
X(Servers,Users,VNFs)                    "Binary decision variable: Which Server? Which VNF? Which SFC?",

*PATH CREATION
BW(Servers,Servers2,Users,VNFs,VNFs2)    "PositiveVariable: Bandwidth on virtual links -> mapped on physical links"
BWu(Servers,Servers2,Users);


BINARY VARIABLES
V(Servers,VNFs),
X(Servers,Users,VNFs);

POSITIVE VARIABLES
BW(Servers,Servers2,Users,VNFs,VNFs2),
BWu(Servers,Servers2,Users);



EQUATIONS
Obj                                              ""
DemandSatisfaction(Users,VNFs)              ""
ActivateServer(Servers,Users,VNFs)               ""
SeverLoad(Servers)                               ""
FlowRouting(Users,Servers,VNFs,VNFs2)       ""
Forcing(Servers,Users,VNFs)                           ""
SingleFlow(Servers,Users) ;
*SingleVNF(VNFs);



Obj..
         z =e= SUM((Servers,VNFs),V(Servers,VNFs)) + SUM((Servers,Servers2,Users,VNFs,VNFs2),BW(Servers,Servers2,Users,VNFs,VNFs2));


*SFC DEMAND + VNF MAPPING
DemandSatisfaction(Users,VNFs)..
         SUM(Servers,X(Servers,Users,VNFs)) =e= 1$UserSC(VNFs,Users);

*ACTIVATE SERVER
ActivateServer(Servers,Users,VNFs)$UserSC(VNFs,Users)..
         V(Servers,VNFs) =g=   X(Servers,Users,VNFs);

*UPDATE CPU LOAD
SeverLoad(Servers)..
         SUM((Users,VNFs)$UserSC(VNFs,Users),X(Servers,Users,VNFs)* CPU_Req(VNFs)) =l= 400;

*PATH CREATION
FlowRouting(Users,Servers,VNFs,VNFs2)$(SCs(Users,VNFs,VNFs2) AND UserSC(VNFs,Users) AND UserSC(VNFs2,Users) AND ord(VNFs2)>ord(VNFs))..
         SUM(Servers2$Topology(Servers,Servers2), BW(Servers,Servers2,Users,VNFs,VNFs2)) - SUM(Servers2$Topology(Servers2,Servers), BW(Servers2,Servers,Users,VNFs,VNFs2)) =e=    (X(Servers,Users,VNFs) - X(Servers,Users,VNFs2))*UserBW(Users);


*OTHER CONSTRAINTS
Forcing(Servers,Users,VNFs)$(ord(VNFs) = 1)..
         X(Servers,Users,VNFs) =e= 1$Users_AP(Users,Servers);

*SINGLE FLOW PER USER
SingleFlow(Servers,Users)..
         SUM(Servers2$Topology(Servers,Servers2),SUM((VNFs,VNFs2)$(SCs(Users,VNFs,VNFs2) AND ord(VNFs2)>ord(VNFs)),BW(Servers,Servers2,Users,VNFs,VNFs2))) =l=  UserBW(Users);

*SINGLE VNF
*SingleVNF(VNFs)..
*         SUM(Servers,V(Servers,VNFs)) =e= 1;



MODEL VNFs_Placement /all/;

SOLVE VNFs_Placement using MIP minimizing z;

DISPLAY VNFs, Users, Users_App, Users_AP, UserBW, UserSC, App_Definition, CPU_Req, BW_Req,V.l, X.l, BW.l;


$ontext
*###############    Count of Servers Switched ON ###############
Parameter OnServers;
OnServers = 0;
OnServers = sum(Servers, Y.l(Servers));

*###############    To Store VNF Deployements ###############
Parameter Deployed(VNFs,Servers);
Deployed(VNFs,Servers) = 0;
Deployed(VNFs,Servers) =  X.l(VNFs,Servers);

*###############    To Store Current Link Load ###############
Parameter LinkLoad(Servers, Servers2);
LinkLoad(Servers, Servers2)=0;
loop(Servers,
loop(Servers2,
LinkLoad(Servers, Servers2) = sum((VNFs,VNFs2,Apps),BW.l(Servers,Servers2,VNFs,VNFs2,Apps))););

*###############    To Store Network Delay ###############
Parameter NetworkDelay(Apps);
NetworkDelay(Apps) = 0;
NetworkDelay(Apps) = Delay.l(Apps);
$offtext

*###############    To Store Host Utilization ###############
Parameter HostUtilization(Servers);
HostUtilization(Servers) = 0;
loop(Servers, HostUtilization(Servers) = SUM((Users,VNFs)$UserSC(VNFs,Users),X.l(Servers,Users,VNFs)* CPU_Req(VNFs)));


Parameter PhysicalBW(Servers,Servers2);
PhysicalBW(Servers,Servers2) = 0;
Loop((Servers,Servers2)$Topology(Servers,Servers2),PhysicalBW(Servers,Servers2) =  SUM((Users,VNFs,VNFs2)$(SCs(Users,VNFs,VNFs2) AND ord(VNFs2)>ord(VNFs)),BW.l(Servers,Servers2,Users,VNFs,VNFs2)));




DISPLAY HostUtilization, PhysicalBW;
