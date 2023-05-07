import static org.junit.Assert.assertEquals;

import java.util.*;

import org.junit.Test;

public class TesteRoadsAndLibraries {
    
    @Test
    public void testeCaso1() {

        int numeroEstradas = 3;
        int custoRepararEstradas = 2;
        int custoConstruirNovaEstrada = 1;
        List<List<Integer>> cidades = new ArrayList<>();

        cidades.add(List.of(1, 2));
        cidades.add(List.of(3, 1));
        cidades.add(List.of(2, 3));

        int esperado = 4;
        long resultado = Resultado.roadsAndLibraries(numeroEstradas, custoRepararEstradas, custoConstruirNovaEstrada, cidades);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso2() {

        int numeroEstradas = 6;
        int custoRepararEstradas = 2;
        int custoConstruirNovaEstrada = 5;
        List<List<Integer>> cidades = new ArrayList<>();

        cidades.add(List.of(1, 3));
        cidades.add(List.of(3, 4));
        cidades.add(List.of(2, 4));
        cidades.add(List.of(1, 2));
        cidades.add(List.of(2, 3));
        cidades.add(List.of(5, 6));
        

        int esperado = 12;
        long resultado = Resultado.roadsAndLibraries(numeroEstradas, custoRepararEstradas, custoConstruirNovaEstrada, cidades);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso3() {

        int numeroEstradas = 6;
        int custoRepararEstradas = 2;
        int custoConstruirNovaEstrada = 3;
        List<List<Integer>> cidades = new ArrayList<>();

        cidades.add(List.of(1, 2));
        cidades.add(List.of(1, 3));
        cidades.add(List.of(4, 5));
        cidades.add(List.of(4, 6));
        
        int esperado = 12;
        long resultado = Resultado.roadsAndLibraries(numeroEstradas, custoRepararEstradas, custoConstruirNovaEstrada, cidades);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso4() {

        int numeroEstradas = 5;
        int custoRepararEstradas = 6;
        int custoConstruirNovaEstrada = 1;
        List<List<Integer>> cidades = new ArrayList<>();

        cidades.add(List.of(1, 2));
        cidades.add(List.of(1, 3));
        cidades.add(List.of(1, 4));
        
        
        int esperado = 15;
        long resultado = Resultado.roadsAndLibraries(numeroEstradas, custoRepararEstradas, custoConstruirNovaEstrada, cidades);

        assertEquals(esperado, resultado);
    }
}
