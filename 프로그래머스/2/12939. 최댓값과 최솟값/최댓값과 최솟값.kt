class Solution {
    fun solution(s: String): String {
        var answer = ""
        val num_list = s.split(" ").map { it.toInt() }
        val minValue = num_list.minOrNull()
        val maxValue = num_list.maxOrNull()
        answer = "$minValue $maxValue"
        
        return answer
    }
}