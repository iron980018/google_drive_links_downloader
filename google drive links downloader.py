import gdown
import os

#.txt檔路徑
urls_txt_file = r'XXX'
#依據需求更改副檔名
file_extension = ".7z"
download_folder = "./download"

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

with open(urls_txt_file, 'r') as file:
    
    lines = file.readlines()

    # 每次處理三行
    for i in range(0, len(lines), 3):
        name = lines[i].strip()  # 提取第一行為name
        link = lines[i + 1].strip()  # 提取第二行為link
        
        output = download_folder+"/"+name+file_extension

        gdown.download(link, output, quiet=False, fuzzy=True)

        print(name+" download successful")
        
print("all finish !!!")