# Car というクラスを作成します
class Car:
    class_name = "Car"
    
    def _init_(self):
        self.name = None
        
    def show(self):
        print(self.name)
        
#Carクラスのインスタンスを作成します
car = Car()

#Carの変数nameにセダンという文字列を格納します
car.name = "セダン"

#Carのメソッドであるshow（）を実行します
car.show()
#ターミナルにはセダンと表示されます

#Carクラス内にあるクラス変数class_nameをターミナルに表示しています
print(Car.class_name)
#ターミナルにはCarと表示されます