/**
 * This class creates an instance of WontCatchNullPointerException class whose
 * definition is provided by HTTP server and calls its method die()
 *
 * @author Jakub Filak &lt;jfilak@redhat.com&gt;
 */

import java.io.*;
import java.net.*;
import java.lang.Class;
import java.lang.reflect.Method;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;


import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

/**
 * Simple HTTP handler which always return bytes of the configured jar file
 * regardless of the type of HTTP request.
 */
class JarGetter implements HttpHandler {

    private String jarPath;

    public JarGetter(String jarPath) {
        this.jarPath = jarPath;
    }

    public void handle(HttpExchange t) {
        try {
            FileInputStream jarStream = new FileInputStream(this.jarPath);
            t.sendResponseHeaders(200, jarStream.getChannel().size());
            int read = 0;
            byte[] buffer = new byte[1024];
            OutputStream os = t.getResponseBody();
            try {
                while(-1 != (read = jarStream.read(buffer, 0, 1024))) {
                    os.write(buffer, 0, read);
                }
            }
            finally {
                os.close();
            }
        }
        catch(IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}

public class WontCatchRemoteException {
    /**
     * Entry point to the uncaught exception in remote class test.
     */
    public static void main(String args[]) throws IOException, NoSuchMethodException, MalformedURLException, IllegalAccessException, ClassNotFoundException, InvocationTargetException, InstantiationException, IllegalArgumentException {
        String jarPath = null;
        String testClassName = "WontCatchNullPointerException";
        Class<?> testClassInstance = null;
        Object testInstance = null;

        if (args.length == 1) {
            jarPath = args[0];
        }
        else {
            System.err.println("Path to a jar needed");
            System.exit(1);
        }

        System.out.println("WontCatchRemoteException " + jarPath);

        HttpServer server = HttpServer.create(new InetSocketAddress(54321), 0);
        server.createContext("/", new JarGetter(jarPath));
        server.setExecutor(null); // creates a default executor
        server.start();

        try {
            Method method = URLClassLoader.class.getDeclaredMethod("addURL", new Class[]{URL.class});
            method.setAccessible(true);
            method.invoke(ClassLoader.getSystemClassLoader(), new Object[]{new URL("http://localhost:54321/willuncaught.jar")});

            testClassInstance = Class.forName(testClassName);

            Constructor ctor = testClassInstance.getDeclaredConstructors()[0];
            testInstance = ctor.newInstance(3);
        }
        finally {
            server.stop(0);
        }

        if (null == testInstance) {
            System.out.println("Couldn't get " + testClassName + ".class ...");
            System.exit(1);
        }

        testClassInstance.getMethod("die").invoke(testInstance);

        System.out.println("Is it possible to survive a head shot? Yes, of course!");
    }
}

// finito

