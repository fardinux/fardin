#coding:utf-8
class Oyun(object):
  def __init__(self):
    self.pul = 100
    self.fabrika = 5
    self.isci = 20
    self.guc = 100

  def goster(self):
    print "Güc", self.guc
    print "Pul", self.pul
    print "Işçi", self.isci
    print "Fabrika" , self.fabrika
    
oyun = Oyun()

class Oyuncu(Oyun):
  def __init__(self):
    Oyun.__init__(self)
    
  def fabQur(self, eded):
    if self.guc >= eded*5 and self.pul >= eded*10:
      self.fabrika += eded
      self.pul -= eded*10
      self.guc -= eded*5 
      print "Təbriklər! %d ədəd fabrika qurdunuz!" % eded
      return oyuncu.goster()
    else:
      print "Kifayət qədər pulunuz/gücünüz yoxdur."

oyuncu = Oyuncu()

class Dusman(Oyun):
  def __init__(self):
    Oyun.__init__(self) 
    self.eqo = 0
  def goster(self):
    Oyun.goster(self)
    print "Eqo" , self.eqo
  def fabDagit(self, eded):
    oyuncu.fabrika -= eded
    self.eqo += eded*2
    print "Təbriklər düşman, oyunçunun %d ədəd fabrikasını dağıtdınız\nüstəlik eqonuz da artdı!" % eded

dusman = Dusman()
