/Atividade da Parada 03 do Curso Kick! Turma F utilizando Portugol - Bianca e Ingrid//

programa
{

    funcao inicio()
    {

        cadeia resposta,operacao
        real n1,n2
        escreva("Deseja utilizar a nossa calculadora ?")
        leia(resposta)
        enquanto (resposta=="sim"){
            escreva("primeiro valor: ")
            leia(n1)

            escreva("segundo valor: ")
            leia(n2)
            escreva("Escolha uma operação +,-,,/:")
            leia(operacao)
            se (operacao=="+"){
                escreva("\n ",n1+n2,"\n ")
                }
            senao se (operacao=="-"){
                escreva("\n ",n1-n2,"\n ")
                }
            senao se (operacao=="/"){
                escreva("\n ",n1/n2,"\n ")
                }
            senao se (operacao==""){
                escreva("\n ",n1*n2,"\n ")
                }
            senao {
                escreva("\n VALOR INVÁLIDO!!!!!!" )
                }


        escreva("Deseja continuar a utilizar a nossa calculadora ?")
        leia(resposta)}
        escreva("FIM!")
    }
}