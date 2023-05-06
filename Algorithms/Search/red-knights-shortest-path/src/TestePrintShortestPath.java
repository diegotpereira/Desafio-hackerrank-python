import static org.junit.Assert.assertEquals;

import java.io.*;

import org.junit.Test;

public class TestePrintShortestPath {

    @Test
    public void testeCaso1() {

        int n = 7;
        int i_start = 6;
        int j_start = 6;
        int i_end = 0;
        int j_end = 1;
    
        String esperadoMovimento = "UL UL UL L";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }

    @Test
    public void testeCaso2() {

        int n = 6;
        int i_start = 5;
        int j_start = 1;
        int i_end = 0;
        int j_end = 4;
    
        String esperadoMovimento = "Impossible";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }
    
    @Test
    public void testeCaso3() {

        int n = 7;
        int i_start = 0;
        int j_start = 3;
        int i_end = 4;
        int j_end = 3;
    
        String esperadoMovimento = "LR LL";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }

    @Test
    public void testeCaso4() {

        int n = 5;
        int i_start = 4;
        int j_start = 1;
        int i_end = 0;
        int j_end = 3;
    
        String esperadoMovimento = "UR UR";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }

    @Test
    public void testeCaso5() {

        int n = 10;
        int i_start = 9;
        int j_start = 9;
        int i_end = 6;
        int j_end = 3;
    
        String esperadoMovimento = "Impossible";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }


    @Test
    public void testeCaso6  () {

        int n = 10;
        int i_start = 9;
        int j_start = 9;
        int i_end = 5;
        int j_end = 3;
    
        String esperadoMovimento = "UL UL L L";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }

    @Test
    public void testeCaso7() {

        int n = 30;
        int i_start = 25;
        int j_start = 2;
        int i_end = 23;
        int j_end = 29;
    
        String esperadoMovimento = "UR R R R R R R R R R R R R R";
        
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
    
        Resultado.printShortestPath(n, i_start, j_start, i_end, j_end);
    
        String atualSaida = outContent.toString().trim();
        
        if (atualSaida.equals("Impossible")) {
            
            assertEquals("Impossible", atualSaida);
        } else {
            
            String[] actualOutputArray = atualSaida.split("\n");
            String atualMovimento = actualOutputArray[1].trim();
            
            assertEquals(esperadoMovimento, atualMovimento);
        }

    }
}
