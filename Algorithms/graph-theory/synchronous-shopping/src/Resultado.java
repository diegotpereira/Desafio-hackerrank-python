import java.util.*;
import java.util.stream.IntStream;

public class Resultado {

    public static int shop(int numeroLojas, int numeroTiposPeixe, List<String> lojas, List<List<Integer>> estradas) {

        int[] oferta = new int[numeroLojas];
        List<List<Node>> grafo = new ArrayList<>();

        // Itera sobre as lojas e processa as ofertas
        lojas.stream().forEach(loja -> {

            String[] tiposPeixes = loja.split(" ");
            int numTipos = Integer.parseInt(tiposPeixes[0]);

            // Calcula o valor binário que representa as ofertas da loja atual
            int tipos = IntStream.range(0, numTipos)
            .mapToObj(i -> Integer.parseInt(tiposPeixes[i + 1]))
            .map(tipo -> 1 << (tipo - 1))
            .reduce(0, (a, b) -> a | b);

            // Armazena as ofertas da loja atual
            oferta[grafo.size()] = tipos;

            // Cria uma lista vazia para as conexões do grafo da loja atual
            grafo.add(new ArrayList<>());

        });

        // Itera sobre as estradas e adiciona as conexões no grafo
        estradas.stream().forEach(estrada -> {

            int a = estrada.get(0) - 1;
            int b = estrada.get(1) - 1;
            int t = estrada.get(2);

            // Adiciona uma conexão da loja 'a' para a loja 'b'
            grafo.get(a).add(new Node(b, t, 0));

            // Adiciona uma conexão da loja 'b' para a loja 'a'
            grafo.get(b).add(new Node(a, t, 0));
        });

        int[][] tempo = new int[1 << numeroTiposPeixe][numeroLojas];

        // Inicializa a matriz de tempos com o valor máximo
        Arrays.stream(tempo).forEach(t -> Arrays.fill(t, Integer.MAX_VALUE));

        PriorityQueue<Node> pilhaMinima = new PriorityQueue<>(Comparator.comparingInt(n1 -> n1.tempo));

        // Adiciona o nó inicial na pilha mínima
        pilhaMinima.offer(new Node(0, 0, oferta[0]));

        // Define o tempo para chegar no nó inicial como 0
        tempo[oferta[0]][0] = 0;

        List<Node> candidatos = new ArrayList<>();


        while (!pilhaMinima.isEmpty()) {
            
            // Obtém o nó com menor tempo da pilha mínima
            Node atual = pilhaMinima.poll();

            if (atual.label == numeroLojas - 1) {
                
                // Adiciona o nó aos candidatos se for o último nó
                candidatos.add(atual);
            }

            // Itera sobre as conexões do nó atual no grafo
            grafo.get(atual.label).stream().forEach(node -> {

                // Atualiza o status com base na oferta do nó
                int novoStatus = (atual.status | oferta[node.label]);

                if (atual.tempo + node.tempo < tempo[novoStatus][node.label]) {
                    
                    // Atualiza o tempo para chegar ao nó
                    tempo[novoStatus][node.label] = atual.tempo + node.tempo;

                    // Adiciona o nó na pilha mínima
                    pilhaMinima.offer(new Node(node.label, atual.tempo + node.tempo, novoStatus));
                }
            });
        }

        int min = Integer.MAX_VALUE;

        // Itera sobre os candidatos e encontra o mínimo
        for (int indice = 0; indice < candidatos.size(); indice++) {
            
            Node atual = candidatos.get(indice);

            for (int compare = indice; compare < candidatos.size(); compare++) {
                
                Node outro = candidatos.get(compare);

                if ((atual.status | outro.status) == (1 << numeroTiposPeixe) -1) {
                    
                    min = Math.min(min, Math.max(atual.tempo, outro.tempo));
                }
            }
        }

        return min;
        
    }

    // // Método para calcular a menor distância entre duas lojas de peixe
    // // dado o número de lojas, o número de tipos de peixe, uma lista de lojas e uma lista de estradas entre as lojas
    // public static int shop(int numeroLojas, int numeroTiposPeixe, List<String> lojas, List<List<Integer>> estradas) {

    //     // Inicializa um array com a oferta de cada loja
    //     int[] oferta = new int[numeroLojas];

    //     // Inicializa um grafo como uma lista de lista de nós
    //     List<List<Node>> grafo = new ArrayList<>();

    //     // Loop para percorrer cada loja
    //     for (int indice = 0; indice < numeroLojas; indice++) {

    //         // Obtém os tipos de peixes da loja atual
    //         String[] tiposPeixes = lojas.get(indice).split(" ");
    //         int numTipos = Integer.parseInt(tiposPeixes[0]);
    //         int tipos = 0;

    //         // Loop para percorrer cada tipo de peixe
    //         for (int compare = 0; compare < numTipos; compare++) {
                
    //             // Calcular uma representação binária dos tipos de peixe
    //             int tipo = Integer.parseInt(tiposPeixes[compare + 1]);
    //             tipos |= (1 <<(tipo - 1));
    //         }

    //         // Define a oferta da loja atual
    //         oferta[indice] = tipos;

    //         // Adiciona uma nova lista de nós ao grafo
    //         grafo.add(new ArrayList<>());
    //     }

    //     // Loop para percorrer cada estrada
    //     for (List<Integer> estrada : estradas) {
            
    //         // Construir o grafo de conexões entre as lojas
    //         // Obtém a origem, o destino e o tempo da estrada atual
    //         int a = estrada.get(0) - 1;
    //         int b = estrada.get(1) - 1;
    //         int t = estrada.get(2);

    //         // Adiciona um novo nó à lista de nós correspondente à origem
    //         grafo.get(a).add(new Node(b, t, 0));

    //         // Adiciona um novo nó à lista de nós correspondente ao destino
    //         grafo.get(b).add(new Node(a, t, 0));
    //     }

    //     // Inicializa uma matriz de tempos para cada possível combinação de oferta
    //     int[][] tempo = new int[1 << numeroTiposPeixe][numeroLojas];

    //     // Define cada tempo inicialmente como o valor máximo de inteiros
    //     for(int[] t : tempo) Arrays.fill(t, Integer.MAX_VALUE);

    //     // Inicializa uma fila de prioridade para armazenar os nós do grafo ordenados por tempo
    //     PriorityQueue<Node> pilhaMinima = new PriorityQueue<>(Comparator.comparingInt(n1 -> n1.tempo));

    //     // Adiciona o nó da loja inicial à fila de prioridade e define o tempo inicial como zero
    //     pilhaMinima.offer(new Node(0,0, oferta[0]));
    //     tempo[oferta[0]][0] = 0;

    //     // Inicializa uma lista de nós candidatos para armazenar as soluções
    //     List<Node> candidatos = new ArrayList<>();

    //     // Loop até que a fila de prioridade esteja vazia
    //     while(!pilhaMinima.isEmpty()) {

    //         // Executar o algoritmo de busca mínima
    //         // Obtém o próximo nó da fila de prioridade
    //         Node atual = pilhaMinima.poll();

    //         // Se o nó atual for a última loja, adiciona-o à lista de candidatos
    //         if(atual.label == numeroLojas - 1) candidatos.add(atual);

    //         for(Node node : grafo.get(atual.label)) {

    //             // Atualizar os tempos mínimos para cada nó
    //             int novoStatus = (atual.status | oferta[node.label]);

    //             if(atual.tempo + node.tempo < tempo[novoStatus][node.label]) {

    //                 // Atualiza o tempo para chegar ao nó
    //                 tempo[novoStatus][node.label] = atual.tempo + node.tempo;
                    
    //                 // Adiciona o nó na pilha mínima
    //                 pilhaMinima.offer(new Node(node.label, atual.tempo + node.tempo, novoStatus));
                    
    //             }
    //         }
    //     }

    //     int min = Integer.MAX_VALUE;

    //     for(int indice = 0; indice < candidatos.size(); indice++) {

    //         // Encontrar a solução mínima entre os candidatos finais
    //         Node atual = candidatos.get(indice);

    //         for (int compare = indice; compare < candidatos.size(); compare++) {
                
    //             Node outro = candidatos.get(compare);

    //             // Verifica se os candidatos possuem todos os tipos de peixe
    //             if ((atual.status | outro.status) == (1 << numeroTiposPeixe) - 1) {
                    
    //                 min = Math.min(min, Math.max(atual.tempo, outro.tempo));
    //             }
    //         }
    //     }

    //     return min;
    // }
    
}

