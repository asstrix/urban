import os, time

directory = f"C:\\Users\\{os.getlogin()}\\Downloads\\"
for i, j, k in os.walk(directory):
	for file in k:
		path = os.path.join(i, file)
		size = os.path.getsize(path)
		htime = time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(os.path.getmtime(path)))
		dirname = os.path.dirname(path)
		print(f'file name: {path}, dir_name: {dirname}, size: {size / 1024:.2f} Kb, modified time: {htime}')