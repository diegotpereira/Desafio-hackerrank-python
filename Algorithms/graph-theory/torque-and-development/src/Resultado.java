import java.util.*;


// A tarefa do problema "Torque and Development" no HackerRank é determinar o custo mínimo para 
// conectar todas as cidades em uma região. A região é composta por várias cidades, e cada cidade 
// pode ou não estar conectada a outras cidades através de estradas.

// O problema apresenta os seguintes parâmetros:

// Número de cidades (n) na região.
// Número de estradas (m) existentes atualmente.
// Custo de construir uma nova estrada (croad).
// Custo de reparar uma estrada existente (c_lib).
// Uma matriz de conexões que indica quais cidades estão conectadas por estradas.
// O objetivo é determinar o custo mínimo para conectar todas as cidades. Existem duas opções:

// Construir uma nova estrada entre duas cidades não conectadas, com custo croad.
// Reparar uma estrada existente entre duas cidades conectadas, com custo c_lib.
// O problema pede para implementar uma função chamada "findMinCost" que receba os parâmetros mencionados acima e retorne o custo mínimo necessário para conectar todas as cidades da região.

// Você pode resolver o problema implementando a lógica necessária na linguagem de programação de sua escolha e submeter sua solução no HackerRank para verificar se está correta.

public class Resultado {

    // Verificar se o custo de reparar (c_lib) é menor ou igual ao custo de construir uma nova estrada (c_road). 
    // Se for o caso, reparar for melhor. Portanto, o custo total será c_lib multiplicado 
    // pelo número total de cidades (n).
    // Caso contrário, se o custo de construir uma nova estrada (c_road) for menor do que reformar uma estrada (c_lib), 
    // é mais econômico construir estradas para conectar todas as cidades. O objetivo é minimizar o custo total.
    // Para isso, o problema pode ser convertido em um problema de encontrar componentes conectados em um grafo. 
    // Cada cidade é representada por um nó no grafo, e as estradas representam as arestas que conectam as cidades.
    // Construir o grafo: Converter as informações das estradas fornecidas em uma estrutura de dados de grafo. 
    // Cada cidade é um nó, e as estradas são as arestas bidirecionais que conectam as cidades.
    // Utilizar uma busca em profundidade (DFS) ou busca em largura (BFS) para encontrar todos os nós (cidades) conectados 
    // a partir de um determinado nó. Isso irá identificar um grupo de cidades que podem ser alcançadas a partir de uma cidade inicial.
    // Para cada grupo de cidades encontrado, é necessário calcular o custo mínimo de fornecer serviços (estradas e bibliotecas). 
    // O custo é calculado somando o custo de construir estradas entre as cidades (c_road) multiplicado pelo número de estradas 
    // necessárias, e adicionando o custo de construir uma biblioteca (c_lib) para o grupo de cidades.
    // Repetir o passo 5 e 6 para cada nó (cidade) que ainda não foi visitado no grafo. Isso garante que todos os grupos de cidades 
    // sejam identificados e calculados corretamente.
    // Somar todos os custos calculados para obter o custo total mínimo para fornecer serviços de biblioteca e estradas para todas as 
    // cidades.

    // Função para calcular o custo mínimo de construção de estradas ou de reformas.
    public static long roadsAndLibraries(int numeroEstradas, int custoRepararEstradas, int custoConstruirNovaEstrada, List<List<Integer>> cidades) {

        // Lista para armazenar os pais dos nós.
        List<Integer> parent = new ArrayList<>();

        // Lista para armazenar a classificação dos nós.
        List<Integer> classificacao = new ArrayList<>();

        // Mapa para contar a frequência dos pares de nós.
        HashMap<Integer, Integer> freqMapa = new HashMap<>();

        // Variável para armazenar o resultado final.
        long resultado = 0;

        // Inicialização dos pais e classificações dos nós.
        for (int indice = 0; indice <= numeroEstradas; indice++) {
            
            parent.add(indice);
            classificacao.add(0);

        }

        // Unir os conjuntos disjuntos das cidades.
        for (int indice = 0; indice < cidades.size(); indice++) {
            
            int origem = cidades.get(indice).get(0);
            int destino = cidades.get(indice).get(1);

            uniao(origem, destino, parent, classificacao);
        }

        // Contar a frequência dos pais dos nós.
        for (int indice = 1; indice <= numeroEstradas; indice++) {
            
            Integer buscarParente =  buscarParente(indice, parent);
            freqMapa.put(buscarParente, freqMapa.getOrDefault(buscarParente, 0) + 1);
        }

        // Calcular o custo mínimo considerando a reparação de estradas e a construção de novas estradas.
        for (Integer valor : freqMapa.values()) {
            
            resultado += Math.min((long) valor * custoRepararEstradas, ((long) (valor - 1) * custoConstruirNovaEstrada) + custoRepararEstradas);
        }

        return resultado;
    }

    // Função para unir dois conjuntos disjuntos com base na classificação.
    private static void uniao(int origem, int destino, List<Integer> parent, List<Integer> classificacao) {

        // Encontrar o pai da origem.
        int tmpOrigem = buscarParente(origem, parent);

        // Encontrar o pai do destino.
        int tmpDestino = buscarParente(destino, parent);

        // Se a classificação da origem for maior que a classificação do destino,
        if (classificacao.get(tmpOrigem) > classificacao.get(tmpDestino)) {
            
            // torna o pai do destino igual ao pai da origem.
            parent.set(tmpDestino, tmpOrigem);

        // Se a classificação da origem for menor que a classificação do destino,
        } else if (classificacao.get(tmpOrigem) < classificacao.get(tmpDestino)) {
            
            // torna o pai da origem igual ao pai do destino.
            parent.set(tmpOrigem, tmpDestino);

        // Se as classificações forem iguais,
        } else {

            // escolhe um dos pais como pai e incrementa a classificação.
            parent.set(tmpDestino, tmpOrigem);
            classificacao.set(tmpOrigem, classificacao.get(tmpOrigem) + 1);
        }
    }

    // Função para encontrar o pai de um elemento em um conjunto disjunto.
    private static Integer buscarParente(int origem, List<Integer> parent) {

        // Se o elemento atual for o pai de si mesmo,
        if (origem == parent.get(origem)) {

            // significa que encontramos o pai.
            return origem;
            
        }

        // Atualiza o pai do elemento atual para otimizar futuras consultas.
        parent.set(origem, buscarParente(parent.get(origem), parent));

        // Retorna o pai encontrado.
        return parent.get(origem);

        // return parent.set(parent.get(origem), buscarParente(parent.get(origem), parent));
    }

    // public static long roadsAndLibraries(int numeroEstradas, int custoRepararEstradas, int custoConstruirNovaEstrada, List<List<Integer>> cidades) {


    //     // Se o custo de reparar estrada for menor ou igual ao custo de construir uma estrada,
    //     // então é mais eficiente reformar a estrada em cada cidade, já que o custo é menor.
    //     if(custoRepararEstradas <= custoConstruirNovaEstrada) {

    //         return (long) custoRepararEstradas * numeroEstradas;
    //     }

    //     // Constrói um gráfico (grafo) a partir da lista de cidades e s  uas conexões.
    //     Map<Integer, List<Integer>> arestas =  construirGrafo(cidades);

    //     // Conjunto para acompanhar as cidades já visitadas e recapadas (conectadas).
    //     Set<Integer> recapado = new HashSet<>();

    //     // Variável para armazenar o custo total.
    //     long custo = 0;

    //     // Itera sobre cada cidade.
    //     for (int indice = 1; indice <= numeroEstradas; indice++) {
            
    //         // Se a cidade ainda não foi recapada (visitada anteriormente),
    //         if(!recapado.contains(indice)) {

    //             // Executa uma busca em profundidade (DFS) para encontrar todas as cidades conectadas à cidade atual.
    //             Set<Integer> cidadeGrupo = dfs(new HashSet<>(), arestas, indice);

    //             // Determina o número de estradas que precisam ser construídas para conectar todas as cidades do grupo.
    //             int estradasParaConstruir = cidadeGrupo.size() - 1;

    //             // Incrementa o custo com o número de estradas a serem construídas multiplicado pelo custo de construção de cada estrada.
    //             custo += (long) estradasParaConstruir * custoConstruirNovaEstrada;

    //             // Adiciona o custo de reparar cada estrada em cada grupo de cidades.
    //             custo += custoRepararEstradas;

    //              // Itera sobre cada cidade no grupo.
    //             for(int cidade : cidadeGrupo) {

    //                 // Adiciona a cidade ao conjunto de recapadas, indicando que ela já foi visitada.
    //                 recapado.add(cidade);
    //             }
    //         }
    //     }
        
    //     // Retorna o custo total.
    //     return custo;
    // }

    // // Realiza uma busca em profundidade (DFS) a partir de um nó específico em um grafo.
    // private static Set<Integer> dfs(Set<Integer> visitado, Map<Integer, List<Integer>> arestas, int indice) {

    //     // Se o nó ainda não foi visitado,
    //     if (!visitado.contains(indice)) {
            
    //         // Marca o nó como visitado.
    //         visitado.add(indice);

    //         // Verifica se o nó possui conexões (arestas) no grafo.
    //         if (arestas.get(indice) != null) {

    //             // Itera sobre cada conexão do nó.
    //             for (int conexao : arestas.get(indice)) {

    //                 // Chama recursivamente a busca em profundidade para o nó conectado.
    //                 dfs(visitado, arestas, conexao);
                    
    //             }
                
    //         }
    //     }

    //     // Retorna o conjunto de nós visitados.
    //     return visitado;
    // }

    // // Constrói um gráfico (grafo) a partir da lista de cidades e suas conexões.
    // private static Map<Integer, List<Integer>> construirGrafo(List<List<Integer>> cidades) {

    //     // Cria um mapa para armazenar as arestas (conexões) entre as cidades.
    //     Map<Integer, List<Integer>> arestas = new HashMap<>();

    //     // Itera sobre cada lista de cidade na lista de cidades fornecida.
    //     for (List<Integer> cidade : cidades) {
            
    //         // Obtém a cidade de origem e a cidade de destino da lista atual.
    //         int origem = cidade.get(0);
    //         int destino = cidade.get(1);

    //         // Se a cidade de origem ainda não está presente no mapa de arestas,
    //         if (!arestas.containsKey(origem)) {

    //             // Adiciona a cidade de origem ao mapa com uma lista vazia de conexões.
    //             arestas.put(origem, new ArrayList<>());
                
    //         }

    //         // Se a cidade de destino ainda não está presente no mapa de arestas,
    //         if (!arestas.containsKey(destino)) {

    //             // Adiciona a cidade de destino ao mapa com uma lista vazia de conexões.
    //             arestas.put(destino, new ArrayList<>());
    //         }

    //         // Adiciona a conexão bidirecional entre a cidade de origem e a cidade de destino.
    //         arestas.get(origem).add(destino);
    //         arestas.get(destino).add(origem);

    //     }

    //     // Retorna o mapa de arestas.
    //     return arestas;
    // }


    // // Implementa o método roadsAndLibraries para calcular o custo mínimo de construir estradas e bibliotecas.
    // public static long roadsAndLibraries(int numeroEstradas, int custoRepararEstradas, int custoConstruirNovaEstrada, List<List<Integer>> cidades) {

    //     // Cria uma lista de listas para representar as estradas entre as cidades.
    //     ArrayList<ArrayList<Integer>> arr = new ArrayList<>();

    //     for (int indice = 0; indice < numeroEstradas; indice++) {
            
    //         // Cria uma lista vazia para cada estrada.
    //         arr.add(new ArrayList<Integer>());
    //     }

    //     for (int indice = 0; indice < cidades.size(); indice++) {
            
    //         // Obtém a primeira cidade da conexão (índice 0) e ajusta o índice para começar em 0 (subtraindo 1).
    //         // Adiciona a segunda cidade da conexão (índice 1) ajustada para começar em 0 à lista de estradas.
    //         // Preenche a lista de estradas com as conexões entre as cidades.
    //         arr.get(cidades.get(indice).get(0) - 1).add(cidades.get(indice).get(1) - 1);

    //         // Obtém a segunda cidade da conexão (índice 1) e ajusta o índice para começar em 0 (subtraindo 1).
    //         // Adiciona a primeira cidade da conexão (índice 0) ajustada para começar em 0 à lista de estradas.
    //         // Ajusta os índices das cidades para começar em 0 (subtraindo 1).
    //         arr.get(cidades.get(indice).get(1) - 1).add(cidades.get(indice).get(0) - 1);
    //     }

    //     // Cria um array de booleanos para acompanhar as estradas visitadas.
    //     boolean[] visitado = new boolean[numeroEstradas];

    //     // Inicializa as variáveis de custo total e número de estradas construídas.
    //     long custo = (long) numeroEstradas * custoRepararEstradas;
    //     long estrada = 0;

    //     for (int indice = 0; indice < numeroEstradas; indice++) {
            
    //         // Se a estrada não foi visitada,
    //         if (!visitado[indice]) {

    //             // Chama o método conectarEstrada para encontrar todas as estradas conectadas a partir da estrada atual.
    //             estrada += conectarEstrada(indice, arr, visitado);

    //             // Calcula o custo total considerando o número de estradas construídas e o número de estradas restantes.
    //             long tempCusto = ((long) numeroEstradas - estrada) * (long) custoRepararEstradas + estrada * (long) custoConstruirNovaEstrada;

    //             // Atualiza o custo mínimo, se necessário.
    //             custo = Math.min(custo, tempCusto);
                
    //         }
    //     }

    //     // Retorna o custo mínimo total.
    //     return custo;
    // }

    // // Conecta as estradas a partir de uma origem específica e retorna o número de estradas conectadas.
    // private static long conectarEstrada(int origem, ArrayList<ArrayList<Integer>> arr, boolean[] visitado) {

    //     // Inicializa o contador de estradas e marca a origem como visitada.
    //     long estradas = 0;
    //     visitado[origem] = true;

    //      // Cria uma fila e adiciona a origem inicial.
    //     Queue<Integer> fila = new LinkedList<>();
    //     fila.add(origem);

    //     // Enquanto a fila não estiver vazia,
    //     while(!fila.isEmpty()) {

    //         // Remove o próximo elemento da fila.
    //         int atual =  fila.poll();

    //         // Itera sobre cada estrada conectada ao nó atual.
    //         for (int proxima : arr.get(atual)) {
                
    //             // Se a estrada ainda não foi visitada,
    //             if (visitado[proxima] != true) {
                    
    //                 // Marca a estrada como visitada.
    //                 visitado[proxima] = true;

    //                 // Incrementa o contador de estradas conectadas.
    //                 estradas++;

    //                 // Adiciona a estrada à fila para processamento futuro.
    //                 fila.add(proxima);
    //             }
    //         }
    //     }

    //     // Retorna o número total de estradas conectadas.   
    //     return estradas;
    // }
    
}
