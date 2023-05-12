import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TesteCountArray {

    @Test
    public void testeCaso1() {

        int tamanhoArrayParaConstruido = 4;
        int  valorMaximoPermitidoElemento  = 3;
        int elementoEspecialRepetido = 2;
        int esperado = 3;
        long resultado = Resultado.countArray(tamanhoArrayParaConstruido, valorMaximoPermitidoElemento, elementoEspecialRepetido);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso2() {

        int tamanhoArrayParaConstruido = 5;
        int  valorMaximoPermitidoElemento  = 2;
        int elementoEspecialRepetido = 2;
        int esperado = 0;
        long resultado = Resultado.countArray(tamanhoArrayParaConstruido, valorMaximoPermitidoElemento, elementoEspecialRepetido);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso3() {

        int tamanhoArrayParaConstruido = 761;
        int  valorMaximoPermitidoElemento  = 99;
        int elementoEspecialRepetido = 1;
        int esperado = 236568308;
        long resultado = Resultado.countArray(tamanhoArrayParaConstruido, valorMaximoPermitidoElemento, elementoEspecialRepetido);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso4() {

        int tamanhoArrayParaConstruido = 942;
        int  valorMaximoPermitidoElemento  = 77;
        int elementoEspecialRepetido = 13;
        int esperado = 804842436;
        long resultado = Resultado.countArray(tamanhoArrayParaConstruido, valorMaximoPermitidoElemento, elementoEspecialRepetido);

        assertEquals(esperado, resultado);
    }
    
}
