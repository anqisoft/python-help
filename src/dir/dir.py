'''
<en>
	Function: Test the output of dir(), vars() and locals(), globals()
	Skip: getattr(), hasattr() and callable()
	Author: AnQi
	Version: v1.0.0
	Date: 2023-6-8
</en>
<zh_cn>
	功能：测试dir()、vars()和locals()、globals()的输出
	跳过：getattr()、hasattr()和callable()
	作者：安启
	版本：v1.0.0
	日期：2023-6-8
</zh_cn>
<zh_tw>
	功能：測試dir()、vars()和locals()、globals()的輸出
	跳過：getattr()、hasattr()和callable()
	作者：安啟
	版本：v1.0.0
	日期：2023-6-8
</zh_tw>
'''
import os

top_catalog = '../../output/dir/success'
if not os.path.exists(top_catalog):
	os.makedirs(top_catalog)
del top_catalog

print(vars(), end="", flush=True, file=open("../../output/dir/success/global_vars.txt", "w", encoding="utf-8"))
print(locals(), end="", flush=True, file=open("../../output/dir/success/global_locals.txt", "w", encoding="utf-8"))
print(globals(), end="", flush=True, file=open("../../output/dir/success/global_globals.txt", "w", encoding="utf-8"))

DIR = dir()
def main():
	top_catalog = '../../output/dir/success'
	# if not os.path.exists(top_catalog):
	# 	os.makedirs(top_catalog)

	print(DIR, end="", flush=True, file=open(f"{top_catalog}/index.txt", "w", encoding="utf-8"))
	print(vars(), end="", flush=True, file=open(f"{top_catalog}/vars.txt", "w", encoding="utf-8"))
	print(locals(), end="", flush=True, file=open(f"{top_catalog}/locals.txt", "w", encoding="utf-8"))
	print(globals(), end="", flush=True, file=open(f"{top_catalog}/globals.txt", "w", encoding="utf-8"))

	for any in DIR:
		catalog: str = f"{top_catalog}/{any}"
		if not os.path.exists(catalog):
			os.makedirs(catalog)

		print(dir(any), end="", flush=True, file=open(f"{catalog}/help.txt", "w", encoding="utf-8"))
		print(vars(), end="", flush=True, file=open(f"{catalog}/vars.txt", "w", encoding="utf-8"))
		print(locals(), end="", flush=True, file=open(f"{catalog}/locals.txt", "w", encoding="utf-8"))
		print(globals(), end="", flush=True, file=open(f"{catalog}/globals.txt", "w", encoding="utf-8"))

if __name__ == '__main__':
	main()