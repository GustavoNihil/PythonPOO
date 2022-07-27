from associacao import Escritor, Caneta, MaquinaDeEscrever
# Na associação não há um vínculo obrigatório entre as classes - ao contrário da agregação ou composição -

escritor = Escritor('Guimarães Rosa')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina # O atributo "ferramenta" do objeto "escritor" recebe outro objeto, que por sua vez pode executar um método
escritor.ferramenta.escrever()


