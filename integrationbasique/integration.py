import csv
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
global g
g=Decimal(-9.80665)
#intégration basique d'une liste de valeurs:une ligne = temps,valeur_x,valeur_y,valeur_z
def integrateList(list_to_integrate,initial_values):
    #global integrated_list, i
    # vitesse_n=vitesse_{n-1}+accel_n*(temp_n-temp_{n-1})
    integrated_list=[]
    integrated_list.append(initial_values)
    #print("integree initiale",integrated_list)
    time = 0.
    i_vit = 0
    compteur_de_lignes = 0
    for acc_row in list_to_integrate:
        compteur_de_lignes = compteur_de_lignes + 1
        # print (
        #     'acc_row ligne', compteur_de_lignes, ' ', acc_row, 'type', type(acc_row), "i-vit", i_vit, "vit-liste prec",
        #     integrated_list[i_vit])
        vit_row = [Decimal(0),Decimal(0),Decimal(0),Decimal(0)]
        # if i_vit!=0:
        time = acc_row[0] - integrated_list[i_vit][0]
        # print("delta t", time)
        vit_row = []
        vit_row.append(acc_row[0])  # timestamp
        # vit_row.append(vit_liste[i_vit,1] + acc_row[1] * time)
        for i in range(1, 4):
            print ("i", i, 'vit prec', integrated_list[i_vit][i], 'acc courant', acc_row)
            vit_row.append(integrated_list[i_vit][i] + acc_row[i] * (acc_row[0] - integrated_list[i_vit][0]))
        integrated_list.append(vit_row)
        i_vit = i_vit + 1
    integrated_list.pop(0)
    return integrated_list

acc_liste=[]
#lecture du csv, conversion en liste
with open('../tour de la bourse accéléromètre.csv', newline='') as csvfile:
    accreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in accreader:
        #print(', '.join(row))
        acc_liste.append(row)
#print (acc_liste[6])
acc_liste.pop(0) #strip des entêtes
acc_liste = np.asarray(acc_liste)
# print ('acc_liste:',acc_liste)
# y a des vides dans la liste...
clean_acc_liste=[]
# i_acc_liste=0
for row in acc_liste:
    # print('element brut:',row)
    newRow = []
    for x in row:
        if x=='':
            x=Decimal(0.)
        #print('type',type(x),"valeur",x,"converti",Decimal(x))
        # if type(x) is Decimal:
        #     print("x est décimal:" , x)
        #     newRow.append(x)
        # else:
        #print("x n'est pas décimal:" , x)
        z=Decimal(x)
        #print("z",z,"type",type(z))
        newRow.append(z)
#    row = [Decimal(x) for x in row]
    if len(newRow)<4:
        print('element incomplet:',newRow)
        # for i in range(len(newRow),4):
        #     if i<4 :
        #         newRow.append(Decimal(0.))
        #     else:
        #         newRow.append(Decimal(g))
    else:
        # la correction sert à virer g dans les accélérations.
        newRow=[sum(x) for x in zip(newRow, [Decimal(0),Decimal(0),Decimal(0),g])]
        # print('element completé:',newRow)
        clean_acc_liste.append(newRow)

    # i_acc_liste=i_acc_liste+1
# print ('clean_acc_liste:',clean_acc_liste)
vit_liste=[]
#vitesse deu départ : le premier échantillon
vit_init = clean_acc_liste.pop() # ça retire le premier élément
vit_liste=integrateList(clean_acc_liste, vit_init)
# print ("vit_liste",vit_liste)
# position nulle au départ. Là on ne peut pas prendre de premier échantillon, on n'en a pas
pos_liste=integrateList(vit_liste, [Decimal(0), Decimal(0),Decimal(0),Decimal(0)])
print ('pos_liste:',pos_liste)
xyData = np.asarray(pos_liste)[:,[1,2]]
print ('xyData:',xyData)
plt.xlabel('x')
plt.ylabel('y')
x, y = xyData.T
plt.plot(x,y)
#plt.scatter(*zip(*xyData))
# plt.show()
# txData = np.asarray(pos_liste)[:,[0,3]]
# print ('txData:',txData)
# plt.xlabel('t')
# plt.ylabel('z')
# x, y = txData.T
# plt.plot(x,y)
#plt.scatter(*zip(*xyData))
plt.show()
