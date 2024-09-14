# gst/utils.py
# utils.py

def get_state_name_by_code(code):
    state_codes = {
        '01': 'JAMMU AND KASHMIR', '02': 'HIMACHAL PRADESH', '03': 'PUNJAB', '04': 'CHANDIGARH',
        '05': 'UTTARAKHAND', '06': 'HARYANA', '07': 'DELHI', '08': 'RAJASTHAN', '09': 'UTTAR PRADESH',
        '10': 'BIHAR', '11': 'SIKKIM', '12': 'ARUNACHAL PRADESH', '13': 'NAGALAND', '14': 'MANIPUR',
        '15': 'MIZORAM', '16': 'TRIPURA', '17': 'MEGHALAYA', '18': 'ASSAM', '19': 'WEST BENGAL',
        '20': 'JHARKHAND', '21': 'ODISHA', '22': 'CHATTISGARH', '23': 'MADHYA PRADESH', '24': 'GUJARAT',
        '26': 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU', '27': 'MAHARASHTRA',
        '29': 'KARNATAKA', '30': 'GOA', '31': 'LAKSHADWEEP', '32': 'KERALA', '33': 'TAMIL NADU',
        '34': 'PUDUCHERRY', '35': 'ANDAMAN AND NICOBAR ISLANDS', '36': 'TELANGANA', '37': 'ANDHRA PRADESH',
        '38': 'LADAKH', '97': 'OTHER TERRITORY', '99': 'CENTRE JURISDICTION'
    }
    return state_codes.get(code, '')
