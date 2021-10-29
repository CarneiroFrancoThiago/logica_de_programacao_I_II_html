from TelefonesBr import TelefonesBr
import re

telefone = "5541996539358"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)










#   Caracteres	        Descrição	                                     Exemplos
#   []	        Define um range ou um grupo de caracteres       	[0-9]; [a-z]; [abc]
#   *	        Marca nenhuma, uma ou mais ocorrências	                  sol*
#   {}	        Quantidade de repetições de uma ocorrência definida	    [abc]{5}
#   \d	        Qualquer número de 0 até 9	                            \d{3,4}
#   \w	        Qualquer número de a té 9 letra de a até z ou _	        \w{10}
#   |	        Um ou outro                                             	@$
#   ()	        Captura e agrupa	                                     (\w{4})