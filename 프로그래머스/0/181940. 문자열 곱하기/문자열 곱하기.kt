class Solution {
    fun solution(my_string: String, k: Int): String {
        var answer: String = ""
        repeat(k) {
            answer = answer + my_string
        }
        return answer
    }
}