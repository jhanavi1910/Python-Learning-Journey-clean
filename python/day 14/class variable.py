class student:
   college="maharaja institue of technology"
   def __init__(self,name):
        self.name=name
   def display(self):
       print (f"student name is {self.name} and college is {self.college}")
s1=student("jhanavi")
s2=student("rao")
s1.display()
s2.display()

      
