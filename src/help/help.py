'''
<en>
	Function: Try to output the results of the help() command to files
	Unfinished: The output of the help() command of various data types, common methods, and common modules.
	Note: Will open the default browser and redirect to url: https://xkcd.com/353/.
	Author: AnQi
	Version: 0.0.1
	Date: 2023-6-9
	Email: anqisoft@gmail.com
</en>
<zh_cn>
	功能：尝试将help()命令的结果输出到文件中
	未完：各种数据类型、常用方法、常用模块的help()命令的输出
	注意：会打开默认浏览器并重定向到url：https://xkcd.com/353/。
	作者：安启
	版本：0.0.1
	日期：2023-6-9
	邮箱：anqisoft@gmail.com
</zh_cn>
<zh_tw>
	功能：嘗試將help()命令的結果輸出到文件中
	未完：各種數據類型、常用方法、常用模塊的help()命令的輸出
	注意：會打開默認瀏覽器並重定向到url：https://xkcd.com/353/。
	作者：安啟
	版本：0.0.1
	日期：2023-6-9
	郵箱：anqisoft@gmail.com
</zh_tw>
'''
import os
import sys


def main():
	top_catalog = '../../output/help'
	if not os.path.exists(top_catalog):
		os.makedirs(top_catalog)

	def change_stdout_and_help(name, filename):
		sys.stdout = open(filename, 'w', encoding='utf-8')
		help(name)
		sys.stdout = sys.__stdout__

	def help_top():
		for name in ['modules', 'keywords', 'symbols', 'topics', 'builtins']:  # No: 'exceptions'
			change_stdout_and_help(name, f'{top_catalog}/{name}.txt')

	def help_dir():
		catalog = f'{top_catalog}/dir'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		# Removed: '__annotations__', '__builtins__', '__cached__',
		for name in ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', ]:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	def help_modules():
		catalog = f'{top_catalog}/modules'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['___failed', '___success', '_asyncio', '_asyncio_d', '_bz2', '_bz2_d', '_ctypes', '_ctypes_d',
		             '_ctypes_test', '_ctypes_test_d', '_decimal', '_decimal_d', '_elementtree', '_elementtree_d',
		             '_hashlib', '_hashlib_d', '_lzma', '_lzma_d', '_msi', '_msi_d', '_multiprocessing',
		             '_multiprocessing_d', '_overlapped', '_overlapped_d', '_queue', '_queue_d', '_socket', '_socket_d',
		             '_sqlite3', '_sqlite3_d', '_ssl', '_ssl_d', '_testbuffer', '_testbuffer_d', '_testcapi',
		             '_testcapi_d', '_testconsole', '_testconsole_d', '_testimportmultiple', '_testimportmultiple_d',
		             '_testinternalcapi', '_testinternalcapi_d', '_testmultiphase', '_testmultiphase_d', '_tkinter',
		             '_tkinter_d', '_uuid', '_uuid_d', '_zoneinfo', '_zoneinfo_d', 'pyexpat', 'pyexpat_d', 'select',
		             'select_d', 'unicodedata', 'unicodedata_d', 'winsound', 'winsound_d', '__future__', '_aix_support',
		             '_bootlocale', '_bootsubprocess', '_collections_abc', '_compat_pickle', '_compression',
		             '_markupbase', '_osx_support', '_py_abc', '_pydecimal', '_pyio', '_sitebuiltins', '_strptime',
		             '_threading_local', '_weakrefset', 'abc', 'aifc', 'antigravity', 'argparse', 'ast', 'asynchat',
		             'asyncio', 'asyncore', 'base64', 'bdb', 'binhex', 'bisect', 'bz2', 'cProfile', 'calendar', 'cgi',
		             'cgitb', 'chunk', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'colorsys', 'compileall',
		             'concurrent', 'configparser', 'contextlib', 'contextvars', 'copy', 'copyreg', 'crypt', 'csv',
		             'ctypes', 'curses', 'dataclasses', 'datetime', 'dbm', 'decimal', 'difflib', 'dis', 'distutils',
		             'doctest', 'email', 'encodings', 'ensurepip', 'enum', 'filecmp', 'fileinput', 'fnmatch',
		             'formatter', 'fractions', 'ftplib', 'functools', 'genericpath', 'getopt', 'getpass', 'gettext',
		             'glob', 'graphlib', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'http', 'idlelib', 'imaplib',
		             'imghdr', 'imp', 'importlib', 'inspect', 'io', 'ipaddress', 'json', 'keyword', 'lib2to3',
		             'linecache', 'locale', 'logging', 'lzma', 'mailbox', 'mailcap', 'mimetypes', 'modulefinder',
		             'msilib', 'multiprocessing', 'netrc', 'nntplib', 'ntpath', 'nturl2path', 'numbers', 'opcode',
		             'operator', 'optparse', 'os', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil',
		             'platform', 'plistlib', 'poplib', 'posixpath', 'pprint', 'profile', 'pstats', 'pty', 'py_compile',
		             'pyclbr', 'pydoc', 'pydoc_data', 'queue', 'quopri', 'random', 're', 'reprlib', 'rlcompleter',
		             'runpy', 'sched', 'secrets', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd',
		             'smtplib', 'sndhdr', 'socket', 'socketserver', 'sqlite3', 'sre_compile', 'sre_constants',
		             'sre_parse', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau',
		             'symbol', 'symtable', 'sysconfig', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'test',
		             'textwrap', 'this', 'threading', 'timeit', 'tkinter', 'token', 'tokenize', 'trace', 'traceback',
		             'tracemalloc', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'unittest', 'urllib', 'uu',
		             'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'wsgiref', 'xdrlib', 'xml', 'xmlrpc',
		             'zipapp', 'zipfile', 'zipimport', 'zoneinfo', '_distutils_hack', '_virtualenv', 'pip',
		             'pkg_resources', 'setuptools', 'wheel', ]:
			try:
				print(name)
				change_stdout_and_help(name, f'{catalog}/{name}.txt')
			except Exception as e:
				print(name, e.__traceback__.tb_lineno, e)
				continue

	def help_keywords():
		catalog = f'{top_catalog}/keywords'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		# Removed: '__peg_parser__',
		for name in ['FALSE', 'None', 'TRUE', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
		             'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
		             'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
		             'yield', ]:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	def help_symbols():
		catalog = f'{top_catalog}/symbols'
		if not os.path.exists(catalog):
			os.makedirs(catalog)

		filename = f'{catalog}/all.txt'
		if os.path.exists(filename):
			os.remove(filename)

		open(filename, 'a', encoding='utf-8').close()

		temp_filename = f'{catalog}/temp.txt'
		for name in ['!=', '"', '"""', '%', '%=', '&', '&=', "'", "'''", '(', ')', '*', '**', '**=', '*=', '+', '+=',
		             ',', '-', '-=', '.', '...', '/', '//', '//=', '/=', ':', '<', '<<', '<<=', '<=', '<>', '==', '>',
		             '>=', '>>', '>>=', '@', 'J', '[', '\\', ']', '^', '^=', '_', '__', '`', 'b"', "b'", 'f"', "f'",
		             'j', 'r"', "r'", 'u"', "u'", '|', '|=', '~', ]:
			# sys.stout = open(filename, 'a', encoding='utf-8')
			# help(name)
			# sys.stdout = sys.__stdout__

			change_stdout_and_help(name, temp_filename)
			with open(temp_filename, 'r', encoding='utf-8') as f1, open(filename, 'a', encoding='utf-8') as f2:
				f2.write(f'help({name})\n')
				f2.write(f1.read())

		if os.path.exists(temp_filename):
			os.remove(temp_filename)

	def help_topics():
		catalog = f'{top_catalog}/topics'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['ASSERTION', 'ASSIGNMENT', 'ATTRIBUTEMETHODS', 'ATTRIBUTES', 'AUGMENTEDASSIGNMENT', 'BASICMETHODS',
		             'BINARY', 'BITWISE', 'BOOLEAN', 'CALLABLEMETHODS', 'CALLS', 'CLASSES', 'CODEOBJECTS', 'COMPARISON',
		             'COMPLEX', 'CONDITIONAL', 'CONTEXTMANAGERS', 'CONVERSIONS', 'DEBUGGING', 'DELETION',
		             'DICTIONARIES', 'DICTIONARYLITERALS', 'DYNAMICFEATURES', 'ELLIPSIS', 'EXCEPTIONS', 'EXECUTION',
		             'EXPRESSIONS', 'FLOAT', 'FORMATTING', 'FRAMEOBJECTS', 'FRAMES', 'FUNCTIONS', 'IDENTIFIERS',
		             'IMPORTING', 'INTEGER', 'LISTLITERALS', 'LISTS', 'LITERALS', 'LOOPING', 'MAPPINGMETHODS',
		             'MAPPINGS', 'METHODS', 'MODULES', 'NAMESPACES', 'NONE', 'NUMBERMETHODS', 'NUMBERS', 'OBJECTS',
		             'OPERATORS', 'PACKAGES', 'POWER', 'PRECEDENCE', 'PRIVATENAMES', 'RETURNING', 'SCOPING',
		             'SEQUENCEMETHODS', 'SEQUENCES', 'SHIFTING', 'SLICINGS', 'SPECIALATTRIBUTES', 'SPECIALIDENTIFIERS',
		             'SPECIALMETHODS', 'STRINGMETHODS', 'STRINGS', 'SUBSCRIPTS', 'TRACEBACKS', 'TRUTHVALUE',
		             'TUPLELITERALS', 'TUPLES', 'TYPEOBJECTS', 'TYPES', 'UNARY', 'UNICODE', ]:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	datatypes_catalog = f'{top_catalog}/datatypes'

	def help_datatype_kinds():
		catalog = f'{datatypes_catalog}/kinds'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['numbers', 'string', 'list', 'tuple', 'set', 'dict']:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	def help_datatypes_built_in():
		catalog = f'{top_catalog}/datatypes/built_in'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['int', 'float', 'complex', 'True', 'False', 'None', 'str', 'list', 'dict', 'tuple', 'set']:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	def help_datatypes_base():
		catalog = f'{datatypes_catalog}/base'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['int', 'float', 'bool', 'str', 'bytes']:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	def help_datatypes_advanced():
		catalog = f'{datatypes_catalog}/advanced'
		if not os.path.exists(catalog):
			os.makedirs(catalog)
		for name in ['object', 'array', 'list', 'tuple', 'set', 'dict', 'bytearray', 'complex', 'range', 'frozenset',
		             'memoryview', 'slice', 'type', 'property', 'super', 'classmethod', 'staticmethod', 'contextlib',
		             'collections', 'collections.abc', 'enum', 'functools', 'itertools', 'numbers', 'operator',
		             'reprlib', 'weakref', 'types', 'typing', 'copy', 'pprint', ]:
			change_stdout_and_help(name, f'{catalog}/{name}.txt')

	help_top()
	help_dir()

	help_modules()
	help_keywords()
	help_symbols()
	help_topics()

	help_datatype_kinds()
	help_datatypes_base()
	help_datatypes_built_in()
	help_datatypes_advanced()


if __name__ == '__main__':
	main()
