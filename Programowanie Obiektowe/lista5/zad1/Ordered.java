/*
 * Karolina Jędraszek
 * lista 5 zad 1
 * Windows vs code, openjdk version 17.0.6
 */
public interface Ordered extends Comparable<Ordered>
{
    int get_order();

    @Override
    int compareTo( Ordered toCompare);
}
