"""
Generate the synthetic health analytics sample dataset.

ALL DATA PRODUCED BY THIS SCRIPT IS SYNTHETIC. It contains no real patients,
providers, facilities, or health records. Any resemblance to a real person or
organisation is coincidental.

Run from the repository root:
    python scripts/generate_sample_data.py

Uses a fixed random seed, so output is reproducible. Standard library only.
"""

import csv, random, datetime, os, pathlib
random.seed(42)

OUT = pathlib.Path(__file__).resolve().parent.parent / "data"
OUT.mkdir(exist_ok=True)

# ---------- DimDepartment ----------
depts = [
    ("Emergency Department","Acute Care","Royal Sydney General","NSW"),
    ("Cardiology","Medical Specialties","Royal Sydney General","NSW"),
    ("Orthopaedics","Surgical Services","Royal Sydney General","NSW"),
    ("Oncology","Medical Specialties","Parkville Health Centre","VIC"),
    ("Maternity","Women's Health","Parkville Health Centre","VIC"),
    ("Respiratory Medicine","Medical Specialties","Parkville Health Centre","VIC"),
    ("General Surgery","Surgical Services","Brisbane Northside Hospital","QLD"),
    ("Intensive Care","Acute Care","Brisbane Northside Hospital","QLD"),
    ("Rehabilitation","Sub-Acute Care","Brisbane Northside Hospital","QLD"),
    ("Paediatrics","Women's Health","Adelaide Central Hospital","SA"),
    ("Renal Medicine","Medical Specialties","Adelaide Central Hospital","SA"),
    ("Mental Health","Community Services","Adelaide Central Hospital","SA"),
]
with open(f"{OUT}/DimDepartment.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["DepartmentKey","DepartmentName","ServiceLine","FacilityName","State"])
    for i,d in enumerate(depts,1): w.writerow([i,*d])

# ---------- DimProvider ----------
first=["Amara","Liam","Priya","Noah","Chen","Isla","Ravi","Mia","Tomas","Grace","Hugo","Sana","Elias","Nina","Omar","Zara","Felix","Ada","Kai","Leila"]
last=["Whitfield","Nguyen","Kaur","O'Brien","Zhang","Fitzgerald","Menon","Sullivan","Petrov","Achebe","Lindqvist","Rahman","Moreau","Castellano","Haddad","Okafor","Brennan","Silva","Yamamoto","Novak"]
specialties=["Cardiology","Emergency Medicine","Orthopaedic Surgery","Oncology","Obstetrics","Respiratory Medicine","General Surgery","Intensive Care","Rehabilitation Medicine","Paediatrics","Nephrology","Psychiatry"]
ptypes=["Consultant","Registrar","Specialist","Visiting Medical Officer"]
with open(f"{OUT}/DimProvider.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["ProviderKey","ProviderName","Specialty","ProviderType","YearsExperience"])
    for i in range(1,61):
        w.writerow([i,f"Dr {random.choice(first)} {random.choice(last)}",random.choice(specialties),random.choice(ptypes),random.randint(2,34)])

# ---------- DimPatient ----------
agebands=["0-17","18-34","35-49","50-64","65-79","80+"]
ageweights=[8,18,20,22,22,10]
genders=["Female","Male","Other"]
regions=["Inner Sydney","Western Sydney","Melbourne Metro","Regional VIC","Brisbane Metro","Regional QLD","Adelaide Metro","Regional SA"]
ins=["Medicare Only","Private - Basic","Private - Gold","DVA","Workers Compensation"]
inw=[46,18,22,7,7]
with open(f"{OUT}/DimPatient.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["PatientKey","PatientID","AgeBand","Gender","Region","InsuranceType","ChronicConditionFlag"])
    for i in range(1,801):
        ab=random.choices(agebands,ageweights)[0]
        chronic="Yes" if random.random() < (0.55 if ab in ("65-79","80+") else 0.18) else "No"
        w.writerow([i,f"PT-{100000+i}",ab,random.choices(genders,[49,49,2])[0],random.choice(regions),random.choices(ins,inw)[0],chronic])

# ---------- DimDate ----------
start=datetime.date(2024,7,1); end=datetime.date(2026,6,30)
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
with open(f"{OUT}/DimDate.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["DateKey","Date","Year","Quarter","MonthNumber","MonthName","DayOfWeek","IsWeekend","FinancialYear"])
    d=start
    while d<=end:
        fy = d.year+1 if d.month>=7 else d.year
        w.writerow([int(d.strftime("%Y%m%d")),d.isoformat(),d.year,f"Q{(d.month-1)//3+1}",d.month,months[d.month-1],
                    d.strftime("%A"),"Yes" if d.weekday()>=5 else "No",f"FY{fy-1}-{str(fy)[2:]}"])
        d+=datetime.timedelta(days=1)

# ---------- FactEncounter ----------
adm=["Emergency","Elective","Transfer","Day Procedure"]
admw=[44,34,8,14]
outcomes=["Discharged Home","Transferred","Discharged to Rehab","Deceased","Left Against Advice"]
outw=[80,8,8,2,2]
days=(end-start).days
with open(f"{OUT}/FactEncounter.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["EncounterID","DateKey","PatientKey","ProviderKey","DepartmentKey","AdmissionType",
                "LengthOfStayDays","ReadmittedWithin30Days","WaitTimeMinutes","TotalCost","ReimbursedAmount","SatisfactionScore","Outcome"])
    for i in range(1,6001):
        d=start+datetime.timedelta(days=random.randint(0,days))
        a=random.choices(adm,admw)[0]
        dept=random.randint(1,12)
        los = 0 if a=="Day Procedure" else max(1,int(random.lognormvariate(1.0,0.7)))
        if dept==8: los=max(los,2)
        wait = random.randint(5,320) if a=="Emergency" else random.randint(0,60)
        base = 850 if a=="Day Procedure" else 2400
        cost = round(base + los*random.uniform(900,2100) + random.uniform(0,1800),2)
        reimb = round(cost*random.uniform(0.62,0.98),2)
        readm = "Yes" if random.random() < (0.14 if los>5 else 0.06) else "No"
        sat = min(10,max(1,round(random.gauss(8.1 if wait<90 else 6.6,1.4))))
        w.writerow([f"ENC-{200000+i}",int(d.strftime("%Y%m%d")),random.randint(1,800),random.randint(1,60),dept,a,
                    los,readm,wait,cost,reimb,sat,random.choices(outcomes,outw)[0]])
print("done")
