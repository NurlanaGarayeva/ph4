       
# # class Sahmat:
# #     def __init__(self):
# #         print("Sahmat yaradıldı")
         
# #     def bu_nedir(self):
# #         print("Bu sahmatdır")
          
# #     def bir_dama(self):
# #         print("Bir dama gede bilir")
         
         
# # class At(Sahmat):
# #     def __init__(self):
# #         super().__init__()
# #         print("At yaradıldı")
        
# #     def bu_nedir(self):
# #         print("Bu atdır")   
        
# #     def hereketi(self):
# #         print("L herfi seklinde hereket edir")   
        
        
# # class fil(Sahmat):
# #     def __init__(self):
# #         super().__init__()
# #         print("fil yaradıldı")
        
# #     def bu_nedir(self):
# #         print("Bu fildir")   
        
# #     def hereketi(self):
# #         print("Yanliz diaqonal hereket edir")          
        
        
# # class top(Sahmat):
# #     def __init__(self):
# #         super().__init__()
# #         print("Top yaradıldı")
        
# #     def bu_nedir(self):
# #         print("Bu topdur")   
        
# #     def hereketi(self):
# #         print("Duz xett uzerinde hereket edir") 
        
        
                        
# # sahmat = Sahmat()   
# # at = At() 
# # fil = fil() 
# # top = top()
           
# # sahmat.bu_nedir()   
# # at.bu_nedir() 
# # fil.bu_nedir()   





class Sahmat:
    def __init__(self):
        print("Sahmat yaradıldı")
         
    def bu_nedir(self):
        print("Bu sahmatdır")
          
    def hereketi(self):
        print("Bir dama gede bilir")
         
         
class At(Sahmat):
    def __init__(self):
        super().__init__()
        print("At yaradıldı")
        
    def bu_nedir(self):
        print("Bu atdır")   
        
    def hereketi(self):
        print("L herfi seklinde hereket edir")   
        
        
class Fil(Sahmat):
    def __init__(self):
        super().__init__()
        print("Fil yaradıldı")
        
    def bu_nedir(self):
        print("Bu fildir")   
        
    def hereketi(self):
        print("Yanliz diaqonal hereket edir")          
        
        
class Top(Sahmat):
    def __init__(self):
        super().__init__()
        print("Top yaradıldı")
        
    def bu_nedir(self):
        print("Bu topdur")   
        
    def hereketi(self):
        print("Duz xett uzerinde hereket edir") 
        
        
sahmat = Sahmat()   
at = At() 
fil = Fil() 
top = Top()     


def sahmat_gedisleri(gedisler):
    gedisler.hereketi()  

sahmat_gedisleri(sahmat)
sahmat_gedisleri(at)   
sahmat_gedisleri(fil)
sahmat_gedisleri(top) 
