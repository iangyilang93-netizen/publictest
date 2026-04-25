
class Book:
      def __init__(self,title: str,author: str,borrow: bool):
          self.title=title
          self.author=author
          self.borrow=borrow

      def borrownow(self):
          if self.borrow == True:
            print(f"{self.title}は貸し出し中です")
          else:
            self.borrow = True
            print(f"{self.title}を借りました")
    
      def returnbook(self):
          if self.borrow == False:
            print(f"{self.title}はすでに返却されています")
          else:
            self.borrow = False
            print(f"{self.title}は返却されました")
            
      def show(self):
          print(f"本のタイトルは{self.title}、著者は{self.author}、貸出{self.borrow}")
          
b1 = Book("a","A",False)
b2 = Book("b","B",False)
b3 = Book("c","C",False)

b1.borrownow()
b2.borrownow()

b2.returnbook()

b1.show()
b2.show()
