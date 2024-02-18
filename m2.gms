OPTION limrow = 100;
OPTION limcol = 100;

SETS
    VNFs         "Set of VNFs"
    Apps         "Set of IoT Apps"
    Servers      "Set of Servers"
    Users        "Set of Users";

ALIAS (Servers, Servers2);
ALIAS (VNFs, VNFs2, VNFs3);

PARAMETERS
    Topology(Servers, Servers2)        "Topology with bidirectional links"
    LinkDelay(Servers, Servers2)       "Link delays"
    App_Definition(VNFs, Apps)         "VNFs -> Apps relation and order"
    CPU_Req(VNFs)                      "VNF CPU requirements"
    BW_Req(Apps)                       "App bandwidth requirements"
    Users_AP(Users, Servers)           "User -> AP Association"
    Users_App(Users, Apps)             "User -> App Association"
    HostUtilizationCap(Servers)        "Server Utilization Capacity"
    LinkCap(Servers, Servers2)         "Max link capacity"
    UserBW(Users)                      "User bandwidth requirements"
    UserSC(VNFs, Users)                "User to VNF association"
    SCs(Users, VNFs, VNFs2)            "Service Chains";

PARAMETER M /1000000/;

$GDXIN data.gdx
$LOAD VNFs Apps Servers HostUtilizationCap Users Users_AP Users_App Topology LinkDelay App_Definition BW_Req CPU_Req LinkCap UserBW UserSC SCs

VARIABLES
    z                                   "Objective function"
    V(Servers, VNFs)                    "Server-VNF mapping"
    X(Servers, Users, VNFs)             "Server-SFC-VNF mapping"
    BW(Servers, Servers2, Users, VNFs, VNFs2) "Bandwidth on virtual links";

BINARY VARIABLES
    V(Servers, VNFs),
    X(Servers, Users, VNFs);

POSITIVE VARIABLES
    BW(Servers, Servers2, Users, VNFs, VNFs2);

EQUATIONS
    Obj
    DemandSatisfaction(Users, VNFs)
    ActivateServer(Servers, Users, VNFs)
    SeverLoad(Servers)
    FlowRouting(Users, Servers, VNFs, VNFs2)
    Forcing(Servers, Users, VNFs)
    SingleFlow(Servers, Users);

* Objective function to minimize costs
Obj..
    z =e= SUM((Servers, VNFs), V(Servers, VNFs) * HostUtilizationCap(Servers)) + SUM((Servers, Servers2, Users, VNFs, VNFs2), BW(Servers, Servers2, Users, VNFs, VNFs2) * LinkCap(Servers, Servers2));

* Ensure demand satisfaction for each user and VNF combination
DemandSatisfaction(Users, VNFs)..
    SUM(Servers, X(Servers, Users, VNFs)) =e= SUM(Apps, App_Definition(VNFs, Apps));

* Server activation based on VNF deployment
ActivateServer(Servers, Users, VNFs)..
    SUM(VNFs, V(Servers, VNFs)) =g= 1;

* Enforce server load does not exceed capacity
SeverLoad(Servers)..
    SUM(VNFs, V(Servers, VNFs) * CPU_Req(VNFs)) =l= HostUtilizationCap(Servers);

* Define more equations as needed

MODEL VNFs_Placement /all/;
SOLVE VNFs_Placement USING MIP MINIMIZING z;

$GDXOUT Optimization_output.gdx
$UNLOAD V L X L BW L
$GDXOUT
