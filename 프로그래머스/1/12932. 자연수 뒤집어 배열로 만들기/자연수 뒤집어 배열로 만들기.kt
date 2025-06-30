class Solution {
    fun solution(n: Long): ArrayList<Int> {
        val answer = ArrayList<Int>()
        for (i in n.toString().reversed()) {
            answer.add((i.toString()).toInt())
        }
        return answer
    }
}