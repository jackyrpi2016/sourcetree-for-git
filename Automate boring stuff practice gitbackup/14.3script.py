>>> # read pdf and write pdf
>>> import os
>>> os.chdir('/Users/lichenglong/Desktop')
>>>
>>> import PyPDF2
>>> pdfFile = open('meetingminutes1.pdf', 'rb')
>>> # read mode, in binary
>>> # pass the file to the reader
>>> reader = PyPDF2.PdfFileReader(pdfFile)
>>> # get pages #
>>> reader.numPages
19
>>> # page # starts from 0
>>> page0 = reader.getPage(0)
>>> page0.extractText()
'OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of \nMarch 7\n, 2014\n        \n     The Board of Elementary and Secondary Education shall provide leadership and \ncreate policies for education that expand opportunities for children, empower \nfamilies and communities, and advance Louisiana in an increasingly \ncompetitive glob\nal market.\n BOARD \n of ELEMENTARY\n and \n SECONDARY\n EDUCATION\n  '
>>> # use for loop to get all the pages' content
>>> for pageNum in range(reader.numPages):
	print(reader.getPage(pageNum).extractText())

OOFFFFIICCIIAALL  BBOOAARRDD  MMIINNUUTTEESS   Meeting of 
March 7
, 2014
        
     The Board of Elementary and Secondary Education shall provide leadership and 
create policies for education that expand opportunities for children, empower 
families and communities, and advance Louisiana in an increasingly 
competitive glob
al market.
 BOARD 
 of ELEMENTARY
 and 
 SECONDARY
 EDUCATION
  
 LOUISIANA STATE BOARD OF ELEMENTARY AND SECONDARY EDUCATION
   MARCH 7, 2014
  
 The Louisiana Purchase Room
  Baton Rouge, LA
   
 
 
The Louisiana State Board of Elementary and Secondary Education met in 
regular
 session on
 March 7, 2014
, in the Louisiana Purcha
se Room, located in the Claiborne 
Building in Baton Rouge, Louisiana.  The meeting was called to order at 
9:17 a.m.
 by 
Board President 
Chas Roemer
 and opened with a prayer by
 Ms. Terry Johnson, Bossier 
Parish School System
.  
Board members present were 
Dr. Lottie Beebe, Ms. Holly Boffy, Mr. Jim Garvey, Mr.
 Jay 
Guillot, Ms.
 Carolyn Hill, Mr. Walter Lee, 
Dr. Judith Miranti, 
Mr. Chas Roemer
, and 
Ms. Jane Smith
.  Ms. Connie Bradford
 and Ms. Kira Orange Jones were
 absent.
  
Dr. Charlie Michel, Lafourche Parish Sch
ool System,
 led the Pledge of Allegiance.
  Agenda
 Item 2.
 On motion of Mr. Garvey, seconded by Ms. Boffy, the Board approved the 
agenda, as printed and disseminated.
 (Schedule 1)
  Agenda
 Item 3.
 On motion of Ms. Smith, seconded by Ms. Boffy, the Board app
roved the 
minutes of January 15, 2014.
  Agenda
 Item 4.
 Report by the State Superintendent of Education
  State Superintendent of Education John White provided an update on the 
intense and increased support that the LDE is providing to teachers to 
assist wi
th 
new academic expectations.  The LDE has established the 
following support structures:  
(1) 
network teams are working directly with 
superintendents; 
(2) 
district planning teams and district planning guides 
have been established in every district; and 
(3) teacher leader team
s are
 doubling to 4,000 next year.  Sample test items are being released.  The 
curriculum package for next year is being released.
  Next year™s 
assessment guides will be produced in the following weeks.
  
BOARD MINUTES
 -2- MARCH 7, 2014
     * * * * * * * * * *  On Poin
t of Personal Privilege, Ms. Hill recognized the Capitol Senior 
High School Alumni Association for its dedication to the school and its 
students throughout several transitions, and presented a Certificate of 
Appreciation to Mr. W. T. W
infield.
  Agenda
 Item 5.
 Board Committee Reports
   Agenda
 Item 5.1.
 Academic Goals and Instructional Improvement Committee
  (Schedule 2)
  5.1.
1 On motion of 
Dr. Miranti,
 seconded by 
Mr. Lee,
 the Board receive
d the 
minutes of the Accountability Commission meetings held Janua
ry 9, 2014, 
and January 27, 2014.
  5.1.
2 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
received
 the 
minutes of the 
Special Education Advisory Panel meeting held 
February
 20, 2014.
  5.1.
3 On motion of 
Dr. Beebe, 
seconded by 
Mr. Garvey,
 the 
Boar
d approve
d, as a Notice of Intent, revisions to Bulletin 119, 
Louisiana School 
Transportation Specifications and Procedures
: §2509. Used School 
Buses
, as amended and presented by the LDE
.   * * * * * * * * * *  Public comments were received on the followi
ng 
Academic Goals and 
Instructional Improvement Committee 
agenda item:
  Agenda Item 3.2., ﬁConsideration of policy recommendations relative to 
the implementation of the Jump Start career education program.ﬂ
  Support:
  None.
 Oppose:
  None.
 Information Only/
Other:
  Ms. 
Debra Schum, Louisiana Association 
of Principals.
  
BOARD MINUTES
 -3- MARCH 7, 2014
    5.1.
4 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, the creation of Bulletin 138, 
Jump Start Program
:  §101.  
Overview, 
§201.  Jump Start Program 
Authorization, 
§301.  General 
Provisions, and 
§303.  Jump Start Instructional Staff, as presented by the 
LDE.
  Further, the 
Board 
approved
, as a Notice of Intent, 
the creation of 
§305.  
Student Participation in Jump Start Programs, as amended and 
presented
.  5.1.
5 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 111, 
The Louisiana School, District, 
and State Accountability System
:  §409.  Calculating a 9
-12 Assessment 
Index, and §613.  Calculat
ing a Graduation Index
, as presented by the 
LDE
.  5.1.
6 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 746, 
Louisiana Standards for State 
Certification of School Personnel
:  §501.  Introduct
ion; adding a new 
§505.  Career and Technical Certificate Types Issued after September 1, 
2014; renumbering and renaming the original §505. to 
§506.  CTTIE
-1 and CTTIE
-2 Certificate Eligibility Requirements; adding a new §507.  
CTTIE Areas of Specializatio
n; renumbering and renaming the original 
§507. to §509.  CTTIE
-1 Certificates Renewal Guidelines for certificates 
initially issued prior to September 1, 2014; deleting the original §509.  
CTTIE
-2 Certificates Renewal Guidelines; and §511.  Process for 
Rein
stating Lapsed CTTIE Certificates
, as presented by the LDE.
  Further, the Board 
approved
, as a Notice of Intent, revisions to §504.  
Career and Technical Certificate Types Issued after July 1, 2006, as 
amended and presented.
  5.1.
7 On motion of Dr. Mirant
i, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 118, 
Statewide Assessment 
Standards and Practices
:  §701.  Overview of Assessment Programs in 
Louisiana, §2209.  WorkKeys, and §3501.  Approved Home Study 
Program Stud
ents
, as presented by the LDE
.  5.1.
8 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 741, 
Louisiana Handbook for School 
Administrators
:  §2317.  High Schools and §2318.  The College Diploma
, as presented by the LDE
.  
BOARD MINUTES
 -4- MARCH 7, 2014
   5.1.
9 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 1566, 
Pupil Progression Policies and 
Procedures
:  §503.  Regular Placement
, as presented by the LDE
.  5.1.
10 On motion of Dr. Miranti, seconded by Mr. Lee, 
the Board 
approved
, as a 
Notice of Intent, revisions to Bulletin 111, 
The Louisiana School, District, 
and State Accountability System
: §301. School Performance Score Goal; 
§303. Transition from Fall 2013 to Sp
ring 2015; §413. Dropout/Credit 
Accumulation Index Calculations; §517. Inclusion of Schools; §521. 
Pairing/Sharing of Schools with Insufficient Test Data; §603. Determining 
a Cohort for 
a Graduation; §611. Documenting a Graduation Index; 
§1301. Reward Elig
ibility; §2301. Schools Requiring 
Reconstitution/Alternate Governance Plans; §3101. Appeals/Waivers and 
Data Certification Processes; §3301. Inclusion of New Schools; §3303. 
Reconfigured Schools; §4101. Valid Data Considerations; §4301. 
Inclusion of All Di
stricts; and §4317. District Accountability Data 
Corrections
, as presented by the LDE
.  Dr. Beebe was recorded as being opposed to the motion.
  5.1.
11 On motion of 
Dr. Miranti,
 seconded by 
Mr. Lee,
 the Board receive
d the 
Summary of Public Comments and Age
ncy Response regarding revisions
 to Bulletin 135, 
Health and Safety
:  Chapter 5. 
 Injury Management 
Program Rules for Serious Sports Injuries and Chapter 7: Glossary, and 
direct
ed BESE staff to pr
oceed
 with the final adoption of the January 20, 
2014, Notic
e of Intent regarding revisions to Bulletin 135, 
Health and 
Safety
, Chapters 5 and
 7.  Agenda
 Item 5.2.
 Administration and Finance Committee
 (Schedule 3)
   5.2.
1 On motion of 
Mr. Guillot,
 seconded by 
Mr. Lee
, the Board 
received
 the 
report on 8(g) monitor
ing visits conducted by Board staff.
  5.2.
2 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
received
 the 
quarterly report from the LDE Director of Internal Audit.
  5.2.
3 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
received
 the 
repor
t on LDE contracts of $50,000 and under approved by the State 
Superintendent of Education.
  
BOARD MINUTES
 -5- MARCH 7, 2014
    5.2.
4 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
received
 the 
reports requested by the Minimum Foundation Program (MFP) Task 
Force pertaining to th
e regulations governing students with dyslexia and 
student access to technology.
  5.2.
5 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board ratif
ied
 the 
Board President's submission of the value
-added asses
sment model 
report to the House Committee on
 Education 
and the 
Senate 
Committee 
on Education.
   * * * * * * * * * *  Public comments were received on the following 
Administration and 
Finance Committee 
agenda item:
  Agenda Item 4.1., ﬁ
Consideration of the Minimum Foundation Program 
(MFP) Formula for
 FY 2014
-2015.ﬂ  Support:
  None.
 Oppose:
  None.
 Information Only/Other:
 Mr. 
Shawn Fleming, Louisiana 
Developmental Disabilities Council.
  5.2.
6 On motion of 
Mr. Guillot
, seconded by 
Mr. Garvey
, the Board
 deferred 
until a Special Board Meeting to be held d
uring the week of March 10
-14, 
2014:  ﬁConsideration of the Minimum Foundation Program (MFP) 
Formula for FY 2014
-2015.ﬂ  5.2.7
 On motion of Mr. Guillot, seconded by Mr. Lee, the Board, in recognition 
that the proposed 2014
-2015 MFP formula does not includ
e funding for 
early childhood education, committed to developing a strategy of 
equitable early childhood education funding in future fiscal years and 
supports legislation throughout the 2014 Regular Legislative Session that 
allows for the consideration of 
4-year
-old pre
-kindergarten education as a 
component of elementary and secondary education.
  5.2.
8 On motion of 
Mr. Guillot
, seconded by 
Mr. Lee
, the Board approve
d the 
revised 8(g) program and budget for FY 
2013-2014.  Dr. Beebe recused herself from voti
ng on this item.
  
BOARD MINUTES
 -6- MARCH 7, 2014
    5.2.
9 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approved the 
revised program and budget for the 8(g) statewide program, Early 
Childhood Literacy Program (LDE) (S069), for FY 2013
-2014.  Dr. Beebe recused herself from vot
ing on this item.
  5.2.
10 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approved the 
revised program and budget for the 8(g) statewide program, Compass 
(LDE) (S067), for FY 2013
-2014.  Dr. Beebe was recorded as being opposed to the motion.
  5.2.11 On motion of Mr. Guillot, seconded by Mr. Lee,
 the Board approved the 
revised program and budget for the 8(g) statewide program, 
Expanding 
High School Choice
 (LDE) (S0
73), for FY 2013
-2014.  Dr. Beebe recused herself from voting on this item.
  5.2.
12 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approved the 
revised program and budget for the 8(g) statewide program, 
New Schools 
Incubation Program
 (LDE) (S07
4), for FY 2013
-2014.  Dr. Beebe and Ms. Hill were recorded as being opposed to the m
otion.
    5.2.
13 School and District Innovations
 - Other
  On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approve
d the 
following allocation:
   Allocation:
  RSD Charter School Transformation
 Amount:
  $250,000
.00
 Funding Period:
 07/01/
2013 - 06/30/
2014 Source of Funds:
 IAT 
- 8(g)
  Purpose:  The purpose of these funds is to support RSD transformation 
activities.
  Basis of Allocation:  The 
LDE 
supports the efforts of the RSD to create an 
environment with the conditions necessary for charter 
schools 
to succeed 
and to support the transformation process for low
-performing schools. 
  (Motion continues on page 7)
  
BOARD MINUTES
 -7- MARCH 7, 2014
   Funds may be used to provide professional development, stabilize school 
staffing during the transformation process, provide for additional staffi
ng 
resources needed to successfully transition a direct
-run school to a charter 
school, and other activities that support the development of a high 
performing charter 
school 
environment.
  Dr. Beebe recused herself from voting on this item.
    5.2.
14 Depar
tmental Support 
- Other
  On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approve
d the 
following allocation:
   Allocation:
  Educator Leader Cadre Substitute Reimbursement
 Amount:
  $1,893.36
 Funding Period:
 10/01/
2013 - 12/13/2014
 Source of Funds:
 Federal
  Purpose:  The purpose of the Teacher Leader Advisors is to develop an 
understanding of the changes required of Common Core and Compass, 
including reviewing and creating materials for implementation
, serving as 
a Common Core expert
, assisting in bui
lding a growing network of teacher 
leaders throughout the state
, and attending face
-to-face meetings to 
provide recommendations and fe
edback on resources and tools.
  Basis of Allocation:  Allocations to school districts are to reimburse the 
districts for t
he substitutes paid to work while the Teacher Leader 
Advisors met in Baton Rouge on October 15
-16, 
2013, 
and December
 13, 
2013, to begin their work for the program.
  Dr. Beebe recused herself from voting on this item.
  5.2.
15 Office of Management and Fina
nce 
Œ Competitive
  On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board approve
d the 
following allocation:
   Allocation:
  Early Childhood Community Network Pilots
 Amount:
  $676,666.67
 Funding Period:
 03/08/2014 - 06/30/2014
 Source of Funds:
 State 
- IAT
  (Motion continues on page 8)
  
BOARD MINUTES
 -8- MARCH 7, 2014
   Purpose:  The purpose of these funds is to support Early Childhood 
Community Network Pilots to implement the five strategies outlined in the 
Early Childhood Care and Education Network 
- Roadmap to 2015, which 
are as follows:
  1. Unify expectations;
 2. Support teachers and providers;
 3. Measure and recognize progress;
 4. Fund high quality providers; and
 5. Provide clear information and high quality choices.
  The ultimate goal of the Early Childhood Care and Education Network is 
to prepare ou
r youngest learners for kindergarten.
  Basis of Allocation:  Allocations 
were determined competitively via a 
request for applications.  The selection of the Community Network Pilots 
occurred through a two
-step process 
Œ 1. Application review for basic 
requ
irements and 2. Interview with the finalists
.  The interview sought to 
determine networks that could demonstrate their readiness to work on the 
five strategies listed above.
  Dr. Beebe recused herself from voting on this item.
  5.2.
16 On motion of Mr. Gui
llot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract:
  Contractor:
   LSU
-Health Science Center
 Contract Period:
  01/31/2014
 - 09/30/2014
 Contract Amount:
  $102,734
.00
 Fund:
    Federal Fund 
- IDEA Part B
 Competitive Process:
 Non Competit
ive
  Description of Service:  This agreement will provide for activities for the 
federally funded 2008
-2013 Deaf Blind Project for which funding was 
extended through 9/30/14 to be completed.  Activities will include building 
capacity of current and future 
educators working with students who are 
deaf-blind
, facilitation of effective instructional strategies for students with 
deaf-blindness, and outreach and early intervention identification for 
families and service providers.
  
BOARD MINUTES
 -9- MARCH 7, 2014
    5.2.
17 On motion of Mr. Guil
lot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract:
  Contractor:
   Department of Health and Hospitals
 Contract Period:
  04/01/2014 
- 08/31/2014
 Contract Amount:
  $196,252.00
 Fund:
    Federal Funds 
- USDA
 Competitive Process:
 Non Compet
itive
  Description of Service:  
This Interagency Agreement will provide that the 
Louisiana Department of Health and Hospitals, Office of Public Health 
(DHH), Sanitarian Services Section
, conduct pre
-opening inspections of 
each food service site or preparat
ion facility participating in the SFSP.  
The sanitarian services will perform at least one (1) other inspection 
(besides the pre
-opening inspection) at each site/facility during the period 
of operation and record inspection results on the appropriate inspe
ction 
form.
  5.2.
18 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract amendment:
  Contractor:
   Volunteers of America North LA
 Contract Period:
  07/01/2013
 - 06/30/2014
 Previous Amount:
  $360,000.00
 Amended Amoun
t:  $38,400.00
 Contract Amount:
  $398,400
.00
 Fund:
    Federal 
- Title IV 
- 21st Century Community 
    Learning Centers (21
st CCLC)
 Competitive Process:
 Competitive
/21st CCLC RFP Process
  Description of Service:  
The c
ontract provides before
-, during
-, and 
after
-school academic enrichment opportunities for children attending low
-performing schools through the establishment and operation of 21
st Century Community Learning Centers.
  5.2.
19 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract amendment:
  Contractor:
   Urban Support Agency, Inc.
 Contract Period:
  07/01/2013
 - 06/30/2014
  (Motion continues on page 10)
  
BOARD MINUTES
 -10- MARCH 7, 2014
   Previous Amount:
  $639,000.00
 Amended Amount:
  $133,800.00
 Contract Amount:
  $772,800.00
 Fund:
    Federal 
- Title IV 
- 21st Century Community 
    Learning
 Centers (21
st CCLC)
 Competitive Process:
 Competitive/21
st CCLC RFP Process
  Description of Service:  
The c
ontract provides before
-, during
-, and after
-school academic enrichment opportunities for children at
tending low
-performing schools through the establishment and operation of 21
st Century Community Learning Centers.
  5.2.
20 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract amendment:
  Contractor:
   Outreach Comm
unity Development 
Corporation
 Contract Period:
  07/01/2013
 - 06/30/2014
 Previous Amount:
  $240,000.00
 Amended Amount:
  $6,000.00
 Contract Amount:
  $246,000
.00
 Fund:
    Federal 
- Title IV 
- 21st Century Community 
    Learning
 Centers (21
st CCLC)
 Competitive
 Process:
 Competitive/21
st CCLC RFP Process
  Description of Service:  
The c
ontract provides before
-, during
-, and after
-school academic enrichment opportunities for children attending low
-performing schools through the establishment and operation of 21
st Century Community Learning Centers.
  5.2.
21 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract
 amendment
:  Contractor:
   NZBC Urban Corporation
 Contract Period:
  07/01/2013 
- 06/30/2014
 Previous Amount:
  $180,000.0
0 Amended Amount:
  $8,400.00
 Contract Amount:
  $188,400.00
 Fund:
    Federal 
- Title IV 
- 21st Century Community 
    Learning Centers (21
st CCLC)
 Competitive Process:
 Competitive/21
st CCLC RFP Process
  (Motion continues on page 11)
  
BOARD MINUTES
 -11- MARCH 7, 2014
   Description of Service: 
 The c
ontract provides before
-, during
-, and after
-school academic enrichment opportunities for children attending low
-performing schools through the establishment and operation of 21
st Century Community Learning Centers.
  5.2.
22 On motion of Mr. Guillot,
 seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract amendment:
  Contractor:
   Akili Academy/Crescent City Schools
 Contract Period:
  07/01/2013
 - 06/30/2014
 Previous Amount:
  $492,000.00
 Amended Amount:
  $74,400.00
 Contract Amount:
  $566,400
.00
 Fund:
    Federal 
- Title IV 
- 21st Century Community 
    Learning Centers (21
st CCLC)
 Competitive Process:
 Competitive/21
st CCLC RFP Process
  Description of Service:  
The c
ontract provides before
-, during
-, and after
-school academic enrichment opportun
ities for children attending low
-performing schools through the establishment and operation of 21
st Century Community Learning Centers.
  5.2.
23 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following LDE contract
 amendment:
  Contra
ctor:
   Karen Boudreaux
 Contract Period:
  02/01/2012 
- 01/31/2015
 Previous Amount:
  $79,500.00
 Amended Amount:
  $25,500.00
 Contract Amount:
  $105,000.00
 Fund:
    Federal Fund 
- Title III
 Competitive Process:
 Non Competitive
  Description of Service:  The co
ntract is being amended for the contractor 
to calculate the performance of Title III subgrantee Local Education 
Agencies (LEAs) and the 
state on ESEA/NCLB Title III Annual 
Measurable Achievement Objective
s (AMAOs) for the 2013
-2014 school 
years, using stud
ent assessment data (ELDA, LEAP, 
iLEAP, etc.).
  
BOARD MINUTES
 -12- MARCH 7, 2014
    5.2.
24 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract 
amendment
:  Contractor:
   Blitch/Knevel Architects, Inc.
 Contract Period:
  03/09/2012 
- 03/09/2015
 Previo
us Amount:
  $1,473,321.00
 Amended Amount:
  $15,433.60
 Contract Amount:
  $1,488,754.60
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  
This amendment provides for the additional 
service for a Phase II environmental subsurface
 investigation, and a pre
-renovation ACM and LBP survey for Drew
 Elementary School renovation. 
It adds three (3) days to the design time due to Hurricane Isaac and 
fourteen (14) days to design time due to historic preservation revisions.  
This amendment pr
ovides for reimbursable expenses for regulatory 
agency approvals and for the printing of bidding documents.
  5.2.
25 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract:
  Contractor:
   Byron J. Stewart and Associate
s, APC 
     Architects and Planners
 Contract Period:
  03/07/2014 
- 03/07/2017
 Contract Amount:
  $105,034.00
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This project 
provides for 
the refurbishment of 
Rosenwald Elementary 
School.
  5.2.
26 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   Jacobs Project Management Company/CSRS 
     Consortium
 Contract Period:
  12/01/2013 
- 11/30/2016
 Previous Amount:
  $23,5
90,758.00
 Amended Amount:
  $1,069,673.31
  (Motion continues on page 13)
  
BOARD MINUTES
 -13- MARCH 7, 2014
   Contract Amount:
  $24,660,431.31
 Fund:
    IAT 
- FEMA/Lexington Insurance Proceeds
 Competitive Process:
 Competitive
  Description of Service:  
This amendment provides for additional ser
vices 
as directed by the RSD; additional service for support to RSD and ﬁOPSB 
v. Lexington, et al.;ﬂ additional service for claims consulting services; and 
additional service for grants management 
- Phase 1 
- negative 
balance/grant debt/undocumented advanc
es/applied payment proposal 
for the RSD multi
-site Capital Plan.
  5.2.
27 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   Mahlum Scairono Martinez Architects, LLC
 Contract Period:
  01/0
7/2013 
- 01/07/2015
 Previous Amount:
  $35,640.00
 Amended Amount:
  $21,390.00
 Contract Amount:
  $57,030.00
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This amendment provides for the relocation of 
playground equipment at 
William Fischer School and the relocation of 
playground equipment at Little Woods Elementary School.
  5.2.
28 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   Richard C Lambert, LLC
 Cont
ract Period:
  06/17/2010 
- 06/17/2014
 Previous Amount:
  $262,656.51
 Amended Amount:
  $8,032.24
 Contract Amount:
  $270,688.75
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This 
amendment provides for the adjustment of 
the 
basic s
ervices 
fee for Village de L™est Elementary School (
roof) and 
modular 
demo based on the 
final 
construction 
price of the project. It also 
provides for prolonged 
contract 
administration for the 
various 
roof and 
repair 
projects based on 48 days of 
liqui
dated 
damages at no fault of the 
designer.
  
BOARD MINUTES
 -14- MARCH 7, 2014
   5.2.
29 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   Shaw Environmental and Infrastructure
 Contract Period:
  02/14/2013 
- 02/14/2015
 Previ
ous Amount:
  $49,500.00
 Amended Amount:
  $14,640.00
 Contract Amount:
  $64,140.00
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This amendment provides for 
additional 
services 
for 
corrective 
action 
work 
plan 
preparation.
  5.2.
30 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract:
  Contractor:
   VergesRome Architects, APAC
 Contract Period:
  03/07/2014 
- 03/07/2017
 Contract Amount:
  $2,696,406.00
 Fund:
    IAT 
- FEMA 
 Competitive Proce
ss: Competitive
  Description of Service:  This project consists of the renovation of John 
McDonogh High School.
  5.2.
31 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   VergesRome Archi
tects, APAC
 Contract Period:
  10/16/2013 
- 10/16/2016
 Previous Amount:
  $265,287.00
 Amended Amount:
  $20,625.00
 Contract Amount:
  $285,912.00
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This
 amendment provides for the ad
ditional 
services for a water flow test, a 
Phase 
I environmental site assessment
, lead 
and asbestos investigation
, and a topographic survey for Live Oak 
Elementary School 
refurbishment.
  
BOARD MINUTES
 -15- MARCH 7, 2014
    5.2.
32 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   VergesRome Architects, APAC
 Contract Period:
  09/16/2010 
- 09/16/2015
 Previous Amount:
  $944,413.20
 Amended Amount:
  $38,546.20
 Contract Amount:
  $982,959.40
 Fund:
    IAT 
- FEMA 
 Competitive Proce
ss: Competitive
  Description of Service:  This amendment adjusts the 
designer™s 
fee for 
basic 
services for 
mothballing of 
closed 
schools 
- safe and 
secure at 
George Mondy Elementary School based on the revised AFC.  The 
project was canceled
, but is now bei
ng reinstated by the 
owner
, and additional scope of work is being added to the project.  It also provides for 
the addition of a new project and project number 
for d
emolition of 
the 
caretaker™s 
cottage at George Mondy Elementary School and 
at 
Andrew 
J. Bell
 Junior 
High School.
  5.2.
33 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
approved
 the 
following RSD contract amendment:
  Contractor:
   Waggonner and Ball Architects, APC
 Contract Period:
  08/15/2012 
- 08/15/2015
 Previous Amount:
  $1,151,421.0
8 Amended Amount:
  $5,500.00
 Contract Amount:
  $1,156,921.08
 Fund:
    IAT 
- FEMA 
 Competitive Process:
 Competitive
  Description of Service:  This amendment provides for 
additional 
services 
for a land survey at 
the n
ew 
three
-section PK
-8 school at Sherwood 
Forest School (New 
Œ PK-8).
  5.2.
34 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board:
  a. approved
 the 
Change 
Order for the construction contract with C.D.W. 
Services, L.L.C., for the mothballing of Andrew J. Bell Junior High 
School (project number 2
011-0853-0001) in the amount of 
  (Motion continues on page 16)
  
BOARD MINUTES
 -16- MARCH 7, 2014
   $361,334.40 in order to provide for: 
 (1) removal of Regulated 
Asbestos
-Containing Materials (RACM) for all hazardous materials in 
Building
-E (Christy Building) and Building A (Annex Building
) due to 
construction debris and finishes that were dislodged during the 
necessary repairs to structural walls; 
(2) installation of a course of 
brick and mortar cap over the brick wall at the demolished breezeway 
roof; and 
(3) general contractor's performa
nce and payment bonds 
and overhead and
 profit for the additional work; and
  b. directed
 the RSD to submit the approved Change Order for 
consideration and approval at the next regularly scheduled meeting of 

the Joint Legislative Committee on the Budget.
  5.2.
35 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board:
  a. approved
 the Change 
Order for the construction contract with FHP 
Tectonics Corporation for the refurbishment of Frederick A. Douglass 

High School (project number: 2012
-0868-0001) in the amount o
f $378,871.98 in order to provide for: 
 (1) asbestos removal associated 
with classroom window replacement, due to the uncovering of 
unforeseen caulk at these openings that consisted of 
Regulated 
Asbestos
-Containing 
Material
s (RACM)
; (2) repair of existing 
Reinforced 
Concrete 
Pipe (RCP); and 
(3) deletion of the installation of 
flood gates and 
Fiber 
Reinforced 
Panels (FRP) for the gymnasium, at 
the owner™
s request; and
  b. directed
 the RSD to submit the approved Change Order for 
consideration and approval at the
 next regularly scheduled meeting of 
the Joint Legislative Committee on the Budget.
  5.2.
36 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
received
 the 
report on the BESE Budget.
  5.2.
37 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board 
received
 the 
BESE member notification protocol developed by the State 
Superintendent
 of Education.
  5.2.
38 On motion of Mr. Guillot, seconded by Mr. Lee, 
the Board
 approved, as a 
Notice of Intent, revisions to Bulletin 1929, 
Louisiana Accounting and 
Unifo
rm Governmental Handbook
, adding Chapter 15. Expenditure 
Requirements, §1501. Seventy Percent Expenditure Requirement.
  
BOARD MINUTES
 -17- MARCH 7, 2014
    Agenda
 Item 5.3.
 Educator Effectiveness Committee
 (Schedule 4)
   5.3.
1 On motion of 
Ms. Boffy
, seconded by 
Mr. Guillot
, the Board re
ceive
d the 
update regarding the study of the state accountability system and 
value
-added model.
  5.3.
2 On motion of Ms. Boffy, seconded by Mr. Guillot, 
the Board 
deferred until 
April 2014:  ﬁConsideration of
 revisions to Bulletin 746, 
Louisiana 
Standards 
for State Cer
tification of School Personnel,
 regarding 
endorsements to existing teaching certificates
.ﬂ  Agenda
 Item 5.4.
 School Innovation and Turnaround Committee
 (Schedule 5)
   5.4.
1 On motion of 
Mr. Garvey
, seconded by
 Mr. Lee, the Board approve
d the
 request for a material amendment to the charter governing Linwood 
Public Charter School, operated by Shreveport Charter Schools, Inc., to 
add kindergarten and first grade in the fall of 2014 and expand an 
additional grade per year until the school serves 
grades K
-8.   * * * * * * * * * *  Public comments were received on the following 
School Innovation and 
Turnaround Committee 
agenda item:
  Agenda Item 3.1., ﬁ
Consideration of 
revisions to Bulletin 126, 
Charter 
Schools
, regarding charter school renewal and
 extension, evaluation of 
alternative charter schools, and streamlining of policies.ﬂ
  Support:
  None.
 Oppose:
  None.
 Information Only/Other:
 Mr. 
Shawn Fleming, Louisiana 
Developmental Disabilities Council.
  5.4.
2 On motion of Mr. Garvey, seconded by Mr. 
Guillot, the Board approved, 
as a Notice of Intent, revisions to Bulletin 126, 
Charter Schools
: §103. 
Definitions
; §105. Purpose of Charter Schools
; §505. Eligibility to Apply 
for a Type 4 Charter School
; §1101. Charter School Evaluation
; §1103. 
Alternate 
Evaluation of Charter Schools
; §1303. Extension Review
; §1503. Charter Renewal Process and Timeline
; §1903. Material 
  (Motion continues on page 18)
 
BOARD MINUTES
 -18- MARCH 7, 2014
    Amendments for BESE
-Authorized Charter Schools
; §1905. Non
-Material 
Amendments for BESE
-Authorized Charter
 Schools
; §2301. State 
Funding
; §2303. Federal Funding
; §2713. At
-Risk Students
; §2907.  
Leave of Absence
; and §2909. Employee Benefits, as presented by the 
LDE.
  Dr. Beebe and Ms. Hill were recorded as being opposed to the motion.
  Agenda
 Item 6.
 Board A
dvisory Council Reports
   Agenda
 Item 6.1.
 Nonpublic School Council
 (Schedule 6)
  On motion of Dr. Miranti, seconded by Mr. Guillot, the Board received the 
minutes of the Nonpublic School Council meeting held February 4, 2014, 
and approved the tentative a
genda for March 25, 2014.
  Agenda
 Item 6.2.
 Superintendents™ Advisory Council
 (Schedule 7)
  On motion of 
Dr. Miranti,
 seconded by 
Mr. Guillot,
 the Board received the 
minutes of the
 Superintendents™ Advisory Council meeting held 
February
 13, 2014, and appr
oved the tentative agenda for March
 20, 
2014.  With no further business to come before the Board, the meeting was adjourned at 
10:15
 a.m.
  
>>> 
>>> # combine pdf files, write pdf
>>> import PyPDF2
>>> # open all the pdf files and create readers for them
>>> pdf1File = open('meetingminutes1.pdf', 'rb')
>>> pdf2File = open('meetingminutes2.pdf', 'rb')
>>> reader1 = PyPDF2.PdfFileReader(pdf1File)
>>> reader2 = PyPDF2.PdfFileReader(pdf2File)
>>>
>>> writer = PyPDF2.PdfFileWriter()

>>> for pageNum in range(reader1.numPages):
	page = reader1.getPage(pageNum)
	writer.addPage(page)
>>> # skip second file's cover page
>>> for pageNum in range(1, reader2.numPages):
	page = reader2.getPage(pageNum)
	writer.addPage(page)

>>> # create a blank pdf
>>> outputFile = open('combinedMinutes.pdf', 'wb')
>>> writer.write(outputFile)
>>> # close all the files
>>> outputFile.close()
>>> pdf2File.close()
>>> pdf1File.close()

