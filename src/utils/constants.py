test_time:str = 'Test_Time(s)'
date_time:str = 'Date_Time'
step_time:str = 'Step_Time(s)'
c_index:str = 'Cycle_Index'
step_index:str = 'Step_Index'
current:str = 'Current(A)'
voltage:str = 'Voltage(V)'
charge_cap:str = 'Charge_Capacity(Ah)'
discharge_cap:str = 'Discharge_Capacity(Ah)'
channel:str = 'Channel'
dataset_root:str = 'src/dataset'
ds_cleaned:str = f'{dataset_root}/cleaned'
index:str = 'Index'

charge_indexes = [
    1,
    3,
    5,
    6,
    8,
    7,
    9,
]
discharge_indexes = [
    1,
    2,
    3,
    4,
    5,
    6,
    8,
    9,
]
white_list = [
    test_time,
    date_time,
    step_time,
    c_index,
    step_index,
    voltage,
    current,
    charge_cap,
    discharge_cap]

charge_list = [
    test_time,
    step_time,
    step_index,
    c_index,
    current,
    voltage,
    charge_cap
]

discharge_list = [
    test_time,
    step_time,
    step_index,
    c_index,
    current,
    voltage,
    discharge_cap
]