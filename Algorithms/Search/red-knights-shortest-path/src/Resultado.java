import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// A tarefa do problema "Red Knight's Shortest Path" do 
// HackerRank é encontrar o caminho mais curto que o cavaleiro 
// vermelho (Red Knight) deve seguir em um tabuleiro de xadrez 
// para alcançar uma posição de destino em um número mínimo de movimentos, 
// utilizando movimentos específicos que um cavaleiro pode fazer no xadrez. 
// O problema pede que você implemente uma função que receba a posição inicial 
// do cavaleiro vermelho e a posição de destino como entrada e retorne a 
// sequência de movimentos que o cavaleiro deve seguir para chegar ao seu 
// destino, ou imprima "IMPOSSIBLE" caso não seja possível alcançar a posição de destino.

public class Resultado {


    // // Esta é a função que imprime o caminho mais curto entre dois pontos em um tabuleiro de xadrez.
    // // Ela recebe as coordenadas do ponto inicial (i_start, j_start) e do ponto final (i_end, j_end).
    // public static void printShortestPath(int n, int i_start, int j_start, int i_end, int j_end) {

    //     // Se não for possível chegar ao ponto final a partir do ponto inicial, ela imprime "Impossible".
    //     // Ela usa a função BFS para encontrar o caminho mais curto.
    //     if (!BFS(new Cord(i_start, j_start, ""), new Cord(i_end, j_end, ""), n)) {

    //         System.out.println("Impossible");
            
    //     }
    // }

    
    public static boolean BFS(Cord atual, Cord meta, int n) {

        // Array com os movimentos possíveis do cavalo
        int[][] movimentos = { { -2, -1 }, { -2, 1 }, { 0, 2 }, { 2, 1 }, { 2, -1 }, { 0, -2 } };

        // Strings que representam os movimentos possíveis do cavalo
        String[] movimentoStrings = { "UL", "UR", "R", "LR", "LL", "L" };

        // Mapa para armazenar os pares de cada coordenada visitada
        Map<Cord, Cord> parentes = new HashMap<>();

        // Fila para armazenar as coordenadas a serem visitadas
        Queue<Cord> fila = new LinkedList<>();

        // Conjunto para armazenar as coordenadas já visitadas
        Set<String> visitado = new HashSet<>();

        // Adiciona a coordenada atual na fila e no conjunto de visitados
        fila.add(atual);
        visitado.add(atual.x + "," + atual.y);

        // Enquanto a fila não estiver vazia, continua a busca
        while (!fila.isEmpty()) {
            
            // Pega a próxima coordenada da fila
            atual = fila.poll();

            // Se a coordenada atual é a meta, imprime o menor caminho encontrado
            if (atual.x == meta.x && atual.y == meta.y) {
                
                String imprimir = "";
                int i = -1;

                // Percorre os pais da meta até a origem, concatenando os movimentos
                while (atual != null) {
                    
                    imprimir = atual.movimento + " " + imprimir;
                    atual = parentes.get(atual);
                    i++;
                }

                // Imprime o tamanho do caminho e os movimentos na ordem correta
                System.out.println(i);
                System.out.println(imprimir.substring(1));

                return true;
            }
            
            // Percorre os movimentos possíveis a partir da coordenada atual
            for (int i = 0; i < movimentos.length; i++) {
                
                int x = atual.x + movimentos[i][0];
                int y = atual.y + movimentos[i][1];

                // Se a coordenada resultante é válida e ainda não foi visitada, adiciona na fila
                if (y < n && x < n && x >= 0 && y >= 0 && !visitado.contains(x + "," + y)) {
                    
                    Cord num = new Cord(x, y, movimentoStrings[i]);

                    // próximo nó a ser explorado é adicionado à fila
                    fila.add(num);

                    // o pai do nó atual é armazenado no mapa "parentes"
                    parentes.put(num, atual);

                    // nó é adicionado ao conjunto "visitado" para garantir que ele não seja visitado novamente.
                    visitado.add(x + "," + y);
                }
            }
        }

        return false;
    }

    // O método recebe como parâmetros o tamanho do tabuleiro n, as coordenadas de início (i_start, j_start)
    // e as coordenadas de fim (i_end, j_end) e imprime o caminho mais curto possível de um cavalo de xadrez
    // partindo de (i_start, j_start) até chegar em (i_end, j_end)
    public static void printShortestPath(int n, int i_start, int j_start, int i_end, int j_end) {

        // A matriz movimentos armazena os possíveis movimentos do cavalo em cada jogada, onde o primeiro valor do par indica a
        int[][] movimentos = {{-2, -1}, {-2, 1}, {0, 2}, {2, 1}, {2, -1}, {0, -2}};

        // vetor de strings correspondente a cada movimento
        String[] movimentoStrings = {"UL", "UR", "R", "LR", "LL", "L"};
    
        // cria um objeto Cord para a posição inicial e final
        Cord start = new Cord(i_start, j_start, "");
        Cord end = new Cord(i_end, j_end, "");
    
        // gera uma lista de Cord com o caminho percorrido pelo cavalo até chegar na posição final
        List<Cord> caminho = Stream.iterate(start, c -> {

            // para cada Cord da lista, gera uma lista de Cords possíveis com base na matriz de movimentos
            return Arrays.stream(movimentos)
                    .map(movimento -> new Cord(c.x + movimento[0], c.y + movimento[1], ""))

                    // filtra apenas as Cords que estão dentro do tabuleiro
                    .filter(c2 -> c2.x >= 0 && c2.x < n && c2.y >= 0 && c2.y < n)

                    // pega a primeira Cord da lista (movimento mais próximo da posição final)
                    .findFirst()
                    .orElse(null);
        })

            // limita o número de Cords gerados (para evitar um loop infinito)
            .limit(n * n)

            // adiciona o movimento correto em cada Cord do caminho percorrido
            .peek(c -> {
                if (!c.movimento.isEmpty()) {

                    // encontra o índice do movimento na matriz de movimentos e adiciona a string correspondente
                    int index = Arrays.asList(movimentos).indexOf(new int[]{c.x - c.movimento.charAt(0), c.y - c.movimento.charAt(1)});
                    c.movimento = movimentoStrings[index];
                }
            })

            // remove as Cords inválidas (nulas ou sem movimento) antes da posição final
            .dropWhile(c -> c == null || c.movimento.isEmpty() || !c.equals(end))

            // transforma o resultado em uma lista
            .collect(Collectors.toList());
    

        // verifica se o caminho é inválido (vazio ou não chegou na posição final)
        if (caminho.isEmpty() || !caminho.get(caminho.size() - 1).equals(end)) {
            System.out.println("Impossible");
        } else {

            // imprime o número de movimentos e o caminho percorrido
            System.out.println(caminho.size() - 1);
            caminho.stream().skip(1).forEach(c -> System.out.print(c.movimento + " "));
            System.out.println();
        }
    }
    
    
}

    // public static void printShortestPath(int n, int i_start, int j_start, int i_end, int j_end) {

    //     int[][] movimentos = { { -2, -1 }, { -2, 1 }, { 0, 2 }, { 2, 1 }, { 2, -1 }, { 0, -2 } };
    //     String[] movimentoStrings = { "UL", "UR", "R", "LR", "LL", "L" };

    //     List<Cord> caminho = Stream.iterate(new Cord(i_start, j_start, ""), atual -> {

    //         return Arrays.stream(movimentos)
    //                      .map(movimento -> new Cord(atual.x + movimento[0], atual.y + movimento[1], ""))
    //                      .filter(c -> c.x >= 0 && c.x < n && c.y >= 0 && c.y < n)
    //                      .findFirst()
    //                      .orElse(null);
    //     })
    //     .limit(n * n)
    //     .peek(c -> {
    //         String movimento = movimentoStrings[Arrays.asList(movimentos).indexOf(new int[] {c.x - atual.x, c.y - atual.y})];
    //         c.movimento = (movimento != null && !movimento.isEmpty()) ? movimento : "";
    //     })
    //     .dropWhile(c -> c == null || c.movimento.isEmpty() || c.x != i_end || c.y != j_end)
    //     .collect(Collectors.toList());

    //     if (caminho.isEmpty() || caminho.get(caminho.size() - 1).x != i_end || caminho.get(caminho.size() - 1).y != j_end) {
            
    //         System.out.println("Impossible");

    //     } else {

    //         System.out.println(caminho.size() - 1);
    //         caminho.stream().skip(1).forEach(c -> System.out.print(c.movimento + " "));
    //         System.out.println();
    //     }
    // }



class Cord {

    int x;
    int y;
    String movimento;

    // Construtor da classe
    public Cord(int x, int y, String movimento) {

        this.x = x;
        this.y = y;
        this.movimento = movimento;
    }
}