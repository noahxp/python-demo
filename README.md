# Python 入門

## 環境安裝

- windows : <https://www.python.org/downloads/>
  - 建議可以從 Microsoft Store 安裝，可自動設定環境變數及日後的自動版更
- mac os :
  - 先安裝 HomeBrow : <https://brew.sh/index_zh-tw>

    ```bash
    # 透過 HomeBrew 安裝 python
    $ brew install python3
    ```

### pip 指令

- python 已帶 pip 指令
- 如電腦同時安裝 python2/python3 ，要使用 python3 時，指令改用 `pip3`
- pip 常用指令

  ```bash
  # pip 常用指令
  $ pip3 install 套件名稱   # 安裝套件
  $ pip3 uninstall 套件名稱 # 移除套件
  $ pip3 install --upgrade 套件名稱  # 升級套件
  $ pip3 show 套件名稱 # 顯示套件相關資訊
  ```

- requirements.txt

  - pip 可用 requirements.txt 作為管理套件相依性，意即目前的應用程式所需安裝的套件

  ```bash
  # pip 用 requirements.txt 安裝套件
  $ pip3 install -r requirements.txt
  ```

- macOS 無法安裝 pandas 套件解決方法 : 自行編譯

  ```bash
  # 如有使用 virtual env ，請先切換到 virtual env 下
  # 先安裝編譯必要套件
  $ pip3 install numpy cython

  # 自行編譯並安裝 pandas 套件
  $ git clone git@github.com:pandas-dev/pandas.git
  $ cd pandas
  $ python3 setup.py install
  ```


## 開發工具(IDE)

- VS Code

  下載並安裝 VSCode : <https://code.visualstudio.com/download>

  - extensions :

    Python Extension : 讓 VS Code 支援 Python 語法提示

    ![python extension](./docs/python-extension.png)

    Pylance Extension : 調整 LanguageServer 為 Pylance (比預設Python extension有更好的支援)

    ![pylance extension](./docs/pylance-extension.png)

    ~~Code Runner : 快速在 VS Code 裡執行 Python 程式~~。Python Plugin 已自帶快速執行方式，可不裝此 plugin

    ![Code Runner](./docs/code-runner-extension.png)

  - 安裝 extension 必要套件
    於 extension 安裝完後，第一次啟用時，會提示安裝，或則自行透選 pip 套件安裝

    ```docs
    autopep8
    pylint
    ```

  - 設定直譯器

    - 按「ctrl+shift+p」(mac : cmd+shift+p) 後輸入「python」，選擇「python: Select Interpreter」，然後選擇 Python安裝的版本
    - 如電腦有多版本的Python ，可設定 Code Runer 使用指定的版本:

      按「ctrl+shift+p」(macos: cmd+shift+p」後輸入「settings」，選擇「Preference:Open Settings(JSON)，在 settings.json加入以下內容，以確保使用的是安裝的 Python版本執行

      ```JSON
      "code-runner.executorMap": {
        "python": "$pythonPath -u $fullFileName"
      }
      ```

  - 自動格式化設定: FormatOnSave

    VS Code > Preferences > Settings > 輸入「FormatOnSave」

    ![FormatOnSave](./docs/format-on-save.png)

    VS Code > Preferences > Settings > 輸入「Python Formatting」

    ![Python Formatting](./docs/format-autopep8.png)

  - 安裝 VS Code 到 Shell(command line)

    VS Code > ctrl+shift+p (macos: cmd+shift+p) > 輸入「shell」，選擇如下圖安裝 code command 到 PATH裡，以後即可在專案資料夾下，輸「code . 」以 VS Code 開啟專案

    ![Open VSCode in Shell](./docs/shell-open.png)

  - 使用 VS Code 開發多種程式語言，可能會安裝多種語言所需的 extensions ，為避免 VS Code 載入愈來愈慢，可透過 .vscode/extensions.json 管理目前專案所需的 extensions ，以 Python 為例內容如下。細節見[官方說明](https://code.visualstudio.com/docs/editor/extension-gallery#_workspace-recommended-extensions)

    ```json
    {
      "recommendations": [
        "ms-python.vscode-pylance",
        "ms-python.python"
      ]
    }
    ```

  - 各語言建議 extensions : https://github.com/noahxp/tools/tree/master/ide

  - VS Code 使用 Python Virtual Environment
    - 在 Python 環境先安裝 virtualenv 套件

      ```bash
      #!/bin/bash
      $ pip3 install virtualenv
      ```

    - 在專案資料夾，透過 CLI 建立 Virtual Environment

      ```bash
      #!/bin/bash
      $ virtualenv .venv
      # 或直接用指定版本建立 virtual env, ex:
      $ /xxxx/python3.11 -m venv .venv
      ```

    - 切換到 Python Virtual Environment 的 Python Interpreter (Runtime)

      VS Code > ctrl+shift+p (macos: cmd+shift+p)，輸入「`Python: Select Interpreter`」，選擇有 .venv 的 python runtime

    - 不在 IDE 裡，也可以手動切換到 virtualenv

      ```bash
      #!/bin/bash
      . .venv/bin/active
      ```

## Python 摘要

### Code Style

- [pep8](https://www.python.org/dev/peps/pep-0008/)
- 4個空格當縮排
- Class : UpperCamelCase
- Function/Variables : lowercase_with_underscores

### 資料型別

Data Type | Example
----------|--------------------
str | x = "Hello World"
int | x = 20
float | x = 20.5
complex | x = 1j
list | x = ["apple", "banana", "cherry"]
tuple | x = ("apple", "banana", "cherry")
range | x = range(6)
dict | x = {"name" : "John", "age" : 36}
set | x = {"apple", "banana", "cherry"}
frozenset | x = frozenset({"apple", "banana", "cherry"})
bool | x = True
bytes | x = b"Hello"
bytearray | x = bytearray(5)
memoryview | x = memoryview(bytes(5))

#### 資料型別轉換

函式 | 功能
----|-------------------------
int() | 數值字串轉換為整數型別
float() | 數值字串轉換為浮點型別
str() | 數值型別轉換為文字型別

### 變數

- 不需特別宣告，型別依內容自動指定 （弱型別)

- 「del」關鍵字，可刪除變數或集合裡的內容

- 「type()」函式，可取得變數型別

### 列出所有內建函式

- 在 cli 互動模式執行

```bash
dir(__builtins__)
```

### 範例

- [判斷式](./example/condition.py)
- [迴圈](./example/loop.py)
- [continue、break、pass](./example/loop-advanced.py)
- [function(函式)](./example/function.py)
- [function 關鍵字參數](./example/function-keyword-param.py)
- [anonymous function(lambda)](./example/lambda.py)
- [class](./example/class.py)
- [可直接使用的內建函式](https://docs.python.org/zh-tw/3.9/library/functions.html)
- [Error Handler](./example/error-handler.py)
- [引用模組](./example/import.py)
- [內建模組 1](https://docs.python.org/zh-tw/3/tutorial/stdlib.html)
- [內建模組 2](https://docs.python.org/zh-tw/3/tutorial/stdlib2.html)
