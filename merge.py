import shutil
from pathlib import Path

um = Path(r'C:\caminho\do\arquivo1.txt')
dois = Path(r'C:\caminho\do\arquivo2.txt')
#pode adicionar mais aquivos para incluir no array


newfile = input("Informe o nome do arquivo: ")
print()
print("O conteúdo mesclado dos arquivos estará em", newfile)

with open(newfile, "wb") as wfd: 

#caso tenho adicionado mais arquivos coloque o nome de todos no array abaixo.
#Eu preferi fazer assim pq eu tinha alguns arquivos especificos, mas caso seja todos os arquivos de uma pasta pode usar o for baseado em todos os arquivos da pasta

	for f in [um, dois]: 
		with open(f, "rb") as fd: 
			shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10) 

print("\nConteudo mesclado com sucesso.!") 
print("Gostaria de abrir o arquivo ? (y / n): ") 

check = input() 
if check == 'n': 
	exit() 
else: 
	print() 
	c = open(newfile, "r") 
	print(c.read()) 
	c.close() 
