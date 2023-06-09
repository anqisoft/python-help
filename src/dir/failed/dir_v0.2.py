'''
<en>
	Explain: This is a failed attempt, and in the end only index.txt, as well as top_catalog.txt, top_catalog/help.txt.
	Author: AnQi
	Version: v0.2
	Date: 2023-6-8
</en>
<zh_cn>
	说明：这是一次失败的尝试，最终仅得到index.txt，以及top_catalog.txt、top_catalog/help.txt。
	作者：安启
	版本：v0.2
	日期：2023-6-8
</zh_cn>
<zh_tw>
	說明：這是一次失敗的嘗試，最終僅得到index.txt，以及top_catalog.txt、top_catalog/help.txt。
	作者：安啟
	版本：v0.2
	日期：2023-6-8
</zh_tw>
'''
import os

def main():
	top_catalog = '../../../output/dir/failed/v0.2'
	if not os.path.exists(top_catalog):
		os.makedirs(top_catalog)

	print(dir(), end="", flush=True, file=open(f"{top_catalog}/index.txt", "w", encoding="utf-8"))

	for any in dir():
		# print(dir(any), end="", flush=True, file=open(f"{top_catalog}/{any}.txt", "w", encoding="utf-8"))

		catalog: str = f"{top_catalog}/{any}"
		if not os.path.exists(catalog):
			os.makedirs(catalog)

		print(dir(any), end="", flush=True, file=open(f"{catalog}/help.txt", "w", encoding="utf-8"))

if __name__ == '__main__':
	main()