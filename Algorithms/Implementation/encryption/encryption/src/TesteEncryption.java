import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class TesteEncryption {

    @Test
    public void testeCaso1() {

        String s = "haveaniceday";
        String esperado = "hae and via ecy";

        String resultado = Resultado.encryption(s);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso2() {

        String s = "feedthedog";
        String esperado = "fto ehg ee dd";

        String resultado = Resultado.encryption(s);

        assertEquals(esperado, resultado);
    }

    @Test
    public void testeCaso3() {

        String s = "chillout";
        String esperado = "clu hlt io";

        String resultado = Resultado.encryption(s);

        assertEquals(esperado, resultado);
    }
    
}
