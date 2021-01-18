DIAS = int(input());
ANOS = int(DIAS/365);
DIAS -= ANOS*365;
MESES = int(DIAS/30);
DIAS -= MESES*30;
print(repr(ANOS)+" ANOS");
print(repr(MESES)+" MESES");
print(repr(DIAS)+" DIAS");