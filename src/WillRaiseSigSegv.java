public class WillRaiseSigSegv {
        static native void raiseSigSegv();

        public static void main(String[] args) {
            System.loadLibrary("willjavasegfault");
            raiseSigSegv();
        }
}
