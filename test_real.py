# Process to get the masks of the controller and the object

import os

base_path = "/home/hanxiao/Desktop/Research/proj-qqtt/proj-QQTT/data/rope_variants"
case_name = "rope_1"
TEXT_PROMPT = "twine.hand"
camera_num = 3

for camera_idx in range(camera_num):
    print(f"python real_usage.py --base_path {base_path} --case_name {case_name} --TEXT_PROMPT {TEXT_PROMPT} --camera_idx {camera_idx}")
    os.system(f"python real_usage.py --base_path {base_path} --case_name {case_name} --TEXT_PROMPT {TEXT_PROMPT} --camera_idx {camera_idx}")
    os.system(f"rm -rf real_data/{case_name}/{camera_idx}")