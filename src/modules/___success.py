import os

def main():
	catalog = '../../output/modules'
	if not os.path.exists(catalog):
		os.makedirs(catalog)

	def get_system_modules():
		'''
			<en>Function: Get all modules in the system</en>
			<zh_cn>功能：获取系统中所有的模块</zh_cn>
			<zh_tw>功能：獲取系統中所有的模塊</zh_tw>
		'''
		import sys

		modules = sys.modules.keys()
		with open(f'{catalog}/sys_modules.txt', 'w') as f:
			for module in modules:
				f.write(module + '\n')

	def get_all_modules():
		'''
			<en>Function: Get all modules in the system</en>
			<zh_cn>功能：获取系统中所有的模块</zh_cn>
			<zh_tw>功能：獲取系統中所有的模塊</zh_tw>
		'''
		import pkgutil

		all_modules = [module for module in pkgutil.iter_modules()]

		with open(f'{catalog}/all_modules.txt', 'w') as f:
			for module in all_modules:
				module_name = module.name
				f.write(module_name + '\n')

		for module in all_modules:
			module_name = module.name
			try:
				module_dir = dir(__import__(module_name))
				sub_catalog = f'{catalog}/{module_name}'
				if not os.path.exists(sub_catalog):
					os.makedirs(sub_catalog)

				# print(dir(module), end="", flush=True, file=open(f"{sub_catalog}/dir.txt", "w", encoding="utf-8"))

				with open(f"{sub_catalog}/dir.txt", 'w') as f:
					for item in module_dir:
						f.write(str(item) + '\n')
			except Exception as e:
				print(e.__traceback__.tb_lineno, e)
				continue


	get_system_modules()
	get_all_modules()

if __name__ == '__main__':
	main()