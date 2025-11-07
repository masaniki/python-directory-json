import sys
from pathlib import Path
import argparse
import yaml
import json
import doctest

def mainCLI():
    """
    Abst: CLIを処理する関数。

    Expl:
    - path名は絶対pathでも相対pathでもok.
    - "-a"(=--all) commandで隠しfileや隠しdirectoryも表示。
    - "-y"(=--yaml)でyamlで出力する。
    - "-f"(=--file)でfile出力する。

    Ideas:
    - maxDepthの機能を付けるか？

    Returns:
        Type: dict
        Abst: {directory名(str):[i(int):i番目の子directory名(str)]}という木構造。
    """
    parser=argparse.ArgumentParser()
    parser.add_argument("dirName",type=str,help="Put in directory name. Both absolute and relative is OK.")
    parser.add_argument("-y","--yaml",help="Output as a YAML format.",action="store_true")
    parser.add_argument("-a","--all",help="Visit hidden file.",action="store_true")
    parser.add_argument("-f","--file",type=str,help="Output as a file.")
    args=parser.parse_args()
    dirname=Path(args.dirName)
    outDict=directoryBFS(dirname.resolve(),isAll=args.all)
    if(args.yaml):
        if(args.file is None):
            yaml.safe_dump(outDict,sys.stdout)
        else:
            with open(args.file,mode="w",encoding="utf-8") as f:
                yaml.safe_dump(outDict,f)
    else:
        if(args.file is None):
            print(outDict)
        else:
            with open(args.file,mode="w",encoding="utf-8") as f:
                json.dump(outDict,f)

def directoryBFS(startDir:Path,isAll:bool=None):
    """
    Abst: directory構造を幅優先探索する関数。

    Args:
      startDir:
        Type: Path
        Abst: 探索を開始するdirectory名。
      isAll:
        Type: Bool.
        Abst: {True⇒隠しfileも探索, False⇒隠しfileを通過。}
        Default: false.
    Returns:
      Type: dict
      Abst: {directory名(str):[i(int):i番目の子directory名(str)]}という木構造。
      Expl:
      - {directory名(str):[i(int):i番目の子directory名|file名(str)]}。
      - file名の時は、終端nodeになる。
    """
    if(isAll is None):
        isAll=False
    outDict={startDir.name:[]}
    visitQueue=[startDir]  #訪れるdirectory(Path型)を格納する。
    dictQueue=[outDict[startDir.name]]  #訪れるdirectoryに対応するlist型を格納する。
    while(True):
        if(visitQueue==[]):
            break
        curDir=visitQueue.pop(0)
        curList=dictQueue.pop(0)
        for childPath in curDir.iterdir():
            childName=childPath.name
            if((not isAll) and childName[0]=='.'):
                continue
            if(childPath.is_file()):
                curList.append(childName)
            else:
                childDict={childName:[]}
                curList.append(childDict)
                visitQueue.append(childPath)
                dictQueue.append(childDict[childName])
    return outDict


if(__name__=="__main__"):
    mainCLI()
