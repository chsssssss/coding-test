class Solution {
    fun solution(n: Long): Long {
        var answer: Long = 0
        var temp = ArrayList<Int>()
        for (i in n.toString().toList()) {
            temp.add(i.toString().toInt())
        }
        temp.sortDescending()
        
        return temp.joinToString("").toLong()
    }
}