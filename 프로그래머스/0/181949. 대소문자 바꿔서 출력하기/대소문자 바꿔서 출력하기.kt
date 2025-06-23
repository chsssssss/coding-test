fun main(args: Array<String>) {
    val s1 = readLine()!!
    var result = ""
    for(s in s1) {
        if(s.isUpperCase()) {
            result += s.toLowerCase()
        }
        else{
            result += s.toUpperCase()
        }
    }
    print(result)
}