import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=0
    filter1=employees.loc[(employees['employee_id']%2==1)&(employees['name'].str[0]!='M'),'bonus']=employees['salary']
    result=employees[['employee_id','bonus']].sort_values(by='employee_id',ascending=True)
    return result