/**
 * This class produces some kind of modern art
 *
 * @author Martin Milata &lt;mmilata@redhat.com&gt;
 */
public final class WontCatchSuppressedException implements AutoCloseable
{
    public int level;

    public WontCatchSuppressedException(int n) {
        level = n;
    }

    @Override
    public void close() {
        die(level, false);
    }

    public static void die(int n, boolean main_chain) {
        String is_main_chain = main_chain ? "yes" : "no";

        if (n <= 0) {
            throw new RuntimeException(is_main_chain);
        } else {
            try (WontCatchSuppressedException w = new WontCatchSuppressedException(n-1);
                 WontCatchSuppressedException v = new WontCatchSuppressedException(n-1)) {
                die(n-1, main_chain);
            } catch (RuntimeException e) {
                throw new RuntimeException(is_main_chain, e);
            }
        }
    }

    public static void main(String[] args) {
        die(3, true);
    }
}
