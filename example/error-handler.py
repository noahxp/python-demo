a = 3
b = 0

try:
    try:
        c = a/b
    except NameError:
        print('NameError')

    except ZeroDivisionError as error:
        print('ZeroDivisionError=', error)
        raise RuntimeError from exec()
        # raise # 無參數時，拋回原錯誤類別
    except:
        print("exception unhandler...(except-1)")
    else:
        print('no error, result=', c)
    finally:
        pass
except:
    print("exception un-handler...(except-2)")
