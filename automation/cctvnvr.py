import requests
import pandas as pd
from datetime import datetime
from requests.auth import HTTPDigestAuth

# NVR API configurations
NVR_CONFIGS = [
    {
        "name": "NVR 1",
        "ip": "http://<nvr1_ip>",
        "username": "your_username1",
        "password": "your_password1"
    },
    {
        "name": "NVR 2",
        "ip": "http://<nvr2_ip>",
        "username": "your_username2",
        "password": "your_password2"
    },
    # Add more NVR configurations as needed
]

# Fetch all cameras and their status for a specific NVR
def get_camera_status(nvr_config):
    url = f"{nvr_config['ip']}/ISAPI/ContentMgmt/InputProxy/channels"
    response = requests.get(url, auth=HTTPDigestAuth(nvr_config['username'], nvr_config['password']))
    response.raise_for_status()
    return response.json()

# Generate report on camera statuses for all NVRs
def generate_camera_report():
    all_report_data = []
   
    for nvr_config in NVR_CONFIGS:
        camera_data = get_camera_status(nvr_config)
       
        for camera in camera_data['InputProxyChannelList']['InputProxyChannel']:
            camera_id = camera['id']
            camera_name = camera['name']
            camera_status_url = f"{nvr_config['ip']}/ISAPI/System/Video/inputs/channels/{camera_id}/status"
           
            status_response = requests.get(camera_status_url, auth=HTTPDigestAuth(nvr_config['username'], nvr_config['password']))
            status_response.raise_for_status()
            status = status_response.json()['status']
           
            all_report_data.append({
                "NVR Name": nvr_config['name'],
                "Camera Name": camera_name,
                "Camera ID": camera_id,
                "Status": status,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
   
    # Convert report data to DataFrame and save to Excel
    df = pd.DataFrame(all_report_data)
    df.to_excel("hikvision_camera_status_report.xlsx", index=False)
    print("Report saved as 'hikvision_camera_status_report.xlsx'")

# Execute the report generation
generate_camera_report()