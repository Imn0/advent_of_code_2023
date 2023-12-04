import java.io.File
import java.io.InputStream
import kotlin.text.equals

fun main() {
    val inputStream: InputStream = File("input.txt").inputStream()
    var total = 0
    inputStream.bufferedReader().forEachLine { line ->
        val splited = line.split(":", "|")
        val winning = splited[1].split(" ").filter { !it.isNullOrBlank()}.toList()
        val to_match = splited[2].split(" ").filter { !it.isNullOrBlank()}.toList()
        var current = winning.intersect(to_match).size
        if(current <= 1){
            total += current
        } else {

            total += Math.pow(2.0, (current-1).toDouble()).toInt()
        }
    } 
    println(total)
}