#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import traci

import sumolib


def start_sumo(sumo_binary, sumo_config):
    traci.start([sumo_binary, "-c", sumo_config])
    print("Simulation started")


def end_sumo():
    traci.close()
    print("Simulation ended")

'''

def edge_density(target_edge, time):

    density_data = {}

    vehicles_on_edge = traci.edge.getLastStepVehicleIDs(target_edge)
    lanes = traci.edge.getLaneIDs(target_edge)

    lane_lengths = [traci.lane.getLength(lane) for lane in lanes]
    avg_length = sum(lane_lengths) / lane_lengths


    if avg_length > 0:
        edge_density = len(vehicles_on_edge) / avg_length
    else:
        edge_density = 0
        
    density_data[time] = {"edge_density (#/m)" : edge_density}

    return density_data

'''

def edge_speed_avg(target_edge):
    avg_speed = traci.edge.getLastStepMeanSpeed(target_edge)
    return avg_speed*3.6


#분과 속도/min을 list로 반환
speeds = []
times = []
minute_speeds = []
minute = 0

def edge_speed_avg_min(target_edge):

    global speeds, times, minute_speeds, minute

    minute_speeds.append(edge_speed_avg(target_edge))
 #   value = edge_speed_avg(target_edge)
#    print(f"Returned value from edge_speed_avg: {value}")
    if len(minute_speeds) == 60:
        avg_speed = sum(minute_speeds) / 60
        speeds.append(avg_speed)
        times.append(minute)
        minute += 1
        minute_speeds = []

    return times, speeds

def reset_data():
    global speeds, times, minute_speeds, minute
    speeds = []
    times = []
    minute_speeds = []
    minute = 0    


def vehicle_speed(vehicle_id):
    return traci.vehicle.getSpeed(vehicle_id)

'''
def calculate_flow_speed(flow_id):
    # 현재 시뮬레이션에서 모든 차량의 ID를 가져옴
    vehicle_ids = traci.vehicle.getIDList()
    
    # flow_id에서 생성된 차량 필터링 (예: "flowID.index" 형식)
    flow_vehicles = [vid for vid in vehicle_ids if vid.startswith(flow_id)]
    
    # 해당 차량들의 속도 계산
    speeds = []
    for vehicle_id in flow_vehicles:
        speed = traci.vehicle.getSpeed(vehicle_id)  # 개별 차량의 속도 (m/s)
        speeds.append(speed)
    
    # 평균 속도 계산 (m/s -> km/h 변환)
    if speeds:
        avg_speed = sum(speeds) / len(speeds) * 3.6  # m/s to km/h
    else:
        avg_speed = 0  # 해당 flow에서 생성된 차량이 없는 경우 0
    
    return avg_speed
'''

def vehicle_position(vehicle_id):
    return traci.vehicle.getPosition(vehicle_id)

def flow_position(flow_id):

    vehicle_ids = traci.vehicle.getIDList()
    flow_vehicles = [vid for vid in vehicle_ids if vid.startswith(flow_id)]
    positions = []
    for vehicle_id in flow_vehicles:
        position = traci.vehicle.getPosition(vehicle_id)
        positions.append(position)
    
    if not flow_vehicles:   
        return "Not Found"
    
    return positions


def vehicle_type(vehicle_id):
    return traci.vehicle.getTypeID(vehicle_id)





def vehicle_info():
    veh_ids = traci.vehicle.getIDList()

    for vid in veh_ids:
        vtype = traci.vehicle.getTypeID(vid)
        speed = traci.vehicle.getSpeed(vid)*3.6
        x, y = traci.vehicle.getPosition(vid)

    print(f"ID={vid}, type={vtype}, speed={speed:.2f} km/h, pos=({x:.2f}, {y:.2f})")


def plot_graph(title, x, y):
    plt.figure(figsize=(10,5))
    plt.plot(x, y, linewidth = 1, color="blue")
    plt.title(title)
    plt.grid(True)
    plt.show()

