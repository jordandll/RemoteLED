
import java.net.Socket
import java.net.SocketTimeoutException
import java.net.InetSocketAddress
import java.io.IOException
import java.lang.Thread

// Control codes.
const val LED_ON = 1
const val LED_OFF = 0

fun main() {
	// Network info.
	// TODO: Create code to parse the 'args' passed to 'main' for '--host' and '--port' options.
	val HOST = "127.0.0.1"
	val PORT = 9001
	val ADDR = InetSocketAddress(HOST, PORT)

	// Create and connect client socket.
	var s = Socket()
	try {
		s.connect(ADDR, 2000)
	}
	catch(e: SocketTimeoutException) {
		println("ERROR:\tA timeout occured when trying to connect to remote socket.")
		return
	}
	catch(e: IOException) {
		// println("ERROR:\t" + e.getMessage())
		e.printStackTrace()
		return
	}

	// Send control code.
	var s_out = s.getOutputStream()
	s_out.write(LED_ON)
	
	
	// Pause for server.
	Thread.sleep(1000)

	// Close socket.
	s.shutdownOutput()
	s.close()
}
