'''
<en>
	Explain: This is a failed attempt, because there will be one more top_catalog.
	Author: AnQi
	Version: 0.1
	Date: 2023-6-8
</en>
<zh_cn>
	说明：这是一次失败的尝试，将多出一项top_catalog。
	作者：安启
	版本：0.1
	日期：2023-6-8
</zh_cn>
<zh_tw>
	說明：這是一次失敗的嘗試，將多出一項top_catalog。
	作者：安啟
	版本：0.1
	日期：2023-6-8
</zh_tw>
'''
import os

top_catalog = '../../../output/dir/failed/v0.1'
if not os.path.exists(top_catalog):
	os.makedirs(top_catalog)

print(dir(), end="", flush=True, file=open(f"{top_catalog}/index.txt", "w", encoding="utf-8"))

for any in dir():
	# print(dir(any), end="", flush=True, file=open(f"{top_catalog}/{any}.txt", "w", encoding="utf-8"))

	catalog: str = f"{top_catalog}/{any}"
	if not os.path.exists(catalog):
		os.makedirs(catalog)

	print(dir(any), end="", flush=True, file=open(f"{catalog}/help.txt", "w", encoding="utf-8"))