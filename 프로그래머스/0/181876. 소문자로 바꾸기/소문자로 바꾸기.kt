class Solution {
    fun solution(myString: String): String {
        var answer: String = ""
        for (i in myString) {
            answer += i.toLowerCase()
        }
        return answer
    }
}