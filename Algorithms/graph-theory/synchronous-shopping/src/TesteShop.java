import static org.junit.Assert.assertEquals;

import java.util.*;

import org.junit.Test;

public class TesteShop {
    
    @Test
    public void testeCaso1() {

        int numeroLojas = 5;
        int numeroTiposPeixe = 5;
        List<String> lojas = Arrays.asList("1 1", "1 2", "1 3", "1 4", "1 5");
        List<List<Integer>> estradas = new ArrayList<>();

        estradas.add(Arrays.asList(1, 2, 10));
        estradas.add(Arrays.asList(1, 3, 10));
        estradas.add(Arrays.asList(2, 4, 10));
        estradas.add(Arrays.asList(3, 5, 10));
        estradas.add(Arrays.asList(4, 5, 10));

        int esperado = 30;
        int resultado = Resultado.shop(numeroLojas, numeroTiposPeixe, lojas, estradas);

        assertEquals(esperado, resultado);
        
    }

    @Test
    public void testeCaso2() {

        int numeroLojas = 6;
        int numeroTiposPeixe = 3;
        List<String> lojas = Arrays.asList("2 1 2", "1 3", "0", "2 1 3", "1 2", "1 3");
        List<List<Integer>> estradas = new ArrayList<>();

        estradas.add(Arrays.asList(1, 2, 572));
        estradas.add(Arrays.asList(4, 2, 913));
        estradas.add(Arrays.asList(2, 6, 220));
        estradas.add(Arrays.asList(1, 3, 579));
        estradas.add(Arrays.asList(2, 3, 808));
        estradas.add(Arrays.asList(5, 3, 298));
        estradas.add(Arrays.asList(6, 1, 927));
        estradas.add(Arrays.asList(4, 5, 171));
        estradas.add(Arrays.asList(1, 5, 671));
        estradas.add(Arrays.asList(2, 5, 463));

        int esperado = 792;
        int resultado = Resultado.shop(numeroLojas, numeroTiposPeixe, lojas, estradas);

        assertEquals(esperado, resultado);
        
    }

    @Test
    public void testeCaso3() {

        int numeroLojas = 6;
        int numeroTiposPeixe = 4;
        List<String> lojas = Arrays.asList("1 2", "1 2", "1 1", "2 3 4", "2 3 4", "1 4");
        List<List<Integer>> estradas = new ArrayList<>();

        estradas.add(Arrays.asList(5, 4, 646));
        estradas.add(Arrays.asList(4, 1, 997));
        estradas.add(Arrays.asList(2, 1, 881));
        estradas.add(Arrays.asList(2, 6, 114));
        estradas.add(Arrays.asList(3, 1, 46));
       

        int esperado = 2989;
        int resultado = Resultado.shop(numeroLojas, numeroTiposPeixe, lojas, estradas);

        assertEquals(esperado, resultado);
        
    }
}
