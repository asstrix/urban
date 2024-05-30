import os, time

directory = f"C:\\Users\\{os.getlogin()}\\Downloads\\"
for i, j, k in os.walk(directory):
	for file in k:
		fullpath = os.path.join(i, file)
		size = os.path.getsize(fullpath)
		htime = time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(os.path.getmtime(fullpath)))
		dirname = os.path.dirname(i)
		print(f'file name: {fullpath}, dir_name: {dirname}, size: {size / 1024:.2f} Kb, time: {htime}')