import scala.io.Source
import scala.collection.mutable.ListBuffer
import java.math.BigInteger

object base26Convert{
    def convert(b26: String): Int = {
        var sum: Int = 0
        var power: Int = 0
        for (i <- b26.length - 1 to 0 by -1) {
            sum += (b26(i).toInt - 'A'.toInt) * Math.pow(26, power).toInt
            power += 1
        }
        return sum 
    }
}

class Node(var left: Int, var right: Int)


object day8p2 {
    var graph: List[Node] = List()
    var path: String = ""
    var nodes: List[Int] = List()

    def main(args: Array[String]): Unit = {
        val filePath = "input.txt"
        
        var fileContents: List[String] = List()

        try {
        val source = Source.fromFile(filePath)
        fileContents = source.getLines().toList
        source.close()
        } catch {
        case e: Exception =>
            println(s"Error reading file: ${e.getMessage}")
            System.exit(1)
        }


        val graphBuffer: ListBuffer[Node] = ListBuffer.fill(base26Convert.convert("ZZZ")+1)(new Node(-1, -1)) 

        val pattern = """(\w+)\s*=\s*\((\w+),\s*(\w+)\)""".r


        fileContents.zipWithIndex.foreach { case (line, index) =>
        if (index == 0) {
            this.path = line
        }
        if (index > 1) {
            line match {
                case pattern(key, value1, value2) =>
                    val index = base26Convert.convert(key)
                    if( key.charAt(2) == 'A')
                    {
                        nodes = nodes :+ index
                    }
                    if ( key.charAt(2) == 'Z')
                    {
                        println(s"$index % 26 = ${index % 26}")
                    }
                    val left = base26Convert.convert(value1)                 
                    val right = base26Convert.convert(value2)                 
                    graphBuffer(index).left = left
                    graphBuffer(index).right = right
                case _ =>
                    println("Pattern does not match the input string.")
            }
        }
        }
        println(nodes.length)
        this.graph = graphBuffer.toList
        var answers: List[Int] = List()

        nodes.foreach( i => answers = answers :+ calculatePath(0, 0, i))
        println(answers.foldLeft(BigInt(1))((acc, num) => lcm(acc, num)))
    }

    def calculatePath(index: Int, total: Int, current : Int): Int = {
        if( current % 26 == 25 ){
            return total
        }
        var i = index
        if( i >= this.path.length)
        {
            i = 0
        }
        if( path.charAt(i) == 'R'){
            return calculatePath(i +1, total +1, this.graph(current).right)
        } else {
            return calculatePath(i +1, total +1, this.graph(current).left)
        }
    }

    def gcd(a: BigInt, b: BigInt): BigInt = if (b == 0) a else gcd(b, a % b)
  
    def lcm(a: BigInt, b: BigInt): BigInt = (a * b).abs / gcd(a, b)
}
