import os
import time


def probel(s):
    if s[0]==' ':
        return s[1:]
    elif s[-1]==' ':
        return s[:-1]
with open('recipes.txt') as file:
    x=file.readlines()
for i in range(len(x)-1):
    x[i]=x[i].replace('\n','')
    if len(x[i]) > 0:
        print(x[i][0])
cook_book={}
sost='nazv'  #'nazv','chislo','ingr'
nazvanie=''
kolvo_ing=-1
ingrid={'ingredient_name':'','quantity':-1,'measure':''}
for i in range(len(x)):
    if x[i]!='':
        if sost == 'ingr':
            for j in range(i,i+kolvo_ing):
                s=''
                sost_ing='imy' #imy kolvo mera
                for simv in x[j]:
                    if simv!='|':
                        s+=simv
                    elif sost_ing=='imy':
                        s=probel(s)
                        ingrid['ingredient_name']=s
                        s=''
                        sost_ing='kolvo'
                    elif sost_ing=='kolvo':
                        s = probel(s)
                        ingrid['quantity']=int(s)
                        s=''
                        sost_ing='mera'
                    if sost_ing=='mera' and simv==x[j][len(x[j])-1]:
                        s = probel(s)
                        ingrid['measure']=s
                        cook_book[nazvanie].append(ingrid)
                        ingrid = {'ingredient_name': '', 'quantity': -1, 'measure': ''}
                        print(cook_book)
            sost='cont'
            cont=kolvo_ing
        elif sost == 'chislo':
            kolvo_ing=int(x[i])
            sost='ingr'
        elif sost == 'nazv':
            cook_book[x[i]]=[]
            nazvanie=x[i]
            sost='chislo'
        elif sost == 'cont' and cont == 2:
            sost='nazv'
        elif sost == 'cont':
            cont-=1

print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    outP={}
    for bludo in dishes:
        for bludo_cook in cook_book:
            if bludo==bludo_cook:
                for ingr in cook_book[bludo_cook]:
                    if outP.get(ingr['ingredient_name'])==None:
                        outP[ingr['ingredient_name']]={'quantity':ingr['quantity']*person_count,'measure':ingr['measure']}
                    else:
                        outP[ingr['ingredient_name']]['quantity']+=ingr['quantity']*person_count
    return outP
print(get_shop_list_by_dishes(['???????????????????? ??????????????????', '??????????'], 2))

#???????????? 3
a=['1.txt','2.txt','3.txt']
sort=[]
sort_ind=[]
sortOut=['0' for i in a]
for i in a:
    with open('SORTed/'+i,'r',encoding='UTF-8') as f:
        ff=f.readlines()
        ff.append(i)
        sort_ind.append(len(ff))
        sort.append(ff)
sort_ind=sorted(sort_ind)
for i in range(len(sort_ind)):
    for j in sort:
        if sort_ind[i]==len(j):
            sortOut[i]=j
f=open('????????????.txt','w',encoding='UTF-8')
for i in sortOut:
    f.write('\n'+i[-1]+'\n')
    f.write(str(len(i)-1)+' ??????.'+'\n')
    for j in i[:-1]:
        f.write(j)
f.close()












