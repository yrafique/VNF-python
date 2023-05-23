**Commented code is with Chain omitted

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
         Users_AP(Users)                "Parameter to define User -> AP Association"
         Users_App(Users)               "Parameter to define User -> Application Association"
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
         z                                       "Variable to define the objective function",
         X(VNFs,Servers)                         "Binary Decision Variable to indicate, which VNFs is installed on which server",
         Y(Servers)                              "Binary Decision Variable to indicate, server is on",
         BWv(Servers,Servers2,VNFs,VNFs2,Apps)   "Positive variable to define link bandwidth on virtual link between VNFs",
         BWp(Servers,Servers2)                   "Positive variable bandwidth on a physical link between servers",
         CPU(Servers)                            "Decision Variable to indicate the CPU resource utilization on a server",
         Delay(Apps)                             "Variable to define the total delay experienced by each app";

BINARY VARIABLES         X(VNFs,Servers),Y(Servers);
POSITIVE VARIABLES       BWv(Servers,Servers2,VNFs,VNFs2,Apps),BWp(Servers,Servers2), CPU(Servers), Delay(Apps);

***************************************************************************************************************************************************************************************************

EQUATIONS
Obj                                             "Objective to minimize cost by using least number of servers and by sharing common VNFs among Apps's"
AppsSatisfied(VNFs)                             "Constraint to ensure Apps requirements are satisfied"
ServerLoad(Servers)                             "Constraint to ensure server load is updated when VNFs are deployed"
ServerLoadCap(Servers)                          "Constraint to ensure server load does not exceed the maximum load (<x%)"
ActivateServer(Servers)                         "Constraint to ensure server status = ON"
vLinkBandwidth(Servers,VNFs,VNFs2,Apps)         "Constraint to ensure virtual banwdith between two VNFs is updated"
pLinkBandwidth(Servers,Servers2)                "Constraint to ensure physical banwdith is updated based on passing traffic between s & s'"
BandwidthCapacity(Servers,Servers2)            "Constraint to ensure link bandwidth does not exceed maximum capacity"
*DelayConstraint(Apps)                          "Constraint to calculate the precieved delay by each application";
ConnectAP(Servers,Users)
;

Obj..
         z =e= SUM(Servers,Y(Servers) *1000) + SUM((VNFs,Servers), X(VNFs,Servers)*100) + SUM(Apps,Delay(Apps)) + SUM((Servers,Servers2),BWp(Servers,Servers2)*10) ;  ;

ActivateServer(Servers)..
         SUM((VNFs), X(VNFs,Servers)) =l= M*Y(Servers) ;

ServerLoad(Servers)..
         CPU(Servers) =e= SUM((VNFs),X(VNFs,Servers)*CPU_Req(VNFs));

ServerLoadCap(Servers)..
         CPU(Servers)  =l= HostUtilizationCap(Servers);

AppsSatisfied(VNFs)..
         SUM(Servers,  X(VNFs,Servers))  =e= 1$SUM(Apps,App_Definition(VNFs,Apps)>=1);


vLinkBandwidth(Servers,VNFs,VNFs2,Apps)$(ORD(VNFs) ne ORD(VNFs2))..
         SUM((Servers2), BWv(Servers,Servers2,VNFs,VNFs2,Apps)*Topology(Servers,Servers2)
         - BWv(Servers2,Servers,VNFs,VNFs2,Apps)*Topology(Servers2,Servers))
         =e= BW_Req(Apps)*(X(VNFs,Servers) - X(VNFs2,Servers)) ;


pLinkBandwidth(Servers,Servers2)$Topology(Servers,Servers2)..
              BWp(Servers,Servers2) =e= SUM((VNFs,VNFs2,Apps)$(ORD(VNFs) ne ORD(VNFs2)),BWv(Servers,Servers2,VNFs,VNFs2,Apps));


ConnectAP(Servers,Users)$Users_AP(Users)..
              SUM(Servers2, BWp(Servers,Servers2)*Topology(Servers,Servers2) + BWp(Servers2,Servers)*Topology(Servers2,Servers)) =g=   Sum(Apps,Users_App(Users)*  BW_Req(Apps));


BandwidthCapacity(Servers,Servers2)$Topology(Servers,Servers2)..
         SUM((VNFs,VNFs2,Apps)$(ORD(VNFs) ne ORD(VNFs2) ), BWp(Servers,Servers2)+BWp(Servers2,Servers)) =l= LinkCap(Servers,Servers2);


*DelayConstraint(Apps)..
*         Delay(Apps) =e= SUM((Servers,Servers2)$Topology(Servers,Servers2), LinkDelay(Servers,Servers2)*BWp(Servers,Servers2)) ;

***************************************************************************************************************************************************************************************************

MODEL VNFs_Placement /all/;

SOLVE VNFs_Placement using MIP min z;

***************************************************************************************************************************************************************************************************

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

*###############    To Store Host Utilization ###############
Parameter HostUtilization(Servers);
HostUtilization(Servers) = 0;
loop(Servers, HostUtilization(Servers) = CPU.l(Servers));

***************************************************************************************************************************************************************************************************

DISPLAY X.l, Y.l,BW.l,Chain,CPU.l,LinkDelay, Delay.l, LinkLoad, Users, Users_AP,Users_App, LinkStatus.l
$offtext


DISPLAY      X.l, Y.l, BWv.l, BWp.l, Users_AP, Users_APP















