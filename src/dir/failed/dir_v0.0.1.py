'''
<en>
	Explain: This is a failed attempt, and I haven't figured out why yet. The content of all files is None.
	Author: AnQi
	Version: 0.0.1
	Date: 2023-6-8
</en>
<zh_cn>
	说明：这是一次失败的尝试，目前暂时还没想明白为什么。所有文件的内容都是None。
	作者：安启
	版本：0.0.1
	日期：2023-6-8
</zh_cn>
<zh_tw>
	說明：這是一次失敗的嘗試，目前暫時還沒想明白為什麼。所有文件的內容都是None。
	作者：安啟
	版本：0.0.1
	日期：2023-6-8
</zh_tw>
'''

import os

DIR = dir()
def main():
	top_catalog = '../../../output/dir/failed/v0.0.1'
	if not os.path.exists(top_catalog):
		os.makedirs(top_catalog)

	print(help("modules"), '\n', end="", flush=True, file=open(f"{top_catalog}/index.txt", "w", encoding="utf-8"))  # => None

	for any in DIR:
		# catalog: str = f"{top_catalog}/{any}"
		#
		# if not os.path.exists(catalog):
		# 	os.makedirs(catalog)
		#
		# print(help(any), end="", flush=True, file=open(f"{catalog}/help.txt", "w", encoding="utf-8")) # => None
		print(f'help({any})', help(any), '\n', end="", flush=True, file=open(f"{top_catalog}/index.txt", "a", encoding="utf-8"))  # => None

if __name__ == '__main__':
	main()