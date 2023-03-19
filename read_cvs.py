import csv

def get_application_records():
    application_record_dict = []
    ids = []
    with open('application_record.csv', 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for i, row in enumerate(csvreader):
            if i >= 10000:  # Stop after 10000 rows
                break
            ids.append(row[0])
            application_record_data = {
            'id' : row[0] ,
            'code_gender' : row[1],
            'flag_own_car' : row[2],
            'flag_own_realty' : row[3],
            'cnt_children' : row[4],
            'amt_income_total' : row[5],
            'name_income_type' : row[6],
            'name_education_type' : row[7],
            'name_family_status' : row[8],
            'name_housing_type' : row[9],
            'days_birth' : row[10],
            'days_employed' : row[11],
            'flag_mobil' : row[12],
            'flag_work_phone' : row[13],
            'flag_phone' : row[14],
            'flag_email' : row[15],
            'occupation_type' : row[16],
            'cnt_fam_members' : row[17]}
            application_record_dict.append(application_record_data)
    return ids, application_record_dict 


