import os
import requests
from pathlib import Path

# s3 bucket where data is stored
url = "https://qca-data.s3.amazonaws.com/"

# local path where the data will be downloaded
local_base_path = "qca-data/"

# remote list of folders and files to be downloaded
folders_list = ["fig2/", "fig3a/", "fig3b/", "fig4/", "figS15/"] 
files_list = ["program_params.json", "U.npy", "T.npy", "r.npy", "samples.npy"]

for folder in folders_list:
    local_folder_path = local_base_path+folder
    if not os.path.exists(local_folder_path):
        os.makedirs(local_folder_path)
    for file in files_list:
        file_path = folder+file
        local_file_path = local_folder_path + file
        r = requests.get(url+file_path)
        open(local_file_path,"wb").write(r.content)
