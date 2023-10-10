// A tarefa do problema "Encryption" no HackerRank é a seguinte:

// Você recebe uma string composta por caracteres alfabéticos e espaços. 
// Sua tarefa é criptografar a mensagem seguindo um algoritmo específico.

// O algoritmo de criptografia funciona da seguinte forma:

// Remova todos os espaços da string original.
// Determine o número de linhas (L) e colunas (C) da grade retangular onde 
// a mensagem será criptografada. Você deve garantir que L x C seja maior 
// ou igual ao número de caracteres na mensagem, e L seja o mais próximo possível de C.
// Preencha a grade com a mensagem original, preenchendo de cima para baixo 
// e da esquerda para a direita. Os espaços em branco são preenchidos com letras, 
// se necessário, para manter o número de caracteres na mensagem original.
// Leia a mensagem criptografada coluna por coluna, da esquerda para a direita, 
// separando cada coluna por um espaço.
// O desafio envolve implementar um programa que execute esse algoritmo de 
// criptografia em uma mensagem de entrada e retorne a mensagem criptografada.

public class Resultado {

    // public static String encryption(String s) {
   
    //     // Inicializa uma string 'res' para armazenar a mensagem criptografada.
    //     String res = "";

    //     // Calcula o comprimento da string de entrada e a raiz quadrada desse comprimento.
    //     double string_quadrada = Math.sqrt(s.length());

    //     // Arredonda o valor da raiz quadrada para cima para determinar o número de colunas da grade retangular.
    //     int celular = (int) Math.ceil(string_quadrada);

    //     // Loop para percorrer as colunas da grade.
    //     for (int i = 0; i < celular; i++) {
            
    //         int j = 0;

    //         // Loop para percorrer as linhas da grade e adicionar caracteres à mensagem criptografada.
    //         while (i + j < s.length()) {
                
    //             // Adiciona o caractere da posição atual à mensagem criptografada.
    //             res += s.charAt(i + j);

    //             // Move para a próxima linha na mesma coluna.
    //             j += celular;
    //         }

    //         // Adiciona um espaço em branco para separar as colunas da grade na mensagem criptografada.
    //         res += " ";
    //     }

    //     // Retorna a mensagem criptografada.
    //     return res;
    // }


    // Definindo uma função chamada 'encryption' que recebe uma string 's' e retorna a mensagem criptografada.
    public static String encryption(String s) {

        // Inicializa uma string 'res' para armazenar a mensagem criptografada.
        String res = "";

        // Calcula o número de colunas necessárias para a grade retangular, arredondando para cima a raiz quadrada do comprimento da string.
        int coluna  = (int) Math.ceil(Math.sqrt(s.length()));

        // Calcula o número de linhas necessárias para a grade retangular, dividindo o comprimento da string pelo número de colunas e arredondando para cima, se necessário
        int linha = (s.length() / coluna) + (((s.length() % coluna) > 0) ? 1 : 0);

        // Loop para percorrer as colunas da grade.
        for (int i = 0; i < coluna; i++) {

            int k = i;
            
            // Loop para percorrer as linhas da grade.
            for (int j = 0; j < linha; j++) {

                // Verifica se 'k' está dentro dos limites da string.
                if (k < s.length()) {
                    
                    // Adiciona o caractere da posição 'k' à mensagem criptografada.
                    res += s.charAt(k);
                }

                // Move para a próxima linha na mesma coluna.
                k += coluna;
            }

            // Adiciona um espaço em branco para separar as colunas da grade na mensagem criptografada, exceto para a última coluna.
            if(i < coluna - 1) res += " ";
        }

        // Retorna a mensagem criptografada.
        return res;
    }
    
}
