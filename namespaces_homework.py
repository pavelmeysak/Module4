def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# inner_function() - при вызове будет ошибка, так как имя функции находится в локальной области
# видимости функции test_function и к ней нельзя оратиться из глобального пространства


