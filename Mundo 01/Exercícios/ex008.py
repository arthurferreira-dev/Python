medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a \n{:.0f}cm \n{:.0f}mm \n{:.0f}dm \n{}dam \n{}hm \n{}km'.format(medida, cm, mm, dm, dam, hm, km))