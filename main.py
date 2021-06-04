import random

#{"eventCategory":"General Health","eventLabel":"all","plan_type":"Preferred provider organization (PPO)", "y1":"84%","y2":"85%","y3":"84%","y4":"86%","y5":"79%","delta":"-7%","indicator":"2","sparkline_data":"84,85,84,86,79"},

def get_delta_indicator(delta):
    return_value = 0

    if delta == 0:
        return_value = 0
    if delta > 0 and delta <= 6:
        return_value = 1
    if delta > 6:
        return_value = 2
    if delta < 0 and delta <= 6:
        return_value = -1
    if delta < -6:
        return_value = -2

    return return_value

SHRM_healthcare = [
                    {
                        "name": "General Health",
                        "plans": ["Preferred provider organization","Health maintenance organization (HMO)","Point of service (POS)","Indemnity plan (fee-for-service)"]
                    },
                    {
                        "name": "HSA & FSA",
                        "plans": ["Medical flexible spending account (FSA) (IRC Section 125)","Health savings account (HSA)","Health reimbursement arrangement (HRA)","Qualified Small Employer Health Reimbursement Arrangement (QSEHRA)"]
                    },
                    {
                        "name": "Prescription Drug",
                        "plans": ["Prescription drug coverage bundled with medical insurance","Mail-order prescription program","Pharmacy management program (independent of medical plan management)"]
                    },
                    {
                        "name": "Retirement",
                        "plans": ["Traditional 401(k) or similar defined contribution retirement savings plan (e.g., 403(b)s, 457s, federal Thrift Savings Plan)","Roth 401(k) or similar defined contribution retirement savings plan","Traditional defined benefit pension plan (open to all employees)"]
                    },
                    {
                        "name": "401(k)",
                        "plans": ["Automatic enrollment for NEW or EXISTING employees","Hardship withdrawals","Loans against savings plan balance"]
                    },
                    {
                        "name": "Vacation & Sick",
                        "plans": ["Paid open/unlimited leave","Paid vacation time","Paid sick time"]
                    },
                    {
                        "name": "Family",
                        "plans": ["Paid family leave","Elder care leave above federal FMLA leave","Paid leave to care for immediate family"]
                    },
                    {
                        "name": "Flex Work",
                        "plans": ["Flextime during core business hours (allowing employees to choose their work hours within limits during core business hours)","Flextime outside of core business hours (allowing employees to choose their work hours outside of core business hours)","Compressed workweek (allowing full-time employees to work longer days for part of the week or pay period in exchange for shorter days or a day off each week or pay period)","Break arrangements (employees who generally can only take assigned breaks enter into an arrangement with their employers giving them more flexibility over when they take breaks)"]
                    },
                    {
                        "name": "Family Friendly",
                        "plans": ["Elder care referral service providing employees with the names of elder care providers (separate from or part of an EAP","Dependent care flexible spending account (IRC Section 125)","Bring child to work in emergency (i.e., as backup care for an unexpected event)","Subsidized child care center or program"]
                    },
                    {
                        "name": "Professional Development",
                        "plans": ["Formal training or education provided by or paid for by employer to keep skills current","Certification/recertification fees","Formal mentoring program","Professional memberships (e.g., SHRM)"]
                    },
                    {
                        "name": "Wellness",
                        "plans": ["General wellness program","Onsite seasonal flu vaccinations","Tobacco cessation program"]
                    }
                ]

parent = "SHRM.utils.healthcare"

filter_types = ["all",
                "M","NE","S","W",
                "SM","MD","LG","XL",
                "CONSTR","EDUHLTH","FINANCE","GOVT","LSHOSP","MANFCT","OTHER","OTHSERV","PROFBUS","R_W_T_U"]

with open('my_json.txt', 'w') as the_file:

    for obj in SHRM_healthcare:
        
        #json_string = '{"eventCategory":"General Health","eventLabel":"all","plan_type":"Preferred provider organization (PPO)", "y1":"84%","y2":"85%","y3":"84%","y4":"86%","y5":"79%","delta":"-7%","indicator":"2","sparkline_data":"84,85,84,86,79"},'

        for filter_type in filter_types:
        
            for plan in obj['plans']:

                y1 = random.randrange(50, 90, 2)
                y2 = random.randrange(60, 90, 2)
                y3 = random.randrange(70, 90, 2)
                y4 = random.randrange(80, 90, 2)
                y5 = random.randrange(80, 90, 2)
                delta = y5-y4
                delta_indicator = get_delta_indicator(delta)
                json_string = '"eventCategory":"{}","eventLabel":"{}","plan_type":"{}", "y1":"{}%","y2":"{}%","y3":"{}%","y4":"{}%","y5":"{}%","delta":"{}%","indicator":"{}","sparkline_data":"{},{},{},{},{}"'.format(obj['name'], filter_type, plan, y1, y2, y3, y4, y5, delta, delta_indicator, y1, y2, y3, y4, y5)
                #print('{' + json_string + '},\n')
                the_file.write('{' + json_string + '},\n')

the_file.close()