import os  
import sys  
  
def read_file(file_path):  
    with open(file_path, 'r', encoding='utf-8') as file:  
        lines = file.readlines()  
    # 使用制表符分割每一行，并返回第二列内容  
    return [line.strip().split('\t')[1] for line in lines if len(line.strip().split('\t')) > 1]  # 确保有足够多的列  
  
def extract_data(file1_path, file2_path, output_dir):  
    file1_data = read_file(file1_path)  
    with open(file2_path, 'r', encoding='utf-8') as file:  
        file2_data = file.readlines()  
  
    # 确保输出目录存在  
    os.makedirs(output_dir, exist_ok=True)  
  
    for item in file1_data:  
        for line in file2_data:  
            columns = line.strip().split('\t')  # 使用制表符分割列  
            if item in columns[5]:  # 检查第6列是否包含file1_data中的内容  
                output_file_path = os.path.join(output_dir, f"{item}.txt")  
                with open(output_file_path, 'a', encoding='utf-8') as output_file:  
                    output_file.write(columns[-1] + '\n')  # 提取最后一列内容  
  
# 检查是否提供了足够的命令行参数  
if len(sys.argv) != 4:  
    print("Usage: python script_name.py file1_path file2_path output_dir")  
    sys.exit(1)  
  
# 从命令行参数获取文件路径和输出目录  
file1_path = sys.argv[1]  
file2_path = sys.argv[2]  
output_dir = sys.argv[3]  
  
# 提取数据并保存到文件  
extract_data(file1_path, file2_path, output_dir)