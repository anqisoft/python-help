'''
<en>
	Function: Test the output of help()
	Result: Failed, although the corresponding html file and modules/help.txt file are generated, the content is not what you want.
			Need to change to command line execution: python -m pydoc -w ___failed > "../../output/modules/python -m pydoc -w ___failed.txt"
	Author: AnQi
	Version: v1.0.0
	Date: 2023-6-8
</en>
<zh_cn>
	功能：测试help()的输出
	结果：失败，虽然生成了相应的html文件及modules/help.txt文件，但内容并不是想要的。需改到命令行执行：python -m pydoc -w ___failed > "../../output/modules/python -m pydoc -w ___failed.txt"
	作者：安启
	版本：v1.0.0
	日期：2023-6-8
</zh_cn>
<zh_tw>
	功能：測試help()的輸出
	結果：失敗，雖然生成了相應的html文件及modules/help.txt文件，但內容並不是想要的。需改到命令行執行：python -m pydoc -w ___failed > "../../output/modules/python -m pydoc -w ___failed.txt"
	作者：安啟
	版本：v1.0.0
	日期：2023-6-8
</zh_tw>
'''


def main():
	import os

	# help('modules')

	catalog = '../../output/modules'
	if not os.path.exists(catalog):
		os.makedirs(catalog)

	result = help('modules')
	print(result, end='', flush=True, file=open(f'{catalog}/___failed.txt', 'w', encoding='utf-8'))


if __name__ == '__main__':
	main()
	
'''
<en>
	Result: The result of help('modules') is displayed on the command line, 
	but the actual file ../../output/modules/___failed.txt is only None.
</en>
<zh_cn>结果：在命令行显示出了help('modules')的结果，而实际文件../../output/modules/___failed.txt中仅为None。</zh_cn>
<zh_tw>結果：在命令行顯示出了help('modules')的結果，而實際文件../../output/modules/___failed.txt中僅為None。</zh_tw>
'''
