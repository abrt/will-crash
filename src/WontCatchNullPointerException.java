/**
 * This class produces uncaught NullPointerException
 *
 * @author Jakub Filak &lt;jfilak@redhat.com&gt;
 */
public final class WontCatchNullPointerException
{
    /* Approximate number of recurrent calls until the exception is thrown
     */
    private final int stack_height;

    /* Initializes a new instance
     */
    public WontCatchNullPointerException(int height) {
        stack_height = height;
    }

    /* Throws NullPointerException
     */
    public void die() {
        die_hard(stack_height);
    }

    /* If @ttl is equal or less than zero throws NullPointerException;
     * otherwise call itself with decremented @ttl.
     */
    private void die_hard(int ttl) {
        if (ttl <= 0) {
            Object o = null;
            System.out.println("Dead object : " + o.toString());
        }

        die_hard(ttl - 1);
    }

    public static void main(String[] args) {
        WontCatchNullPointerException inst = new WontCatchNullPointerException(3);
        inst.die();

        System.out.println("Is it possible to survive a head shot? Yes, of course!");
    }
}
