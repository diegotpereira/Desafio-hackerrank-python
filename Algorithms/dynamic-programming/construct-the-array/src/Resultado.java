// A tarefa do problema "Construct the Array" no HackerRank é determinar o número de maneiras diferentes 
// de construir um array de tamanho n, seguindo certas regras específicas.

// O problema define as seguintes regras para construir o array:

// O array deve ser composto apenas pelos números inteiros de 1 a k, onde k é um número inteiro dado.
// O primeiro elemento do array deve ser 1.
// Para cada elemento subsequente do array, ele deve ser diferente do elemento anterior e pode estar no intervalo de 1 a k.
// O objetivo é determinar o número de maneiras diferentes de construir o array de tamanho n que satisfaça as regras mencionadas.

// A entrada do problema consiste em três números inteiros: n, k e x. Onde n é o tamanho do array, k é o valor máximo permitido para cada elemento do array e x é um elemento especial que deve ser repetido exatamente uma vez no array.

// A saída esperada é o número de maneiras diferentes de construir o array de tamanho n que satisfaça as regras mencionadas.

// No link fornecido, você pode encontrar uma descrição mais detalhada do problema, bem como exemplos de entrada e saída esperada.


public class Resultado {

    public static long countArray(int tamanhoArrayParaConstruido, int  valorMaximoPermitidoElemento, int elementoEspecialRepetido) {

        // Definir o valor do módulo como 10^9 + 7.
        int mod = (int) Math.pow(10, 9) + 7;

        // Inicializar arrays para armazenar o número de sequências finais em 'x' e não finais em 'x'.
        long finalEmX[] = new long[tamanhoArrayParaConstruido + 1];
        long naoFinalEmX[] = new long[tamanhoArrayParaConstruido + 1];

        // Definir os valores iniciais para o primeiro elemento do array.
        // Se o elemento especial é 1, há 1 sequência final em 'x'; caso contrário, 0.
        finalEmX[1] = elementoEspecialRepetido == 1 ? 1 : 0;

        // Se o elemento especial é 1, não há sequência não final em 'x'; caso contrário, 1.
        naoFinalEmX[1] = elementoEspecialRepetido == 1 ? 0 : 1;

        // Iterar para cada elemento do array, começando do segundo elemento.
        for (int i = 2; i <= tamanhoArrayParaConstruido; i++) {
            
            // Calcular o número de sequências finais em 'x' para a posição atual, 
            // com base no valor anterior de sequências não finais em 'x'.
            finalEmX[i] = naoFinalEmX[i - 1] % mod;

            // Calcular o número de sequências não finais em 'x' para a posição atual, 
            // com base nos valores anteriores de sequências finais e não finais em 'x'.
            naoFinalEmX[i] = (finalEmX[i - 1] * (valorMaximoPermitidoElemento - 1) + 
            naoFinalEmX[i - 1] * (valorMaximoPermitidoElemento - 2)) % mod;
        }

        // Retornar o número de sequências finais em 'x' para o tamanho do array especificado.
        return finalEmX[tamanhoArrayParaConstruido];
    }

    // public static long countArray(int tamanhoArrayParaConstruido, int  valorMaximoPermitidoElemento, int elementoEspecialRepetido) {

    //     // Se o elemento especial é 1, a será 1; caso contrário, será 0.
    //     long a = 1 == elementoEspecialRepetido ? 1 : 0;

    //     // Se a é 1, b será 0; caso contrário, será 1.
    //     long b = a == 1 ? 0 : 1;

    //      // Valor para realizar operações de módulo.
    //     int mod = 1000_000_007;

    //     // Iterar para cada elemento do array
    //     for (int i = 1; i < tamanhoArrayParaConstruido; i++) {
            
    //         // Armazenar os valores anteriores
    //         long prevA = a;
    //         long prevB = b;

    //         // Atualizar os valores de a e b com base nos valores anteriores
    //         a = prevB % mod;
    //         b = (prevA * (valorMaximoPermitidoElemento - 1) + prevB * (valorMaximoPermitidoElemento - 2)) % mod;

           
    //     }

    //     // Retornar o valor final de a
    //     return a;
    // }

}
