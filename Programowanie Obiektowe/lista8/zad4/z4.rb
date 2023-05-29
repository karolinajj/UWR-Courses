#Karolina Jędraszek
#lista 8, zadanie 4
#ruby 3.2.2

class Jawna
  def initialize(napis)
    @napis = napis
  end

  def zaszyfruj(klucz) #klucz jest słownikiem
    wynik = ""
    for i in 0..@napis.size do
      if klucz[@napis[i]] #czy w slowniku istnieje taki klucz
        wynik += klucz[@napis[i]]
      else
        Zaszyfrowana.new("") #jeśli nie istnieje zwracam puste, zaszyfrowane słowo
      end
    end
    Zaszyfrowana.new(wynik)
  end

  def to_s()
    @napis
  end

end

class Zaszyfrowana
  def initialize(napis)
    @napis = napis
  end

  def odwroc(slownik) #funkcja odwraca słownik, tj. klucze stają się wartościami, wartości kluczam
    wynik = {}
    klucze = slownik.keys #tablica z kluczami
    for key in klucze do
      wynik[slownik[key]] = key
    end
    wynik
  end

  def odszyfruj(klucz) #klucz jest słownikiem
    wynik = ""

    odwr_klucz = odwroc(klucz) #odwrócony słownik

    for i in 0..@napis.size do
      if odwr_klucz[@napis[i]] #czy w slowniku istnieje taki klucz
        wynik += odwr_klucz[@napis[i]]
      else 
        Jawna.new("") #jeśli nie istnieje zwracam puste, jawne słowo
      end
    end
    Jawna.new(wynik)
  end

  def to_s()
    @napis
  end

end

#----------------------------------------------
klucz1 = {'a' => 'b', 'b' => 'c', 'c' => 'd'}
j1 = Jawna.new("abc");
print("Słowo jawne: ", j1, "\n")
z1 = j1.zaszyfruj(klucz1)
print("Slowo po zaszyfrowaniu: ",z1 , "\n")
j2 = z1.odszyfruj(klucz1)
print("Slowo po rozszyfrowaniu: ",j2 , "\n")