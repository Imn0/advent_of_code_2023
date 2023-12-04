import java.io.File
import java.io.InputStream
import kotlin.text.equals

data class Card(val bonus: Int, var countOfBonus : Int)

fun main() {
    val inputStream: InputStream = File("input.txt").inputStream()
    val cardsList: MutableList<Card> = mutableListOf()
    inputStream.bufferedReader().forEachLine { line ->
        val splited = line.split(":", "|")
        val winning = splited[1].split(" ").filter { !it.isNullOrBlank()}.toList()
        val to_match = splited[2].split(" ").filter { !it.isNullOrBlank()}.toList()
        cardsList.add(Card(winning.intersect(to_match).size, 1) )
    } 

    for(i in cardsList.indices){
        for (j in 1..cardsList[i].countOfBonus) {
            for (h in 1..cardsList[i].bonus){
                cardsList[i+h].countOfBonus++
            }
        }
    }
    val total = cardsList.sumOf { it.countOfBonus }
    println(total)
}