test_time:str = 'Test_Time(s)'
c_index:str = 'Cycle_Index'
step_Index:str = 'Step_Index'
current:str = 'Current(A)'
voltage:str = 'Voltage(V)'
charge_cap:str = 'Charge_Capacity(Ah)'
discharge_cap:str = 'Discharge_Capacity(Ah)'
channel:str = 'Channel'
dataset_root = 'src/dataset'
ds_cleaned = f'{dataset_root}/cleaned'
index = 'Index'

white_list = [
    test_time,
    c_index,
    step_Index,
    voltage,
    current,
    charge_cap,
    discharge_cap]