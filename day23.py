import sys
print("当前解释器:", sys.executable)
try:
    import jieba
    print("jieba:可用,版本", jieba.__version__)
except ModuleNotFoundError:
    print("jieba:不可用(这是个干净房间)")